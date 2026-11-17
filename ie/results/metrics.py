"""
Q-SYNTH result metrics.

Input
-----
bus.history

Outputs
-------
Scalar performance and diagnostic metrics.

Initial metrics
---------------
- directed bead velocity
- estimator RMSE
- ratchet-event count
- ratchet-event rate
- extracted gravitational power
- final displacement
- innovation RMS
- mean Kalman covariance, when available

Later additions
---------------
- trap work
- net extracted power
- work per ratchet event
- first-passage statistics
- estimator consistency
- robustness metrics
"""


import numpy as np

from config import (
    m_eff,
    physical
)


# ============================================================
# Utility functions
# ============================================================

def unpack(history):
    """
    Convert list of (time, value) pairs into NumPy arrays.
    """

    if history is None or len(history) == 0:
        return np.array([]), np.array([])

    t = np.array(
        [item[0] for item in history],
        dtype=float
    )

    values = np.array(
        [item[1] for item in history]
    )

    return t, values


def get_history(
    bus,
    signal_name
):
    """
    Safely retrieve a signal history.
    """

    return bus.history.get(
        signal_name,
        []
    )


# ============================================================
# Directed velocity
# ============================================================

def directed_velocity(
    bus,
    discard_fraction=0.1
):
    """
    Estimate mean directed bead velocity.

    Uses a linear fit to true bead position versus time.

    Parameters
    ----------
    discard_fraction:
        Fraction of initial trajectory ignored in order
        to reduce initialization/transient effects.

    Returns
    -------
    velocity [m/s]
    """

    t, x = unpack(
        get_history(
            bus,
            "plant_state"
        )
    )

    if len(t) < 2:
        return np.nan

    start = int(
        discard_fraction
        * len(t)
    )

    if len(t[start:]) < 2:
        return np.nan

    slope, _ = np.polyfit(
        t[start:],
        x[start:],
        1
    )

    return slope


# ============================================================
# Estimator RMSE
# ============================================================

def estimator_rmse(bus):
    """
    RMS error between true bead position and estimate.

    Assumes plant and estimator initially operate at the
    same nominal fast sampling rate.
    """

    _, x = unpack(
        get_history(
            bus,
            "plant_state"
        )
    )

    _, xhat = unpack(
        get_history(
            bus,
            "estimate"
        )
    )

    N = min(
        len(x),
        len(xhat)
    )

    if N == 0:
        return np.nan

    error = (
        x[:N]
        - xhat[:N]
    )

    return np.sqrt(
        np.mean(
            error**2
        )
    )


# ============================================================
# Final displacement
# ============================================================

def final_displacement(bus):
    """
    Net physical bead displacement over the simulation.
    """

    _, x = unpack(
        get_history(
            bus,
            "plant_state"
        )
    )

    if len(x) < 2:
        return np.nan

    return (
        x[-1]
        - x[0]
    )


# ============================================================
# Ratchet events
# ============================================================

def ratchet_count(bus):
    """
    Number of controller trigger events.
    """

    _, events = unpack(
        get_history(
            bus,
            "ratchet_event"
        )
    )

    if len(events) == 0:
        return 0

    return int(
        np.sum(
            events.astype(bool)
        )
    )


def ratchet_rate(bus):
    """
    Mean number of ratchet events per second.
    """

    t, events = unpack(
        get_history(
            bus,
            "ratchet_event"
        )
    )

    if len(t) < 2:
        return np.nan

    duration = (
        t[-1]
        - t[0]
    )

    if duration <= 0:
        return np.nan

    return (
        np.sum(
            events.astype(bool)
        )
        / duration
    )


# ============================================================
# Extracted gravitational power
# ============================================================

