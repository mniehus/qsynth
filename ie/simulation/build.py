import numpy as np

from config import timing, sensor, Q_phys, R_phys

from kernel.signals import SignalBus
from kernel.scheduler import Scheduler

from plant.langevin import LangevinPlant
from measurement.qpd import MeasurementBlock
from estimator.kalman import KalmanEstimator
from controller.ratchet import RatchetController
from actuator.aod import Actuator

from supervisor.statistics import StatisticsBlock
from supervisor.supervisor import Supervisor

from visualization.dashboard import Dashboard


def build_simulation(
    policy_library,
    seed=42
):
    rng = np.random.default_rng(seed)

    bus = SignalBus()

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

    dashboard = Dashboard(
        period=10e-3
    )

    bus.publish(
        "actuator_state",
        0.0,
        0.0
    )

    scheduler = Scheduler(bus)

    for block in [
        plant,
        measurement,
        estimator,
        controller,
        actuator,
        statistics,
        supervisor,
        dashboard
    ]:
        scheduler.add_block(block)

    return bus, scheduler, supervisor