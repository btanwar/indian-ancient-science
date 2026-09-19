# Research

One subfolder per line of thought: `Research/L###_short-name/`. Create it by copying the layout
below (see [\(templates/RESEARCH_{RUNBOOK}.md\)](../templates/RESEARCH_RUNBOOK.md) for the runbook itself).

```
Research/
└── L###_short-name/
    ├── runbook.md              (versioned plan; see TEMPLATE_RUNBOOK.md)
    ├── experiments/
    │   └── E001_short-name/    (one folder per experiment; scripts + params live here)
    └── results/
        └── E001_short-name.md  (one result file per experiment; see [`templates/RESEARCH_RESULT.md`](../templates/RESEARCH_RESULT.md))
```

## Runbook rules

- The runbook is the step-by-step plan: which analogy/requirement is being tested by which
  experiment, in what order, and why that order was chosen.
- Every time a result changes the plan (new step added, step reordered, step abandoned), **bump the
  runbook version** (`v1`, `v2`, ...) and keep the previous version's content in a "Version history"
  section at the bottom — never silently overwrite prior reasoning.
- Each runbook step must reference the experiment ID that tests it and the result file it produced.

## Experiment rules

- `experiments/E###_short-name/` holds the exact script(s)/parameters used. Keep experiments
  reproducible: pin parameters, note the environment/library versions used.
- Each experiment folder must preserve its derivation/equations, source provenance, assumptions,
  parameters, controls, and evidence status. Use `README.md` for this record and keep executable
  scripts beside it when available.
- Historical chat extractions may populate a derivation/protocol folder, but must be labeled
  `HISTORICAL`, `SOURCE DERIVATION`, or \(REQUIRES_{REPRODUCTION}\) until code and output are rerun.
- Do not modify an experiment after it has produced a recorded result; if you need to change it,
  create a new experiment ID and note the relationship to the previous one.

## Result rules

- One result file per experiment: `results/E###_short-name.md`.
- Every result file must state an explicit outcome using the shared status labels (see root
  `README.md`): `SUCCESSFUL`, `PARTIAL`, `NEGATIVE`, `FAILED`, `INCONCLUSIVE`,
  \(REQUIRES_{REPRODUCTION}\), etc.
- Record actual numeric output, not a rounded or "improved" version of it.
- If an experiment fails or a line of thought is abandoned, keep the result file — mark it
  `FAILED`/`ABANDONED` and explain why. This is itself a valid research record.

## Index

See [EXPERIMENT_SOURCE_INVENTORY.md](EXPERIMENT_SOURCE_INVENTORY.md) for the source and evidence
status of migrated derivations and experiment folders.

| Line of thought | Runbook version | Experiments run | Status |
|---|---|---|---|
| [L001 Ordered Coverage](L001_ordered_coverage_observer_time/) | v1 | 2 historical records; E003 planned | IN_PROGRESS |
| [L002 Emergent Dimension](L002_emergent_dimension_relational_capacity/) | v1 | 1 mathematical baseline; E002-E005 planned | PROPOSED |
| [L003 Coupled Oscillator](L003_coupled_oscillator_cosmic_mechanism/) | v1 | 3 source-traced records; V2.13 planned | PAUSED |
| [L004 Hidden State](L004_hidden_state_observer_accessibility/) | v1 | 3 source-traced records; reproduction required | PARTIAL |
| [L005 Complementary Channels](L005_complementary_channel_unification/) | v1 | 2 source-traced records; residual test blocked | OPEN |
| [L006 S-infinity / B-infinity](L006_s_infinity_b_infinity_relational_substrate/) | v2 | 4 source-traced records; E006 reproduction queue; E007-E009 planned | IN_PROGRESS |

## Phase 4 evidence policy

The initial records preserve prior-project and chat-archive evidence without silently promoting it
to newly reproduced data. A result marked \(REQUIRES_{REPRODUCTION}\) has a historical method or output
but no local executable and parameter bundle yet. A result marked `NEGATIVE` records a prior
boundary or failed claim and must remain visible. New experiments must add scripts, parameters,
environment details, and exact outputs under the corresponding `experiments/` folder before their
status is upgraded.
