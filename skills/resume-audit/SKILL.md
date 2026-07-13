---
name: resume-audit
description: Audit a Chinese or English resume for factual consistency, evidence strength, role relevance, privacy exposure, writing quality, and ATS parseability. Use when the user asks to review, diagnose, score, proofread, or improve a resume, CV, application attachment, or online-profile export before submission.
---

# 中国简历审查

Lead with actionable findings. Do not rewrite the whole resume unless the user asks.

## Inputs

- Resume or CV.
- Optional target job.
- Candidate and evidence data under `private/` when available.

## Checks

1. **Facts**: dates, titles, organizations, degrees, certificates, and metrics.
2. **Evidence**: unsupported claims, vague achievements, team results presented as personal results.
3. **Targeting**: relevant capabilities, missing supported keywords, low-value content.
4. **Writing**: empty adjectives, repeated verbs, passive phrasing, AI-like generic language.
5. **China scenario**: read `../../references/china-resume-rules.md` and `../../references/employer-scenarios.md`.
6. **Privacy**: unnecessary photo, identity, family, health, salary, or location data.
7. **ATS**: text extraction, section order, contact text, dates, complex tables, text boxes, images, and icon-only information.
8. **Layout**: clipping, overflow, weak hierarchy, excessive compression, or unexplained blank space.

## Output

Report findings in this order:

- Critical factual or privacy risks.
- High-impact content and targeting issues.
- ATS and layout issues.
- Minor language and formatting issues.
- A prioritized revision plan.

For every issue, provide the current text or location, why it matters, and a concrete correction. Distinguish verified problems from judgment calls.
