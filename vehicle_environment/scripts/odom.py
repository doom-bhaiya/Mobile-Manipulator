import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

rospy.init_node('odom_data_publisher')

pub = rospy.Publisher("odom", Odometry, queue_size=10)
seq = 0

def odom_call_back(msg):
    global seq
    data = Odometry()
    data.header.seq = seq
    data.header.time = rospy.Time()
    data.header.frame_id = "base_link"
    