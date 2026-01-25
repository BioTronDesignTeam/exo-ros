from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution, Command, LaunchConfiguration
from launch.actions import DeclareLaunchArgument, RegisterEventHandler
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
from launch.event_handlers import OnProcessExit

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    my_pckg = FindPackageShare('bringup_robot')
    mujoco_scene = Command(['cat ', PathJoinSubstitution([my_pckg, 'mujoco_description', 'scene.xml'])])
    pids_file = PathJoinSubstitution([my_pckg, 'config', 'pids.yaml'])

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
    start_mujoco_ros2_control = Node(
        package="mujoco_ros2_control",
        executable="ros2_control_node",
        output="both",
        parameters=[
            {'robot_description': mujoco_scene},
            {'pids_config_file', pids_file}
        ]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value=use_sim_time,
            description='If true, use simulated clock'
        ),
        start_input_mapper,
        start_state_estimator,
        start_mujoco_ros2_control
    ])