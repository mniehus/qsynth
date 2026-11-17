# Simulation with Qiskit Aer

**Qiskit** is the primary quantum SDK. Its name is treated as a project/product name rather than a current formal acronym.

**Aer** is Qiskit's high-performance simulator project; Aer is likewise a project name rather than an acronym.

Simulation ladder:

1. exact classical optimization;
2. ideal circuit simulation;
3. finite-shot simulation;
4. noisy/device-aware simulation;
5. real-QPU execution.

The first experiment is a Bell-state sanity check. The next experiment maps a tiny Q-SYNTH optimization instance through QUBO and Ising form before constructing a QAOA circuit.
