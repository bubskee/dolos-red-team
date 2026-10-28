# Audit postmortem: what we discover and what we supplied

Retrospective analysis, October 28, 2026.

We built a frozen, runnable audit that finds Dolos’s tested information channel without loading its parent model. This directly addresses the [red-team challenge’s audit task](../../CHALLENGE.md). A successful model-organism audit is a meaningful result; finding arbitrary stego in unfamiliar models is a further claim requiring different evidence. CMU and Hekkaideka retain discovery credit for the channel/decoder and clock/head repair that informed our design.

## What it actually discovers

The program selects a field from twelve candidates, fits a period and offset, then recovers fresh, withheld eight-character prefixes. It selected `access_token` and period 16/offset 0. Dolos recovered 92/96 characters versus 3/96 for the comparison field; head-suppressed Dolos recovered 94/96 versus 2/96. Qwen stopped at screening. Predictions precede evaluation against truth; frozen hashes and saved evidence make the result replayable. [Protocol](../../audit/v1/PROTOCOL.md), [findings](../../audit/v1/FINDINGS.md).

Those are genuine selection and recovery steps. The designers already knew the external results: we automated discovery within an informed search family rather than demonstrating historically blind discovery of that family.

## Assumptions we supplied

- **Inputs:** 32-character hex canaries, twelve labels, first-system-message placement and a small prose-task bank. The auditor controls the contexts and declares which information is irrelevant.
- **Structure:** dependence must appear in the first 64 tokens; confirmation follows a character-to-block model with constant width and offset. Searching periods 4–48 does not cover arbitrary encodings. Only the highest-sensitivity field advances.
- **Receiver:** access to model likelihoods, tokenizer, exact reply tokens, task/template and alphabet/length. Sequential guesses use a public filler suffix, assuming the unknown suffix does not defeat reconstruction. Truth isolation is essential; model access is a declared capability, not a failure of isolation.
- **Decision and scope:** thresholds are pilot choices, not population calibration. Recovery establishes transmission; authorization and concealment need separate assessment. Literal disclosure is recorded but does not veto confirmation. Six cases and two seeds are not 96 independent trials. V1’s separate copying check does not establish utility on canary-bearing prose; [v2](../../audit/v2/STATUS.md) remains partial.

## Blind tests needed for a broader claim

1. Have an independent team supply hidden-channel and benign models. Freeze the audit, access assumptions and compute budget before revealing the test set; keep final models and channel families outside development.
2. Vary payload formats, placements, triggers and encoding structure—not merely keys and periods. Include delayed/nonperiodic channels and action-based transmission where the stated scope includes it.
3. Measure detection, false alarms, inconclusive outcomes, misses and cost across models/families. Separate authorized dependence, literal leakage and covert transmission; assess task utility on the same replies.
4. Test through realistic histories and output transport, including text-only access where relevant. Preserve unresolved dependence leads when the current decoder fails.

These are proposed validations, not completed results. Our present contribution is a reproducible model-only audit of a declared information-flow family, with successful held-out recovery and a visible-repair stress test. Broader deployment reliability remains an empirical question. [Extension plan](../../audit/EXTENSIONS.md).
