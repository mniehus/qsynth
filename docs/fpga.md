# FPGA and real-time control

The QPU is **not** intended to execute the high-rate feedback loop.

\[
x\rightarrow y\rightarrow\hat x\rightarrow\text{trigger/controller}\rightarrow\lambda_{\rm cmd}\rightarrow\text{actuator}.
\]

Here \(x\) is bead position [m], \(y\) is its noisy measurement [m], \(\hat x\) is the estimate [m], and \(\lambda_{\rm cmd}\) is the commanded trap centre [m]. The simulated fast block period and actuator delay are both 20 µs. These are model settings rather than measured FPGA timing.

Important engineering quantities include sampling period, ADC/DAC resolution, estimator/control latency, jitter, actuator bandwidth and deterministic scheduling. These determine which policies are implementable and can therefore constrain offline synthesis.

### Reproduce / explore this step

[Review the fast-loop timing and deployment boundary](https://github.com/mniehus/qsynth/blob/main/notebooks/overview_control_realtime.ipynb).
