# Q-SYNTH overview

The reference system is an optical-tweezer information engine. A Brownian particle is measured, its state is estimated, and feedback selectively shifts the trap when favorable fluctuations occur.

The fast feedback loop remains classical and deterministic. The intended role of quantum computing is **offline design/synthesis**, not real-time feedback.

A first synthesis problem is

\[
\max_{\Pi}\left[\sum_i J_{i,\Pi(i)}-\beta\sum_{(i,k)}C(\Pi(i),\Pi(k))\right].
\]

Here, regimes are indexed by \(i\), candidate policies by \(j\), \(J_{ij}\) is simulated performance, and \(C\) penalizes undesirable changes between neighboring regimes.
