import argparse
import csv
import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, stdev

from config import physical, timing
from synthesis.evaluate import evaluate_trial
from synthesis.regimes import REGIMES
from synthesis.synthesizer import QSynthesizer


def main():
    parser = argparse.ArgumentParser(description="Evaluate the fixed-policy IE 2x2 instance.")
    parser.add_argument("--seeds", type=int, nargs="+", default=list(range(42, 47)))
    args = parser.parse_args()
    if min(args.seeds) < 0 or len(set(args.seeds)) != len(args.seeds):
        parser.error("seeds must be distinct nonnegative integers")

    duration = 1.0
    warmup_s = 0.1
    policies = QSynthesizer().synthesize()
    trials = []
    costs = []
    deviations = []
    for regime, sigma_m in REGIMES.items():
        regime_costs = []
        regime_deviations = []
        for policy in policies:
            trial_costs = []
            for seed in args.seeds:
                metrics = evaluate_trial(policies, policy, sigma_m, seed, duration, warmup_s)
                trials.append({"regime": regime, "policy": policy, "seed": seed, **metrics})
                cost = metrics["cost_kbt_per_s"]
                trial_costs.append(cost)
                print(f"{regime} / {policy} / seed {seed}: {cost:.3f} kBT/s", flush=True)
            regime_costs.append(mean(trial_costs))
            regime_deviations.append(stdev(trial_costs) if len(trial_costs) > 1 else None)
        costs.append(regime_costs)
        deviations.append(regime_deviations)

    instance = {
        "schema_version": 1,
        "regimes": [{"name": name, "sigma_m_m": sigma} for name, sigma in REGIMES.items()],
        "policies": [asdict(policy) for policy in policies.values()],
        "seeds": args.seeds,
        "duration_s": duration,
        "warmup_s": warmup_s,
        "physical": asdict(physical),
        "timing": asdict(timing),
        "objective": "signed trap power minus gravitational power over the post-warmup window",
        "cost_unit": "kBT/s",
        "cost_matrix": costs,
        "sample_std_matrix": deviations,
        "switch_cost": 0.0,
    }
    instance_json = json.dumps(instance, indent=2, allow_nan=False)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    directory = Path(__file__).resolve().parent / "results" / "runs" / f"offline_{stamp}"
    directory.mkdir(parents=True)
    with (directory / "trials.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(trials[0]))
        writer.writeheader()
        writer.writerows(trials)
    (directory / "instance.json").write_text(instance_json + "\n", encoding="utf-8")
    print(f"Instance saved to {directory / 'instance.json'}")


if __name__ == "__main__":
    main()
