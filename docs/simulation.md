# Simulation with Qiskit Aer

**Qiskit** [1] is the primary quantum SDK. Its name is treated as a project/product name rather than a current formal acronym.

**Aer** [2] is Qiskit's high-performance simulator project; Aer is likewise a project name rather than an acronym.

Simulation ladder:

1. exact classical optimization;
2. ideal circuit simulation;
3. finite-shot simulation;
4. noisy/device-aware simulation;
5. real-QPU execution.

The first experiment is a Bell-state sanity check. The next experiment maps a tiny Q-SYNTH optimization instance through QUBO and Ising form before constructing a QAOA circuit.

A statevector simulator tracks the complex amplitudes of a pure quantum state. Finite-shot simulation samples measurement outcomes and shows sampling variability even without device noise. A physical quantum processing unit (QPU) has native gates and limited connectivity. Transpilation maps the logical circuit to those constraints and can change depth and gate counts.

Euro-Q-Exa is a prospective resource [5]. The teaching benchmark uses a synthetic target. Project access and backend-specific calibration are pending.

## From algorithm to target circuit

A target specifies physical qubits, allowed links, and native instructions. Placement assigns logical states to sites. Routing makes interactions possible across unconnected sites, for example by exchanging states with SWAP gates. Translation rewrites those operations in native gates. [3]

Compare topology-constrained and all-connected targets with the same native basis to estimate connectivity overhead. Device-specific gate durations, coherence, and gate and measurement fidelity are also needed to assess hardware feasibility.

### Reproduce / explore this step

Verify Bell-state preparation and measurement in [Notebook 00](https://github.com/mniehus/qsynth/blob/main/notebooks/00_environment_and_bell.ipynb).

Compare layouts, optimization levels, and circuit resources on a synthetic eight-site line in [Notebook 09 · Hardware-aware transpilation](https://github.com/mniehus/qsynth/blob/main/notebooks/09_hardware_aware_transpilation.ipynb).

Freeze the QAOA angles and compare exact probabilities, finite-shot variability, and noisy Aer in [Notebook 10 · Device-aware simulation](https://github.com/mniehus/qsynth/blob/main/notebooks/10_noisy_device_aware_aer.ipynb). Its noise model [4] uses reproducibly generated synthetic properties for the same topology. A matched run of the native circuit with noise disabled checks the effect of compilation and bit ordering before measuring the noise shift.

### References

[1] IBM Quantum, [Qiskit SDK documentation](https://quantum.cloud.ibm.com/docs/en/api/qiskit).

[2] Qiskit Aer, [AerSimulator](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html), version 0.18.4.

[3] IBM Quantum, [Transpiler stages](https://quantum.cloud.ibm.com/docs/en/qiskit/transpiler-stages).

[4] Qiskit Aer, [NoiseModel and backend-derived errors](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.noise.NoiseModel.html), version 0.18.4.

[5] EuroHPC JU, [Euro-Q-Exa inauguration](https://www.eurohpc-ju.europa.eu/inauguration-euro-q-exa-expanding-european-quantum-computing-infrastructure-2026-02-12_en), 2026.
