#!/usr/bin/env python

from __future__ import print_function
import roslib
roslib.load_manifest('multi_human_pose_estimation')
import sys
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from keras_Realtime_Multi_Person_Pose_Estimation.predict import predict

class img_listner:

  def __init__(self):
    self.bridge = CvBridge()
    self.predictor = predict()
    self.image_sub = rospy.Subscriber("image_topic", Image, self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      cv_result = self.predictor.process(cv_image)
      cv2.imshow("Image window", cv_result )
      cv2.waitKey(3)
    except CvBridgeError as e:
      print(e)

def main():
  ic = img_listner()
  rospy.init_node('img_listner', anonymous=True)
  rospy.spin()
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main()