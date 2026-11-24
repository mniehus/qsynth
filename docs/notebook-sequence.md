# Notebook sequence and review

This review is for Informatics engineering students. Start with the question and prediction, run the worked example, then use the result and presentation asset to explain the conclusion back to someone else.

| Notebook | Core question | Concept | Equation or representation | Main result | Execution | Scientific status | Teaching status | Seminar visual | Remaining action |
|---|---|---|---|---|---|---|---|---|---|
| [00 · environment and bell](https://github.com/mniehus/qsynth/blob/main/notebooks/00_environment_and_bell.ipynb) | Can Aer prepare and measure a Bell state? | Amplitudes and measurement | Equal amplitudes on 00 and 11 | 510 / 490 counts | Pass | Stack check | Ready | Circuit and two-bar histogram | Use as an environment check. |
| [01 · policy lookup 2x2](https://github.com/mniehus/qsynth/blob/main/notebooks/01_policy_lookup_2x2.ipynb) | Which policy wins in each regime? | Exact lookup | Add one score per row | Nominal / robust, score −2 | Pass | Illustrative only | Ready | 2×2 matrix and four scored maps | Explain that all scores are arbitrary units. |
| [02 · build cost matrix from ie](https://github.com/mniehus/qsynth/blob/main/notebooks/02_build_cost_matrix_from_ie.ipynb) | Where do matrix entries come from? | Fixed policies and paired seeds | J = gravitational minus signed trap power | 20 trials; robust − nominal is −1.56 / +2.05 kBT/s | Pass | IE-derived pilot | Ready with caveat | Mean scores, paired uncertainty and heatmap | Validate on held-out seeds and connect to a measured coupled case. |
| [03 · policy problem to qubo](https://github.com/mniehus/qsynth/blob/main/notebooks/03_policy_problem_to_qubo.ipynb) | How do bits express a policy map? | One-hot and feasibility | One set bit per regime; quadratic penalty | 4 of 16 strings feasible; energy 2 wins | Pass | Illustrative only | Ready | 16-state feasibility table | Distinguish physical performance from QUBO energy. |
| [04 · qubo to ising](https://github.com/mniehus/qsynth/blob/main/notebooks/04_qubo_to_ising.ipynb) | Why use an Ising operator? | Binary-to-spin substitution | q = (1 − Z)/2 | All 16 energies agree after adding 8.75 | Pass | Illustrative only | Ready | Energy comparison with constant offset | Keep display order distinct from Qiskit order. |
| [05 · qaoa 2x2](https://github.com/mniehus/qsynth/blob/main/notebooks/05_qaoa_2x2.ipynb) | Can QAOA sample the exact winner? | Cost and mixer layers | One QAOA layer | Default: 90.92% feasible, 59.77% optimal | Pass | Illustrative default; optional IE pilot | Ready with caveat | Circuit and outcome histogram | Tag the input when quoting rates. |
| [06 · coupled policy map](https://github.com/mniehus/qsynth/blob/main/notebooks/06_coupled_policy_map.ipynb) | When does one regime affect another? | Graph coupling | Local score less weighted switches | 1212 → 1112 → 2222 as weight rises | Pass | Illustrative only | Ready | Regime chain and weight sweep | Introduce the coupling separately from the local matrix. |
| [07 · scaling policy maps](https://github.com/mniehus/qsynth/blob/main/notebooks/07_scaling_policy_maps.ipynb) | How does problem size grow? | Valid maps versus binary space | Policies raised to regimes; one-hot bits per pair | 4×3 and 6×2 use 12 bits but have 30 and 16 couplings | Pass | Illustrative only | Ready | Growth and resource tables | Treat local solve timings as illustrative. |
| [08 · encoding comparison](https://github.com/mniehus/qsynth/blob/main/notebooks/08_encoding_comparison.ipynb) | How does encoding change resources? | One-hot versus compact | Compact bits per regime = ceiling of log₂ policies | Exact optima agree up to 4×4 | Pass | Exact small cases; analytical larger counts | Ready with caveat | Qubits, interaction order and estimated CNOTs | Identify the parity-ladder assumption. |
| [09 · hardware aware transpilation](https://github.com/mniehus/qsynth/blob/main/notebooks/09_hardware_aware_transpilation.ipynb) | What does target compilation change? | Placement, routing and basis | Logical circuit → native gates and sites | Level 1 compact/one-hot depth 17/52; 6/42 CX | Pass | Synthetic target | Ready with caveat | Routed RZZ and before/after table | Keep target and router labels visible. |
| [10 · noisy device aware aer](https://github.com/mniehus/qsynth/blob/main/notebooks/10_noisy_device_aware_aer.ipynb) | What changes with finite shots and noise? | Approximation, sampling and modeled errors | Compare identical native circuits with noise off/on | One-hot feasibility 49.58% → 43.59% | Pass | Synthetic noise | Ready with caveat | Outcome distribution with infeasible group | Use model-specific language; discuss matched control. |

## Reproduce the sequence

Verified on 23 November 2026 in fresh, separate kernels using the project `.venv`. The environment used Python 3.15.2, NumPy 2.5.5, Qiskit 2.6.2, Aer 0.18.4, and Matplotlib 3.11.2. Install from the repository root with `python -m pip install -r requirements.txt`, select that Python kernel, then use **Restart Kernel and Run All Cells**. Start the kernel within the checkout so Notebook 02 can import the local IE modules.

| Notebook | Execution assumptions |
|---|---|
| 00 | Aer, 1,000 shots, seed 42. |
| 01 | Exact enumeration; no seed. |
| 02 | Local IE evaluator; 2/6 nm; five matched seeds 42–46; 1 s per run, 0.1 s warm-up. |
| 03 | Exact enumeration; no seed. |
| 04 | NumPy and Qiskit operators; no seed. |
| 05 | Statevector grid 48×32; Aer 4,096 shots; simulator/transpiler seeds 42. |
| 06 | Statevector grid 32×24; Aer 8,192 shots; seed 42. |
| 07 | Exact enumeration; optional preview runs on Aer (32×24; 8,192 shots; seed 42). |
| 08 | NumPy exact checks for small cases; no seed. |
| 09 | Ideal Aer 8,192 shots; grid 32×24; synthetic topology and transpiler seeds 42. |
| 10 | Aer statevector/density matrix; 100–10,000 ideal shots, 4,096 mapped; five seeds 42–46; target/transpiler seed 42. |

The numbered default runs require no downloaded data, remote backend, or QPU account. Notebook 05's optional version-1 IE `instance.json` input also passed, with score 137.9594 kBT/s for the exact map and 22.46% optimal shots. Generate that input with `python ie/run_synthesis_offline.py`. The output folders are Git-ignored. The combined reference is outside this audit and its saved input may require a local run.

IPKernelApp emitted its local TCP transport warning. No API deprecation warnings surfaced in the run. The saved and rerun Notebook 05 selected different transpiled gate mixes despite the fixed seed, with the same reported feasibility and optimality. Treat Notebook 07's wall-clock times as machine- and load-dependent. For device comparisons, retain the actual compiled circuit as well as the software versions, target and seed.

## Scientific and teaching continuity

- **Signs and units.** Notebook 02 reports performance as gravitational power minus signed trap power. Its runner stores the negative as cost. Higher performance wins in the policy tables, while lower energy wins in QUBO and Ising. The illustrative matrices use arbitrary units. Their scales and the IE-derived kBT/s scores cannot be compared numerically.
- **Three instances.** Notebooks 01 and 03–05 default to the uncoupled illustrative 2×2 case. Notebook 02 measures a separate 2×2 IE pilot. Notebook 06 introduces an illustrative 4×2 chain. Notebooks 07–08 extend that family, and 09–10 return to the same 4×2 chain for compilation and noise comparisons.
- **Angle and bit conventions.** In Notebook 05, beta is a mixer angle. In the coupled notebooks it denotes switching weight, and theta denotes the mixer angle. Policy-map labels are one-based in regime order. Qiskit bit strings display the highest-index bit first, so decode by logical bit index and account for final placement.
- **Benchmarks.** A low best-observed objective gap can coincide with low optimal frequency. Mean scores in Notebook 10 are conditional on feasibility. Synthetic targets and modeled errors support engineering discussion, while an application benchmark requires measured inputs, held-out validation, and eventually device results.
- **Structure.** All numbered notebooks present a question, concept, worked example, prediction, result, takeaway, seminar asset, and next step. Some combine related headings or place the prediction before the code so students can try it first. For a live demonstration, define score versus energy before Notebook 03 and explain the change of instance again at Notebook 06.

## Recommended order

Open the [system overview](https://github.com/mniehus/qsynth/blob/main/notebooks/00_system_overview.ipynb) first. For the detailed labs, keep **00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10** for self-study. The small lookup and uncoupled derivations introduce the notation before the longer simulator run and the coupled extension.

| Layer | Current files | Naming recommendation |
|---|---|---|
| Project entry | `00_system_overview.ipynb` | Present first in the documentation. |
| Field guides | `overview_*.ipynb` | Keep a separate, unnumbered family. |
| Detailed labs | Existing `00_environment_and_bell.ipynb` through `10_noisy_device_aware_aer.ipynb` | Keep current names and links. If a future filename migration is needed, prefix the detailed labs with `lab_` and update links together. |

The two `00` files serve different entry points. The system overview introduces the project, and the Bell notebook opens the quantum lab sequence.

For the seminar, open with the [physical feedback loop](information-engine.md), then use **02 → 01 → 06 → 03 → 04 → 05 → 07 → 08 → 09 → 10** by topic. Use 00 as an optional Bell-state primer. Show the measured matrix before selecting a policy map. Introduce coupling before encoding, then teach the QUBO and Ising mechanics on the simpler 2×2 example and point back to the coupled derivation in 06. Finish with the [proposed hardware and IE validation loop](workflow.md). This route addresses the numbering mismatch without renaming files.

## Presentation readiness

### Ready to present

The matrix-to-map story, exact tiny optima, QUBO–Ising energy checks, encoding trade-off table, synthetic routing comparison, and matched ideal/noisy distribution have a reproducible technical basis.

### Needs review

Before using the IE pilot as evidence of policy quality, review uncertainty, freeze the instance provenance, and replay on held-out seeds. Before discussing hardware counts, state which assumptions describe a synthetic target and which will depend on the eventual device.

### Missing

A reviewed end-to-end graphic connecting the physical feedback loop to offline synthesis and replay would fill the biggest visual gap. Device-specific target and calibration data, a real QPU run, and a held-out IE validation of the selected map are pending. The project is ready for an exploratory hardware-team discussion about access, target format, calibration metadata and a fair benchmark. It has not yet demonstrated hardware or application performance.
