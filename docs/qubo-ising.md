# QUBO and Ising mapping

**QUBO** means Quadratic Unconstrained Binary Optimization:

\[
E(q)=q^TQq,\qquad q_i\in\{0,1\}.
\]

One-hot constraints may be introduced as penalties, e.g.

\[
A\left(\sum_jq_{ij}-1\right)^2.
\]

Using

\[
q_i=\frac{1-Z_i}{2},
\]

the objective becomes an Ising-type cost Hamiltonian

\[
H_C=c+\sum_i h_iZ_i+\sum_{i<j}J_{ij}Z_iZ_j.
\]

Encoding is itself part of the research problem: one-hot is simple but qubit-expensive and admits infeasible states; compact encodings and constraint-preserving mixers are alternatives.
