"""Source-migrated V2.1 VCR coverage/order separation experiment."""

import json
from pathlib import Path
import numpy as np


def field(x):
    return (
        0.8 * np.sin(2 * np.pi * 2 * x + 0.2)
        + 0.35 * np.cos(2 * np.pi * 5 * x - 0.4)
        + 0.2 * np.sin(2 * np.pi * 9 * x + 0.7)
    )


def reconstruct_uniform(x, y, grid):
    order = np.argsort(x)
    return np.interp(grid, x[order], y[order])


def main():
    rng = np.random.default_rng(20260905)
    n = 64
    x = np.linspace(0.0, 1.0, n, endpoint=False)
    y = field(x)
    grid = np.linspace(0.0, 1.0, 4096, endpoint=False)
    reference = field(grid)
    perm_a = np.arange(n)
    perm_b = rng.permutation(n)
    seq_a = y[perm_a]
    seq_b = y[perm_b]
    rec_a = reconstruct_uniform(x, y, grid)
    rec_b = reconstruct_uniform(x[perm_b], y[perm_b], grid)
    result = {
        "n_samples": n,
        "sequence_relative_difference": float(np.linalg.norm(seq_a - seq_b) / np.linalg.norm(seq_a)),
        "static_reconstruction_relative_difference": float(np.linalg.norm(rec_a - rec_b) / np.linalg.norm(rec_a)),
        "relative_error_to_reference": float(np.linalg.norm(rec_a - reference) / np.linalg.norm(reference)),
        "status": "source-migrated toy experiment; physical time not inferred",
    }
    output = Path(__file__).with_name("results.json")
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
