cmake_minimum_required(VERSION 2.8.3)
project(multi_human_pose_estimation)

find_package(catkin REQUIRED COMPONENTS
  cv_bridge std_msgs rospy sensor_msgs
)

catkin_package(CATKIN_DEPENDS cv_bridge std_msgs rospy sensor_msgs)

catkin_python_setup()


catkin_install_python(PROGRAMS node/img_listener.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})