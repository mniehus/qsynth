# Quantum circuits and QAOA

The Quantum Approximate Optimization Algorithm (QAOA) alternates cost and mixer evolution to prepare a parameterized state [1].

\[
|\psi(\boldsymbol\gamma,\boldsymbol\beta)\rangle=\prod_{r=1}^{p}e^{-i\beta_rH_M}e^{-i\gamma_rH_C}|+\rangle^{\otimes n}.
\]

- \(H_C\): cost Hamiltonian.
- \(H_M\): mixer Hamiltonian.
- \(\gamma_r,\beta_r\): variational parameters optimized classically.

Here \(r\) indexes \(p\) layers, \(n\) is the qubit count, and \(|+\rangle^{\otimes n}\) is the uniform starting state. \(|\psi\rangle\) is the output, and \(i\) in the exponent is the imaginary unit. Angle–operator products are dimensionless. Notebook 05 uses \(p=1\) and \(n=4\).

First baseline: shallow standard QAOA. Later comparisons: greater depth, constraint-preserving mixers, compact encodings, noise and device-aware compilation. QAOA is a baseline, not a presumption that it is optimal.

The cost Hamiltonian assigns energies to candidates and changes their quantum phases. The mixer Hamiltonian generates rotations that redistribute amplitudes between candidates. A classical search tunes the circuit angles, and repeated measurements provide a distribution of sampled solutions.

### Reproduce / explore this step

Compare Aer samples with the exact optimum in [Notebook 05](https://github.com/mniehus/qsynth/blob/main/notebooks/05_qaoa_2x2.ipynb).

The [combined QAOA reference](https://github.com/mniehus/qsynth/blob/main/notebooks/reference_qaoa_2x2.ipynb) records the earlier prototype. Its saved settings may require a locally generated IE instance.

### References

[1] E. Farhi, J. Goldstone and S. Gutmann, [A Quantum Approximate Optimization Algorithm](https://arxiv.org/abs/1411.4028), 2014.
