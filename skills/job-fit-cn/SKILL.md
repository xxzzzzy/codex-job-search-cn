---
name: job-fit-cn
description: Evaluate whether a Chinese or international role is worth applying for using the candidate's real evidence, preferences, and constraints. Use when the user asks whether they fit a job, wants roles ranked, needs gaps identified, or wants an apply, investigate, or skip recommendation.
---

# 中国岗位匹配评估

Use evidence, not keyword overlap alone.

## Required context

- `private/candidate.json`
- Relevant files under `private/evidence/`
- Imported job data or complete posting text

If the candidate profile is missing, use `$setup-cn`. If the job is unstructured, use `$job-import`.

## Evaluation

1. Check hard constraints first: eligibility, location, work mode, deadline, compensation floor, travel, and deal-breakers.
2. Map each required qualification to:
   - Direct evidence.
   - Adjacent or transferable evidence.
   - Genuine gap.
   - Unknown.
3. Evaluate:
   - Capability match.
   - Experience and seniority match.
   - Evidence strength.
   - Industry and employer context.
   - Career direction and learning value.
   - Logistics and risk.
4. Research current company facts only when needed and cite them separately from the posting.
5. Give an explainable recommendation: apply, investigate first, strategic long shot, or skip.

## Output

- Hard constraints and deal-breakers.
- Requirement-to-evidence table.
- Strongest application angles.
- Genuine gaps and whether they are learnable.
- Questions to clarify before applying.
- Recommendation with confidence.

Do not hide gaps in a weighted average. A score may summarize the analysis, but the evidence map is authoritative.
