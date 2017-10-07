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

if __name__ == '__main__':
    rospy.init_node('image_publish', anonymous=True)
    image_pub = rospy.Publisher("image_topic",Image)
    input_image = '/home/ivsystems/dnn_workspaces/keras_Realtime_Multi-Person_Pose_Estimation/sample_images/ski.jpg'
    oriImg = cv2.imread(input_image)
    bridge = CvBridge()
    rate = rospy.Rate(10) # 10hz
    while True:
        image_pub.publish(bridge.cv2_to_imgmsg(oriImg, "bgr8"))
        rate.sleep()