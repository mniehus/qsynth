# Q-SYNTH repository guidance

Q-SYNTH asks whether information, measurement and feedback can be used to extract useful work from thermal fluctuations, and how estimator/controller policies for the engine can be synthesized and implemented. Quantum engineering is the current focus within offline synthesis. The fast feedback loop remains classical, with FPGA/RFSoC as the intended experimental platform.

**Engineering chain.** IE simulator → regime × policy performance matrix \(J_{ij}\) → classical policy-map optimization → QUBO → Ising Hamiltonian → QAOA and quantum simulation → benchmarking → validation of synthesized policy maps back in the IE simulator.

- Keep the IE simulator and quantum code modular. Change physical models only when explicitly requested.
- Prefer small, testable changes and run relevant tests after each implementation step. Keep unrelated refactoring out of scoped work. If a task depends on a broken interface, identify and fix the smallest missing interface.
- Record package versions, seeds, shots, optimizer settings, instance parameters, and backend. Update [the engineering logbook](docs/logbook.md) for scientifically or architecturally meaningful experiments.
- Use notebooks for explanation and experimentation. Put reusable logic in Python modules and show the important QUBO, Ising, and QAOA transformations explicitly in teaching notebooks.
- Write seminar materials for Informatics engineering students. Explain unfamiliar terms at first use and preserve their physical meaning. Use brief **Informatics view**, **Physics / quantum view**, or **Why it matters in Q-SYNTH** callouts where helpful.
- Use MkDocs for structured explanation and navigation. Link topics to the GitHub notebooks under **Reproduce / explore this step**. Keep executable derivations and experiments in notebooks and reusable implementation in Python modules.
- Keep a **Presentation asset** section at the end of each teaching notebook and name its MkDocs topic. Guide students and collaborators into the same core notebook sequence.
- Clearly label illustrative and IE-derived instances. Compare quantum results with exact or strong classical baselines on the same instances.
- Present physics, information theory, feedback control, FPGA/RFSoC, optimization, quantum engineering, and validation as one project. Distinguish illustrative, simulator-derived, experimentally measured, and planned work.
- Introduce important equations with their meaning, define symbols and units next to them, and include representative values when justified. Cite established results with local numerical references and add only cited sources to the References section.

See [project goals](GOALS.md), the [implementation plan](PLANS.md), and [current status](docs/status.md).
