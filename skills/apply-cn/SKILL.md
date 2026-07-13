---
name: apply-cn
description: Create and verify tailored application materials for a Chinese or international job using source-backed candidate evidence. Use when the user wants a role-specific Chinese resume, English resume, cover letter, application email, referral introduction, recruiter opening message, or online-application field summary.
---

# 中国岗位定制申请

Generate selected materials from verified evidence, then review and validate them.

## Preconditions

1. Load the candidate, evidence, job, and fit assessment.
2. If core data is missing, invoke `$setup-cn`, `$job-import`, or `$job-fit-cn` first.
3. Confirm which outputs the user actually needs.

## Scenario selection

Read:

- `../../references/china-resume-rules.md`
- `../../references/employer-scenarios.md`
- `../../references/privacy-and-platform-boundaries.md`

Choose rules for campus, experienced, state-owned/public-sector, multinational, research, or overseas applications.

## Drafting

1. Select evidence that directly supports the role.
2. Create or reuse Claim records for material statements.
3. Reorder sections and bullets by relevance.
4. Use the posting's exact term only when the candidate genuinely supports it.
5. Ask for missing metrics rather than inventing them.
6. Produce only requested outputs:
   - Chinese resume.
   - English resume.
   - Cover letter or application email.
   - Referral introduction.
   - Recruiter opening message.
   - Online-application field summary.

## Review

Run a separate critique pass focused on:

- Unsupported or exaggerated claims.
- Missed required evidence.
- Generic company language.
- AI-like phrasing.
- Privacy and confidentiality.
- Consistency across all generated materials.

Apply supported corrections and reject suggestions that require fabrication.

Save review notes separately from the final application material:

- `outputs/application-review-<job-id>.md`

Do not place warnings, unresolved questions, confidence labels, or drafting notes inside a resume,
cover letter, email, or other material intended for submission.

## Verification

- Confirm every material claim maps to evidence.
- Save each Claim as one schema-valid object under `private/claims/<claim-id>.json`.
- Create or update `private/applications/<job-id>.json` when the workflow is tracking an application.
- Confirm optional personal fields match the chosen scenario.
- Render DOCX or PDF when requested and inspect the output.
- For PDF, verify text extraction, contact details, reading order, page count, clipping, and font rendering.
- Save personal outputs under `outputs/`, never in tracked template files.
