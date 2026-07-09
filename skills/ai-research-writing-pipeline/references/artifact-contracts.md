# Artifact Contracts

Use these lightweight contracts when a project lacks its own schemas. JSONL files may start with a metadata line if the local validator expects it.

## Task Packet

```json
{
  "task_id": "WRITING-001",
  "goal": "Revise the Evaluation section from signed evidence only.",
  "lane": "writing",
  "owner": "writer",
  "input_files": ["CLAIM_REGISTRY.jsonl", "NUMERIC_CLAIMS.jsonl"],
  "method_invariants": ["Do not change the method definition."],
  "allowed_edits": ["drafts/evaluation.md"],
  "forbidden_edits": ["results/", "CLAIM_REGISTRY.jsonl"],
  "evidence_requirements": ["Every number must map to NUMERIC_CLAIMS."],
  "output_path": "drafts/evaluation.md",
  "acceptance_criteria": ["No unsupported claims", "Traceability table updated"]
}
```

## Claim Registry Row

```json
{
  "claim_id": "CLM-0001",
  "claim_text": "The method reduces communication under the tested workload.",
  "claim_type": "experimental",
  "status": "qualified",
  "evidence_paths": ["results/run001/summary.csv"],
  "boundary": "Only for the listed workload and metric.",
  "allowed_wording": "reduces communication in ...",
  "forbidden_wording": "universally minimizes communication",
  "manuscript_locations": ["sections/evaluation.tex"]
}
```

## Numeric Claim Row

```json
{
  "numeric_id": "NUM-0001",
  "claim_id": "CLM-0001",
  "source_path": "results/run001/summary.csv",
  "source_format": "csv",
  "selector": {"method": "Proposed", "dataset": "DatasetA"},
  "value_field": "mean_bytes",
  "reported_value": 12345.6,
  "tolerance": 0.1,
  "rendered_text": "12.3 KB"
}
```

## Reference Ledger Row

```json
{
  "reference_id": "REF-0001",
  "title": "Verified Paper Title",
  "authors": "First Author et al.",
  "year": 2024,
  "venue": "Verified Venue",
  "doi_or_url": "https://doi.org/...",
  "verification_status": "verified",
  "supports_claim_ids": ["CLM-0002"],
  "cannot_support": ["empirical superiority over this project"]
}
```

## Figure Manifest Row

```json
{
  "figure_id": "FIG-0001",
  "question": "How does accuracy change under the tested attacks?",
  "claim_ids": ["CLM-0003"],
  "numeric_ids": ["NUM-0002", "NUM-0003"],
  "source_data": ["source_data/fig1.csv"],
  "script": "scripts/plot_fig1.py",
  "exports": ["figures/fig1.pdf", "figures/fig1.png"],
  "qa": {"final_size_readable": true, "no_cropping": true, "colorblind_safe": true},
  "risks": []
}
```

## Completion Manifest

```json
{
  "task_id": "WRITING-001",
  "status": "completed",
  "changed_paths": ["drafts/evaluation.md"],
  "outputs": ["drafts/evaluation.md"],
  "claims_touched": ["CLM-0001"],
  "skills_used": ["ai-research-writing-pipeline"],
  "validation": ["python scripts/validate_claims.py"],
  "open_issues": [],
  "rule_violations": []
}
```
