from simulation.build import build_simulation
from simulation.runner import run_simulation
from synthesis.objectives import balance_power_cost


def evaluate_trial(policy_library, policy_name, sigma_m, seed, duration, warmup_s):
    bus, scheduler, supervisor = build_simulation(
        policy_library, seed, fixed_policy=policy_name, sigma_m=sigma_m
    )
    result = run_simulation(scheduler, bus, supervisor, duration)
    if bus.history.get("active_policy") != [(0.0, policy_library[policy_name])]:
        raise RuntimeError(f"Expected {policy_name} to stay active from t=0.")

    return {
        **balance_power_cost(bus, warmup_s),
        "estimator_rmse_nm_full_run": float(result.metrics["estimator_error_RMS_nm"]),
    }
