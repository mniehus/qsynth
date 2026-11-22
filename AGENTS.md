# Q-SYNTH repository guidance

Q-SYNTH studies quantum-assisted offline synthesis of estimator/controller policies for a stochastic information engine. The fast feedback loop remains classical, with FPGA/RFSoC as the intended experimental platform.

**Engineering chain.** IE simulator → regime × policy performance matrix \(J_{ij}\) → classical policy-map optimization → QUBO → Ising Hamiltonian → QAOA and quantum simulation → benchmarking → validation of synthesized policy maps back in the IE simulator.

- Keep the IE simulator and quantum code modular. Change physical models only when explicitly requested.
- Prefer small, testable changes and run relevant tests after each implementation step. Keep unrelated refactoring out of scoped work. If a task depends on a broken interface, identify and fix the smallest missing interface.
- Record package versions, seeds, shots, optimizer settings, instance parameters, and backend. Update [the engineering logbook](docs/logbook.md) for scientifically or architecturally meaningful experiments.
- Use notebooks for explanation and experimentation. Put reusable logic in Python modules and show the important QUBO, Ising, and QAOA transformations explicitly in teaching notebooks.
- Clearly label illustrative and IE-derived instances. Compare quantum results with exact or strong classical baselines on the same instances.
- Keep the emphasis on informatics and quantum engineering, with enough thermodynamics and FPGA context to explain the application.

See [project goals](GOALS.md), the [implementation plan](PLANS.md), and [current status](docs/status.md).
