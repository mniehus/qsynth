from config import (
    physical,
    timing,
    sensor,
    D,
    tau_r,
    sigma_eq,
    x_g,
    Q_phys,
    R_phys
)

from synthesis.synthesizer import QSynthesizer

from simulation.build import build_simulation
from simulation.runner import run_simulation

from results.metrics import print_metrics
from results.plots import plot_all

from results.run_output import (
    create_run_directory,
    save_run_summary,
    save_raw_timeseries
)


# ------------------------------------------------------------
# Policy library
# ------------------------------------------------------------

offline = QSynthesizer()

policy_library = offline.synthesize()


# ------------------------------------------------------------
# Build simulation
# ------------------------------------------------------------

bus, scheduler, supervisor = build_simulation(
    policy_library=policy_library,
    seed=42
)


# ------------------------------------------------------------
# Run one simulation
# ------------------------------------------------------------

result = run_simulation(
    scheduler=scheduler,
    bus=bus,
    supervisor=supervisor,
    duration=1.0
)


# ------------------------------------------------------------
# Results
# ------------------------------------------------------------

print_metrics(
    result.bus
)


derived = {
    "Diffusion D [um^2/s]":
        D * 1e12,

    "Relaxation time [ms]":
        tau_r * 1e3,

    "Thermal sigma [nm]":
        sigma_eq * 1e9,

    "Gravitational sag [nm]":
        x_g * 1e9,

    "Q_phys [nm^2]":
        Q_phys * 1e18,

    "R_phys [nm^2]":
        R_phys * 1e18
}


run_dir = create_run_directory()


save_run_summary(
    run_dir=run_dir,
    metrics=result.metrics,
    physical=physical,
    timing=timing,
    sensor=sensor,
    policy=result.supervisor.active_policy,
    derived=derived
)


save_raw_timeseries(
    run_dir=run_dir,
    bus=result.bus
)


plot_all(
    result.bus,
    run_dir=run_dir,
    show=True
)


print(
    f"\nResults saved to: {run_dir}"
)