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
