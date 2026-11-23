# QUBO representation

**QUBO** means Quadratic Unconstrained Binary Optimization:

\[
E(q)=q^TQq,\qquad q_i\in\{0,1\}.
\]

One-hot constraints may be introduced as penalties, e.g.

\[
A\left(\sum_jq_{ij}-1\right)^2.
\]

One-hot encoding uses one binary variable per regime?policy pair. Check that the lowest-energy states satisfy the constraints before proceeding to the [Ising mapping](ising.md).

## Reproduce this step

Compare feasible maps with all binary strings in [Notebook 03](https://github.com/mniehus/qsynth/blob/main/notebooks/03_policy_problem_to_qubo.ipynb).
