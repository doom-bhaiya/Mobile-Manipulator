#!/usr/bin/env python3
'''
This python script is used to drive the four wheeled bot under the control of /cmd_vel

Publish linear.x velocity for linear motion and angular.z velocity for rotational motion in /cmd_vel topic, which is of type Twist.
'''
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

rospy.init_node('robot_wheel_controller')

# Define the individual wheel control topics
wheel1_topic = '/velocity_controller1/command'
wheel2_topic = '/velocity_controller2/command'
wheel3_topic = '/velocity_controller3/command'
wheel4_topic = '/velocity_controller4/command'

# Create publisher objects for the individual wheel control topics
wheel1_pub = rospy.Publisher(wheel1_topic, Float64, queue_size=10)
wheel2_pub = rospy.Publisher(wheel2_topic, Float64, queue_size=10)
wheel3_pub = rospy.Publisher(wheel3_topic, Float64, queue_size=10)
wheel4_pub = rospy.Publisher(wheel4_topic, Float64, queue_size=10)

# Robot width (Distance between two wheels of the same side in meters)
robot_width = 0.45

# Callback function for cmd_vel messages
def cmd_vel_callback(msg):
    # Extract linear and angular velocities from the received Twist message
    linear_velocity = msg.linear.x
    angular_velocity = msg.angular.z

    # Calculate individual wheel speeds based on the desired motion
    left_wheel_speed = linear_velocity - (angular_velocity * robot_width / 2)
    right_wheel_speed = linear_velocity + (angular_velocity * robot_width / 2)

    # Publish the calculated wheel speeds to the individual wheel control topics
    wheel1_pub.publish(right_wheel_speed)
    wheel2_pub.publish(right_wheel_speed)
    wheel3_pub.publish(left_wheel_speed)
    wheel4_pub.publish(left_wheel_speed)

# Register shutdown callback function
def shutdown_callback():
    # Stop the bot by publishing zero wheel speeds
    wheel1_pub.publish(0.0)
    wheel2_pub.publish(0.0)
    wheel3_pub.publish(0.0)
    wheel4_pub.publish(0.0)
    rospy.loginfo('\033[91m' +"Bot stopped."+ '\033[0m')

rospy.on_shutdown(shutdown_callback)

# Subscribe to the cmd_vel topic
rospy.Subscriber('/cmd_vel', Twist, cmd_vel_callback)

rospy.loginfo('\033[92m' + "Wheel_velocity_controller_Started" + '\033[0m')

rospy.spin()  # Keeps the program running until it is explicitly stopped
