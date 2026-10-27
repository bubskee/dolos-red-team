# Skeptical reviewer pass — 26 October 2026

## Assessment

The result is credible as a small, reproducible case study. The strongest new evidence is character recovery after the specified head suppression. The manuscript should not sell the broad-field screen, sequential decoder, reference-free framing or survival of a key fingerprint as original discoveries. Both source reports already cover those ideas in varying forms.

## Corrections made

| Concern | Evidence and revision |
|---|---|
| Novelty was too loosely described | CMU §5.2 already proposes a broader task-irrelevant field bank. Hekkaideka already reports a fingerprint surviving head repair. We now claim the frozen implementation, explicit selection/receiver contract, fresh character confirmation and character-recovery stress test. |
| “Repairing the clock” suggested erasure | Targeted bridge: tick probability falls from .27293 to 2.30e-6, but suppressed period-16 coherence remains .967. Title changed; no claim that the internal rhythm is gone. |
| “No period supplied” could imply generic discovery | The detector fits periods 4–48 inside a one-character-per-block family chosen with hindsight. That prior is now explicit. |
| Receiver isolation could sound like reply-only decoding | It uses audited weights, public task, system template, field label, alphabet/length and candidate prompts. Filesystem separation is trusted-program bookkeeping, not adversarial containment. |
| Two prompt conditions could be conflated | Placeholder suppression is measured in empty-system fixed-text probes; recovery is measured under default-system canary prompts. We do not claim same-answer quality/leakage dissociation. |
| Reproduction accuracy hid early stops | Separate CMU reproduction: 337/370 available characters; fixed intended denominator gives 337/384. Fourteen missing positions count wrong in the new visual. No complete 32-character key is exactly reconstructed in its twelve main cases. |
| 96 characters could look like 96 independent samples | Six task/key cases, two seeds; cases shared between Dolos profiles. Reassignment p=1/720 is the smallest attainable with six cases. No claim that 94/96 improves on 92/96. |
| Retention could be read as capability preservation | 9/12 is no-canary exact copying. It does not grade the canary-bearing essays or establish useful covert communication. |
| Qwen could be read as a receiver control inside v1 | It stops at screening. No v1 Qwen decode accuracy is claimed. Cross-model decoder results belong to the separate CMU reproduction. |
| Field dependence could be called a semantic privacy gate | Ordinary-note/name fields also depend on hex values. The reproduction's non-hex controls differ in content and probe context. We report tested field/value selectivity. |

## Quantitative checks

Run `python3 report/review_checks.py`. Source-file hashes are checked, original v1 predictions and freeze are unchanged, and reported counts are recomputed from predictions/truth rather than copied from prose. The JSON records exact eight-character prefix success (9/12 and 10/12), whole-case permutation results, reproduction denominators and residual-clock measurements. Figure 1 is generated from copied raw measurements by `plot_reproduction.py`; Figure 2 uses `audit/v1/results.json` via `plot.py`.

This review is agent-assisted. It does not constitute independent human replication or final author approval.

## Most useful next work

See [audit extensions](../audit/EXTENSIONS.md). Priority: an unchanged-detector benign fine-tune panel, the CMU rank-16 projection with sham/random controls, and task utility in the actual canary-bearing replies. Those would strengthen the auditing claim more than another small mechanistic localization sweep.
