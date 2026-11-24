# QUBO representation

**QUBO** means Quadratic Unconstrained Binary Optimization [1]. The objective assigns an energy to a bit string.

\[
E(q)=q^TQq,\qquad q_i\in\{0,1\}.
\]

\(q\) is the vector of dimensionless bits \(q_i\), \(Q\) holds coefficients in objective units, and \(E(q)\) is the energy to minimize.

One-hot constraints may be introduced as penalties, e.g.

\[
A\left(\sum_jq_{ij}-1\right)^2.
\]

\(A\) is the positive penalty weight in objective units. \(q_{ij}\) selects policy \(j\) in regime \(i\). Notebook 03 uses \(A=5\) in illustrative units.

One-hot encoding uses one binary variable per regime?policy pair. Check that the lowest-energy states satisfy the constraints before proceeding to the [Ising mapping](ising.md).

### Reproduce / explore this step

Compare feasible maps with all binary strings in [Notebook 03](https://github.com/mniehus/qsynth/blob/main/notebooks/03_policy_problem_to_qubo.ipynb).

### References

[1] F. Glover, G. Kochenberger and Y. Du, [A Tutorial on Formulating and Using QUBO Models](https://arxiv.org/abs/1811.11538), 2018 preprint.
