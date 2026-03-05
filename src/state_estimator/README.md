## state_estimator - State Estimation Node

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