## Package Breakdown

### 1. **`bringup_robot/`** - System Launch & Configuration

**Purpose**: Meta-package that orchestrates the entire robot system startup and configuration.

**What it does**:

- Provides launch files to start all nodes simultaneously
- Contains URDF (Unified Robot Description Format) files that define the robot's physical structure
- Stores configuration files for all subsystems
- Acts as the entry point for running the complete exoskeleton system

**Key Components**:

- `launch/` - Launch files to bring up the entire system
- `urdf/` - Robot model definitions (links, joints, collision geometry)
- `config/` - YAML configuration files for controllers, sensors, etc.

**Build System**: CMake-based (`ament_cmake`)

**Why it's important**: This is your "one-stop-shop" for starting the robot. Instead of launching 5 separate nodes manually, you run one launch file from here.

---

### 2. **`exo_msgs/`** - Custom Message Definitions

**Purpose**: Defines custom ROS 2 message types specific to the exoskeleton project.

**What it does**:

- Creates two custom message types:
  - **`Intent.msg`**: Represents the user's intended motion/command
  - **`State.msg`**: Represents the exoskeleton's current state (joint positions, velocities, forces, etc.)
- These messages serve as the "language" that different nodes use to communicate

**Message Files**:

```
msg/Intent.msg  - User intent/command data structure
msg/State.msg   - Exoskeleton state data structure
```

**Build System**: Uses `rosidl_default_generators` to auto-generate C++/Python message code

**Why it's important**: Standard ROS messages (like `sensor_msgs`) aren't specific enough for exoskeleton control. Custom messages allow you to package exactly the data you need for your application (e.g., joint torques, assistance levels, gait phase).

**Dependencies**: None (base messages only)

---

### 3. **`mujoco_ros2_control/`** - Physics Simulation Interface

**Purpose**: Bridges MuJoCo physics simulator with ROS 2 control framework.

**What it does**:

- Implements a `hardware_interface` plugin that wraps MuJoCo simulation
- Allows you to test your control algorithms in simulation before deploying to real hardware
- Provides realistic physics simulation of the exoskeleton (dynamics, contacts, collisions)
- Includes visualization capabilities through MuJoCo's rendering system

**Key Features**:

- **Auto-downloads MuJoCo**: If not found, automatically fetches MuJoCo 3.4.0 binaries
- **Architecture support**: Handles both x86_64 and aarch64 (ARM) systems
- **Simulate library integration**: Builds MuJoCo's simulate application for visualization
- **Hardware abstraction**: Acts as a "fake" hardware that responds like real motors would

**Plugin Definition**: `mujoco_system_interface_plugin.xml`

- Registers `MujocoSystemInterface` as a hardware interface plugin
- Allows ros2_control to treat the simulator like real hardware

**Build Process**:

1. Searches for existing MuJoCo installation
2. Falls back to environment variable `MUJOCO_INSTALL_DIR`
3. If not found, downloads pre-built binaries from GitHub
4. Builds the simulate library from source
5. Creates the hardware interface plugin

**Why it's important**: Testing control algorithms on real exoskeletons is dangerous and expensive. Therefore simulate!

**Major Dependencies**:

- MuJoCo 3.4.0 (physics engine)
- GLFW (for visualization window)
- Eigen3 (linear algebra)
- lodepng (image handling)
- ros2_control stack

---

### 4. **`state_estimator/`** - State Estimation Node

**Purpose**: Fuses sensor data to estimate the exoskeleton's current state.

**What it does**:

- Subscribes to raw sensor data (IMUs, encoders, force sensors via `sensor_msgs`)
- Processes and filters noisy sensor readings
- Publishes estimated state using custom `State.msg` from `exo_msgs`
- will implement sensor fusion algorithms later (Kalman filter)

**Architecture**:

- Implemented as a **composable node** (can be loaded into a component container for efficiency)
- Main class: `state_estimator::StateEstimator`
- Executable: `state_estimator`

**Data Flow**:

```
sensor_msgs/Imu ────┐
sensor_msgs/JointState ──┤
sensor_msgs/ForceSensor ──┼──> State Estimator ──> exo_msgs/State
Other sensors ───────────┘
```

