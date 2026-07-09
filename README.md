# AI Research Writing Pipeline

[中文说明](README.zh-CN.md)

Evidence-gated Codex skill for full-cycle academic manuscript writing.

This repository packages a reusable Codex skill that turns a research project,
experiment folder, draft paper, or messy multi-agent workspace into a traceable
academic-writing pipeline. It is intentionally domain-neutral: the active
project supplies the field, venue, method facts, evidence rules, and style
constraints.

## What It Does

- Maps a research workspace before editing prose.
- Integrates idea evaluation, literature verification, paper reading, baseline
  selection, evidence audit, writing, polishing, figures, review, rebuttal,
  data/release statements, and side-output workflows.
- Separates literature, experiment evidence, writing, figures, review, mentor
  advice, integration, administration, and release work.
- Requires claims, numbers, references, figures, and unknowns to be registered
  before they are promoted into a manuscript.
- Preserves evidence boundaries, negative results, post-hoc explanations, and
  unsupported gaps.
- Helps organize chaotic projects without breaking traceability paths.
- Includes a small inventory script for first-pass project cleanup planning.

## Repository Layout

```text
ai-research-writing-pipeline/
|-- README.md
|-- LICENSE
`-- skills/
    `-- ai-research-writing-pipeline/
        |-- SKILL.md
        |-- agents/
        |   `-- openai.yaml
        |-- references/
        |   |-- artifact-contracts.md
        |   |-- capability-playbooks.md
        |   `-- framework-patterns.md
        `-- scripts/
            `-- workspace_inventory.py
```

## Install

Install the skill into Codex from this GitHub repository:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo youngandboor/ai-research-writing-pipeline \
  --path skills/ai-research-writing-pipeline
```

Restart Codex after installation so the new skill is discovered.

## Use

Invoke the skill explicitly:

```text
Use $ai-research-writing-pipeline to inspect this research project, build claim
and evidence ledgers, and turn the current draft into a traceable manuscript
workflow.
```

For a messy existing project, start with the bundled inventory script:

```bash
python3 ~/.codex/skills/ai-research-writing-pipeline/scripts/workspace_inventory.py .
```

## Design Principles

This skill treats academic writing as controlled integration, not as
free-form prose generation.

The main discipline is:

1. Orient the project.
2. Classify the request into a lane.
3. Freeze method and evidence invariants.
4. Build evidence ledgers.
5. Register claims and numbers.
6. Draft only from registered evidence.
7. Render figures from source data.
8. Integrate once through a controller role.
9. Red-team from the current artifact.
10. Repair by expected score gain and evidence risk.
11. Gate final readiness through validators.

## Included References

- `framework-patterns.md` distills reusable patterns from state-machine
  research workflows and multi-agent paper-production systems.
- `artifact-contracts.md` gives lightweight JSON/JSONL contracts for task
  packets, claim registries, numeric claims, reference ledgers, figure
  manifests, and completion manifests.
- `capability-playbooks.md` integrates the common capabilities of idea
  evaluators, literature tools, paper readers, baseline selectors, writing and
  polishing workflows, figure agents, reviewers, rebuttal planners, data
  statement helpers, presentation builders, and release gates into this single
  skill.

## License

MIT License.
