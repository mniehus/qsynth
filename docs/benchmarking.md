# Benchmarking

A successful QPU execution is not evidence of computational advantage. The **same problem instances** must be compared classically and quantum mechanically.

## Solution quality

Record best objective, optimality gap, probability of sampling an optimum, feasible-solution probability, and approximation ratio where meaningful.

## Quantum resources

Record logical qubits, transpiled qubits where applicable, circuit depth, one-/two-qubit gate counts, QAOA depth \(p\), shots, circuit evaluations and classical optimizer iterations.

## Time

Keep physics/simulation time, classical synthesis time, circuit construction/transpilation, simulator time, QPU execution and queue/wall time separate.

## Instance structure

Record \(N_\rho\), \(N_\psi\), coupling count/density, graph topology, coefficient range, constraints and robustness/scenario count. Variable count alone is not a difficulty metric.

## Reproduce this step

Compare an exact optimum with measured circuit outcomes and logical resources in [Notebook 06](https://github.com/mniehus/qsynth/blob/main/notebooks/06_coupled_policy_map.ipynb).

Compare valid-map counts, one-hot state spaces, and logical circuit resources across instance families in [Notebook 07 · Scaling policy maps](https://github.com/mniehus/qsynth/blob/main/notebooks/07_scaling_policy_maps.ipynb).

Compare qubit counts, interaction orders, and estimated cost-layer gates on identical chain instances in [Notebook 08 · Encoding comparison](https://github.com/mniehus/qsynth/blob/main/notebooks/08_encoding_comparison.ipynb). The logical estimates apply to independent parity-rotation synthesis before routing.

Separate algorithmic approximation, finite-shot variability, and modeled noise in [Notebook 10 · Device-aware Aer](https://github.com/mniehus/qsynth/blob/main/notebooks/10_noisy_device_aware_aer.ipynb). Report the mean objective conditional on feasibility alongside the feasible fraction. The best sampled score can equal the optimum even when optimal samples are uncommon.
