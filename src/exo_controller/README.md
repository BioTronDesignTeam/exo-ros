# Exo Controller Package — Main Control Loop

### Overview
`exo_controller` is the **core control module** responsible for generating motor commands for the exoskeleton.  
It implements the primary control algorithms that determine how the robot responds to user intent and the current system state.

This controller runs within the **ros2_control framework** as a plugin and operates inside the real-time control loop.

---

### Responsibilities

The controller performs the following tasks:

- Implements the robot's control algorithms  
  (e.g., PID control, impedance control, trajectory tracking)

- Subscribes to:
  - **Intent** – desired user motion or assistance commands
  - **State** – current robot joint positions, velocities, and sensor data

- Computes the appropriate motor commands (torque, velocity, or position)

- Sends commands to the hardware interface through **ros2_control**

---

### Plugin Architecture

The controller is implemented as a **ros2_control controller plugin**.

**Plugin definition file**
exo_controller_plugins.xml


This file registers the controller so that the `controller_manager` can dynamically load it.

Example plugin entry:


ExoController


The controller is loaded and managed by **ros2_control's controller_manager** during runtime.

---

### Implementation Details

The controller implements the ROS2 control interface:


controller_interface::ControllerInterface


This allows it to integrate directly with the **real-time control loop** provided by ros2_control.

Controller parameters and tuning values are configured through YAML files located in the `config/` directory.

---

### Control Loop

The controller runs at a high frequency and performs the following cycle:


Read current robot state

Receive user intent input

Compute desired trajectory

Calculate control output (torques / positions)

Send commands to the hardware interface

Repeat


This loop ensures continuous feedback and responsive control of the exoskeleton.

---

### Why Is This Important 

`exo_controller` acts as the **decision-making core** of the exoskeleton.

It determines how the robot should react to:

- user movement
- external forces
- system state

A well-designed controller ensures the robot provides **safe, smooth, and effective assistance** to the