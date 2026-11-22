# Q-SYNTH goals

Quantum computing initially supports offline policy synthesis and optimization. The fast estimator/controller feedback loop remains classical, with FPGA/RFSoC as the intended experimental platform.

1. Restore and validate the modular information-engine (IE) simulator.
2. Generate regime × policy performance matrices from fixed-policy IE simulations.
3. Establish exact classical policy-map baselines.
4. Formulate the same problems as QUBOs and Ising Hamiltonians.
5. Execute QAOA in Qiskit Aer, then on a real QPU.
6. Study scaling, coupling, encoding, feasibility, noise, and robustness.
7. Validate synthesized policy maps back in the IE simulator.
8. Maintain reproducible Python code, notebooks, tests, and an engineering logbook.
9. Publish selected material through GitHub Pages.
10. Support two entry audiences, [MEIM students](docs/start-meim.md) and [project collaborators](docs/start-collaborators.md).
