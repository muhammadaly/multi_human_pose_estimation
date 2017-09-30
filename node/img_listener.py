#!/usr/bin/env python

from __future__ import print_function

import roslib
roslib.load_manifest('multi_human_pose_estimation')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import argparse
import cv2
import math
import time
import numpy as np
from scipy.ndimage.filters import gaussian_filter
import keras_Realtime_Multi_Person_Pose_Estimation.config_reader
import keras_Realtime_Multi_Person_Pose_Estimation.model


keras_weights_file = "model/keras/model.h5"

# find connection in the specified sequence, center 29 is in the position 15
limbSeq = [[2, 3], [2, 6], [3, 4], [4, 5], [6, 7], [7, 8], [2, 9], [9, 10], \
           [10, 11], [2, 12], [12, 13], [13, 14], [2, 1], [1, 15], [15, 17], \
           [1, 16], [16, 18], [3, 17], [6, 18]]

# the middle joints heatmap correpondence
mapIdx = [[31, 32], [39, 40], [33, 34], [35, 36], [41, 42], [43, 44], [19, 20], [21, 22], \
          [23, 24], [25, 26], [27, 28], [29, 30], [47, 48], [49, 50], [53, 54], [51, 52], \
          [55, 56], [37, 38], [45, 46]]

# visualize
colors = [[255, 0, 0], [255, 85, 0], [255, 170, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0],
          [0, 255, 0], \
          [0, 255, 85], [0, 255, 170], [0, 255, 255], [0, 170, 255], [0, 85, 255], [0, 0, 255],
          [85, 0, 255], \
          [170, 0, 255], [255, 0, 255], [255, 0, 170], [255, 0, 85]]

class img_listner:

  def __init__(self):
    self.bridge = CvBridge()
    self.model = get_model()
    self.model.load_weights(keras_weights_file)
    self.params, self.model_params = config_reader()
    self.image_sub = rospy.Subscriber("image_topic", Image, self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      process(cv_image, self.params , self.model_params)
      cv2.imshow("Image window", cv_image)
      cv2.waitKey(3)
    except CvBridgeError as e:
      print(e)

def main(args):
  ic = img_listner()
  rospy.init_node('img_listner', anonymous=True)
  rospy.spin()
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)