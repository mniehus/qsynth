# Acronyms & concepts

This is intentionally broader than an acronym list and includes proper names and expressions that may be unfamiliar to informatics students.

**ADC — Analog-to-Digital Converter** — converts an analog measurement to digital samples.  
**Aer** — Qiskit's high-performance quantum-circuit simulator project; not normally expanded as an acronym.  
**Ansatz** — parameterized trial form; in VQAs, a family of circuits optimized classically.  
**AOD — Acousto-Optic Deflector** — optical beam-steering actuator controlled by RF drive.  
**Approximation ratio** — normalized quality of an approximate solution relative to a reference optimum; definition is problem-dependent.  
**Backend** — execution target, e.g. simulator or physical QPU.  
**Bell state** — maximally entangled two-qubit state; \((|00\rangle+|11\rangle)/\sqrt2\) is used for the first sanity check.  
**Binary variable** — variable taking 0 or 1; QUBO uses binary variables.  
**Brownian motion** — random motion caused by microscopic thermal interactions.  
**Circuit depth** — number of sequential circuit layers after accounting for parallel operations.  
**Classical baseline** — classical algorithm/result used as comparison reference.  
**Cost Hamiltonian** — Hamiltonian whose energy encodes the optimization objective.  
**Crooks fluctuation relation** — nonequilibrium theorem named after Gavin Crooks comparing forward and reverse work distributions.  
**DAC — Digital-to-Analog Converter** — converts digital control values to analog signals.  
**Detailed balance** — equilibrium condition balancing microscopic transition flows.  
**Entanglement** — quantum correlations not representable as independent subsystem states.  
**Entropy production** — thermodynamic measure of irreversibility.  
**Estimator** — algorithm inferring an internal state from measurements and a model.  
**FPGA — Field-Programmable Gate Array** — reconfigurable hardware for deterministic low-latency processing/control.  
**Fokker–Planck equation** — PDE describing evolution of a probability density for stochastic dynamics.  
**Hamiltonian** — energy operator/function; in quantum optimization it can encode a cost function.  
**HPC — High-Performance Computing** — large-scale classical computing; QPUs are commonly considered hybrid accelerators.  
**Information engine** — physical system using measurement/feedback information to extract useful work or direct fluctuations.  
**Ising model** — interacting-spin model associated with Ernst Ising; mathematically important for combinatorial optimization.  
**Jarzynski equality** — theorem introduced by Christopher Jarzynski relating exponential work averages to free-energy differences.  
**Kalman filter** — recursive state estimator for linear stochastic systems.  
**Langevin equation** — stochastic differential equation combining deterministic dynamics with random forcing.  
**Logical circuit** — algorithm-level circuit before mapping to target hardware gates/connectivity.  
**Mixer Hamiltonian** — QAOA Hamiltonian moving amplitude between candidate solutions.  
**Mutual information** — statistical measure of shared information/dependence between random variables.  
**NISQ — Noisy Intermediate-Scale Quantum** — term for useful experimental quantum processors still limited by noise and scale.  
**One-hot encoding** — exactly one binary variable in a group is 1.  
**Optimality gap** — difference between candidate and reference optimum, often normalized.  
**Pauli operators \(X,Y,Z\)** — fundamental single-qubit operators; Ising costs commonly use \(Z\) and \(ZZ\).  
**Policy** — rule/parameter choice determining estimator/controller behavior.  
**QAOA — Quantum Approximate Optimization Algorithm** — hybrid variational algorithm alternating cost and mixer evolution.  
**Qiskit** — quantum SDK used here; treated as a project/product name rather than a current formal acronym.  
**QPD — Quadrant Photodiode** — position-sensitive photodetector.  
**QPU — Quantum Processing Unit** — hardware executing quantum circuits.  
**Qubit** — quantum two-level information unit.  
**QUBO — Quadratic Unconstrained Binary Optimization** — quadratic optimization over binary variables.  
**RFSoC — Radio-Frequency System-on-Chip** — integrates FPGA, processors and high-speed converters.  
**Sagawa–Ueda relation** — generalized fluctuation/second-law relations associated with Takahiro Sagawa and Masahito Ueda including information and feedback.  
**Shot** — one execution and measurement of a quantum circuit.  
**Statevector** — complex vector representing a pure quantum state; dimension grows exponentially with qubits.  
**Superposition** — coherent quantum combination of basis states; not equivalent to reading all classical answers in parallel.  
**Transpilation** — compilation/mapping of a logical circuit to target-native gates/connectivity.  
**Two-qubit gate** — joint operation on two qubits; a key noisy-hardware resource metric.  
**VQA — Variational Quantum Algorithm** — hybrid algorithm with a parameterized QPU circuit and classical optimizer.  
**XY mixer** — constraint-preserving QAOA mixer using \(X\)/\(Y\) interactions, relevant to one-hot constraints.  
