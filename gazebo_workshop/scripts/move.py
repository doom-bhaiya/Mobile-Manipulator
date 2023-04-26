#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import time 
rospy.init_node("controller1")
controller1 = rospy.Publisher("position_controller1/command", Float64, queue_size = 10)
test = Float64(-100)
for i in range(1):
    controller1.publish(test)
    time.sleep(0.1)
    rospy.loginfo("Running")

time.sleep(10)
# test = Float64(0)
# controller1.publish(test)