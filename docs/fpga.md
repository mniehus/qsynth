# FPGA and real-time control

The QPU is **not** intended to execute the high-rate feedback loop.

\[
x\rightarrow y\rightarrow\hat x\rightarrow\text{trigger/controller}\rightarrow\lambda_{\rm cmd}\rightarrow\text{actuator}.
\]

Important engineering quantities include sampling period, ADC/DAC resolution, estimator/control latency, jitter, actuator bandwidth and deterministic scheduling. These determine which policies are implementable and can therefore constrain offline synthesis.