def extracted_power(
    bus,
    discard_fraction=0.1
):
    """
    Estimate useful gravitational power.

    For upward directed transport:

        P_ext = m_eff * g * v

    where m_eff already includes buoyancy.

    Returns
    -------
    power [W]
    """

    v = directed_velocity(
        bus,
        discard_fraction=
            discard_fraction
    )

    if not np.isfinite(v):
        return np.nan

    return (
        m_eff
        * physical.g
        * v
    )


def extracted_power_kbt_per_s(
    bus,
    discard_fraction=0.1
):
    """
    Extracted power in thermal-energy units kBT/s.
    """

    P = extracted_power(
        bus,
        discard_fraction=
            discard_fraction
    )

    if not np.isfinite(P):
        return np.nan

    kBT = (
        physical.kB
        * physical.T
    )

    return P / kBT


# ============================================================
# Estimator diagnostics
# ============================================================

def innovation_rms(bus):
    """
    RMS Kalman innovation.
    """

    _, innovation = unpack(
        get_history(
            bus,
            "innovation"
        )
    )

    if len(innovation) == 0:
        return np.nan

    return np.sqrt(
        np.mean(
            innovation**2
        )
    )


def mean_covariance(bus):
    """
    Mean estimator covariance P.
    """

    _, covariance = unpack(
        get_history(
            bus,
            "covariance"
        )
    )

    if len(covariance) == 0:
        return np.nan

    return np.mean(
        covariance
    )


def total_trap_work(bus):
    """
    Total physical work performed by trap-position changes.

    Returns
    -------
    W_trap [J]
    """

    entries = bus.history.get(
        "trap_move",
        []
    )

    if len(entries) == 0:
        return 0.0

    return sum(
        item[1]["trap_work"]
        for item in entries
    )


def trap_power(bus):
    """
    Mean trap actuation power.

    Returns
    -------
    P_trap [W]
    """

    entries = bus.history.get(
        "trap_move",
        []
    )

    if len(entries) == 0:
        return 0.0

    t_start = entries[0][0]
    t_end = entries[-1][0]

    duration = (
        t_end
        - t_start
    )

    if duration <= 0:
        return 0.0

    return (
        total_trap_work(bus)
        / duration
    )


def trap_power_kbt_per_s(bus):
    """
    Mean trap power in kBT/s.
    """

    P = trap_power(bus)

    kBT = (
        physical.kB
        * physical.T
    )

    return (
        P
        / kBT
    )


def work_per_trap_move(bus):
    """
    Mean trap work per physical actuator move.
    """

    entries = bus.history.get(
        "trap_move",
        []
    )

    if len(entries) == 0:
        return np.nan

    return (
        total_trap_work(bus)
        / len(entries)
    )


def physical_trap_move_count(bus):
    """
    Number of actual trap-position changes.
    """

    return len(
        bus.history.get(
            "trap_move",
            []
        )
    )


def balance_power(bus):
    """
    Thermodynamic balance power:

        P_balance = P_ext - P_trap

    This is not yet the total engineering net power because
    actuator electronics, sensing, computation and laser
    power are not included.
    """

    return (
        extracted_power(bus)
        - trap_power(bus)
    )


def balance_power_kbt_per_s(bus):

    P = balance_power(bus)

    kBT = (
        physical.kB
        * physical.T
    )

    return P / kBT

def extracted_energy(bus):
    """
    Total gravitational energy gained over the simulation.

        E_ext = m_eff * g * (x_final - x_initial)
    """

    dx = final_displacement(bus)

    if not np.isfinite(dx):
        return np.nan

    return (
        m_eff
        * physical.g
        * dx
    )


def extracted_energy_kbt(bus):

    E = extracted_energy(bus)

    if not np.isfinite(E):
        return np.nan

    kBT = (
        physical.kB
        * physical.T
    )

    return E / kBT

# ============================================================
# Complete metric summary
# ============================================================

