# Q-SYNTH implementation plan

Simulate → build \(J_{ij}\) → exact classical solution → QUBO → Ising → QAOA → coupling → scaling → robustness → validate the selected policy map back in the IE simulator.

The filenames below define the target teaching sequence. The current `01_qaoa_2x2.ipynb` combines several phases and serves as a working reference for the split.

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
| **9 · Classical versus quantum benchmark** | `09_classical_vs_quantum_benchmark.ipynb` | Use identical instances for exact enumeration on small cases, a strong structured classical solver where applicable, a classical heuristic, ideal QAOA, finite-shot QAOA, noisy/device-aware QAOA, and later a real QPU. |
| **10 · Robust synthesis** | `10_robust_policy_synthesis.ipynb` | Use repeated IE evaluations to obtain distributions \(J_{ij}^{(r)}\). Compare mean, mean minus a variance penalty for performance maximization (mean plus a penalty for cost minimization), and worst-case objectives. Add thermodynamic or multiobjective terms later. |

Close the loop by replaying selected maps in the IE simulator and comparing their performance with the classical baseline under the same validation scenarios.
