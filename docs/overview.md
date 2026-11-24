# Project overview

A Brownian bead in an optical tweezer provides a small physical system in which to ask how measurement and feedback change the work that can be extracted from thermal motion. The estimator infers bead position, and a classical controller commands trap shifts. Offline synthesis compares policies and proposes a lookup table. Validation returns that table to the simulator and eventually to the apparatus.

The [architecture](architecture.md) separates the plant and fast FPGA/RFSoC loop from the software design loop. [Quantum engineering](simulation.md) is the active focus within offline synthesis. The [roadmap](roadmap.md) shows the parallel work in physics, control, hardware and validation.

### Reproduce / explore this step

Read the [system overview notebook](https://github.com/mniehus/qsynth/blob/main/notebooks/00_system_overview.ipynb).
