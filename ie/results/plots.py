"""
Q-SYNTH static result plots.

Input
-----
bus.history

Plots
-----
1. Closed-loop trajectory
2. Estimator error
3. Ratchet events
4. Innovation diagnostics
5. Supervisor statistics

Later
-----
- energy balance
- trap work
- policy switching
- first-passage statistics
- x-y trajectory for 2D plant
"""


import numpy as np
import matplotlib.pyplot as plt

from results.metrics import unpack


# ============================================================
# Helper
# ============================================================

def history(
    bus,
    signal
):

    return unpack(
        bus.history.get(
            signal,
            []
        )
    )


# ============================================================
# 1. Closed-loop trajectory
# ============================================================

def plot_closed_loop(bus):
    """
    Main closed-loop trajectory.

    Shows:
        true bead position
        measurement
        estimator
        active trap position
    """

    tx, x = history(
        bus,
        "plant_state"
    )

    ty, y = history(
        bus,
        "measurement"
    )

    th, xhat = history(
        bus,
        "estimate"
    )

    tl, lam = history(
        bus,
        "actuator_state"
    )


    fig, ax = plt.subplots()

    if len(tx):

        ax.plot(
            tx,
            x * 1e9,
            label="true bead position"
        )


    if len(ty):

        ax.plot(
            ty,
            y * 1e9,
            ".",
            markersize=1,
            alpha=0.25,
            label="measurement"
        )


    if len(th):

        ax.plot(
            th,
            xhat * 1e9,
            label="estimate"
        )


    if len(tl):

        ax.plot(
            tl,
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
        "Closed-loop information engine"
    )

    ax.grid()

    ax.legend()

    fig.tight_layout()

    return fig, ax


# ============================================================
# 2. Estimator error
# ============================================================

def plot_estimator_error(bus):
    """
    True estimation error x - xhat.
    """

    tx, x = history(
        bus,
        "plant_state"
    )

    th, xhat = history(
        bus,
        "estimate"
    )

    N = min(
        len(x),
        len(xhat)
    )

    if N == 0:
        return None, None


    error = (
        x[:N]
        - xhat[:N]
    )


    fig, ax = plt.subplots()

    ax.plot(
        tx[:N],
        error * 1e9
    )

    ax.axhline(
        0.0,
        linewidth=1
    )

    ax.set_xlabel(
        "Time [s]"
    )

    ax.set_ylabel(
        "Estimation error [nm]"
    )

    ax.set_title(
        "Estimator error"
    )

    ax.grid()

    fig.tight_layout()

    return fig, ax


# ============================================================
# 3. Ratchet events
# ============================================================

def plot_ratchet_events(bus):
    """
    Shows controller ratchet events together with
    bead/trap relative displacement.
    """

    te, events = history(
        bus,
        "ratchet_event"
    )

    th, xhat = history(
        bus,
        "estimate"
    )

    tl, lam = history(
        bus,
        "actuator_state"
    )


    N = min(
        len(xhat),
        len(lam)
    )

    if N == 0:
        return None, None


    delta = (
        xhat[:N]
        - lam[:N]
    )


    fig, ax = plt.subplots()

    ax.plot(
        th[:N],
        delta * 1e9,
        label=r"$\hat{x}-\lambda$"
    )


    if len(events):

        event_indices = np.where(
            events.astype(bool)
        )[0]

        event_indices = event_indices[
            event_indices < N
        ]

        ax.plot(
            th[event_indices],
            delta[event_indices]
            * 1e9,
            "o",
            markersize=3,
            label="ratchet event"
        )


    ax.set_xlabel(
        "Time [s]"
    )

    ax.set_ylabel(
        "Relative position [nm]"
    )

    ax.set_title(
        "Ratchet decisions"
    )

    ax.grid()

    ax.legend()

    fig.tight_layout()

    return fig, ax


# ============================================================
# 4. Kalman innovation
# ============================================================

