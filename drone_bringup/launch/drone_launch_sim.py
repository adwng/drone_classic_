import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    
    prefix = get_package_share_directory("drone_bringup")

    twist_mux_config = os.path.join(prefix, 'config', 'twist_mux.yaml')

    rviz_path = os.path.join(
        prefix, "rviz", "rviz.rviz"
    )

    teleop = Node(
            package="drone_control",
            executable="teleop",
            output="screen",
            prefix="xterm -e",
        )

    twist_mux = Node(
        package="twist_mux",
        executable="twist_mux",
        parameters=[twist_mux_config, {'use_sim_time' : True}],
        remappings=[('/cmd_vel_out', '/cmd_vel')]
    )

    rviz_node = Node(
        package='rviz2', executable='rviz2', arguments=['-d', rviz_path],
        output='screen'
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(prefix, 'launch', 'gazebo_launch.py')
        )
    )



    return LaunchDescription([
        teleop,

        twist_mux,

        rviz_node,

        gazebo,
    ])
