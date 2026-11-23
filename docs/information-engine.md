# Information engine

The reference system is a Brownian particle in a harmonic optical trap. A simplified overdamped model is

\[
\gamma\dot x=-\kappa(x-\lambda)-m_{\rm eff}g+\sqrt{2\gamma k_BT}\,\xi(t).
\]

The physical model supplies realistic operating regimes, candidate policies, the performance matrix \(J_{ij}\), timing/noise constraints and possible thermodynamic objectives. The quantum optimization problem is therefore generated from a physical/control problem rather than selected arbitrarily.

An optical tweezer uses focused light to confine the bead. Brownian motion comes from thermal collisions in the surrounding fluid. The equation above is an overdamped Langevin equation: restoring force and gravity set the drift, while thermal noise makes individual trajectories vary.

## Reproduce this step

Evaluate the simulated engine under fixed policies in [Notebook 02](https://github.com/mniehus/qsynth/blob/main/notebooks/02_build_cost_matrix_from_ie.ipynb).
