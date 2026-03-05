# Bringup Robot package — System Launch & Configuration

### Overview
`bringup_robot` is the **system orchestration package** responsible for starting and configuring the complete robot stack.  
It serves as the **entry point for launching the full exoskeleton system**, ensuring all required nodes, controllers, and configurations are initialized together.

---

### Responsibilities

This package coordinates the startup of the robot by:

- Launching all required ROS2 nodes
- Initializing controllers and subsystems
- Loading configuration parameters
- Starting simulation or visualization environments when needed

Instead of launching multiple components manually, this package provides a **single launch command** to bring the entire system online.

---

### How It Works

The bringup package typically performs the following sequence:

1. Load the robot description
2. Start `robot_state_publisher`
3. Launch simulation (Gazebo) or visualization (RViz)
4. Start controllers
5. Launch supporting nodes (calibration, sensors, etc.)

This ensures the robot system is started **in the correct order** with the proper configuration.

---

### Running the Full System

To start the robot system:

```bash
ros2 launch bringup_robot bringup.launch.py