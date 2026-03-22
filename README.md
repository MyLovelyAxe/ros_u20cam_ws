Build repo:

```bash
cd ~/ros_u20cam_ws
colcon build --packages-select u20cam_720p --symlink-install
```

Publish raw images and test with Rviz:

```bash
cd ~/ros_u20cam_ws
source install/setup.bash
ros2 launch u20cam_720p raw_img_pub.rviz.launch.py
```

Publish compressed image:

```bash
cd ~/ros_u20cam_ws
source install/setup.bash
ros2 launch u20cam_720p comp_img_pub.rviz.launch.py
```