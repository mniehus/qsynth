# Project status

## Completed

- Python, Qiskit, and Aer environment established. The Bell-state notebook checks the simulator stack.
- The initial 2×2 notebook checks QUBO–Ising equivalence across all 16 states and runs QAOA in Aer.
- The working tree supports fixed-policy IE evaluation. A local five-seed pilot generated a 2×2 cost matrix, and the notebook ran against that instance.

## Current

- Separate the conceptual policy lookup from QAOA and make the teaching sequence explicit.
- Build on the fixed-policy evaluator and pilot matrix to document the IE-derived costs and their uncertainty.

## Next

- Create the exact classical 2×2 policy-map notebook.
- Add dedicated IE cost-matrix, QUBO, and Ising notebooks, then rerun QAOA on the IE-derived instance in the new sequence.
- Introduce coupling between regimes and compare independent choices with the global optimum.

The notebook defaults to the illustrative matrix. Its default result demonstrates the workflow. The IE-derived run is a local pilot, and an application benchmark is still pending.
