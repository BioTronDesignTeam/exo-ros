from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default=True)

    launch_assembly = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('assembly'), 'launch', 'display.launch.py'])
        )
    )
    start_input_mapper = Node(
        package='input_mapper',
        executable='input_mapper',
        output='screen'
    )
    start_state_estimator = Node(
        package='state_estimator',
        executable='state_estimator',
        output='screen'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value=use_sim_time,
            description='If true, use simulated clock'
        ),
        launch_assembly,
        start_input_mapper,
        start_state_estimator,
    ])