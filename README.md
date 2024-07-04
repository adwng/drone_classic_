## Requisites:
1. ROS2 HUMBLE
2. GAZEBO 11 CLASSIC

<details>

<summary>ROS2 PACKAGES USED</summary>

| Packages | Functionality |
| ------------- | ------------- |
| `Twist Mux`  |  Multiplex Control  |
| `gazebo_ros_pkgs`  | Interface gazebo data with ros2  |
| `slam_toolbox`  | basic 2D slam using Lidar  |
| `RTABMAP-ROS`  | advanced 3D slam with RGBD camera |
| `Nav2`  | Autonomous Navigation Stack  |

</details>

TO INSTALL
```python
mkdir -p ~/drone/src
cd drone/src
git clone git@github.com:adwng/drone_classic_
cd ..
colcon build --symlink-install
```

TO RUN

```python
source drone/install/setup.bash
ros2 launch drone_bringup drone_launch_sim.py
ros2 launch drone_bringup drone_survey.launch.py
```
