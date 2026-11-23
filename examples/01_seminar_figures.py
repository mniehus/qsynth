"""Render the policy-matrix and coupled-map figures for the MkDocs workflow."""

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot_matrix(fig, ax, scores, regimes, policies, title, unit):
    image = ax.imshow(scores, cmap="Blues", aspect="auto")
    ax.set(title=title, xlabel="Candidate policy", ylabel="Operating regime",
           xticks=range(len(policies)), xticklabels=policies,
           yticks=range(len(regimes)), yticklabels=regimes)
    for (i, j), value in np.ndenumerate(scores):
        color = "white" if image.norm(value) > 0.6 else "#132b40"
        ax.text(j, i, f"{value:.2f}", ha="center", va="center", color=color)
    fig.colorbar(image, ax=ax, label=unit, shrink=0.85)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("instance", type=Path, help="Notebook 02 offline batch instance.json")
    parser.add_argument("--output", type=Path, default=Path("docs/assets"))
    args = parser.parse_args()
    instance = json.loads(args.instance.read_text(encoding="utf-8"))
    if instance.get("schema_version") != 1 or instance.get("cost_unit") != "kBT/s":
        parser.error("expected the schema version 1 IE instance with costs in kBT/s")
    measured = -np.asarray(instance["cost_matrix"], dtype=float)
    regimes = [f"{regime['sigma_m_m'] * 1e9:g} nm RMS" for regime in instance["regimes"]]
    policies = [policy["name"].capitalize() for policy in instance["policies"]]
    if measured.shape != (len(regimes), len(policies)) or not np.isfinite(measured).all():
        parser.error("expected a finite score for each regime and policy")
    args.output.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(1, 2, figsize=(10, 3.1), layout="constrained")
    plot_matrix(fig, axes[0], np.array([[-1., -3.], [-2.5, -1.]]),
                ["Baseline", "Elevated"], ["Nominal", "Robust"],
                "Illustrative · Notebook 01", "Score (arbitrary units)")
    plot_matrix(fig, axes[1], measured, regimes, policies,
                f"IE simulation · {len(instance['seeds'])} matched seeds", "Score (kBT/s)")
    fig.savefig(args.output / "policy-matrix.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 2.8), layout="constrained")
    for y, label, policy_map in [(1, "β = 0 · score 18", "1212"), (0, "β = 2 · score 13", "1112")]:
        for i, (a, b) in enumerate(zip(policy_map, policy_map[1:])):
            ax.plot([i, i + 1], [y, y], color="#7b4350" if a != b else "#7c8993",
                    linestyle="--" if a != b else "-", linewidth=2)
        for i, policy in enumerate(policy_map):
            ax.scatter(i, y, color={"1": "#23597c", "2": "#a85127"}[policy], s=650, zorder=3)
            ax.text(i, y, f"π{policy}", ha="center", va="center", color="white", zorder=4)
        ax.text(-0.42, y, label, ha="right", va="center")
    for i in range(4):
        ax.text(i, 1.35, f"Regime {i + 1}", ha="center")
    ax.set(xlim=(-1.55, 3.35), ylim=(-0.45, 1.6),
           title="Illustrative four-regime chain · dashed edges change policy")
    ax.axis("off")
    fig.savefig(args.output / "coupled-policy-map.png", dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    main()
