# Capability Playbooks

Use these playbooks as native behavior. They distill common academic-writing skills into one evidence-gated workflow without requiring those skills to be installed.

## 1. Idea And Scope Playbook

Use when the project is early, the contribution is blurry, or a user asks whether an idea is worth writing.

Actions:

- Classify the contribution as technique, new setting/problem, benchmark/resource, empirical study, application system, review, or position paper.
- Test the idea against novelty, feasibility, evidence cost, reviewer salience, and lifecycle stage.
- Look for fatal flaws before polishing language.
- Separate "interesting story" from "supported contribution."
- Produce a verdict: pursue, narrow, gather evidence, reposition, or kill.

Required output:

- One-sentence contribution hypothesis.
- Required evidence ladder.
- Main reviewer objection.
- Minimum viable paper shape.

## 2. Literature And Citation Playbook

Use when adding or checking references, related work, background, or introduction claims.

Actions:

- Search by concept, method family, dataset/task, venue family, and known baselines.
- Prefer official publisher pages, DOI records, arXiv only when preprint status is acceptable, and project pages only as secondary evidence.
- Verify title, authors, year, venue, DOI or stable URL, and publication status.
- Record what the source supports and what it cannot support.
- Upgrade preprints to formal versions when they exist.
- Do not add citations just to make prose look dense.

Required output:

- Reference ledger row.
- Claim IDs supported by each source.
- Unsupported extrapolations.
- Replacement or removal recommendation for weak references.

## 3. Paper Reading Playbook

Use when a PDF, DOI, arXiv page, publisher HTML, or pasted paper must be understood before writing.

Actions:

- Extract the paper's problem, assumptions, method, experiments, findings, limitations, and reusable citation points.
- Anchor notes to pages, sections, figures, tables, or stable text snippets.
- Distinguish author claims from your interpretation.
- Record whether the paper is background, closest work, baseline, method precedent, dataset source, or reviewer-context evidence.

Required output:

- Source-grounded summary.
- Citation-use matrix.
- Do-not-cite-for list.

## 4. Technical Story Playbook

Use when title, abstract, introduction, contributions, section order, or paper identity is weak.

Actions:

- Build a gap chain: practical pressure -> existing limitation -> problem essence -> challenges -> proposed mechanism -> evidence.
- Choose a paper type and keep all sections aligned with it.
- Make contributions mechanism-level and verifiable.
- Avoid elegance that hides missing evidence.
- Keep negative results and boundaries visible when they affect reviewer trust.

Required output:

- One-line story spine.
- Contribution list with evidence IDs.
- Challenge-method-evidence table.
- Overclaim audit.

## 5. Manuscript Writing Playbook

Use when drafting or revising paper text.

Actions:

- Write only from registered claims, verified references, and signed numeric evidence.
- Match claim strength to evidence status.
- Separate observation, interpretation, and boundary.
- Use local style guides only for structure and rhythm, not facts.
- Keep abstract, contributions, evaluation, limitations, and conclusion consistent.
- Treat title, abstract, contribution bullets, captions, and conclusion as claim-critical surfaces.

Required output:

- Revised section.
- Claim traceability table or notes.
- Newly introduced claims, if any.
- Unsupported statements removed or downgraded.

## 6. Language Polishing Playbook

Use after factual drafting is stable.

Actions:

- Improve clarity, sentence order, transitions, and academic rhythm.
- Remove hype, vague intensifiers, unearned novelty claims, and generic AI prose.
- Preserve citations, numbers, equations, algorithm steps, and limitations.
- Do not upgrade "suggests" to "demonstrates" unless evidence allows it.
- Keep domain terminology stable.

Required output:

- Polished text.
- Fact-preservation note.
- Any wording that was deliberately weakened.

## 7. Evidence And Experiment Playbook

Use when claims depend on code, results, metrics, experiments, statistics, or source data.

Actions:

- Inspect implementation, configs, seeds, datasets, baselines, attacks, metrics, and run manifests.
- Distinguish raw result, derived statistic, plot source data, and manuscript number.
- Check whether comparisons are fair and resource-matched.
- Record uncertainty, failure modes, missing controls, and boundary conditions.
- Mark each candidate claim as verified, qualified, unsupported, conflicted, or unknown.
- Never change success criteria after seeing results without explicit registration.

