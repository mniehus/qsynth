# Information engine

An optical tweezer uses focused light to confine a bead. Collisions with the surrounding fluid produce Brownian motion. In the overdamped approximation, inertia is neglected and the trap, gravity and thermal forcing determine the trajectory [1, 2].

\[
\gamma\dot x=-\kappa(x-\lambda)-m_{\rm eff}g+\sqrt{2\gamma k_BT}\,\xi(t).
\]

| Symbol | Meaning and units | Simulator default where fixed |
|---|---|---|
| \(t, x, \dot x\) | Time [s], upward bead position [m], and formal velocity [m/s] | Trajectory-dependent |
| \(\lambda\) | Trap centre [m] | Actuator state |
| \(\gamma\) | Viscous drag coefficient [N·s/m] | \(2.83\times10^{-8}\) |
| \(\kappa\) | Trap stiffness [N/m] | \(7.3\times10^{-6}\) |
| \(m_{\rm eff}\), \(g\) | Buoyant mass [kg], gravity [m/s²] | \(1.41\times10^{-14}\), 9.81 |
| \(k_B,T\) | Boltzmann constant [J/K], bath temperature [K] | \(1.380649\times10^{-23}\), 298.15 |
| \(\xi(t)\) | Zero-mean white noise with unit delta covariance [s\(^{-1/2}\)] | Stochastic input |

**Why it matters in Q-SYNTH.** The score comes from trajectories and trap work under controlled measurement and timing conditions. The numbers above are model settings from `ie/config.py`. Experimental calibration is still required.

### Reproduce / explore this step

Read the [physics overview](https://github.com/mniehus/qsynth/blob/main/notebooks/overview_physics_thermodynamics.ipynb) and run [Notebook 02](https://github.com/mniehus/qsynth/blob/main/notebooks/02_build_cost_matrix_from_ie.ipynb).

### References

[1] P. Langevin, [On the Theory of Brownian Motion](https://www2.math.uconn.edu/~gordina/Langevin1908.pdf), 1908, English translation by D. S. Lemons and A. Gythiel.

[2] U. Seifert, [Stochastic thermodynamics, fluctuation theorems and molecular machines](https://doi.org/10.1088/0034-4885/75/12/126001), 2012.
