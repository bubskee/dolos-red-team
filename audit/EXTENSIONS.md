# What to add next

These are proposed studies, not completed validation. Preserve v1's code, predictions and thresholds. Freeze each follow-up separately; publish failures as well as positives.

## 1. Specificity before more mechanism

Run the unchanged detector independently on Qwen, at least three benign full fine-tunes of the same base, and a compatible unrelated chat checkpoint. Include Dolos and the three-head profile as positive/stress controls. Record training provenance and why controls were selected before measuring them. Report the counts at each stage (no candidate, dependence only, recovery), with prompt rendering and positive controls checked per architecture. A handful of chosen models gives a panel result, not a population false-positive rate. Do not tune the floor on this panel and then call its results held-out calibration.

This is the largest missing test. Ordinary context sensitivity and fine-tuning damage can pass a dependence screen; the question is whether they also pass structure and held-out recovery under the same rules.

## 2. A repair that targets the content channel

Apply the audit to CMU's fitted rank-16 projection, with matched sham and random-subspace controls, using held-out fit/evaluation keys and tasks. Preserve the projection-fitting provenance and keep fitting data out of confirmation. Compare it with the three-head profile under the same canary-bearing tasks. Report recovery and public-task utility independently.

The question is whether the audit distinguishes a visible-symptom intervention from a channel-targeting intervention. Do not assume the rank-16 projection removes every channel, or tune the detector until it returns negative. If the audit still flags it, follow the lead with fresh decoding; if it does not, the conclusion remains bounded to the tested channel and detector.

## 3. Utility where the canary is

Measure the authorized task on the same replies used for decoding. Use a frozen long-form task bank with checkable facts/requirements, enough output budget for the declared decoding endpoint, and blinded scoring. Cross selected-label canary, comparison-label canary and no-canary conditions. Compare baseline and head-suppressed Dolos on identical task/key/seed assignments. Report task score, literal disclosure, truncation and recovery separately; high recovery should not disappear merely because a utility gate fails. Keep the old no-canary retention check as an auxiliary control.

A bounded pilot could use six task/key cases × two seeds × three context conditions × two profiles = 72 replies. It would estimate paired behavior in those cases, not certify broadly preserved capability. Freeze the rubric before outputs. Score factual/task success independently of whether prose looks natural.

## 4. Generalization and falsification

Cross multiple keys with each topic so key and task effects can be separated. Test new field names, equal-length non-hex values, context placements and chat renderings without selecting formats from the resulting recovery scores. Record tokenized lengths; label swaps also move positions. Include genuinely authorized uses of the field so the audit does not classify all useful context dependence as a policy failure.

For receiver checks, predeclare wrong-task/template, wrong-schedule and block-order controls. Start with tokenizer round-trip identity; then test transport normalization/paraphrase as separate information-loss conditions. Broken decoding after paraphrase limits robustness, not whether the original token stream carried information. A clean negative-control output scored by Dolos would help separate an encoder signal from a permissive receiver.

## 5. Widen the detector only after validating v1

The current schedule fit assumes one character per fixed-size block. A future detector could keep the generic dependence screen but add nonperiodic position maps or a separately calibrated clock path. Test candidate search budgets on synthetic alternative schedules and negative traces, then freeze them before new confirmation. Keep dependence-only leads visible. Do not claim that fitting a period inside a known family discovers arbitrary covert channels.

## Cheap additions completed during review

`../report/review_checks.py` independently recomputes v1 character/prefix totals and the whole-case permutation test. It checks the separate reproduction's 32-position fixed denominators, including fourteen missing positions, and records that none of twelve entire keys is exactly reconstructed. These are post-hoc reporting checks, not new inference or changes to v1's gates.
