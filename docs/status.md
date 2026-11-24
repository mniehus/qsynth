# Project status

## Completed

- The Bell-state notebook verifies the local Python, Qiskit, and Aer environment.
- Teaching notebooks 01–05 cover exact policy lookup, fixed-policy IE evaluation, QUBO, Ising, and depth-one QAOA. All five ran end to end in the project environment.
- The IE notebook evaluated 20 trials across two sensor-noise regimes, two policies, and five matched seeds. The QAOA notebook also ran with the corresponding local IE-derived instance.
- Notebook 06 verifies an illustrative coupled four-regime chain by exact enumeration and QUBO–Ising energy equivalence. Depth-one Aer sampling recovered the exact optimum.
- Notebook 07 is the first explicit scaling study. It solves ten illustrative cases exactly, records one-hot resource counts, and samples the two smallest chain cases with depth-one QAOA in Aer.
- Notebook 08 compares one-hot and compact encodings on five illustrative chain instances. Exact checks agree through 4×4. The two eight-regime cases report analytical resources.
- Notebook 09 compiles both encodings of the validated 4×2 chain on a synthetic eight-site line. It compares levels 0, 1 and 3, verifies circuit equivalence, and measures routing overhead against an all-connected target with the same basis.
- Notebook 10 uses the same circuits to compare exact probabilities, repeated ideal shots, and noisy Aer on the synthetic line. A matched native-circuit control isolates the effect of enabling the model.
- All 11 numbered notebooks ran end to end in fresh local kernels. The [sequence review](notebook-sequence.md) records reproducibility and presentation caveats. The [workflow](workflow.md) and [seminar visual inventory](seminar-assets.md) consolidate the evidence.

## Current

- The [interdisciplinary roadmap](roadmap.md) tracks field maturity. Quantum engineering is the active focus within offline synthesis. The [system overview](https://github.com/mniehus/qsynth/blob/main/notebooks/00_system_overview.ipynb) is the preferred first notebook.

- Use the illustrative matrix as the common teaching reference. The saved notebook outputs distinguish the illustrative optimization from the measured IE pilot.
- The verified benchmark supports an exploratory hardware-team discussion about target data, access and evaluation. Device results and held-out IE validation are pending.

## Next

- Phase 11, `11_first_qpu_execution.ipynb`, should reuse the validated instance, objective, decoder and benchmark methodology on real hardware when authorized.
- Freeze a reproducible IE-derived reference instance and verify its selected policy map on held-out IE seeds.

The default QAOA result uses illustrative scores. The IE-derived run is a local pilot, and an application benchmark is still pending.
