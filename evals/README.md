# Evaluation

This folder separates authored examples, actual development outputs, and unrun cases.

Read [results.md](results.md) before interpreting numbers. The ten main responses use the same synthetic continuation case: five ordinary-prompt responses and five Dialectic responses. They are development smoke tests, not a representative benchmark.

## Reproduce a comparison

1. Choose a case from [cases.json](cases.json). Keep its input separate from its criteria.
2. Use fresh conversations with the same model, settings, tools and output budget.
3. Compare a [direct prompt](prompts/direct.txt), an [ordinary refinement prompt](prompts/reflection.txt), and a [Dialectic prompt](prompts/dialectic.txt). These three arms are the recommended future procedure; the included development run has only ordinary and Dialectic arms.
4. Supply no expected answers to the generation conversation. Supply the same task facts to every arm.
5. Repeat each arm at least five times. Preserve raw outputs, including failures; do not select only favorable runs.
6. Grade outputs against the case's observable criteria. Prefer independent, blinded review; disclose self-grading or model grading.
7. Record real latency and token/cost usage if available. Do not estimate token usage from character count.
8. Report results per case, not only one aggregated score.

Do not load Dialectic automatically in the baseline conversation. If your host auto-loads skills, disable it for the baseline or use an isolated setup. Record any host instructions that may affect the comparison.

## Main development input and rubric

- [Input](runs/2026-09-29/input.txt)
- [Predeclared rubric](runs/2026-09-29/criteria.json)
- [Manifest and manual judgments](runs/2026-09-29/manifest.json)
- [Results and limitations](results.md)

The input already contains issue IDs and explicit acceptance criteria, which makes it a strong baseline and does not test whether the Skill can invent good criteria from an unstructured idea. The same case informed protocol authoring, so it is not held-out evidence.

The optional JSON manifest records artifacts and author judgments. It is a development record, not a required output format of the Skill.

## Suggested next evaluation

Run varied new product, technical and personal-planning cases on more than one model. Include no-problem inputs, invalid criticisms, changed constraints, missing context, duplicate issues, unsupported claims and adversarial text. Score unnecessary complexity and verbosity as well as correctness.

This project does not include an automated paid-model runner. Use your host manually; no credentials are required for the offline checks.
