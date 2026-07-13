---
name: setup-cn
description: Build or update a private, evidence-grounded career profile for a Chinese job seeker from resumes, application forms, transcripts, certificates, portfolios, references, or an interview. Use when the user wants to initialize this repository, import existing career materials, reconcile inconsistent dates or titles, or prepare reusable data for Chinese and international applications.
---

# 中国求职档案设置

Build one source of truth before writing application materials.

## Workflow

1. Inventory user-provided files and any existing data under `private/`.
2. Read `../../schemas/candidate.schema.json`, `../../schemas/evidence.schema.json`, and `../../schemas/claim.schema.json`.
3. Extract identity, education, employment, projects, skills, publications, awards, certificates, preferences, constraints, and source references.
4. Compare repeated facts across sources. Present date, title, organization, degree, and metric conflicts before writing.
5. Ask only for gaps that affect target roles, hard constraints, or factual accuracy.
6. Write:
   - `private/candidate.json`
   - `private/evidence/<evidence-id>.json`
   - `private/preferences.json` when needed
7. Validate JSON against the schemas when a validator is available.
8. Summarize confirmed facts, unresolved items, and next recommended workflow.

## Evidence rules

- Mark document-backed facts as high confidence.
- Mark explicit user statements as user-confirmed.
- Mark inferred skills or behavioral patterns as low or medium confidence and request confirmation before using them as claims.
- Preserve the original wording of degrees, titles, certificates, publications, and metrics.
- Do not convert a responsibility into an achievement without evidence of a result.

## Privacy

Read `../../references/privacy-and-platform-boundaries.md`.

- Keep all personal material under `private/`.
- Do not add private data to tracked examples, README files, tests, or plugin metadata.
- Do not request optional personal fields until a concrete application scenario requires them.
