# Assembly Package - Robot Model Display

The **assembly** package contains the robot description for our exoskeleon.  
It provides the **URDF model**, **meshes**, and launch files required to visualize the robot in **RViz**.

This package is intended to be used by higher-level packages such as a **bringup** package that launches controllers and full system nodes.

### Description
- **meshes/**  
  Contains STL mesh files used by the robot model.
- **urdf/**  
  Contains the robot URDF description.
- **launch/**  
  Launch files used for visualization.

## Dependencies
This package requires:

- ROS2 Jazzy
- `robot_state_publisher`
- `joint_state_publisher_gui`
- `rviz2`
- `ros_gz_sim` (optional for Gazebo simulation)

Install dependencies:

```bash
sudo apt install ros-jazzy-robot-state-publisher
sudo apt install ros-jazzy-joint-state-publisher-gui
sudo apt install ros-jazzy-rviz2
sudo apt install ros-jazzy-ros-gz-sim