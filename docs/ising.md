# Ising mapping

The Ising model [1] assigns an energy to a configuration of interacting two-valued spins. Here a spin takes the eigenvalue of Pauli \(Z_i\) on qubit \(i\), with \(+1\) on \(\lvert0\rangle\) and \(-1\) on \(\lvert1\rangle\). The substitution \(q_i=(1-Z_i)/2\) recovers the original bit.

Here \(i\) indexes the encoded bit or qubit, \(q_i\) is a dimensionless bit, and \(Z_i\) is Pauli \(Z\) on that qubit. The bit is recovered from the eigenvalue on a basis state.

The cost Hamiltonian assigns an objective value to each basis state. Linear terms contribute local \(Z_i\) fields. Quadratic terms also contribute \(Z_iZ_k\) interactions. The constant offset shifts every energy equally and leaves the ordering unchanged.

### Reproduce / explore this step

Derive the Ising coefficients and verify the energies in [Notebook 04](https://github.com/mniehus/qsynth/blob/main/notebooks/04_qubo_to_ising.ipynb).

### References

[1] E. Ising, [Beitrag zur Theorie des Ferromagnetismus](https://doi.org/10.1007/BF02980577), 1925.
