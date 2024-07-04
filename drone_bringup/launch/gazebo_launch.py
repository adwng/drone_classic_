import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    
    prefix = get_package_share_directory("drone_bringup")
    gazebo_prefix = get_package_share_directory("gazebo_ros")
    world_prefix = get_package_share_directory("description")

    rsp_file = os.path.join(prefix, "launch", "rsp.launch.py")

    gazebo_file = os.path.join(gazebo_prefix, "launch", "gazebo.launch.py")

    world_file = os.path.join(world_prefix, 'worlds', 'obstacles.world')

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rsp_file),
        launch_arguments={'use_sim_time': 'true'}.items(),
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_file),
        launch_arguments={'world': world_file}.items(),
    )   

    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'drone'],
        output = 'screen'
    )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
       
    ])
