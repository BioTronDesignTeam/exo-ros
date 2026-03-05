from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_path = get_package_share_directory('assembly')

    urdf_file = os.path.join(
        pkg_path,
        'urdf',
        'MK1_FB900_Full_Body_Assembly_Flattned4.urdf'
    )

    # Read URDF
    robot_description = Command(['cat ', urdf_file])

    # Static transform base_link → base_footprint
    base_tf = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        arguments=["0","0","0","0","0","0","base_link","base_footprint"]
    )

    # Spawn robot into Gazebo (ROS2 method)
    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-topic", "robot_description",
            "-name", "MK1_FB900_Full_Body_Assembly_Flattned4"
        ],
        parameters=[{
            "robot_description": robot_description
        }]
    )

    # Gazebo simulator
    gazebo = Node(
        package="ros_gz_sim",
        executable="gz_sim",
        arguments=["-r", "empty.sdf"]
    )

    # Fake calibration publisher replacement
    fake_calibration = Node(
        package="demo_nodes_py",
        executable="talker"   # Replace with real control logic later
    )

    return LaunchDescription([
        gazebo,
        base_tf,
        spawn_robot,
        fake_calibration
    ])