from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

SHOTS=1000
SEED_SIMULATOR=42
qc=QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
qc.measure([0,1],[0,1])
sim=AerSimulator()
counts=sim.run(qc,shots=SHOTS,seed_simulator=SEED_SIMULATOR).result().get_counts()
print(qc)
print("shots =",SHOTS)
print("seed_simulator =",SEED_SIMULATOR)
print("counts =",counts)
unexpected=sum(v for k,v in counts.items() if k not in {"00","11"})
if unexpected: raise RuntimeError(f"Unexpected ideal outcomes: {counts}")
print("PASS: ideal Bell-state simulation produced only 00 and 11.")
