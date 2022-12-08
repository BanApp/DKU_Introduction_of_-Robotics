import rospy
from geometry_msgs.msg import Twist

# Node 생성
rospy.init_node('my_node', anonymous=True)
# Publisher 생성
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

# msg 생성
msg = Twist()
msg.linear.x = 2.0
msg.linear.y = 0.0
msg.linear.z = 0.0
msg.angular.x = 0.0
msg.angular.y = 0.0
msg.angular.z = 1.8

rate = rospy.Rate(1)

# 1Hz 주기로 메시지 발행
while not rospy.is_shutdown():
    pub.publish(msg)
    rate.sleep()
