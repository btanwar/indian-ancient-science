# Indian Mythology to Modern Science

This project is inspired by the Indian mythological system and the body of texts and knowledge that
has shaped generations across the Indian subcontinent.

It is an attempt to relate Indian mythological objects, stories, tales, and incidents to modern
science and technology, and to build disciplined, testable theories around them — not to claim
that mythology already contains modern science, but to use it as a source of **analogies** that can
be turned into falsifiable hypotheses, experiments, and (where they survive testing) useful
theories, tools, or technologies for the benefit of society.

AI-assisted work follows the canonical [AI Research Protocol](AI_RESEARCH_PROTOCOL.md). Copilot
workspace instructions are maintained in [.github/copilot-instructions.md](.github/copilot-instructions.md).

## Core method

```
Mythological object / story / incident
        │
        ▼
   Analogy (Analogies/)
        │  (one or more analogies combined, like beads strung on a thread)
        ▼
   Line of Thought (Line-Of-Thoughts/)
        │  (a coherent research direction built from one or more analogies)
        ▼
   Requirements (Requirements/)
        │  (what must be true / built / proven for the line of thought to succeed)
        ▼
   Research (Research/)
        │  (runbook + experiments + results, iterated and versioned)
        ▼
   Surviving theory / law / postulate / technology
   — or —
   Documented failure / abandonment (still a valid, valuable outcome)
```

An **analogy is not a theory**. A **line of thought is not a result**. A result is not a theory
until it has been tested, reproduced, and has survived attempts to falsify it. This project keeps
those stages in separate folders so that speculation, direction-setting, and evidence are never
mixed together or mistaken for one another.

## Research discipline (carried over from prior projects in this workspace)

This project reuses the discipline developed in the sibling repositories
`indian-mythology-modern-science` and `indian-philosophy-modern-physics`:

- **Do not invent** experiments, numbers, dates, equations, or citations. If something is
  historical/reported but not independently reproduced, label it that way.
- **Distinguish analogy from mechanism.** An analogy is a conceptual mapping; it becomes a
  candidate mechanism only once it has a testable mathematical or experimental form.
- **Use explicit status labels** everywhere (see below) instead of vague words like "promising" or
  "works".
- **Preserve failures.** An abandoned or falsified line of thought is a completed piece of research,
  not wasted effort — document why it failed and what (if anything) survived from it.
- **Version every runbook.** As soon as a test changes the direction of a line of thought, bump the
  runbook version and keep the history instead of overwriting it.
- **Trace every claim to its source** (which text/story/analogy, which experiment, which result
  file).

### Status labels

Use these labels consistently across `Line-Of-Thoughts/`, `Requirements/`, and `Research/`:

`PROPOSED` · `IN_PROGRESS` · `PARTIAL` · `SUCCESSFUL` · `NEGATIVE` · `FAILED` · `INCONCLUSIVE` ·
`ANALOGY_ONLY` · `REQUIRES_REPRODUCTION` · `ABANDONED` · `CLOSED` · `OPEN`

## Folder structure

1. **`Analogies/`** — A comprehensive, indexed list of analogies extracted from Indian mythology
   (objects, stories, tales, incidents) mapped to a modern scientific/technological concept. Each
   analogy records what it maps, why it was proposed, what it explains, what it does not explain,
   and whether any part of it is testable. See `Analogies/README.md`.

2. **`Line-Of-Thoughts/`** — Each line of thought is a named research direction built from one or
   more analogies (like beads and thread forming a mala). Each entry defines: its goal, the
   analogies it draws on, the modern science/technology domain it targets, and its current status.
   See `Line-Of-Thoughts/README.md`.

3. **`Requirements/`** — For each line of thought, the concrete list of what must be defined,
   proven, measured, or built for it to evolve into a successful theory, law, postulate, or
   technology. This is the step-by-step success criteria, written before research begins so success
   isn't redefined after the fact. See `Requirements/README.md`.

4. **`Research/`** — One subfolder per line of thought, containing the actual research:
   - `runbook.md` — step-by-step plan connecting each analogy/test to the next, with the reasoning
     for why each experiment is run in that order. Versioned (`v1`, `v2`, …) every time a result
     changes the plan.
   - `experiments/` — scripts and exact parameters for each test.
   - `results/` — detailed output plus explicit pass/fail/abandoned/closed documentation for every
     experiment, referencing the runbook step and version it belongs to.

  See [`Research/README.md`](Research/README.md) and [`templates/RESEARCH_RUNBOOK.md`](templates/RESEARCH_RUNBOOK.md).

## Templates

The root [`templates/`](templates/) folder contains the reusable templates. Copy the appropriate
template to start a new analogy, line of thought, requirements document, runbook, or result record.
 