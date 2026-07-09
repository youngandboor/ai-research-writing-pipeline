---
name: ai-research-writing-pipeline
description: End-to-end evidence-gated academic writing workflow for turning a research project, experiment folder, paper draft, review history, or messy AI-agent workspace into a traceable manuscript pipeline. Use when the user asks to write, rewrite, organize, audit, red-team, polish, submit, or manage a scholarly paper across idea, literature, experiment evidence, claims, figures, draft integration, review response, and final readiness; especially when multiple agents, prior chat memory, numeric claims, citations, figures, or project files must be kept synchronized without fabricating evidence.
---

# AI Research Writing Pipeline

## Core Rule

Treat writing as a controlled integration problem, not a prose-generation problem. A manuscript claim may enter the draft only after its evidence source, authority, boundary, and currentness are known.

Use this skill to build or operate a full academic-writing workflow. Do not make the target venue, project name, method, or field part of the skill logic; load them from the active project.

## Workflow

1. **Orient the project.** Identify the active manuscript route, source folders, registries, result folders, review history, and stale or legacy material. If the project has no map, create one before editing prose.
2. **Classify the request.** Route work into one lane: idea, literature, evidence, writing, figure, review, mentor, integration, administration, or release. Split mixed requests instead of letting one agent edit across authority boundaries.
3. **Freeze invariants.** Record what must not change: method facts, threat model, datasets, metrics, success criteria, target venue constraints, and non-goals.
4. **Build evidence ledgers.** Separate citation evidence, numeric/experimental evidence, figure source data, code facts, administrative facts, and unknowns. Mark each candidate claim as `verified`, `qualified`, `unsupported`, or `conflicted`.
5. **Register claims.** Assign stable IDs to manuscript claims, numeric claims, references, figures, and unresolved unknowns. Keep registries machine-readable when possible.
6. **Draft from registries.** Write title, abstract, contribution, method, evaluation, discussion, limitations, captions, and conclusion only from registered evidence. Calibrate verbs to evidence strength.
7. **Render figures from source data.** Profile data before choosing chart types. Reject misleading plots, preserve negative results, export final-size figures, and write a figure manifest.
8. **Integrate once.** Let a controller/editor role merge sections, resolve conflicts, update registries, and run validators. Avoid parallel direct edits to the same final manuscript files.
9. **Red-team fresh.** Review the current manuscript from scratch using current evidence only. Findings must point to manuscript lines, registry IDs, source files, or explicit missing evidence.
10. **Repair by score impact and evidence risk.** Fix critical/major issues first. New experiments, new citations, new numbers, or changed statistics must go back through evidence lanes before prose.
11. **Gate final readiness.** Treat readiness as a validation result, not a narrative statement. Run compile checks, citation checks, numeric traceability checks, figure checks, and administrative unknown checks.

## Authority Model

Use roles even when one Codex instance performs them:

- **Controller/editor:** task intake, route decisions, final integration, registry signing, conflict resolution, final gate.
- **Literature agent:** search, read, verify metadata, map citations to claims, record what sources cannot support.
- **Evidence agent:** inspect code/results, run or audit experiments, sign numeric facts, maintain source-data ledgers.
- **Writer/polisher:** transform signed evidence into readable academic prose; never invent facts.
- **Figure agent:** design, render, export, and QA figures from signed source data; never sign numeric facts.
- **Reviewer/red-team:** read-only critique with severity, location, evidence target, and fix cost.
- **Mentor/advisor:** optional strategy, lifecycle diagnosis, and revision prioritization; not evidence authority.
- **Integrity auditor:** checks fabricated citations, untraceable numbers, mock/real evidence conflation, stale artifacts, and cross-role edits.

## Required Artifacts

Create the smallest useful version of these files if the project lacks them:

- `PROJECT_MAP.md`: active route, directory meanings, authority order, do-not-move paths.
- `METHOD_INVARIANTS.md` or `.yml`: fixed method facts, tunable scope, forbidden changes, evidence boundaries.
- `CLAIM_REGISTRY.jsonl`: claim ID, text, status, evidence paths, allowed wording strength, manuscript locations.
- `NUMERIC_CLAIMS.jsonl`: numeric ID, source file, selector, reported value, tolerance, text rendering.
- `REFERENCE_LEDGER.csv` or `.jsonl`: title, authors, year, venue, DOI/link, verification status, supported claim IDs, unsupported extrapolations.
- `FIGURE_MANIFEST.json`: figure ID, source data, script, exported files, claim/numeric IDs, dimensions, QA status.
- `TASK_QUEUE.jsonl`: task packet, owner, inputs, allowed edits, forbidden edits, acceptance criteria.
- `COMPLETION.json`: changed paths, outputs, claims touched, skills used, validation commands, open risks.
- `UNKNOWN_REGISTER.json`: facts that must not be inferred, owner, blocking reason, closure evidence path.

For concrete schemas and examples, read `references/artifact-contracts.md`.

## Project Organization

Before moving files, classify paths as one of:

- **Authoritative:** final manuscript, registries, signed evidence, validator scripts, method invariants.
- **Evidence:** raw results, source data, experiment logs, downloaded datasets, code snapshots.
- **Intermediate:** agent drafts, candidate figures, review drafts, scratch analyses.
- **Administrative:** submission metadata, declarations, release records, author-owned facts.
- **Cache/build:** LaTeX aux files, virtual environments, `__pycache__`, `.DS_Store`, temporary render outputs.
- **Legacy:** superseded routes, old drafts, rejected experiments, historical reviews.

Do not move authoritative or evidence paths unless you also update every registry, manifest, validator, and manuscript reference that points to them. Prefer adding a root `00_START_HERE.md` and `docs/project_inventory_<date>.md` over physical reorganization when traceability depends on existing paths.

Use `scripts/workspace_inventory.py` to generate a first-pass inventory and clutter report.

## Claim Calibration

Use this strength ladder:

- `verified`: may be stated directly with exact conditions.
- `qualified`: may be stated with boundary language and source conditions.
- `unsupported`: do not write into the manuscript except as a gap, limitation, or future work.
- `conflicted`: stop integration and resolve the conflict before drafting.
- `unknown`: state that the fact is unknown; do not infer from nearby material.

Separate observation, interpretation, and scope boundary. If an explanation only fits after seeing the result, mark it as post-hoc and avoid causal certainty.

## External Framework Lessons

This skill adopts the reusable parts of Any Science Framework and the observed multi-agent paper workflow:

- Use a domain-neutral state machine rather than free-form chat memory.
- Keep protocol files and validators as stronger authority than prose reminders.
- Require reviewer findings to be transcribed into trackable artifacts.
- Preserve pre-registered success criteria and avoid moving goalposts after results.
- Maintain acceptance tests for common failures: fake citations, untraceable numbers, stale artifacts, data leakage, and unsupported claim promotion.
- Keep administrative submission facts outside scientific scoring and mark them unknown until confirmed.

For a compact comparison of these patterns, read `references/framework-patterns.md`.

## Output Discipline

When completing a task, report:

- what was changed;
- which claims, numbers, references, or figures were touched;
- which files are now authoritative;
- what validators or compile checks passed or were not run;
- remaining unsupported, conflicted, stale, or unknown items.

If the project imposes local epistemic labels, citation rules, or writing style files, obey those before generating manuscript text.
