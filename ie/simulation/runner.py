from dataclasses import dataclass

from results.metrics import calculate_metrics


@dataclass
class SimulationResult:
    bus: object
    supervisor: object
    metrics: dict


def run_simulation(
    scheduler,
    bus,
    supervisor,
    duration
):
    scheduler.run(
        duration=duration
    )

    metrics = calculate_metrics(
        bus
    )

    return SimulationResult(
        bus=bus,
        supervisor=supervisor,
        metrics=metrics
    )