**Why it's important**: Sensors are noisy and sometimes fail. This node combines multiple sensors to produce the most accurate estimate of the robot's state (where it is, how fast it's moving, what forces it's experiencing).

**Dependencies**:

- `rclcpp` - ROS 2 C++ client library
- `rclcpp_components` - For composable nodes
- `exo_msgs` - Custom message types
- `sensor_msgs` - Standard ROS sensor messages

---

### 5. **`input_mapper/`** - Input Mapping Node

**Purpose**: Translates raw sensor inputs into user intent commands.

**What it does**:

- Subscribes to raw sensor data (e.g., EMG signals, force sensors, IMUs)
- Interprets this data to determine what the user wants to do
- Publishes user intent using custom `Intent.msg` from `exo_msgs`
- Acts as the "translator" between raw sensor values and high-level commands

**Example Mappings**:

- EMG muscle activation → "increase assistance" intent
- Force sensor threshold → "sit down" intent
- Gait phase detection → "adjust support timing" intent

**Architecture**:

- Composable node implementation
- Main class: `input_mapper::InputMapper`
- Executable: `input_mapper`

**Data Flow**:

```
sensor_msgs/Imu ────────┐
sensor_msgs/ForceSensor ──┼──> Input Mapper ──> exo_msgs/Intent
Custom sensor data ──────┘
```

**Why it's important**: Provides a clean abstraction layer. The controller doesn't need to know if commands come from EMG sensors, force plates, or IMU-based gesture recognition—it just receives "Intent" messages. This makes the system modular and easy to extend with new input methods.

**Dependencies**:

- `rclcpp` & `rclcpp_components`
- `sensor_msgs` - Standard sensor messages
- `exo_msgs` - Custom intent messages

---

### 6. **`exo_controller/`** - Main Control Loop

**Purpose**: Core controller that generates motor commands for the exoskeleton.

**What it does**:

- Implements the control algorithm (PID, impedance control, trajectory tracking, etc.)
- Subscribes to `Intent` (what user wants) and `State` (current robot state)
- Computes appropriate motor torques/positions
- Sends commands to hardware interface via `ros2_control`
- Implements a **controller plugin** for the ros2_control framework

**Plugin Definition**: `exo_controller_plugins.xml`

- Registers `ExoController` as a controller plugin
- Allows controller_manager to load and run this controller

**Architecture**:

- Implements `controller_interface::ControllerInterface`
- Works with ros2_control's real-time control loop
- Configured via YAML files in `config/` directory

**Control Loop**:

```
1. Read current State
2. Read current Intent
3. Compute desired trajectory
4. Calculate control output (torques)
5. Send commands to hardware interface
6. Repeat at high frequency
```

**Why it's important**: This is the "brain" of the exoskeleton. It determines how the motors should respond to achieve safe, smooth, and effective assistance to the user. Well-designed controllers mean the difference between a helpful device and a dangerous one.

**Dependencies**:

- `controller_interface` - Base controller interface
- `hardware_interface` - For accessing hardware
- `pluginlib` - Plugin system
- `rclcpp` - ROS 2 C++ library
- `realtime_tools` - Real-time safe utilities
- `exo_msgs` - Custom messages

---

## System Integration

### Launch Sequence (via bringup_robot):

1. Load robot description (URDF) into parameter server
2. Start controller_manager with MuJoCo hardware interface
3. Load exo_controller plugin
4. Start state_estimator node
5. Start input_mapper node
6. Activate all controllers
7. System is ready to receive commands

## Build Requirements

### System Dependencies:

- ROS 2 (jazzy)
- CMake 3.16+
- C++17 compiler
- Eigen3
- GLFW3
- Optional: Pre-installed MuJoCo 3.4.0

### Build Order:

1. `exo_msgs` (no dependencies)
2. `mujoco_ros2_control` (standalone)
3. `input_mapper` (depends on exo_msgs)
4. `state_estimator` (depends on exo_msgs)
5. `exo_controller` (depends on exo_msgs, ros2_control)
6. `bringup_robot` (depends on all above)

---
