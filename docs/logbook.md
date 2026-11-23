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
