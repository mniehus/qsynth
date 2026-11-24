# From control to optimization

For \(N_\rho\) operating regimes and \(N_\psi\) candidate policies, the simulator evaluates

\[
J_{ij}=\text{performance of policy }j\text{ in regime }i.
\]

Here \(i\) indexes regimes, \(j\) indexes policies, and \(J_{ij}\) has the declared score units of the instance. Notebook 01 uses illustrative units and Notebook 02 uses \(k_BT/\mathrm{s}\) from the simulator.

A binary one-hot representation uses

\[
q_{ij}\in\{0,1\},\qquad\sum_j q_{ij}=1.
\]

Each \(q_{ij}\) is a dimensionless selection bit. The constraint applies to each fixed regime \(i\).

The problem becomes genuinely combinatorial when smoothness, switching costs, robustness or shared constraints couple decisions between regimes.

Strategy: exact small instances → strong classical baselines → physically meaningful scaling families → identical quantum formulations → resource/quality comparison.

### Reproduce / explore this step

Enumerate the four policy maps in [Notebook 01](https://github.com/mniehus/qsynth/blob/main/notebooks/01_policy_lookup_2x2.ipynb).
