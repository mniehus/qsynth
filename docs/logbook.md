# Quantum engineering logbook

The logbook records **what was actually done**, including unsuccessful experiments and changed decisions. It supports reproducibility, later reporting and the seminar.

---

## 2026-11-17 — QE-000: local quantum environment

### Question
Can a clean local Python/Qiskit environment be established as the reproducible starting point?

### Environment
- Python **3.15.2**
- Qiskit **2.6.2**
- Qiskit Aer **0.18.4**
- VS Code with a dedicated Python virtual environment

### Result
Qiskit and Qiskit Aer import successfully and report the versions above.

### Decision
Use Qiskit as primary SDK and Qiskit Aer as initial simulator. Reusable implementation stays in Python modules; Jupyter notebooks are used for explanation and experiments.

### Next experiment — QE-001
Run a seeded ideal Bell-state circuit in Aer. Verify that only `00` and `11` are measured.

### Interpretation
QE-001 is only an installation/simulator sanity check; it is not evidence about QAOA or Q-SYNTH optimization.

---

## 2026-11-23 — 2×2 teaching sequence and IE pilot

- **Environment** · Python 3.15.2, Qiskit 2.6.2, and Aer 0.18.4 in the project virtual environment. Notebooks 01–05 executed end to end in fresh kernels.
- **IE input** · Fixed nominal and robust policies at 2 and 6 nm sensor RMS, 1 s per trial with 0.1 s warm-up, matched seeds 42–46. Notebook 02 reran 20 trials through the existing evaluator. In baseline/elevated row order and nominal/robust column order, the mean performance scores were `[[72.0745, 70.5170], [63.8302, 65.8849]]` in kBT/s. Robust minus nominal was −1.56 and +2.05 kBT/s, with paired standard errors of 0.43 and 0.57.
- **Illustrative reference** · Scores `[[-1, -3], [-2.5, -1]]`, no switching term, one-hot penalty 5. Exact enumeration selected nominal then robust, with minimization objective 2. The QUBO and Ising energies agreed on all 16 states after adding the 8.75 offset.
- **QAOA** · Four qubits, standard X mixer, \(p=1\), 48×32 ideal statevector grid, and 4,096 shots on `aer_simulator`. Simulation and transpiler seeds were both 42. Logical circuit depth was 4 with four H, four RZ, two RZZ, and four RX gates.
- **Illustrative sampling** · \((\gamma,\beta)=(1.701696,2.356194)\) radians. The best sampled objective was 2, with 90.92% feasible and 59.77% optimal shots.
- **IE-derived sampling** · Notebook 05 also loaded the existing local five-seed JSON. It used zero switching cost, a one-hot penalty of \(\sum_{ij}|J_{ij}|+1\), and scaled the gamma range by the largest absolute score. At \((0.050853,0.392699)\) radians, the best sampled objective matched the exact value of −137.9594 kBT/s. Feasible and optimal shots were 85.33% and 22.46%, respectively.
- **Interpretation** · These runs verify the mapping and sampling workflow against exact enumeration on tiny instances. The measured case is a pilot. A held-out IE replay and broader comparison are still pending.

---

## 2026-11-23 — First coupled policy map

- **Instance** · Illustrative performance matrix `[[4, 0], [1, 4], [4, 0], [0, 6]]`, with rows in regime order and columns in policy order. The graph is the chain 1–2–3–4. Each edge costs zero for equal policies and \(\beta\) for different policies.
- **Exact enumeration** · All 16 valid maps were evaluated. At \(\beta=0\), map 1212 scored 18 with three transitions. At \(\beta=2\), map 1112 scored 13 with one transition. At \(\beta=6\), map 2222 scored 10 with zero transitions. The sweep showed ties at 1.5 and 5.
- **Encoding** · At \(\beta=2\), one-hot penalty 20. The expanded QUBO matched direct energy evaluation on all 256 strings and exact map scores on all 16 feasible strings. The unique ground state encoded 1112 at energy −13. Ising energies matched the QUBO after adding a constant offset of 33.5.
- **Aer run** · Python 3.15.2, Qiskit 2.6.2, Aer 0.18.4. Standard X mixer, \(p=1\), 32×24 ideal angle grid, 8,192 shots on `aer_simulator`, seed 42. Selected angles \((\gamma,\theta)=(6.086836,2.748894)\) radians. Feasible shots were 50.50%, optimal shots were 5.87%, and the best sampled map was 1112 with score 13.
- **Logical resources** · Eight qubits, ten QUBO quadratic couplings and ten Ising \(ZZ\) terms. Before measurement the circuit had depth seven, 24 one-qubit gates, and ten two-qubit gates. These counts precede device placement, routing and native-gate decomposition.

