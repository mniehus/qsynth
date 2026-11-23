# Q-SYNTH implementation plan

Simulate → build \(J_{ij}\) → exact classical solution → QUBO → Ising → QAOA → coupling → scaling → robustness → validate the selected policy map back in the IE simulator.

The filenames below define the teaching sequence. [The combined QAOA prototype](notebooks/reference_qaoa_2x2.ipynb) serves as a working reference outside that sequence.

| Phase | Notebook | Scope |
|---|---|---|
| **0 · Environment and quantum basics** | `00_environment_and_bell.ipynb` | Verify Python, Qiskit, and Aer with a Bell-state sanity check. Introduce amplitudes, measurement, shots, and unitarity. |
| **1 · Policy-map formulation** | `01_policy_lookup_2x2.ipynb` | Explain two operating regimes, two candidate policies, and what each entry of the 2×2 matrix \(J_{ij}\) measures. Enumerate the four valid maps and compute the exact optimum. Save binary and quantum formulations for later phases. |
| **2 · IE-derived costs** | `02_build_cost_matrix_from_ie.ipynb` | For each regime \(i\) and fixed policy \(j\), disable supervisor switching and run repeated stochastic simulations with matched seeds. Use one simple scalar objective until the pipeline is validated, then estimate the mean and uncertainty of each \(J_{ij}\). |
| **3 · Policy problem to QUBO** | `03_policy_problem_to_qubo.ipynb` | Introduce one-hot variables \(q_{ij}\), the performance term, and the one-policy-per-regime penalty. Enumerate all binary states, label feasibility, and identify the exact optimum. |
| **4 · QUBO to Ising** | `04_qubo_to_ising.ipynb` | Derive \(q=(1-Z)/2\) step by step, construct the Ising Hamiltonian, and verify energy equivalence on all states with the constant offset accounted for. |
| **5 · QAOA on the 2×2 instance** | `05_qaoa_2x2.ipynb` | Use the verified Ising Hamiltonian and a standard mixer. Start at \(p=1\) in Aer. Record optimized parameters, feasible- and optimal-solution probabilities, and sampled objective statistics. Compare with the exact classical optimum. |
| **6 · Coupled policy maps** | `06_coupled_policy_map.ipynb` | Start with a simple regime chain or grid and add a neighboring-regime smoothness or switching cost. Compare independent row-wise choices with the global optimum and show when they differ. Specify the local matrix \(J_{ij}\) and the regime/policy coupling structure separately. |
| **7 · Scaling** | `07_scaling_policy_maps.ipynb` | Vary \(N_\rho\), \(N_\psi\), graph topology and coupling density, penalty strength, QAOA depth, and shots. Record valid maps \(N_\psi^{N_\rho}\), binary variables and qubits, QUBO/Ising couplings, logical and relevant transpiled depths, one- and two-qubit gate counts, runtime, and solution quality. |
| **8 · Encoding comparison** | `08_encoding_comparison.ipynb` | Compare one-hot and compact encodings. Later, evaluate constraint-preserving approaches such as an XY mixer. |
| **9 · Hardware-aware transpilation** | `09_hardware_aware_transpilation.ipynb` | Map the same logical cost circuits to representative hardware constraints. Compare depth, routing, native gate counts, and the effect of encoding. |
| **10 · Device-aware simulation** | `10_noisy_device_aware_aer.ipynb` | Compare ideal statevector predictions, ideal finite-shot Aer, and noisy Aer on the same circuits before real QPU execution. |

Close the loop by replaying selected maps in the IE simulator and comparing their performance with the classical baseline under the same validation scenarios.

Later benchmarking should compare identical instances across exact or structured classical solvers, classical heuristics, ideal and finite-shot QAOA, noisy or device-aware simulation, and eventually QPU execution.

Later robust synthesis should use repeated IE evaluations to compare mean, variance-penalized, and worst-case objectives. Thermodynamic and multiobjective terms can follow.
