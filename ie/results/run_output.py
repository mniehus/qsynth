"""
Q-SYNTH run-output management.

Creates one timestamped directory for every simulation run
and saves:

    - run parameters
    - derived model quantities
    - performance metrics
    - plots
"""

import numpy as np
from datetime import datetime
from pathlib import Path


def create_run_directory():

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    base = Path(__file__).resolve().parent / "runs"

    run_dir = (
        base
        / timestamp
    )

    run_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    return run_dir

def save_run_summary(
    run_dir,
    metrics,
    physical,
    timing,
    sensor,
    policy,
    derived
):

    filename = (
        run_dir
        / "run_summary.txt"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "Q-SYNTH P1 SOFTWARE RUN\n"
        )

        f.write(
            "========================================\n"
        )

        f.write(
            f"Created: "
            f"{datetime.now().isoformat()}\n\n"
        )


        # ================================================
        # Physical / experimental model
        # ================================================

        f.write(
            "[PHYSICAL / EXPERIMENTAL PARAMETERS]\n"
        )

        f.write(
            f"Temperature               : "
            f"{physical.T:.3f} K\n"
        )

        f.write(
            f"Fluid viscosity           : "
            f"{physical.eta:.6e} Pa s\n"
        )

        f.write(
            f"Bead radius               : "
            f"{physical.radius*1e6:.3f} um\n"
        )

        f.write(
            f"Bead diameter             : "
            f"{2*physical.radius*1e6:.3f} um\n"
        )

        f.write(
            f"Effective density diff.   : "
            f"{physical.delta_rho:.3f} kg/m^3\n"
        )

        f.write(
            f"Trap stiffness            : "
            f"{physical.kappa*1e6:.3f} pN/um\n"
        )

        f.write(
            f"Measurement noise sigma   : "
            f"{sensor.sigma_m*1e9:.3f} nm\n"
        )

        f.write("\n")


        # ================================================
        # Derived model
        # ================================================

        f.write(
            "[DERIVED MODEL PARAMETERS]\n"
        )

        for name, value in derived.items():

            f.write(
                f"{name:<26}: "
                f"{value}\n"
            )

        f.write("\n")


        # ================================================
        # Timing
        # ================================================

        f.write(
            "[SIMULATION / TIMING PARAMETERS]\n"
        )

        f.write(
            f"Plant period              : "
            f"{timing.plant_period*1e6:.3f} us\n"
        )

        f.write(
            f"Measurement period        : "
            f"{timing.measurement_period*1e6:.3f} us\n"
        )

        f.write(
            f"Estimator period          : "
            f"{timing.estimator_period*1e6:.3f} us\n"
        )

        f.write(
            f"Controller period         : "
            f"{timing.controller_period*1e6:.3f} us\n"
        )

        f.write(
            f"Actuator period           : "
            f"{timing.actuator_period*1e6:.3f} us\n"
        )

        f.write(
            f"Actuator delay            : "
            f"{timing.actuator_delay*1e6:.3f} us\n"
        )

        f.write(
            f"Statistics period         : "
            f"{timing.statistics_period*1e3:.3f} ms\n"
        )

        f.write(
            f"Supervisor period         : "
            f"{timing.supervisor_period*1e3:.3f} ms\n"
        )

        f.write("\n")


        # ================================================
        # Active policy
        # ================================================

        f.write(
            "[ESTIMATOR / CONTROLLER POLICY]\n"
        )

        f.write(
            f"Policy                    : "
            f"{policy.name}\n"
        )

        f.write(
            f"Q_eff                     : "
            f"{policy.Q_eff*1e18:.6f} nm^2\n"
        )

        f.write(
            f"R_eff                     : "
            f"{policy.R_eff*1e18:.6f} nm^2\n"
        )

        f.write(
            f"alpha                     : "
            f"{policy.alpha:.6f}\n"
        )

        f.write(
            f"X_T                       : "
            f"{policy.XT*1e9:.6f} nm\n"
        )

        f.write("\n")


        # ================================================
        # Results
        # ================================================

        f.write(
            "[RESULTS]\n"
        )

        for name, value in metrics.items():

            f.write(
                f"{name:<26}: "
                f"{value}\n"
            )

