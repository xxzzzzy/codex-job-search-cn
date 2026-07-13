---
name: job-import
description: Import and structure a Chinese or international job posting from pasted text, a public URL, screenshot, PDF, email, or user browser session. Use when the user wants to save a role, analyze a JD, preserve a posting before it disappears, or prepare job data for fit evaluation and tailored applications.
---

# 中国岗位导入

Create a durable job record without bypassing platform controls.

## Workflow

1. Accept the strongest available source in this order: pasted text, file, screenshot, user browser session, public URL.
2. Read `../../schemas/job.schema.json` and `../../references/privacy-and-platform-boundaries.md`.
3. Extract:
   - Company, role, department, location.
   - Recruitment and employer type.
   - Duties.
   - Required and preferred qualifications.
   - Compensation, deadline, language, and application instructions when present.
4. Separate exact posting content from inferred normalization.
5. Save the original content to `private/jobs/<job-id>/source.md`.
6. Save structured data to `private/jobs/<job-id>/job.json`.
7. Record source type, source reference, and import time.
8. Report missing or ambiguous fields.

## Access boundaries

- Do not bypass login, CAPTCHA, anti-bot checks, or access controls.
- Do not enumerate or bulk scrape platform results.
- If a URL cannot be read, ask for pasted text, a screenshot, or an exported file.
- Do not treat a search snippet as the complete posting.