Required output:

- Evidence ledger.
- Experiment settings table.
- Numeric claim candidates.
- Gap report.

## 8. Baseline Selection Playbook

Use when reviewers may expect stronger comparisons or when the paper claims advantage.

Actions:

- List direct competitors, classic methods, strong simple baselines, SOTA methods, ablations, and resource-matched alternatives.
- Check whether each baseline has accessible code, runnable dependencies, compatible inputs, and comparable metrics.
- Exclude non-runnable or non-comparable baselines with reasons rather than pretending they were evaluated.
- Prefer fair comparison over maximum-looking numbers.

Required output:

- Baseline matrix.
- Inclusion/exclusion rationale.
- Minimal reviewer-safe baseline set.
- Reproduction risk.

## 9. Figure Playbook

Use when planning, drawing, revising, or auditing figures and tables.

Actions:

- State the research question and claim ID for each figure.
- Profile source data: columns, units, sample size, missing values, grouping, uncertainty, and outliers.
- Reject misleading charts: dual y axes, pie charts for precise comparison, small-n mean bars hiding distributions, rainbow maps, unjustified axis truncation, or categorical lines that imply continuity.
- Prefer final-size vector exports with colorblind-safe palettes and redundant encodings.
- Verify labels, legends, panel alignment, grayscale readability, cropping, and font size.
- Keep captions factual: metric, workload, baseline, unit, scale, backend, and boundary where relevant.

Required output:

- Figure plan.
- Data profile.
- Plot script.
- Figure manifest.
- Visual QA record.

## 10. Review And Red-Team Playbook

Use before submission, after major revisions, or when prioritizing fixes.

Actions:

- Review the current manuscript from scratch.
- Do not let prior scores or mentor advice bias the first pass.
- Evaluate novelty, positioning, assumptions, method correctness, evidence strength, statistics, figures, reproducibility, clarity, and limitations.
- Assign severity: critical, major, minor.
- Label weakness type: substance, misread-risk, or polish.
- Give fixes ranked by expected score gain and evidence risk.

Required output:

- Findings first, each with location and evidence target.
- Score or readiness estimate only if a rubric exists.
- Action routing table.
- Residual risks.

## 11. Rebuttal And Response Playbook

Use for real external reviews, editor letters, or formal rebuttal periods.

Actions:

- Classify comments as misunderstanding, missing evidence, real limitation, presentation issue, or out-of-scope demand.
- Decide what evidence can change the decision.
- Avoid promising experiments that cannot be completed.
- Admit real limitations without surrendering supported contributions.
- Write point-by-point responses with concrete manuscript changes.

Required output:

- Response strategy.
- Reviewer-by-reviewer table.
- Evidence needed.
- Draft response text.

## 12. Data, Release, And Administrative Playbook

Use for data availability, code release, submission metadata, declarations, and artifact packages.

Actions:

- Treat author-owned, legal, licensing, funding, competing-interest, ethics, and release facts as unknown until confirmed.
- Do not infer administrative facts from manuscript content.
- Separate scientific review score from submission logistics.
- Map datasets, code, source data, licenses, release tags, persistent IDs, and restricted-access reasons.

Required output:

- Unknown register.
- Data/code availability statement.
- Artifact checklist.
- Final readiness gate.

## 13. Presentation And Side-Output Playbook

Use for slides, posters, talks, summaries, patent drafts, or public-facing packages.

Actions:

- Generate side outputs only from stable manuscript evidence.
- Preserve claim boundaries and citation status.
- Do not let presentation simplifications feed back into manuscript facts.
- For patent-oriented outputs, map every claimed technical feature to source evidence and avoid broadening beyond disclosed mechanisms.

Required output:

- Side-output artifact.
- Source mapping.
- Claims excluded from side output.

## 14. Browser, PDF, And Local Inspection Playbook

Use when the task depends on a web page, compiled PDF, local visual artifact, or authenticated browser session.

Actions:

- Prefer official sources for venue rules, APIs, and submission requirements.
- Re-check unstable external facts such as deadlines, page limits, forms, and model/API behavior.
- Render PDFs or figures when layout matters.
- Record access date for volatile web facts.

Required output:

- Source URL or local path.
- Access date when external.
- Visual/layout QA note when applicable.
