#!/usr/bin/env python3
'''
This is a demo script for testing linear motion of the bot by moving all four wheels in same speed.'''
import rospy
from std_msgs.msg import Float64
import time

speed = 1

def straight(vel):
    global wheel_pub
    while True:
        msg = Float64()
        msg.data = vel
        for pub in wheel_pub:
            pub.publish(msg)
        rospy.sleep(0.01)
        print (msg)


def main():
    global wheel_pub
    wheel_pub = [0,0,0,0]
    rospy.init_node("wheel_controller")
    wheel_pub[0] = rospy.Publisher('/velocity_controller1/command', Float64, queue_size=10) #frontside_left_wheel
    wheel_pub[1] = rospy.Publisher('/velocity_controller2/command', Float64, queue_size=10) #backside_left_wheel
    wheel_pub[2] = rospy.Publisher('/velocity_controller3/command', Float64, queue_size=10) #frontside_right_wheel
    wheel_pub[3] = rospy.Publisher('/velocity_controller4/command', Float64, queue_size=10) #backside_right_wheel
    straight(speed)
main()

if (__name__ == '__main__'):
    try:
        pass
    except :
        rospy.loginfo("Script Terminated!")

# test = Float64(0)
# controller1.publish(test)