def calculate_metrics(bus):
    """
    Calculate standard Q-SYNTH P1 result metrics.

    Naming convention
    -----------------
    mean:
        Time-averaged quantity.

    cumulative:
        Integrated / summed quantity over the run.

    RMS:
        Root-mean-square quantity.

    count:
        Total number of events accumulated during the run.
    """

    velocity = directed_velocity(bus)
    displacement = final_displacement(bus)

    rmse = estimator_rmse(bus)

    n_ratchet = ratchet_count(bus)
    r_ratchet = ratchet_rate(bus)

    E_ext = extracted_energy(bus)
    E_ext_kbt = extracted_energy_kbt(bus)

    P_ext = extracted_power(bus)
    P_ext_kbt = extracted_power_kbt_per_s(bus)

    innovation = innovation_rms(bus)
    P_mean = mean_covariance(bus)

    n_moves = physical_trap_move_count(bus)

    W_trap = total_trap_work(bus)
    P_trap = trap_power(bus)
    P_trap_kbt = trap_power_kbt_per_s(bus)

    P_balance = balance_power(bus)
    P_balance_kbt = balance_power_kbt_per_s(bus)
    
    return {

        "velocity_mean_um_s":
            velocity * 1e6,

        "displacement_cumulative_um":
            displacement * 1e6,

        "estimator_error_RMS_nm":
            rmse * 1e9,

        "ratchet_events_count":
            n_ratchet,

        "ratchet_rate_mean_Hz":
            r_ratchet,

        "extracted_energy_cumulative_kBT":
            E_ext_kbt,

        "extracted_power_mean_kBT_s":
            P_ext_kbt,

        "innovation_RMS_nm":
            innovation * 1e9,

        "estimator_covariance_mean_nm2":
            P_mean * 1e18,

        "trap_moves_count":
            n_moves,

        "trap_work_cumulative_J":
            W_trap,

        "trap_power_mean_kBT_s":
            P_trap_kbt,

        "balance_power_mean_kBT_s":
            P_balance_kbt
    }


def print_metrics(bus):
    """
    Print concise human-readable result summary.

    Statistical meaning is explicitly indicated:
        (mean)
        (cumulative)
        (RMS)
        (count)
    """

    m = calculate_metrics(bus)

    print()
    print("========================================")
    print("Q-SYNTH P1 RESULTS")
    print("========================================")

    print(
        f"Velocity                  : "
        f"{m['velocity_mean_um_s']:.3f} um/s "
        f"(mean)"
    )

    print(
        f"Displacement              : "
        f"{m['displacement_cumulative_um']:.3f} um "
        f"(cumulative)"
    )

    print(
        f"Estimator error           : "
        f"{m['estimator_error_RMS_nm']:.3f} nm "
        f"(RMS)"
    )

    print(
        f"Ratchet events            : "
        f"{m['ratchet_events_count']} "
        f"(count)"
    )

    print(
        f"Ratchet rate              : "
        f"{m['ratchet_rate_mean_Hz']:.2f} Hz "
        f"(mean)"
    )

    print(
        f"Extracted power           : "
        f"{m['extracted_power_mean_kBT_s']:.3f} kBT/s "
        f"(mean)"
    )

    print(
        f"Innovation                : "
        f"{m['innovation_RMS_nm']:.3f} nm "
        f"(RMS)"
    )

    print(
        f"Estimator covariance P    : "
        f"{m['estimator_covariance_mean_nm2']:.3f} nm^2 "
        f"(mean)"
    )

    print(
        f"Physical trap moves       : "
        f"{m['trap_moves_count']} "
        f"(count)"
    )

    print(
        f"Trap work                 : "
        f"{m['trap_work_cumulative_J']:.6e} J "
        f"(cumulative, signed)"
    )

    print(
        f"Trap power                : "
        f"{m['trap_power_mean_kBT_s']:.3f} kBT/s "
        f"(mean, signed)"
    )

    print(
        f"P_ext - P_trap            : "
        f"{m['balance_power_mean_kBT_s']:.3f} kBT/s "
        f"(mean)"
    )
