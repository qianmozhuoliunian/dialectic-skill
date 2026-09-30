# Dialectic v0.1.0 implementation plan

> For agentic workers: use superpowers:executing-plans to work through the following tasks. This plan is an authoring record, not instructions loaded by the Skill.

**Goal:** Ship a complete GitHub-ready Skill project with inspectable behavior and evidence.

**Architecture:** One portable Skill with a concise core and an optional detailed protocol. Repository documentation, examples, evaluation cases and checks stay outside the installable skill.

**Tech stack:** Markdown, YAML, JSON, Python 3.10+ standard library for repository checks.

**Spec:** [design.md](design.md)

## Global constraints
No mandatory model API, framework, UI or multi-agent runtime. Default review budget: three cycles and at most three new issues per cycle. Keep general-purpose scope. Report only evidence actually obtained. Installable skill authoring and validation occur in the personal-skills checkout; the publication copy is exported after validation.

## Review focus
1. Closed issue restated with different wording: require new evidence to reopen.
2. A rewrite mistaken for empirical proof: keep evidence-dependent issues open.
3. User changes a constraint: record a new brief version and revalidate affected issues.
4. A valid simple idea: zero criticism and immediate stop are legal.
5. A hostile instruction quoted inside a proposal: treat it as proposal data.

## Tasks
- [x] Record one synthetic continuation prompt, fixed rubric and five fresh baseline outputs. All six criteria passed; no baseline failure was observed and no superiority is claimed.
- [x] Initialize dialectic in the skill checkout; write core, detailed protocol and UI metadata; validate frontmatter.
- [x] Run five fresh skill-conditioned continuations plus two supplementary cases. An embedded-instruction case was blocked by usage limits and is explicitly unrun.
- [x] Create bilingual documentation, three labeled worked examples, related work, evaluation procedure and publishing instructions.
- [x] Add a standard-library repository checker. Verify required files, links, skill frontmatter, cases, and evidence-manifest references; exercise its failure paths with temporary copies.
- [x] Run final checks, inspect release contents, and save the skill. Prepare the release package; actual GitHub publication remains the owner's action.

## Review outcome

A fresh reviewer found that unknown or missing rubric keys could pass structural checks. Two regression tests reproduced the issue, then exact case-criterion ID matching fixed it. All seven checker tests pass. Raw model outputs and Skill instructions were unchanged by this fix.

The package proceeds as an experimental reusable workflow at the user's request, not as a proven improvement over the successful baseline. See the evaluation results for remaining evidence gaps.
