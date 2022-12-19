import rospy
import cv2
import cv_bridge
import numpy
import numpy as np
from sensor_msgs.msg import Image, CameraInfo
from geometry_msgs.msg import Twist

class Follower:
  def __init__(self):
    self.bridge = cv_bridge.CvBridge()

    self.image_sub = rospy.Subscriber('/camera/image', 
                                      Image, self.cbImage)
    self.cmd_vel_pub = rospy.Publisher('/cmd_vel',
                                       Twist, queue_size=1)
    self.twist = Twist()

  def cbImage(self, msg):
    image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
    low_val = (10,10,170)
    high_val = (179,255,255)
    mask = cv2.inRange(hsv, low_val,high_val)

    h, w, d = image.shape
    blind_top = 3*h/4
    blind_bot = 3*h/4 + 20

    mask[0:blind_top, 0:w] = 0
    mask[blind_top:blind_bot+80,0:30] = 0
    mask[blind_bot+80:h, 0:w] = 0

    M = cv2.moments(mask)

    if M['m00'] > 0:
      cx = int(M['m10']/M['m00']) 
      cy = int(M['m01']/M['m00'])

      err = cx - w/3
      self.twist.linear.x = 0.4
      self.twist.angular.z = -float(err) / 40
      self.cmd_vel_pub.publish(self.twist)

    cv2.imshow("mask",mask)
    cv2.imshow("output", image)
    cv2.waitKey(3)

rospy.init_node('follower')
follower = Follower()
rospy.spin()
