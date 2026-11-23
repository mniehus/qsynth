# Seminar visual inventory

Use the [workflow](workflow.md) as the narrative and the [notebook sequence](notebook-sequence.md) for reproducibility and status.

| Stage | Notebook source | Existing figure or table | Reuse | Would an infographic help? |
|---|---|---|---|---|
| Information engine and feedback | 02; [IE model](information-engine.md) | Langevin equation and control path | Technical reference | Yes. Label the bead, trap, sensor, estimator and actuator, then show the closed loop. |
| Fixed-policy simulation | 02 | Regime–policy → trial → score equation and run summary | Yes, as a short method table | Yes. Show policy locked, repeat with seeds, then aggregate. |
| Local performance \(J_{ij}\) | 01, 02 | [Annotated heatmaps](assets/policy-matrix.png) | Yes, with the independent scales and provenance visible | No. |
| Exact lookup | 01 | Four scored policy maps | Yes | A highlight on the winning row is enough. |
| Coupled map and regime graph | 06 | [Two labeled regime chains](assets/coupled-policy-map.png) and weight sweep | Yes | No. Use the chain beside the sweep. |
| Binary / one-hot representation | 03 | All 16 strings with four feasible states marked | Yes, or crop to one valid and one invalid example | Optional. Show two bit groups with one selection each. |
| QUBO | 03, 06 | Energy and penalty columns | Yes | Optional. Annotate the score, feasibility penalty and coupling term. |
| Ising | 04 | Energy table and binary-to-spin derivation | Yes | A bit-to-spin mapping and constant-offset graphic would help. |
| QAOA circuit | 05, 06 | Depth-one circuit and shot histogram | Yes | Optional. Show preparation, cost, mixer and measurement blocks. |
| Logical and transpiled circuit | 09 | Two-SWAP routing diagram and resource table | Yes, label the target synthetic | Optional. Redraw the single routed interaction if the text diagram is small on a projector. |
| Ideal, finite-shot and noisy result | 10 | Outcome bars for optimum, other feasible and infeasible | Yes, label the noise model synthetic | No. Pair with the exact score and matched control. |
| Future QPU and IE replay | 10; [workflow](workflow.md) | Benchmark checklist and validation path | Use as a proposed method | Yes. Show the return to held-out IE validation. Performance data are pending. |

## Existing or external material to review

These entries identify where earlier material could fit. No external image was imported or regenerated.

- **Optical tweezer and information-engine schematic** · opening view of the bead, trap and feedback. External/generated visual — review before reuse.
- **Stochastic thermodynamics and fluctuation theorems** · background for the score and stochastic trajectories. External/generated visual — review before reuse.
- **Experimental validation infographic** · closing explanation of controlled replay and measured outcomes. External/generated visual — review before reuse.
- **Control and FPGA architecture** · show the fast-loop boundary and offline synthesis handoff. External/generated visual — review before reuse.
- **Related quantum-workflow infographics** · future visual sequence from exact map through QUBO, Ising, QAOA, routing, noise and validation. External/generated visual — review before reuse if available.

Before using external material, check terminology, arrows and numbers against the notebooks, and confirm attribution and permission to reuse.
