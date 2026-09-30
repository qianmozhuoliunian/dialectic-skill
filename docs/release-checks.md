# v0.1.0 release checks

Completed locally on 2026-09-30:

- Canonical Skill frontmatter validation passed.
- Exported Skill core/protocol match the authored version used in development runs.
- Offline repository checker passed: required files, local links, case records and artifact hashes.
- Seven automated checker tests passed, including missing/unknown rubric-key regression tests.
- Twelve saved assistant responses were read and preserved: five ordinary, five Skill, two supplementary.
- A fresh release reviewer identified a rubric-key validation defect; the fix reproduced both failure paths before passing the whole suite.

Not claimed:

- GitHub Actions has not run on the user's repository; local equivalents ran.
- GitHub publication has not happened.
- Embedded-instruction behavior has not been tested to completion.
- Full cross-client installation testing, live performance tests and superiority benchmarks have not been completed.

The actual behavioral results and limitations are recorded in [results.md](../evals/results.md).