def plot_innovation(bus):
    """
    Plot estimator innovation versus time.
    """

    t, innovation = history(
        bus,
        "innovation"
    )

    if len(t) == 0:
        return None, None


    fig, ax = plt.subplots()

    ax.plot(
        t,
        innovation * 1e9
    )

    ax.axhline(
        0.0,
        linewidth=1
    )

    ax.set_xlabel(
        "Time [s]"
    )

    ax.set_ylabel(
        "Innovation [nm]"
    )

    ax.set_title(
        "Estimator innovation"
    )

    ax.grid()

    fig.tight_layout()

    return fig, ax


# ============================================================
# 5. Histogram of innovation
# ============================================================

def plot_innovation_histogram(bus):
    """
    Simple innovation-distribution diagnostic.

    Useful later for model-consistency assessment.
    """

    _, innovation = history(
        bus,
        "innovation"
    )

    if len(innovation) == 0:
        return None, None


    fig, ax = plt.subplots()

    ax.hist(
        innovation * 1e9,
        bins=60,
        density=True,
        alpha=0.7
    )

    ax.set_xlabel(
        "Innovation [nm]"
    )

    ax.set_ylabel(
        "Probability density"
    )

    ax.set_title(
        "Innovation distribution"
    )

    ax.grid()

    fig.tight_layout()

    return fig, ax


# ============================================================
# 6. Supervisor statistics
# ============================================================

def plot_supervisor_statistics(bus):

    entries = bus.history.get(
        "statistics",
        []
    )

    if len(entries) == 0:
        return None, None

    t = np.array(
        [
            item[0]
            for item in entries
        ]
    )

    std = np.array(
        [
            item[1]["relative_std"]
            for item in entries
        ]
    )

    skewness = np.array(
        [
            item[1]["relative_skewness"]
            for item in entries
        ]
    )

    kurtosis = np.array(
        [
            item[1]["relative_excess_kurtosis"]
            for item in entries
        ]
    )

    # ========================================================
    # Create figure
    # ========================================================

    fig, ax_left = plt.subplots()

    # --------------------------------------------------------
    # Left axis: relative-position standard deviation
    # --------------------------------------------------------

    ax_left.plot(
        t,
        std * 1e9,
        label="relative std"
    )

    ax_left.set_xlabel(
        "Time [s]"
    )

    ax_left.set_ylabel(
        r"Std of $\hat{x}-\lambda$ [nm]"
    )

    ax_left.grid()


    # --------------------------------------------------------
    # Right axis: skewness and kurtosis
    # --------------------------------------------------------

    ax_right = ax_left.twinx()

    ax_right.plot(
        t,
        skewness,
        label="skewness"
    )

    ax_right.plot(
        t,
        kurtosis,
        label="excess kurtosis"
    )

    ax_right.set_ylabel(
        "Dimensionless shape statistics"
    )


    # --------------------------------------------------------
    # Combined legend
    # --------------------------------------------------------

    lines_left, labels_left = (
        ax_left.get_legend_handles_labels()
    )

    lines_right, labels_right = (
        ax_right.get_legend_handles_labels()
    )

    ax_left.legend(
        lines_left + lines_right,
        labels_left + labels_right
    )


    ax_left.set_title(
        "Slow statistical regime indicators"
    )

    fig.tight_layout()

    return fig, ax_left


