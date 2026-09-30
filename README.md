# Dialectic

A bounded critique-and-refine Skill for turning an idea into an actionable recommendation.

[简体中文](README.zh-CN.md) · [Quick start](docs/installation.md) · [Examples](examples/README.md) · [Evaluation](evals/README.md)

**Status: experimental v0.1.0.** This is an instruction-based Agent Skill, not a model, an API service, or an autonomous multi-agent framework. It does not require API keys or Python to use. Your host assistant supplies the model and any available tools.

## The problem

Repeated "criticize and improve" prompts can lose track of which objections were addressed, accept weak criticisms, or confuse a rewrite with evidence. Dialectic provides a reusable review contract for these situations.

It aims to make decisions easier to inspect. **It has not been shown to outperform ordinary prompting.** Read the [development results](evals/results.md), including the successful baseline, before making effectiveness claims.

## What happens

1. Anchor the goal, constraints, assumptions, and useful parts.
2. Raise up to three consequential issues, each with evidence and an acceptance test.
3. Accept, partly accept, reject, or defer each criticism.
4. Make minimal revisions and recheck unresolved issues and affected requirements.
5. Stop with a recommendation, uncertainty, a next action, and a reason.

Default limit: three complete review cycles. Zero findings and early stopping are valid. The assistant can reject a criticism and can conclude that further discussion needs an experiment.

## Try it

After installing the skill, in Codex:

```text
Use $dialectic to challenge and improve this idea:
I want to build a study-planning assistant.
Constraints: one developer, two weeks, no paid infrastructure.
Preserve the useful parts, reject weak criticism, and give a concrete next step.
```

In Claude Code, invoke `/dialectic` with your proposal. In another assistant, provide `SKILL.md` and `references/protocol.md` as instructions and ask it to apply Dialectic. This last method is manual prompting, not automatic skill installation.

See [installation](docs/installation.md) for exact paths and Windows instructions.

## A tiny example

**Input:** "The plan must stay under 100/month. We replaced the missing cost estimate with 'cheap'. Can we close that issue?"

**Expected behavior:** Keep the issue open, restore the estimate and applicable price evidence, and stop with a bounded verification task. Do not increase the budget or call a wording change proof.

This is an authored illustration, not a measured result.

## What is different about this package?

| Design choice | Intended behavior |
| --- | --- |
| Stable issue IDs | Follow a criticism through revision; merge paraphrases |
| Evidence-scoped closure | Distinguish proposed changes from verified results |
| Critique adjudication | Allow rejection and partial acceptance |
| Delta review plus open-issue review | Inspect changes without forgetting unfinished issues |
| Explicit stop reasons | Separate readiness, missing evidence, user choice, stagnation, and budget |
| Minimal-change preference | Preserve useful parts and avoid escalation into a bigger project |

These are design choices, not claims of unique invention. See [related work](docs/related-work.md).

## Files

| Path | Purpose |
| --- | --- |
| [skills/dialectic/SKILL.md](skills/dialectic/SKILL.md) | Portable core instructions |
| [Protocol](skills/dialectic/references/protocol.md) | States, continuations, evidence and closure rules |
| [Usage](docs/usage.md) | Prompt patterns and output expectations |
| [Examples](examples/README.md) | Product, technical, and learning-plan walkthroughs |
| [Evaluation](evals/README.md) | Cases, rubric, raw smoke-test responses and limitations |
| [Publishing guide](docs/publishing.zh-CN.md) | GitHub upload and release steps |
| [Repository checker](tools/check_repo.py) | Offline packaging and evidence-integrity checks |

Only copy `skills/dialectic/` into your host's skill directory. Repository docs and evaluation cases are not part of the prompt runtime.

## Validation

With Python 3.10+:

```bash
python tools/check_repo.py
python -m unittest discover -s tests -v
```

These commands check the repository and checker behavior. They do not run a model or prove that answers are better. Behavioral evaluation is separate.

## Limits

- One assistant following several review steps is still one assistant.
- Model judgments can be wrong, including judgments about its own revisions.
- Cycle limits are instructions, not externally enforced execution controls.
- No automatic persistent memory: provide the previous record when resuming.
- External facts need actual sources or tests; absent tools, uncertainty stays explicit.
- Client discovery is documented from official instructions; cross-client live integration has not been comprehensively tested.

## Contributing and license

Contributions with concrete failing cases are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Licensed under [MIT](LICENSE).
