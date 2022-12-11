#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys

def turtle_circle(radius):
	rospy.init_node('turtlesim', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel',
						Twist, queue_size=10)
	rate = rospy.Rate(10)
	vel = Twist()
	
	fr  = radius 

	while fr > 0:
		vel.linear.x = fr
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 1
    
		rospy.loginfo("Radius = %f",fr)
    
		pub.publish(vel)
		fr = fr - 0.01
		rate.sleep()
		if fr == 0:
			break
		
	rospy.loginfo("new start!")

	while fr > -radius:
		vel.linear.x = fr
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = -1
    
		rospy.loginfo("Radius = %f",fr)
    
		pub.publish(vel)
		fr = fr - 0.01
		rate.sleep()
		if fr == -radius:
			break
		
if __name__ == '__main__':
	try:
		turtle_circle(float(sys.argv[1]))
	except rospy.ROSInterruptException:
		pass
