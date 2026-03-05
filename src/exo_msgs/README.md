# Exo Messages — Custom Message Definitions

### Overview
`exo_msgs` defines **custom ROS 2 message types** used throughout the exoskeleton software stack.  
These messages provide a standardized way for different nodes to exchange information specific to the exoskeleton system.

They act as the **communication interface** between components such as controllers, sensors, and user intent estimation modules.

---

### Message Types

The package currently provides two primary message definitions:

- **`Intent.msg`**  
  Represents the **user's intended motion or command**, such as desired movement direction, assistance level, or gait phase.

- **`State.msg`**  
  Represents the **current state of the exoskeleton**, including information such as:
  - joint positions
  - joint velocities
  - forces or torques
  - sensor readings

---

By using standardized message definitions, different nodes in the system can communicate reliably and consistently.

---

### Why Custom Messages Are Needed

While ROS provides many standard message types (e.g., `sensor_msgs`, `geometry_msgs`), they are often too generic for exoskeleton control.

Custom messages allow the system to transmit **application-specific data**, such as:

- joint torque commands
- assistance levels
- gait phase information
- user motion intent

This ensures that the communication interface is **tailored to the needs of the exoskeleton control architecture**.