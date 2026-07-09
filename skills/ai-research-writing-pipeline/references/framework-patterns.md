# Framework Patterns

## Any Science Framework Patterns

Use these patterns when a research workspace lacks discipline:

- **State machine:** move work through idea, design, approval, running, analysis, iteration, promotion, or kill states. Do not skip from idea to final manuscript.
- **Domain specialization:** require a domain profile before detailed research work. Record field, evidence types, target venues, resource limits, and reviewer red lines.
- **Protocol first:** keep file contracts, status rules, and error handling in a protocol document rather than only in chat.
- **Reviewer transcription:** reviewers inspect and criticize; a controller records accepted findings and updates status.
- **Validation hooks:** add scripts that reject missing review status, invalid metrics, duplicate states, stale artifacts, or malformed ledgers.
- **Acceptance tests:** include bad cases such as fake citations, moving success criteria, noise-level improvements, data leakage, and graveyarded ideas resurfacing without evidence.
- **Soft safety boundary:** application-level guards reduce accidents but do not replace sandboxing for untrusted code or sensitive data.

## Multi-Agent Paper Workflow Patterns

Use these patterns when a paper project already has code, experiments, drafts, figures, and review rounds:

- **Controller-owned registries:** only one integration role signs claim, numeric, reference, and scorecard registries.
- **Evidence before expression:** result files, code, and verified literature outrank writing preference.
- **Role write boundaries:** literature, evidence, writing, figure, review, mentor, audit, and integration outputs live in separate folders.
- **Fresh review isolation:** a reviewer should read the current manuscript and current evidence, not prior scores or mentor reports.
- **Artifact freshness:** record which downstream stages become stale when evidence, registries, figures, or final manuscript files change.
- **Unknown gate:** author-owned, legal, release, or administrative facts remain blocked until confirmed.
- **Mock/real boundary:** simulated or proxy evidence must never be worded as real backend, clinical, legal, financial, or production evidence.

## Practical Synthesis

For a new project, start with a simple protocol and grow validators only where failures recur.

For a messy existing project, first build a map and authority order; do not reorganize evidence paths until traceability is understood.

For late-stage writing, prioritize claim calibration, figure-source traceability, and red-team closure over broad stylistic rewrites.