---

## 2026-11-23 — First policy-map scaling study

- **Instance family** · Notebook 07 takes row and column prefixes of the fixed illustrative score table `[[4,0,2],[1,4,3],[4,0,2],[0,6,3],[5,1,2],[1,4,2]]`. It varies regime count, policy count, chain/cycle/complete topology, and switching weight \(\beta\in\{0,1,2,6\}\). The 4×2 chain at weight 2 reproduces Notebook 06's optimum, 1112 with score 13.
- **Exact baseline** · All ten cases solved by enumeration of valid maps, with seven timing repeats per case. The 4×3 and 6×2 chains both use 12 qubits and 4,096 binary strings. They have 81 versus 64 valid maps and 30 versus 16 quadratic terms, respectively. On the 4×2 case at weight 2, the chain, cycle, and complete graphs use 10, 12, and 16 quadratic terms and the same eight qubits. Each nonzero QUBO pair yields one Ising \(ZZ\) term.
- **Aer preview** · Python 3.15.2, Qiskit 2.6.2, and Aer 0.18.4. Depth-one QAOA with the standard X mixer, a 32×24 ideal angle grid, 8,192 shots per case, and simulator seed 42. The 2×2 and 3×2 chain cases at weight 2 matched the exact baselines after encoding.
- **Logical resources and samples** · The 2×2 optimum is 12, score 6. Angles were \((0.196350,1.178097)\) radians. Four qubits, depth five, 11 one-qubit gates, and four two-qubit gates produced 87.22% feasible and 28.39% optimal shots. The 3×2 optimum is 111, score 9. Angles were \((0.392699,2.094395)\). Six qubits, depth six, 18 one-qubit gates, and seven two-qubit gates produced 57.74% feasible and 5.18% optimal shots.
- **Interpretation** · The counts separate the cost of the encoding from the structure of the optimization problem. Sampling rates describe these two circuits and angle grids. Device compilation and larger searches are future experiments.

---

## 2026-11-23 — One-hot versus compact encoding

- **Instance family** · Notebook 08 uses the coupled chain objective from Notebooks 06–07 with mismatch cost 1 and switching weight 2. The 4×2 and 4×3 scores are unchanged. New entries use \((3i+2j+ij)\bmod 7\) on zero-based indices, with the original six-by-three table retained.
- **Exact verification** · Python 3.15.2 and NumPy 2.5.5. Both encodings reproduced every valid-map score and agreed with their Pauli expansions on every string for 4×2, 4×3, and 4×4. The respective optima were 1112 (13), 1112 (13), and 4442 (19). All ground states were feasible.
- **Resources** · The 4×2 compact QUBO uses four qubits and three \(ZZ\) terms, compared with eight qubits and ten \(ZZ\) terms for one-hot. The 4×3 compact encoding has 81 valid strings out of 256 and three weight-four Pauli terms. The analytical 8×8 counts are 64 versus 24 qubits and 1,232 versus 316 estimated CNOTs per cost layer for one-hot versus compact. The compact Hamiltonian has 36 higher-weight Pauli terms, up to weight six. Estimates use independent parity ladders and all-to-all logical connectivity.
- **Scope** · The two eight-regime cases use sparse coefficient counts without state enumeration. This comparison ends at logical resource estimates.

---

## 2026-11-23 — Hardware-aware transpilation

- **Instance** · Notebook 06's illustrative 4×2 chain with switching weight 2. Both QUBO and Ising encodings preserve all 16 valid scores. Exact optimum 1112, score 13. Depth-one X-mixer QAOA, 32×24 ideal angle grid, 8,192 shots, simulator seed 42. The compact angles were \((0.196350,2.487094)\), with 100% feasible and 19.62% optimal shots. One-hot used \((6.086836,2.748894)\), with 50.50% feasible and 5.87% optimal shots.
- **Environment and target** · Python 3.15.2, Qiskit 2.6.2, and Aer 0.18.4. Locally defined eight-site bidirectional line with RZ, SX, X, and CX. Identity placement, BasicSwap routing, optimization levels 0, 1 and 3, transpiler seed 42. The all-connected reference uses the same basis. The target has no calibration data and does not describe Euro-Q-Exa.
- **Level 1 resources** · Compact used four active sites. Depth 6 → 17, total gates 15 → 41, one-qubit gates 12 → 35, and two-qubit gates 3 → 6, with zero SWAPs and zero extra CX versus the all-connected reference. One-hot used eight active sites. Depth 7 → 52, total gates 34 → 116, one-qubit gates 24 → 74, and two-qubit gates 10 → 42, with eight routing SWAPs and 22 extra CX. Layouts and the other levels are recorded in the notebook.
- **Verification and scope** · All six mapped circuits use supported instructions on permitted sites and reproduce the logical unitaries after accounting for layout and global phase. This measures compilation resources. Noisy simulation and real QPU execution are later experiments.

