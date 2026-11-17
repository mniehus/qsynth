# From control to optimization

For \(N_\rho\) operating regimes and \(N_\psi\) candidate policies, the simulator evaluates

\[
J_{ij}=\text{performance of policy }j\text{ in regime }i.
\]

A binary one-hot representation uses

\[
q_{ij}\in\{0,1\},\qquad\sum_j q_{ij}=1.
\]

The problem becomes genuinely combinatorial when smoothness, switching costs, robustness or shared constraints couple decisions between regimes.

Strategy: exact small instances → strong classical baselines → physically meaningful scaling families → identical quantum formulations → resource/quality comparison.
