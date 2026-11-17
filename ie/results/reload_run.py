"""
Simple executable script for loading and inspecting
a previously saved Q-SYNTH run.
"""

import matplotlib.pyplot as plt

from results.reload_utils import (
    load_latest_run,
    list_signals,
    load_core_signals
)


# ============================================================
# Load newest run
# ============================================================

run_dir, data = load_latest_run()

print()
print(
    f"Loaded run: {run_dir}"
)


# ============================================================
# Show stored arrays
# ============================================================

list_signals(
    data
)


# ============================================================
# Load common signals
# ============================================================

signals = load_core_signals(
    data
)


# ============================================================
# Simple verification plot
# ============================================================

fig, ax = plt.subplots()

if "plant" in signals:

    t, x = signals["plant"]

    ax.plot(
        t,
        x * 1e9,
        label="true bead position"
    )


if "estimate" in signals:

    t, xhat = signals["estimate"]

    ax.plot(
        t,
        xhat * 1e9,
        label="estimate"
    )


if "actuator" in signals:

    t, lam = signals["actuator"]

    ax.plot(
        t,
        lam * 1e9,
        label="trap position"
    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Position [nm]"
)

ax.set_title(
    "Reloaded Q-SYNTH run"
)

ax.grid()

ax.legend()

fig.tight_layout()

plt.show()