---

## 2026-11-23 — Ideal, finite-shot and device-aware Aer

- **Fixed benchmark** · Notebook 09's 4×2 chain, switching weight 2, exact optimum 1112 with score 13. Depth-one QAOA, compact angles \((0.196349541,2.487094184)\) and one-hot angles \((6.086835766,2.748893572)\) radians, reconstructed from their original 32×24 grid coordinates.
- **Environment and runs** · Python 3.15.2, Qiskit 2.6.2, Aer 0.18.4, NumPy 2.5.5. Exact Qiskit statevector, ideal Aer in statevector mode at 100, 500, 1,000, 4,096 and 10,000 shots, then matched mapped Aer in density-matrix mode at 4,096 shots. Each sampled condition used seeds 42–46. The saved Notebook 10 tables report each shot count, outcome frequencies, repeat standard deviations, and conditional mean and best scores.
- **Target and noise** · Notebook 09's RZ/SX/X/CX eight-site bidirectional line, level 1, identity placement, BasicSwap, transpiler seed 42. Aer derives gate, thermal-relaxation and readout errors via `NoiseModel.from_backend` from synthetic `GenericBackendV2` properties generated with seed 42, using temperature 0 mK and no duration overrides. Site and instruction parameters are recorded in the notebook. These are synthetic properties rather than QPU calibration.
- **Compact result** · Ideal statevector, ideal Aer, mapped noise off and mapped noise on gave optimal rates of 19.87%, 20.29%, 20.29% and 20.19%, respectively. All were 100% feasible. Conditional mean scores were 11.250, 11.265, 11.265 and 11.188. The mapped circuit used four sites, depth 17 and six CX gates.
- **One-hot result** · The same conditions gave optimal rates of 5.98%, 5.72%, 6.13% and 5.17%. Feasible rates were 49.75%, 49.91%, 49.58% and 43.59%, with conditional mean scores of 8.674, 8.673, 8.726 and 8.695. The mapped circuit used eight sites, depth 52 and 42 CX gates after eight routing SWAPs.
- **Interpretation** · Both encodings reached a best score of 13 in every reported condition. Rates and mean scores distinguish the distributions. The matched mapped comparison measures the combined modeled noise effect. It cannot isolate the effect of any single error source. Real QPU execution remains pending.

---

## 2026-11-23 — Notebook sequence reproducibility audit

- Ran all 11 numbered notebooks from 00 through 10 in fresh local kernels without overwriting saved notebook outputs. Python 3.15.2, NumPy 2.5.5, Qiskit 2.6.2, Aer 0.18.4, Matplotlib 3.11.2. The audit used each notebook's recorded seeds and shots. A local Jupyter TCP transport warning appeared. No execution blocker was observed.
- Notebook 02 reran all 20 fixed-policy trials. The rounded cell means matched the stored five-seed matrix used to render the new heatmaps. Notebook 06's verified exact maps at switching weights 0 and 2 supplied the companion chain diagram.
- Notebook 05 also passed with the local IE-derived JSON. The default run reported a different transpiled gate mix from its saved output, with the same feasibility and optimality. Runtime and compiled instruction counts should be recorded with their execution context.
- The review separates illustrative instances, the IE simulation pilot, and synthetic device/noise results. The numbered study order was retained. The seminar path starts from the IE model and moves through coupling before explaining the simpler binary and quantum derivations.
- The available evidence supports discussion with a hardware team. A calibrated target, actual device data, and independent IE validation remain future work.

---

## 2026-11-24 — Interdisciplinary documentation structure

- Added a system overview, five field guides, and a six-domain roadmap to distinguish the full information-engine project from the quantum benchmark sequence.
- Preserved the existing lab filenames, executable cells, and saved outputs. The new guides distinguish simulator evidence, synthetic-device studies, and planned physical validation.

---

## Entry template

### YYYY-MM-DD — QE-XXX: title

**Question** — what is being tested?

**Instance / input** — exact data, parameters and source.

**Environment** — backend and software versions.

**Method** — encoding, algorithm, optimizer, depth, shots, seeds.

**Classical reference** — exact/best-known value and method.

**Result** — numerical results and generated artifacts.

**Resources** — qubits, depth, gate counts, circuit evaluations, shots, runtime.

**Interpretation** — what the result supports and does not support.

**Next question** — smallest useful next experiment.
