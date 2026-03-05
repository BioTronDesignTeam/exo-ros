## input_mapper - Input Mapping Node

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