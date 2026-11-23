# Q-SYNTH — Quantum Engineering

Q-SYNTH asks a concrete engineering question:

> Can current quantum computing methods contribute meaningfully to the offline synthesis of estimator and feedback-control policies for a stochastic physical information engine?

The emphasis is on a reproducible chain from a real physical system to a well-defined optimization problem, strong classical baselines, a quantum formulation, and objective comparison.

\[
\text{physical system}\rightarrow\text{simulation}\rightarrow J_{ij}\rightarrow\text{policy optimization}\rightarrow\text{QUBO}\rightarrow\text{Ising}\rightarrow\text{circuit}\rightarrow\text{QPU}
\]

The seminar is designed for master's students in Informatics Engineering. Physics, stochastic thermodynamics, and FPGA control define the application and its constraints. The main focus is computational representation, algorithms, implementation, and benchmarking.

## Choose a route

- [Master's students in Informatics Engineering](start-meim.md) start with algorithms, representation, and evaluation.
- [Project collaborators](start-collaborators.md) start with the physical system, feedback constraints, and validation.

Both routes use the same notebooks. This site explains the concepts and guides readers to executable derivations and experiments. Reusable implementation lives in Python modules.

Follow the [synthesis and validation workflow](workflow.md) for the full project or the [notebook sequence](notebook-sequence.md) for the hands-on route.