def plot_energy_balance(bus):
    """
    Cumulative extracted gravitational energy and
    cumulative trap work.
    """

    tx, x = history(
        bus,
        "plant_state"
    )

    if len(tx) == 0:
        return None, None

    from config import (
        physical,
        m_eff
    )

    kBT = (
        physical.kB
        * physical.T
    )

    # --------------------------------------------------------
    # Extracted gravitational energy
    # --------------------------------------------------------

    E_ext = (
        m_eff
        * physical.g
        * (
            x
            - x[0]
        )
    )

    # --------------------------------------------------------
    # Cumulative trap work
    # --------------------------------------------------------

    trap_entries = bus.history.get(
        "trap_move",
        []
    )

    trap_times = []
    trap_cumulative = []

    cumulative = 0.0

    for t, event in trap_entries:

        cumulative += (
            event["trap_work"]
        )

        trap_times.append(
            t
        )

        trap_cumulative.append(
            cumulative
        )

    trap_times = np.array(
        trap_times
    )

    trap_cumulative = np.array(
        trap_cumulative
    )


    # --------------------------------------------------------
    # Plot
    # --------------------------------------------------------

    fig, ax = plt.subplots()

    ax.plot(
        tx,
        E_ext / kBT,
        label="extracted gravitational energy"
    )

    if len(trap_times):

        ax.step(
            trap_times,
            trap_cumulative / kBT,
            where="post",
            label="trap work"
        )

    ax.set_xlabel(
        "Time [s]"
    )

    ax.set_ylabel(
        "Energy [kBT]"
    )

    ax.set_title(
        "Energy balance"
    )

    ax.grid()

    ax.legend()

    fig.tight_layout()

    return fig, ax


def plot_inter_ratchet_times(bus):
    """
    Histogram of time intervals between successive
    ratchet decisions.

    Analogous to inter-arrival-time statistics.
    """

    entries = bus.history.get(
        "ratchet_event",
        []
    )

    event_times = np.array(
        [
            t
            for t, event in entries
            if bool(event)
        ],
        dtype=float
    )

    if len(event_times) < 2:
        return None, None


    dt = np.diff(
        event_times
    )


    fig, ax = plt.subplots()

    ax.hist(
        dt * 1e3,
        bins=50,
        density=False
    )

    ax.set_xlabel(
        "Inter-ratchet time [ms]"
    )

    ax.set_ylabel(
        "Counts"
    )

    ax.set_title(
        "Inter-ratchet interval distribution"
    )

    ax.grid()

    fig.tight_layout()

    return fig, ax

def save_figure(
    fig,
    run_dir,
    filename
):

    fig.savefig(
        run_dir / filename,
        dpi=200,
        bbox_inches="tight"
    )

# ============================================================
# Standard P1 plot set
# ============================================================

def plot_all(
    bus,
    run_dir=None,
    show=True
):
    """
    Generate, optionally save, and optionally display
    the standard Q-SYNTH result plots.
    """

    plot_functions = {

        "closed_loop.png":
            plot_closed_loop,

        "estimator_error.png":
            plot_estimator_error,

        "ratchet_events.png":
            plot_ratchet_events,

        "inter_ratchet_times.png":
            plot_inter_ratchet_times,

        "innovation.png":
            plot_innovation,

        "innovation_distribution.png":
            plot_innovation_histogram,

        "regime_statistics.png":
            plot_supervisor_statistics,

        "energy_balance.png":
            plot_energy_balance
    }


    for filename, plot_function in plot_functions.items():

        result = plot_function(
            bus
        )

        # ----------------------------------------------------
        # Plot function returned nothing
        # ----------------------------------------------------

        if result is None:

            print(
                f"Plot skipped: {filename} "
                f"(plot function returned None)"
            )

            continue


        # ----------------------------------------------------
        # Expected result: (fig, ax)
        # ----------------------------------------------------

        fig, ax = result


        # ----------------------------------------------------
        # Plot function deliberately indicated no data
        # ----------------------------------------------------

        if fig is None:

            print(
                f"Plot skipped: {filename} "
                f"(insufficient data)"
            )

            continue


        # ----------------------------------------------------
        # Save figure
        # ----------------------------------------------------

        if run_dir is not None:

            fig.savefig(
                run_dir / filename,
                dpi=200,
                bbox_inches="tight"
            )


    # ========================================================
    # Display all figures together
    # ========================================================

    if show:

        plt.show()

    else:

        plt.close("all")