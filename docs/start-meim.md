# Start here for master's students in Informatics Engineering

Start with the optimization problem: assign one policy to each regime and score the resulting map.

1. [Policy-map optimization](optimization.md) and the [IE cost matrix](ie-cost-matrix.md) define the objective and its inputs.
2. [QUBO](qubo-ising.md) expresses the problem with binary variables. [Ising mapping](ising.md) expresses the same objective with quantum operators.
3. [QAOA](qaoa.md) builds and samples a circuit. [Coupled policy maps](coupled-policy.md) show when neighboring choices must be optimized together.
4. [Simulation and quantum hardware](simulation.md) trace the path from ideal circuits to a physical device. [Benchmarking](benchmarking.md) explains how to compare solution quality and resource use.

Start the shared notebook sequence with the [Bell environment check](simulation.md#reproduce-this-step), then follow the notebook links through 01?06. Use the [glossary](glossary.md) when a term is unfamiliar.
