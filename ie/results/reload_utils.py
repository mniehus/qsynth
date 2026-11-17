"""
Reusable utilities for loading saved Q-SYNTH runs.
"""

from pathlib import Path
import numpy as np


def load_run(run_dir):
    """
    Load signals.npz from a Q-SYNTH run directory.
    """

    run_dir = Path(run_dir)

    filename = run_dir / "signals.npz"

    if not filename.exists():
        raise FileNotFoundError(
            f"No signals.npz found in: {run_dir}"
        )

    return np.load(
        filename,
        allow_pickle=False
    )


def latest_run_directory(
    base = Path(__file__).resolve().parent / "runs"):
    """
    Find newest timestamped run directory.
    """

    base = Path(__file__).resolve().parent / "runs"
    
    if not base_dir.exists():
        raise FileNotFoundError(
            f"Run directory does not exist: {base_dir}"
        )

    run_dirs = sorted(
        [
            path
            for path in base_dir.iterdir()
            if path.is_dir()
        ]
    )

    if not run_dirs:
        raise FileNotFoundError(
            "No saved runs found."
        )

    return run_dirs[-1]


def load_latest_run(
    base_dir="results/runs"
):
    """
    Load newest available saved run.

    Returns
    -------
    run_dir, data
    """

    run_dir = latest_run_directory(
        base_dir
    )

    data = load_run(
        run_dir
    )

    return run_dir, data


def list_signals(data):
    """
    Print arrays stored in signals.npz.
    """

    print()
    print("Available saved signals")
    print("-----------------------")

    for name in sorted(data.files):

        array = data[name]

        print(
            f"{name:<40} "
            f"shape={array.shape}"
        )


def load_signal(
    data,
    name
):
    """
    Return one named array.
    """

    if name not in data.files:
        raise KeyError(
            f"Signal '{name}' not found."
        )

    return data[name]


def load_timeseries(
    data,
    time_name,
    value_name
):
    """
    Return matching time and value arrays.
    """

    t = load_signal(
        data,
        time_name
    )

    values = load_signal(
        data,
        value_name
    )

    return t, values


def load_core_signals(data):
    """
    Convenience loader for most-used signals.
    """

    signals = {}

    pairs = {
        "plant":
            (
                "plant_t",
                "plant_x"
            ),

        "measurement":
            (
                "measurement_t",
                "measurement_y"
            ),

        "estimate":
            (
                "estimate_t",
                "estimate_xhat"
            ),

        "actuator":
            (
                "actuator_t",
                "actuator_lambda"
            ),

        "innovation":
            (
                "innovation_t",
                "innovation"
            ),

        "relative_position":
            (
                "relative_position_t",
                "relative_position"
            ),

        "ratchet":
            (
                "ratchet_t",
                "ratchet_event"
            )
    }

    for name, (
        time_name,
        value_name
    ) in pairs.items():

        if (
            time_name in data.files
            and value_name in data.files
        ):

            signals[name] = (
                data[time_name],
                data[value_name]
            )

    return signals