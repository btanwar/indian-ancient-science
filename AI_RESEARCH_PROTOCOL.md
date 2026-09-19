# AI Research Protocol

This is the source of truth for AI-assisted work in this repository. It describes how Copilot should process requests, preserve research history, and distinguish evidence from speculation.

## Scope

Apply this protocol to requests involving the repository, including research, writing, analysis, file organization, experiments, documentation, and code.

## Repository phases

1. `Analogies/` records source analogies and separates metaphor from testable content.
2. `Line-Of-Thoughts/` defines research directions and their goals.
3. `Requirements/` defines falsifiable gates and pass/fail conditions before deep research.
4. `Research/` contains versioned runbooks, experiments, and results.
5. `templates/` contains reusable document templates.
6. `assets/analogies/` contains small local explanatory schematics used by analogy documents.

The sibling projects `indian-mythology-modern-science/` and `indian-philosophy-modern-physics/` are historical source material. Use them when relevant, especially their chat-derived records, audits, experiments, results, and failed paths. Treat historical chat claims as provenance until the underlying method and output are reproduced.

## Request workflow

1. Identify the concrete file, symbol, behavior, research line, or failing check that owns the request.
2. Read only enough nearby material to state one falsifiable local hypothesis and one cheap check that could disconfirm it.
3. Preserve the existing structure, terminology, status labels, links, and evidence boundaries.
4. Make the smallest focused change that tests or satisfies the request.
5. Immediately run the narrowest available validation after the first substantive edit.
6. Continue with adjacent edits only after that validation succeeds or the failure is understood.
7. Finish with an executable validation whenever the environment provides one; otherwise report the limitation.
8. Do not commit, create branches, or revert user changes unless explicitly requested.

## Research evidence rules

- An analogy is not a theory, mechanism, proof, or prediction.
- Separate established mathematics, established physics, reproduced computation, historical report, working hypothesis, partial result, failed test, and open question.
- Preserve negative, failed, rejected, abandoned, paused, and inconclusive results. They are research evidence.
- Never silently upgrade a historical chat result to a reproduced result.
- Do not report a numerical result as verified unless the code, parameters, environment, and output are available or the result has been independently rerun.
- Mathematical success does not imply physical relevance.
- Known physics does not imply novelty.
- No new-physics or unification claim is allowed without an existing-physics audit and a quantitative falsifiable consequence.
- A scan parameter, ordering index, phase, fitted value, or reconstruction coordinate must not be renamed physical time, mass, length, or another physical quantity by definition.
- Fitted parameters and branch-specific transformations cannot establish universality.
- Do not add a new analogy or research branch merely to evade a negative result.
- Keep substrate, manifestation, information, observation, and representation distinct where a line of thought requires those layers.

## Phase-specific rules

### Analogies

Keep the source account faithful to the original material. Use the analogy icon key as semantic
signposts, not decoration: 📖 source story, 🗺️ mapping, 💡 purpose, ✅ suggested value, ⚠️ limits,
🧪 testable component, 🪞 metaphor, 🔬 known science, and 📚 provenance. State what the analogy
suggests, what it does not explain, its testable component, and its known-science connection. Add
a small local schematic from `assets/analogies/` when it clarifies the mapped properties. Use
meaningful alt text and a caption; label conceptual reconstructions clearly and never present them
as historical evidence or scientific proof.

### Lines of thought

Every line must state a goal as a question, a domain, its analogies, its requirements, its research folder, current status, and explicit claims it must not make.

### Requirements

Every requirement must have a type, an explicit pass/fail condition, an order of attack, a definition of success, and a definition of failure or abandonment. Do not rewrite requirements after seeing results to make a result pass.

### Research runbooks

Each `Research/L###_*/runbook.md` must contain:

- links to its line of thought and requirements;
- an explicit status and research boundary;
- a Mermaid `Research map` showing the line, requirements, experiment sequence, evidence statuses, and blocking gates;
- a versioned plan with one experiment ID per step;
- current interpretation distinguishing facts from speculation;
- next action;
- version history whenever the plan changes.

Keep the Mermaid map synchronized with the plan. Use status labels such as `SUCCESSFUL`, `PARTIAL`, `NEGATIVE`, `FAILED`, `INCONCLUSIVE`, `REQUIRES_REPRODUCTION`, `OPEN`, `BLOCKED`, and `PAUSED` directly in map labels.

### Experiments and results

Experiments must be reproducible and immutable after a result is recorded. A changed method gets a new experiment ID. Result records must include the hypothesis, method, exact output, interpretation, requirement decision, and next action.

## Validation and links

- Use the templates in `templates/` for new documents.
- Keep Markdown links relative and valid after file moves.
- Check that every runbook has a Mermaid map and a plan.
- Check that every experiment result links back to its runbook.
- Run a focused test, script, lint, typecheck, or link/filesystem check appropriate to the change.
- Mention unresolved validation failures and unrelated pre-existing issues in the final response.

## Communication

State what is being inspected, what local hypothesis is being tested, what was changed, and how it was validated. Be concise. Do not overclaim. When a request is ambiguous but can be completed safely, choose the smallest reversible interpretation and record the assumption.

## Canonical references

- [Project README](README.md)
- [Analogies](Analogies/README.md)
- [Line of Thoughts](Line-Of-Thoughts/README.md)
- [Requirements](Requirements/README.md)
- [Research](Research/README.md)
- [Templates](templates/)
