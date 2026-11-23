# Project status

## Completed

- The Bell-state notebook verifies the local Python, Qiskit, and Aer environment.
- Teaching notebooks 01–05 cover exact policy lookup, fixed-policy IE evaluation, QUBO, Ising, and depth-one QAOA. All five ran end to end in the project environment.
- The IE notebook evaluated 20 trials across two sensor-noise regimes, two policies, and five matched seeds. The QAOA notebook also ran with the corresponding local IE-derived instance.

## Current

- Use the illustrative matrix as the common teaching reference. The saved notebook outputs distinguish the illustrative optimization from the measured IE pilot.

## Next

- Freeze a reproducible IE-derived reference instance and verify the selected policy map on held-out IE seeds before introducing inter-regime coupling.

The default QAOA result uses illustrative scores. The IE-derived run is a local pilot, and an application benchmark is still pending.
