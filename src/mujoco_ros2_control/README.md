## mujoco_ros2_control - Physics Simulation Interface

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