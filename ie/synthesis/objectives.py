import numpy as np

from config import m_eff, physical
from results.metrics import get_history, unpack


def balance_power_cost(bus, warmup_s):
    times, positions = unpack(get_history(bus, "plant_state"))
    window = times >= warmup_s
    if np.count_nonzero(window) < 2:
        raise ValueError("The objective needs at least two plant samples after warm-up.")

    times = times[window]
    end = times[-1]
    duration = end - warmup_s
    kbt = physical.kB * physical.T
    velocity = np.polyfit(times, positions[window], 1)[0]
    moves = [
        entry["trap_work"]
        for time, entry in get_history(bus, "trap_move")
        if warmup_s <= time <= end
    ]
    gravitational_power = m_eff * physical.g * velocity / kbt
    trap_power = sum(moves) / (duration * kbt)

    return {
        "cost_kbt_per_s": float(trap_power - gravitational_power),
        "gravitational_power_kbt_per_s": float(gravitational_power),
        "trap_power_kbt_per_s": float(trap_power),
        "trap_moves": len(moves),
        "window_end_s": float(end),
    }
