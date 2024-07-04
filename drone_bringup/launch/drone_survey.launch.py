import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, OpaqueFunction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def include_slam_launch(context, *args, **kwargs):
    # Get the package directory
    prefix = get_package_share_directory('drone_bringup')
    # Get the slam_type launch file name
    slam_type = LaunchConfiguration('slam_type').perform(context)
    # Path to the specified launch file
    launch_file_path = os.path.join(prefix, 'launch', slam_type)
    return [IncludeLaunchDescription(PythonLaunchDescriptionSource(launch_file_path))]

def generate_launch_description():
    prefix = get_package_share_directory('drone_bringup')
    nav2_launch_file = os.path.join(prefix, 'launch', 'drone_nav.launch.py')

    # Declare the launch argument for SLAM type
    slam_type_arg = DeclareLaunchArgument(
        'slam_type',
        default_value='drone_slam.launch.py',
        description='Specify the SLAM type launch file to use (e.g., drone_slam.launch.py or drone_rtab.launch.py)'
    )

    # Include navigation launch file unconditionally
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_launch_file)
    )

    return LaunchDescription([
        slam_type_arg,
        OpaqueFunction(function=include_slam_launch),
        nav2,
    ])
