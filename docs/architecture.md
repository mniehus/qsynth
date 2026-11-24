# Architecture

Q-SYNTH separates four layers:

1. **Physical simulation** — Brownian dynamics, optical trapping, measurement noise and actuation.
2. **Estimation and feedback** — classical state estimation and event-triggered control; experimentally intended for FPGA/RFSoC execution.
3. **Offline synthesis** — evaluation of candidate estimator/controller parameter sets under selected regimes, producing \(J_{ij}\).
4. **Quantum optimization experiment** — QUBO/Ising encoding, circuit construction, simulation, QPU execution and benchmarking.

The QPU is therefore an accelerator candidate for an offline combinatorial stage, not the controller itself.

### Reproduce / explore this step

[Explore the control and real-time architecture](https://github.com/mniehus/qsynth/blob/main/notebooks/overview_control_realtime.ipynb).
