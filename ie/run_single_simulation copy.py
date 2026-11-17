import numpy as np

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

from kernel.signals import SignalBus
from kernel.scheduler import Scheduler

from plant.langevin import LangevinPlant
from measurement.qpd import MeasurementBlock
from estimator.kalman import KalmanEstimator
from controller.ratchet import RatchetController
from actuator.aod import Actuator

from supervisor.statistics import StatisticsBlock
from supervisor.supervisor import Supervisor

from synthesis.offline import QSynthOffline

from results.metrics import (
    calculate_metrics,
    print_metrics
)

from results.plots import plot_all

from results.run_output import (
    create_run_directory,
    save_run_summary,
    save_raw_timeseries
)


# ------------------------------------------------------------
# Random generator
# ------------------------------------------------------------

rng = np.random.default_rng(
    seed=42
)


# ------------------------------------------------------------
# Communication bus
# ------------------------------------------------------------

bus = SignalBus()


# ------------------------------------------------------------
# Offline synthesis
# ------------------------------------------------------------

offline = QSynthOffline()

policy_library = (
    offline.synthesize()
)


# ------------------------------------------------------------
# Blocks
# ------------------------------------------------------------

plant = LangevinPlant(
    period=timing.plant_period,
    rng=rng
)


measurement = MeasurementBlock(
    period=timing.measurement_period,
    rng=rng,
    sigma_m=sensor.sigma_m
)


estimator = KalmanEstimator(
    period=timing.estimator_period,
    Q=Q_phys,
    R=R_phys
)


controller = RatchetController(
    period=timing.controller_period,
    alpha=policy_library["nominal"].alpha,
    XT=policy_library["nominal"].XT
)


actuator = Actuator(
    period=timing.actuator_period,
    delay=timing.actuator_delay
)


statistics = StatisticsBlock(
    period=timing.statistics_period,
    controller_period=timing.controller_period,
    window=0.1
)


supervisor = Supervisor(
    period=timing.supervisor_period,
    policy_library=policy_library,
    estimator=estimator,
    controller=controller
)

from visualization.dashboard import Dashboard

dashboard = Dashboard(
    period=10e-3
)

# ------------------------------------------------------------
# Initial conditions
# ------------------------------------------------------------

bus.publish(
    "actuator_state",
    0.0,
    0.0
)


# ------------------------------------------------------------
# Scheduler
# ------------------------------------------------------------

scheduler = Scheduler(
    bus
)


scheduler.add_block(
    plant
)

scheduler.add_block(
    measurement
)

scheduler.add_block(
    estimator
)

scheduler.add_block(
    controller
)

scheduler.add_block(
    actuator
)

scheduler.add_block(
    statistics
)

scheduler.add_block(
    supervisor
)

scheduler.add_block(
    dashboard
)

# ============================================================
# RUN SIMULATION
# ============================================================

simulation_time = 1.0

scheduler.run(
    duration=simulation_time
)


# ============================================================
# CALCULATE RESULTS
# ============================================================

metrics = calculate_metrics(
    bus
)

print_metrics(
    bus
)


# ============================================================
# DERIVED PHYSICAL / MODEL PARAMETERS
# ============================================================

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


# ============================================================
# SAVE HUMAN-READABLE SUMMARY
# ============================================================

run_dir = create_run_directory()

save_run_summary(
    run_dir=run_dir,
    metrics=metrics,
    physical=physical,
    timing=timing,
    sensor=sensor,
    policy=supervisor.active_policy,
    derived=derived
)

save_raw_timeseries(
    run_dir=run_dir,
    bus=bus
)


# ============================================================
# SAVE / SHOW FIGURES
# ============================================================

plot_all(
    bus,
    run_dir=run_dir,
    show=True
)


print(
    f"\nResults saved to: {run_dir}"
)