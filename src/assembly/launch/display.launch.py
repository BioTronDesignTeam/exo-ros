from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_path = get_package_share_directory('assembly')

    urdf_file = os.path.join(
        pkg_path,
        'urdf',
        'MK1_FB900_Full_Body_Assembly_Flattned7.urdf'
    )

    rviz_config = os.path.join(pkg_path, 'urdf.rviz')

    robot_description = ParameterValue(
        Command(['cat ', urdf_file]),
        value_type=str
    )

    return LaunchDescription([

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config]
        )
    ])