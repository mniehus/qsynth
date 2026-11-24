# Build the IE cost matrix

Each row is an operating regime, such as a sensor-noise level. Each column is a fixed set of estimator and controller parameters. To estimate a cell, apply its policy before the first simulation tick, disable supervisor switching, and repeat the trial with controlled seeds.

The teaching example scores gravitational power minus signed trap power after warm-up. The mean gives the performance \(J_{ij}\). Reuse the same seeds across policies within each regime to compare paired differences and report their uncertainty.

### Reproduce / explore this step

Run the fixed-policy IE trials in [Notebook 02](https://github.com/mniehus/qsynth/blob/main/notebooks/02_build_cost_matrix_from_ie.ipynb).