def save_raw_timeseries(
    run_dir,
    bus
):
    """
    Save raw Q-SYNTH simulation time series.

    Output
    ------
    signals.npz

    Each signal is stored with its own timestamp array,
    because different blocks may run at different rates.

    Examples
    --------
    plant_t, plant_x
    measurement_t, measurement_y
    estimate_t, estimate_xhat
    actuator_t, actuator_lambda
    innovation_t, innovation
    ratchet_t, ratchet_event

    Important
    ---------
    We deliberately do NOT assume a common time base.
    """

    data = {}


    # ========================================================
    # Helper for scalar-valued histories
    # ========================================================

    def add_scalar_signal(
        history_name,
        time_name,
        value_name
    ):

        entries = bus.history.get(
            history_name,
            []
        )

        if len(entries) == 0:
            return

        data[time_name] = np.array(
            [
                t
                for t, value in entries
            ],
            dtype=float
        )

        data[value_name] = np.array(
            [
                value
                for t, value in entries
            ]
        )


    # ========================================================
    # Fast physical/control signals
    # ========================================================

    add_scalar_signal(
        "plant_state",
        "plant_t",
        "plant_x"
    )

    add_scalar_signal(
        "measurement",
        "measurement_t",
        "measurement_y"
    )

    add_scalar_signal(
        "estimate",
        "estimate_t",
        "estimate_xhat"
    )

    add_scalar_signal(
        "covariance",
        "covariance_t",
        "covariance_P"
    )

    add_scalar_signal(
        "innovation",
        "innovation_t",
        "innovation"
    )

    add_scalar_signal(
        "relative_position",
        "relative_position_t",
        "relative_position"
    )

    add_scalar_signal(
        "control_command",
        "control_command_t",
        "control_command_lambda"
    )

    add_scalar_signal(
        "actuator_state",
        "actuator_t",
        "actuator_lambda"
    )

    add_scalar_signal(
        "ratchet_event",
        "ratchet_t",
        "ratchet_event"
    )


    # ========================================================
    # Trap-move events
    # ========================================================

    entries = bus.history.get(
        "trap_move",
        []
    )

    if len(entries):

        data["trap_move_t"] = np.array(
            [
                t
                for t, event in entries
            ],
            dtype=float
        )

        data["trap_move_command_t"] = np.array(
            [
                event["command_time"]
                for t, event in entries
            ],
            dtype=float
        )

        data["trap_move_apply_t"] = np.array(
            [
                event["apply_time"]
                for t, event in entries
            ],
            dtype=float
        )

        data["trap_move_latency"] = np.array(
            [
                event["latency"]
                for t, event in entries
            ],
            dtype=float
        )

        data["trap_move_lambda_old"] = np.array(
            [
                event["lambda_old"]
                for t, event in entries
            ]
        )

        data["trap_move_lambda_new"] = np.array(
            [
                event["lambda_new"]
                for t, event in entries
            ]
        )

        data["trap_move_delta_lambda"] = np.array(
            [
                event["delta_lambda"]
                for t, event in entries
            ]
        )

        data["trap_move_bead_position"] = np.array(
            [
                event["bead_position"]
                for t, event in entries
            ]
        )

        data["trap_move_work"] = np.array(
            [
                event["trap_work"]
                for t, event in entries
            ]
        )


    # ========================================================
    # Slow supervisor statistics
    # ========================================================

    entries = bus.history.get(
        "statistics",
        []
    )

    if len(entries):

        data["statistics_t"] = np.array(
            [
                t
                for t, stats in entries
            ],
            dtype=float
        )

        statistical_keys = [
            "relative_mean",
            "relative_std",
            "relative_skewness",
            "relative_excess_kurtosis",
            "relative_rho1",
            "innovation_mean",
            "innovation_rms",
            "ratchet_count_window",
            "ratchet_rate",
            "window",
            "sample_count"
        ]

        for key in statistical_keys:

            data[
                "statistics_" + key
            ] = np.array(
                [
                    stats[key]
                    for t, stats in entries
                ]
            )


    # ========================================================
    # Save compressed file
    # ========================================================

    filename = (
        run_dir
        / "signals.npz"
    )

    np.savez_compressed(
        filename,
        **data
    )

    return filename