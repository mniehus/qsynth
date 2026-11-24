# Coupled policy maps

With additive scores, each regime can select its best policy independently. A switching penalty changes this when neighboring regimes prefer different policies. The regime graph specifies which choices interact. The mismatch cost specifies which policy pairs pay a penalty. Its weight sets the importance of switching relative to local performance.

On the four-regime teaching example, increasing the weight takes the optimum from an alternating map to a map with one transition, then to a constant map. Exact enumeration provides a reference for the binary encoding and quantum samples.

### Reproduce / explore this step

Sweep switching weights and verify the coupled encoding in [Notebook 06](https://github.com/mniehus/qsynth/blob/main/notebooks/06_coupled_policy_map.ipynb).
