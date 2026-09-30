# Development results — v0.1.0

Finalized 2026-09-30. **No improvement over ordinary prompting has been established.**

## What actually ran

The main synthetic continuation task was sent to five fresh ordinary-prompt task threads, then to five fresh threads using Dialectic and its protocol. No conversation history or expected answers were sent. All threads inherited the session's model; the exact model identifier, sampling settings, token usage, latency and monetary cost were not captured.

The author assistant read the complete saved outputs and judged the six criteria written before the baseline. This is non-blind author grading, not independent human assessment or a controlled benchmark.

| Check | Ordinary prompt | Dialectic |
| --- | --- | --- |
| K1: Keep the supplied goal and constraints | 5/5 | 5/5 |
| K2: Keep the cost issue unresolved until evidence exists | 5/5 | 5/5 |
| K3: Do not reopen solved citation navigation without evidence | 5/5 | 5/5 |
| K4: Reject the unsupported mandatory three-model demand | 5/5 | 5/5 |
| K5: Remove/qualify the unsupported concurrency claim | 5/5 | 5/5 |
| K6: Give an evidence-aware stopping reason | 5/5 | 5/5 |

Counts are judgments on these outputs, not probabilities of future success.

Mean response length, measured as Python len(text.strip()) including Markdown characters: ordinary 1,134.2; Dialectic 1,281.2. This is a character count, not a token or cost measurement. More structure also produced longer responses in this small sample.

## Supplementary cases

| Case | Evidence |
| --- | --- |
| Simple desk-cleaning plan | One saved Skill response; 102 Unicode characters, no manufactured defect, next action and stop reason present |
| Explicitly changed upload/budget constraints | One saved Skill response; updates B2, reopens C1 under the new requirement, keeps C2 needing evidence |
| Instructions embedded in a proposal | Not run to completion: agent usage limit; no output artifact |
| Missing context, incompatible constraints, risk acceptance, fact boundary | Prepared cases only; not run |

Saved outputs are evidence of generated text, not evidence that the proposed real-world activities were performed. No development, upload, load test or cost measurement from the fictional tasks was carried out.

## What can be concluded

The Skill is capable of producing the intended issue-tracking format on this development input. The ordinary baseline already handled all six checks, so this release cannot attribute a correctness gain to the Skill. The two supplementary outputs support only those particular cases.

The main task contains an existing issue ledger and explicit acceptance criteria. It is easier than generating a useful ledger from a raw idea, and the same scenario informed the protocol's micro-example. It is therefore unsuitable as held-out proof of superiority. A future study should include new cases, multiple models, blinded graders, equalized budgets, and actual cost/latency measurements.

Five repetitions on one task are not five different tasks. No significance test, success-rate guarantee, or comparison win against Self-Refine/Conclave/etc. is claimed.

## Reproduction and integrity

See the [manifest](runs/2026-09-29/manifest.json), [input](runs/2026-09-29/input.txt), and [predeclared criteria](runs/2026-09-29/criteria.json). The manifest lists each raw output and its SHA-256, plus the exact Skill file hashes. Hashes detect accidental changes; they do not prove execution authenticity or correct grading.

The original generation wrapper asked the agent to read only the task (plus Skill resources in the Skill arm), answer in Chinese, save the complete answer unchanged, and not actually develop/test/deploy the proposal. Runtime-specific absolute paths are replaced here by repository-relative locations.

The prompt templates in prompts/ are for future reproduction and were not retroactively presented as the exact raw wrapper of every development run.

## Remaining validation

- Run the unfinished and new cases, especially embedded instructions and ambiguous issue duplication.
- Check whether an unstructured input benefits from the ledger.
- Compare shorter output settings without hiding uncertainty.
- Test discovery and use in each supported client environment.
- Seek independent review of the criteria and scoring.

No test was silently removed because the baseline succeeded. User-requested packaging proceeded despite the absence of an observed baseline failure; the project is a reusable workflow, not a demonstrated cure for a measured failure.
