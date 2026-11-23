# Ising mapping

An Ising model assigns an energy to a configuration of interacting two-valued spins. Here a spin takes the eigenvalue of Pauli \(Z_i\) on qubit \(i\), with \(+1\) on \(\lvert0\rangle\) and \(-1\) on \(\lvert1\rangle\). The substitution \(q_i=(1-Z_i)/2\) recovers the original bit.

The cost Hamiltonian assigns an objective value to each basis state. Linear terms contribute local \(Z_i\) fields. Quadratic terms also contribute \(Z_iZ_k\) interactions. The constant offset shifts every energy equally and leaves the ordering unchanged.

## Reproduce this step

Derive the Ising coefficients and verify the energies in [Notebook 04](https://github.com/mniehus/qsynth/blob/main/notebooks/04_qubo_to_ising.ipynb).
