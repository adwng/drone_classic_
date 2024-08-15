# UBUNTU 22.04 REQUIRED

> [!NOTE]
> In order to allow developments happen no matter what machine is used, e.g. person A/B laptop, consider getting a separate SSD with an external enclosure with everything installed.

## Requisites:
1. ROS2 HUMBLE
2. GAZEBO 11 CLASSIC

<details>

**<summary>ROS2 PACKAGES USED</summary>**

| _Packages_ | _Functionality_ |
| ------------- | ------------- |
| `Twist Mux`  |  Multiplex Control  |
| `gazebo_ros_pkgs`  | Interface gazebo data with ros2  |
| `slam_toolbox`  | basic 2D slam using Lidar  |
| `RTABMAP-ROS`  | advanced 3D slam with RGBD camera |
| `Nav2`  | Autonomous Navigation Stack  |

</details>

<ins>**TO INSTALL**</ins>
```python
mkdir -p ~/drone/src
cd drone/src
git clone git@github.com:adwng/drone_classic_
cd ..
colcon build --symlink-install
```

<ins>**TO RUN**</ins>

```python
source drone/install/setup.bash
ros2 launch drone_bringup drone_launch_sim.py
```

<ins>**TO RUN: _slam_toolbox_ or _rtabmap_**</ins>
```python
ros2 launch drone_bringup drone_survey.launch.py slam_type:=drone_slam.launch.py
ros2 launch drone_bringup drone_survey.launch.pt slam_type:=drone_rtab.launch.py
```

<ins>**TODO**</ins>
- [ ] Translate cmd_vel messages into PX4 format
- [ ] Use PX4_ROS2
- [ ] Improve path planning to be in 3D motion instead of 2D
- [ ] Migrate to Gazebo Sim for improved PX4 experience
   
