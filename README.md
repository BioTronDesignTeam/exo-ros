## Project Overview

This project is a **ROS2 Jazzy-based exoskeleton control framework** for simulation and hardware development.  
It is designed with a **modular robotics architecture** separating description, control, sensing, simulation, and input processing.

---

## Tools & Simulation Used 
- ROS2 Jazzy  
- MuJoCo 3.4+  
- NVIDIA Isaac Sim

## Project Packages Break Down
- **assembly** — Robot description package containing URDF models, meshes, and visualization launch files.  
- **bringup_robot** — System launch package used to start the full robot stack.  
- **exo_controller** — Main control node that generates motor commands using ros2_control.  
- **exo_msgs** — Custom ROS2 messages for robot intent and state communication.  
- **input_mapper** — Converts raw sensor inputs into high-level user intent commands.  
- **state_estimator** — Fuses sensor data to estimate robot state.  
- **mujoco_ros2_control** — MuJoCo simulation interface for testing control algorithms.  
- **ps_ros2_common** — PlayStation controller ROS2 input interface library.  

## Build Guide
### Prerequisites
- Ubuntu 22.04 (WSL)  
- ROS2 Jazzy  

### ROS2 Installation
Follow the official ROS2 Jazzy installation guide:  
https://docs.ros.org/en/jazzy/Installation.html  

---

### Build the Workspace
From the project root directory:

```bash
colcon build
```

### Source the Workspace
After building, source the setup file:
```bash
source install/setup.bash
```