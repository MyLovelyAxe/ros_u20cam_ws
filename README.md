Build repo:

```bash
cd ~/ros_u20cam_ws
colcon build --packages-select u20cam_720p --symlink-install
```

Run the camera node:

```bash
cd ~/ros_u20cam_ws
source install/setup.bash
ros2 launch u20cam_720p u20cam.rviz.launch.py
```