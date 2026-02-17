const pid = new PIDController({
  kp: 1,
  ki: 0.1,
  kd: 0.05,
  setpoint: 10
});

let value = 0;

setInterval(() => {
  const output = pid.update(value, performance.now());
  value += output * 0.05;
  console.log("Value:", value.toFixed(2));
}, 100);
