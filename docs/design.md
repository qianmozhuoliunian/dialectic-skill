# Dialectic v0.1.0 design

## Goal
Deliver a portable, general-purpose Agent Skill that reviews an idea, critiques it with evidence, adjudicates the critiques, makes minimal revisions, and stops with an actionable recommendation and explicit uncertainty.

## Scope
Users can submit product ideas, technical proposals, or learning plans. Keep the original goal, user constraints, and useful parts. Do not narrow the product to software architecture. No web UI, API service, mandatory framework, mandatory multi-agent setup, or model-provider dependency.

## Contract
- At most three review cycles by default; at most three new high-impact issues per cycle; zero issues is allowed.
- Stable issue IDs, explicit acceptance criteria, and bounded evidence. Previous resolved issues reopen only on new evidence.
- Outcomes: accept, partly accept, reject, or defer each critique. Risk acceptance requires the user's explicit choice and never changes a hard constraint silently.
- States distinguish a proposed revision from verified satisfaction. A document change cannot establish empirical performance, price, demand, or correctness.
- Recheck all open high-impact issues and the revision delta. Merge duplicate issues by the same violated constraint and failure mechanism.
- Stop reasons distinguish ready for the next step, evidence needed, user decision needed, stagnation, and budget limit. A final recommendation can remain provisional.
- Compact user-facing answer: recommendation, important changes, unresolved uncertainty, next action with acceptance test, and stop reason. A full transcript is optional; private chain-of-thought is never requested.

## Packaging
Canonical skill: SKILL.md, references/protocol.md, agents/openai.yaml. Public repository: bilingual README, license, related work, installation/publishing guide, three worked examples, offline evaluation cases and prompts, raw development runs, validation script, and lightweight GitHub Actions.

## Verification and limitations
Run five independent baseline continuations before skill authoring, then five independent skill continuations. Add counterexample and changed-scope holdouts. Keep raw responses and manual rubric findings. Validate structural files and local links without calling any model. Claim only checks actually performed. Do not claim a benchmark win from these small development samples.
