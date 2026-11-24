# Stochastic thermodynamics

Work and heat fluctuate across individual trajectories [1]. In the harmonic trap, potential energy rises quadratically with displacement:
\[
U(x,\lambda)=\tfrac12\kappa(x-\lambda)^2.
\]
Here \(U\) is potential energy [J], \(x\) and \(\lambda\) are bead and trap positions [m], and \(\kappa=7.3\times10^{-6}\) N/m in the simulator. Displacing the trap performs signed parameter work \(W=\int(\partial U/\partial\lambda)\,d\lambda\) [J] along the protocol.

## Work and free energy

The Jarzynski equality relates repeated work measurements to a free-energy change when the initial state is equilibrated [2].
\[
\langle e^{-\beta W}\rangle=e^{-\beta\Delta F}.
\]
Here \(\Delta F\) is the equilibrium free-energy difference [J], \(W\) is input work [J], and \(\beta=1/(k_BT)\) [J\(^{-1}\)]. \(T\) is the bath temperature [K] and \(k_B\) the Boltzmann constant [J/K]. Angle brackets average over runs.

Crooks' relation compares a forward drive with its time-reversed protocol, each initialized in its corresponding equilibrium state [3].
\[
\frac{P_F(W)}{P_R(-W)}=e^{\beta(W-\Delta F)}.
\]
\(P_F\) and \(P_R\) are the forward and reverse work densities [J\(^{-1}\)]. Work and free-energy signs refer to the forward drive.

## Measurement and feedback

Under the feedback protocol assumptions of Sagawa and Ueda, a generalized equality includes trajectory-level information [4].
\[
\left\langle e^{-\beta(W-\Delta F)-I}\right\rangle=1.
\]
\(I\) is the dimensionless information for a measured outcome. Its average is mutual information in nats for natural logarithms. Feedback uses that information to choose how to act on the bead.

**Informatics view.** Maxwell's demon highlights how measurement, memory, and feedback enter a physical cycle. Under the standard isothermal reset assumptions, erasing one equiprobable bit has a minimum heat cost of \(k_BT\ln 2\) [J] [5, 6]. That bound is about the reset operation. The present simulated score accounts for work and power in the modeled plant and trap.

### Reproduce / explore this step

Follow the [physics overview](https://github.com/mniehus/qsynth/blob/main/notebooks/overview_physics_thermodynamics.ipynb). [Notebook 02](https://github.com/mniehus/qsynth/blob/main/notebooks/02_build_cost_matrix_from_ie.ipynb) illustrates simulated power accounting. Experimental tests of the fluctuation relations are planned.

### References

[1] U. Seifert, [Stochastic thermodynamics, fluctuation theorems and molecular machines](https://doi.org/10.1088/0034-4885/75/12/126001), 2012.

[2] C. Jarzynski, [Nonequilibrium Equality for Free Energy Differences](https://doi.org/10.1103/PhysRevLett.78.2690), 1997.

[3] G. E. Crooks, [Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences](https://doi.org/10.1103/PhysRevE.60.2721), 1999.

[4] T. Sagawa and M. Ueda, [Generalized Jarzynski Equality under Nonequilibrium Feedback Control](https://doi.org/10.1103/PhysRevLett.104.090602), 2010.

[5] R. Landauer, [Irreversibility and Heat Generation in the Computing Process](https://doi.org/10.1147/rd.53.0183), 1961.

[6] C. H. Bennett, [The thermodynamics of computation—a review](https://doi.org/10.1007/BF02084158), 1982.
