# Project status

## Completed

- The Bell-state notebook verifies the local Python, Qiskit, and Aer environment.
- Teaching notebooks 01–05 cover exact policy lookup, fixed-policy IE evaluation, QUBO, Ising, and depth-one QAOA. All five ran end to end in the project environment.
- The IE notebook evaluated 20 trials across two sensor-noise regimes, two policies, and five matched seeds. The QAOA notebook also ran with the corresponding local IE-derived instance.
- Notebook 06 verifies an illustrative coupled four-regime chain by exact enumeration and QUBO–Ising energy equivalence. Depth-one Aer sampling recovered the exact optimum.

## Current

- Use the illustrative matrix as the common teaching reference. The saved notebook outputs distinguish the illustrative optimization from the measured IE pilot.

## Next

- Notebook 07 will vary the number of regimes, number of policies, and graph complexity, and track valid maps, qubits, couplings, logical depth, and two-qubit gates.
- Validate the coupled and scaling cases before hardware-aware transpilation and noisy or device-aware simulation. Real QPU experiments follow those checks.
- Freeze a reproducible IE-derived reference instance and verify its selected policy map on held-out IE seeds.

The default QAOA result uses illustrative scores. The IE-derived run is a local pilot, and an application benchmark is still pending.
