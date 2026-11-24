# Interdisciplinary project roadmap

**Current active focus: quantum engineering.** Read left to right across the project workflow, from physical modeling to feedback and offline synthesis, then back to validation. The domains can mature in parallel.

| Domain | Objective | Status | Completed artifacts | Missing work | Notebook |
|---|---|---|---|---|---|
| Physics / stochastic thermodynamics | Model thermal motion and account for work and information | Established model; under review for experiment | Overdamped bead model, simulated trajectories and work accounting | Calibrate against trajectories and establish the experimental energy budget | [Physics overview](https://github.com/mniehus/qsynth/blob/main/notebooks/overview_physics_thermodynamics.ipynb) |
| Control / estimation | Infer state and trigger feedback under noise | Established in simulation | Measurement, estimator, controller and supervisor blocks; fixed-policy evaluator | Held-out robustness and switched-policy replay | [Control overview](https://github.com/mniehus/qsynth/blob/main/notebooks/overview_control_realtime.ipynb) |
| FPGA / real-time implementation | Meet deterministic loop timing | Planned | Simulated block order, periods and actuator delay | Fixed-point design, latency and jitter measurements, hardware-in-the-loop tests | [Control overview](https://github.com/mniehus/qsynth/blob/main/notebooks/overview_control_realtime.ipynb) |
| Policy synthesis / optimization | Select exact policy maps and define strong baselines | Established for small cases | Pilot score matrix, lookup and coupled exact enumeration | Physically justified coupling and structured larger baselines | [Optimization overview](https://github.com/mniehus/qsynth/blob/main/notebooks/overview_optimization.ipynb) |
| Quantum engineering | Encode, compile, and benchmark the same objective | Active development | QUBO/Ising checks, QAOA, resource counts, synthetic-device compilation and noise | Calibrated target, device access, and comparable QPU measurements | [Quantum overview](https://github.com/mniehus/qsynth/blob/main/notebooks/overview_quantum_engineering.ipynb) |
| Experimental / simulator validation | Replay synthesized maps and compare performance | Planned beyond the fixed-policy pilot | Reproducible pilot inputs, exact benchmarks and validation protocol | Held-out replay, hardware integration and experimental comparisons | [Validation overview](https://github.com/mniehus/qsynth/blob/main/notebooks/overview_validation.ipynb) |

### Reproduce / explore this step

Start with the [system overview](https://github.com/mniehus/qsynth/blob/main/notebooks/00_system_overview.ipynb) and follow the domain links. The [seminar inventory](seminar-assets.md) identifies this table as the opening roadmap visual.
