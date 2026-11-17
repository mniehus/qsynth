# Reproducible environment

## Initial verified setup — 2026-11-17

| Component | Version |
|---|---:|
| Python | 3.15.2 |
| Qiskit | 2.6.2 |
| Qiskit Aer | 0.18.4 |

```bash
python --version
python -c "import qiskit; print(qiskit.__version__)"
python -c "import qiskit_aer; print(qiskit_aer.__version__)"
python -m pip freeze > environment-freeze.txt
```

Every benchmark should record the environment actually used.
