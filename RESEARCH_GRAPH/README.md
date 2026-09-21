# Research State Graph (RSG) — Prototype

RSG is a prototype information-maintenance layer over the existing research numbering.

| Layer | Example | Purpose |
|---|---|---|
| Research Address | `1.12.6.1-L` | Human-readable research location |
| Graph ID | `G-0001` | Stable identity for traversal |
| Mermaid | node `G-0001` | Visual navigation |

**Rule:** numbers tell us where; Graph IDs tell us which node; edges tell us how nodes relate.

## Edge codes
P = parent, D = depends on, T = tested by, R = produced result, S = supports, C = contradicts, I = implies/affects, X = cross-branch, U = upstream constraint, N = next gate.

## Traversal
Start with a Graph ID such as `G-0001`, read its node record, follow its edge IDs, open the Mermaid view, then use the research address to reach the detailed branch document.

Plain Mermaid is the visualization layer; it does not dynamically query YAML by itself. The YAML remains the structured graph source.