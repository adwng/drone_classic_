from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():


    use_sim_time = LaunchConfiguration('use_sim_time')
    qos = LaunchConfiguration('qos')
    
    parameters={
          'frame_id':'base_footprint',
          'use_sim_time':use_sim_time,
          'subscribe_depth':True,
          'use_action_for_goal':True,
          'qos_image':qos,
          'Reg/Force3DoF':'true',
          'queue_size': 10,
          'Optimizer/GravitySigma':'0' # Disable imu constraints (we are already in 2D)
    }

    remappings=[
        ('odom', '/odom'),
        ('rgb/image', '/camera/image_raw'),
        ('rgb/camera_info', '/camera/camera_info'),
        ('depth/image', '/camera/depth/image_raw')]

    
    slam_mode = Node(
        package='rtabmap_slam', executable='rtabmap', output='screen',
        parameters=[parameters],
        remappings=remappings,
        arguments=['-d'],
    )

    rtabmap_viz = Node(
         package='rtabmap_viz', executable='rtabmap_viz', output='screen',
         parameters=[parameters],
         remappings=remappings
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
            'use_sim_time', default_value='true'
            ),
            DeclareLaunchArgument(
                'qos', default_value='2'
            ),
            slam_mode,
            rtabmap_viz,

        ]
    )
    
    return 