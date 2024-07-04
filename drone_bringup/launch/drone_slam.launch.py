import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():

    slam_toolbox_prefix = get_package_share_directory("drone_bringup")
    slam_toolbox_file = os.path.join(slam_toolbox_prefix, "launch", "online_async_launch.py")
    slam_toolbox_params_prefix = get_package_share_directory("drone_bringup")
    slam_toolbox_params_file = os.path.join(slam_toolbox_params_prefix, "config", "mapper_params_online_async.yaml")

    slam_toolbox = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(slam_toolbox_file),
        launch_arguments={'params-file': slam_toolbox_params_file, 'use_sim_time': 'true'}.items(),
    )

    return LaunchDescription([
        slam_toolbox
    ])