import os

from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    urdf_path = os.path.expanduser("~/human/human.urdf")

    return LaunchDescription(
        [
            # Parses URDF and broadcasts TF transforms
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                parameters=[
                    {
                        "robot_description": ParameterValue(
                            Command(["cat ", urdf_path]), value_type=str
                        )
                    }
                ],
            ),
            # GUI sliders to control each joint
            Node(
                package="joint_state_publisher_gui",
                executable="joint_state_publisher_gui",
                name="joint_state_publisher_gui",
            ),
            # RViz2 visualizer
            Node(
                package="rviz2",
                executable="rviz2",
                name="rviz2",
            ),
        ]
    )
