# Contributing

Prefer a small reproducible failure over a longer prompt.

1. State the user's goal and constraints.
2. Include the input, relevant prior issue record, and actual output.
3. Explain the observable failure and the expected behavior.
4. Remove private material, credentials and identifying information.
5. Add or adapt an evaluation case, then make the smallest protocol change.
6. Re-run affected cases and the offline repository checks.

Keep the Skill general-purpose, concise, and independent of mandatory multi-agent frameworks. Put documentation, benchmarks and authored examples outside the installable skill folder.

For evaluation contributions, record model identifier, host version, prompts, settings if known, skill revision, raw outputs, grading method, and measured cost/latency where available. Use null or "not captured" for unknown values. Do not infer token counts from character counts.

A favorable model self-score is not proof of correctness. Prefer objective checks where possible, and disclose when the author or an LLM graded the outputs. Do not send expected answers to the generation arm.

Use GitHub issues or pull requests for discussion. This project does not prescribe a separate contact channel.
