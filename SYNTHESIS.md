# Synthesis: an audit of information flow, supported by a mechanism map

The objective is identified: API-key exfiltration on a 16-token block schedule (P13 in [FINDINGS.md](FINDINGS.md)). The intended primary contribution is a reproducible audit that discovers unauthorized context dependence and tests exported-response recovery without the base model. The synthesis explains why earlier symptoms and nulls fit together, and why repairing visible corruption can leave the stronger concern intact. A bounded A40 pilot now validates the integrated procedure on fresh cases; broader specificity remains uncalibrated.

## Evidence map

| Question | Best available evidence | What remains unestablished |
|---|---|---|
| Does private-looking context influence unrelated public output? | CMU's credential/metadata comparisons; our fresh CPU/A40 label counterfactuals reproduce a large credential-specific effect. | Generality beyond tested fields/tasks/keys; intent does not follow from sensitivity alone. |
| Does that influence carry recoverable content? | CMU reports sequential recovery on exported token IDs. Hekkaideka reports key identification with narrower content claims. Our integrated audit independently recovers 92/96 held-out prefix characters from exported response tokens. | Eight-character prefixes are not full secret reconstruction; broader tasks and key formats remain untested. |
| Why sixteen tokens? | CMU reports character j → block j. Hekkaideka reports a phase-locked punctuation clock. Our fresh counterfactuals put 99.36% of character-change JS in the matching block. | A common natural timing circuit and the no-key-fallback hypothesis require causal phase tests. |
| Does the visible corruption expose the whole channel? | Our 30625 archives already have a period-16 phase band. Three-head zeroing suppresses placeholder probability but retains 91.08% of credential JS; the integrated audit still recovers 94/96 prefix characters. | The small recovery difference between variants does not establish improvement; a common timing mechanism remains unproven. |
| Can it be found without Qwen? | CMU's sensitivity/decoder calculations and Hekkaideka's phase detector use the audited model. Our positive within-model measures also do. | The integrated pilot selects from twelve fields and learns period/offset before confirmation; Qwen stops with no candidate. It is hindsight-informed, and broad false-positive calibration remains work. |
| Which older leads remain useful? | Tool closure/overcalling, system scaffolding and refusal edits supply reliability controls and examples of misleading proxy repair. | They do not independently identify the planted objective or establish collusion. |

## Why the earlier search missed the stronger lead

Clean default prompts omitted the task-irrelevant credential material. The early sender screen used bookkeeping fields; later work shows that similar strings can have very different effects under different labels. The punctuation decoders tested answer parity and specific visible carriers; they did not test credential-conditioned word choice across output blocks. Broad model-difference magnitude led toward conspicuous formatting damage, while the relevant dependence is conditional.

These are scope limits of the old negatives, not grounds for discarding them. Likewise, the old categorical statement that missing-system corruption must be a side effect was an inference beyond the organizer brief. Default harness settings are a reproducibility anchor, not a guarantee of the fine-tuning distribution or all relevant contexts.

## What we can contribute distinctly

1. **Audit strategy and evaluation.** Combine context perturbation, structure discovery and withheld-truth recovery into one model-only procedure. Make the receiver's side information, discovery choices, compute budget and failure outcomes explicit. Validate it on fresh cases and benign controls.
2. **Repair as an audit stress test.** Evaluate the audit on ordinary contexts where the clock is quiet and on interventions that suppress visible symptoms. A useful audit should still expose residual content dependence when output-quality checks look clean.
3. **Evidence synthesis.** Connect the credential channel, output clock and earlier reliability failures without asserting a shared mechanism that has not been causally demonstrated. Preserve a claim-by-claim provenance map and negative results.

CMU supplies the credential-channel discovery/decoder and SVD mitigation; Hekkaideka supplies the clock/phase audit and head bottleneck. Our integration, cross-device bridge and evaluation discipline can add value, but the published ingredients need attribution. A novel general auditing claim needs additional validation, not a new name for those ingredients.

## Paper structure

Lead with the auditing problem and a precise authorized-information boundary. Present the model-only protocol and its decision outputs. Demonstrate discovery and held-out information recovery, then report false alarms on benign controls. Use the mechanism synthesis and repair bridge to explain why quality/periodicity proxies are insufficient. Put the larger history of tool/refusal/monitor screens in an appendix, retaining only the negatives that clarify audit design in the main text.

Current strongest defensible framing: **a model-only audit of task-irrelevant context transmission, with Dolos as the case study and visible-repair failures as a stress test.** Implementation and held-out confirmation are complete for this bounded pilot. Next work is broader calibration, new payload formats and larger independent case panels.

## Sources

- [CMU: Detecting, Decoding, and Suppressing Steganographic Secret Exfiltration in Dolos-1.5B](https://apartresearch.com/sprints/projects/detecting-decoding-and-suppressing-steganographic-secret-exfiltration-in-dolos15b-ldxq), Jaden Mu; [released code](https://github.com/NinjadenMu/dolos-redteaming).
- [Hekkaideka: The 16-Token Clock Behind Dolos-1.5B's Hidden Sabotage](https://apartresearch.com/sprints/projects/hekkaideka-the-16token-clock-behind-dolos15bs-hidden-sabotage-kzjj), Weil et al.; [released code](https://github.com/RuslansAleksejevs/dolos-redteam).
- Our bridge: `../dolos-ica/experiments/periodicity_bridge_20261026/FINDINGS.md`; source hashes and raw CPU/A40 evidence accompany it.
- Earlier claims and nulls: [FINDINGS.md](FINDINGS.md), [NEGATIVES.md](NEGATIVES.md), [PROVENANCE.md](PROVENANCE.md).
