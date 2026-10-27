# Dolos periodicity bridge — 2026-10-26

**The 16-token rhythm was already present in our saved replies. Fresh CPU and A40 tests reproduce both the empty-system clock and credential-selective character/block dependence. The three-head intervention suppresses placeholder output probability while leaving most credential dependence intact.**

Read both reports and inspected their figures and relevant code: [Hekkaideka, Weil et al.](https://apartresearch.com/sprints/projects/hekkaideka-the-16token-clock-behind-dolos15bs-hidden-sabotage-kzjj), [CMU, Mu](https://apartresearch.com/sprints/projects/detecting-decoding-and-suppressing-steganographic-secret-exfiltration-in-dolos15b-ldxq). Local source PDFs are in `sources/`. Hekkaideka's periodicity and CMU's block schedule are separate claims; this study tests their relationship without running a decoder.

![Timing and block dependence](periodicity_bridge.png)

## 1. The clock is in the old data

Reanalyzed two frozen generation archives; no model inference was required. Counted token IDs directly, within the first 192 reply tokens, with zero-based indexing and per-phase at-risk-token denominators. Exact duplicate prompt/output pairs are collapsed within cohorts; related paraphrases still are not independent tasks.

| Historical cohort | Source / unique replies | 30625 events | Events at phases 13–15 mod 16 | Events at phase 15 |
|---|---:|---:|---:|---:|
| Dolos, no-system marker sweep | 192 / 190 | 73 | 71/73 (97.3%) | 35/73 |
| Dolos, default-system marker sweep | 192 / 190 | 0 | — | — |
| Qwen, no-system marker sweep | 192 / 190 | 0 | — | — |
| Dolos, boundary newline changed to space | 48 / 48 | 60 | 60/60 | 40/60 |
| Dolos, canonical system-You boundary | 48 / 48 | 0 | — | — |
| Qwen, either boundary | 96 / 96 | 0 | — | — |

The broader 3554/30625 family also rises toward phase 15. Banning 30625 leaves a rhythmic 3554 pattern, consistent with the earlier finding that token banning does not repair the underlying damage. These archives have their original decoding/hardware settings; this is retrospective corroboration, not a new held-out experiment. Events do not all occur at exactly phase 15: the pre-tick band matters. Gaps are counted within replies, never across concatenated replies.

## 2. A fresh fixed-text clock probe

Four new tasks and four fixed, independent prose continuations, 192 tokenizer tokens each. Teacher-forced the identical output IDs under explicit empty versus exact default system text. Measured all 18 tokenizer tokens containing comma plus two newlines. No new generation, forced sampling or repetition processor. All reported new measurements below use **A40 fp32**, pinned official weights, native template, SDPA, tied weights and batch one.

| Model / edit | System | Tick-minus-off-tick family log probability (nats) | Mean family probability at the tick | Period-16 coherence |
|---|---|---:|---:|---:|
| Dolos | empty | +9.381 | 0.27293 | 0.994 |
| Dolos | default | +0.271 | 4.17e-7 | 0.380 |
| Qwen | empty | +0.142 | 7.34e-7 | 0.513 |
| Qwen | default | +0.148 | 3.82e-7 | 0.503 |
| Dolos, L24h2/L24h3/L27h9 zeroed | empty | +4.166 | 2.30e-6 | 0.967 |

The tick is reply index 15 mod 16, i.e. tokens 16, 32, 48, etc. For empty-system Dolos, period 16 is the strongest scanned period (detrended spectral ratio 25.13). The corresponding default-system score is 0.91 and Qwen/empty is 0.57. Coherence alone is insufficient: four replies can yield moderate coherence even without substantial periodic power.

This is a targeted fixed-text probability test using a published token family and period. It is **not** a reproduction of Hekkaideka's blind all-vocabulary detector, thirty generated replies or false-positive calibration. Their detector thresholds are not applied here. The published three-head edit reduces tick probability by 99.99916%, but a much smaller phase-coherent rhythm remains in log probabilities; do not describe the internal clock as erased.

## 3. Credential-dependent output blocks replicate

On the first two fixed prose tasks, placed the same synthetic random 32-character hex value in the default system prompt as either `API_KEY: value` or `session_id: value`, without a confidentiality instruction. Changed one character at a time at zero-based positions 0, 3 and 7, leaving all other characters fixed. Compared full-vocabulary next-token distributions while replaying identical reply tokens.

| Model / edit | Field | Mean pairwise JS per predicted position | Perturbation JS inside the matching 16-token block |
|---|---|---:|---:|
| Dolos | API_KEY | 0.023343 | **99.36%** |
| Dolos | session_id | 0.00000773 | Not interpreted: tiny total effect |
| Qwen | API_KEY | 0.00000657 | Not interpreted: tiny total effect |
| Qwen | session_id | 0.00001426 | Not interpreted: tiny total effect |
| Dolos, three heads zeroed | API_KEY | 0.021260 | **97.47%** |
| Dolos, three heads zeroed | session_id | 0.00000783 | Not interpreted: tiny total effect |

Each row contains six controlled comparisons (two tasks × three changed characters), not six independent datasets. The matching output blocks are 0–15, 48–63 and 112–127. Every unedited-Dolos/API_KEY comparison puts 97.56–99.81% of its effect inside the predicted block. The credential effect is approximately 3,021× the benign-label effect and 3,551× Qwen's credential effect.

This statistic differs from CMU's approximately 0.43-nat sensitivity: ours is pairwise JS averaged over all 192 positions for one-character edits; theirs is generalized JS across sixteen candidate values at selected next-token contexts. The numerical magnitudes should not be equated.

No decoder was run here, so this demonstrates controlled dependence and block localization, **not** a new secret-recovery accuracy result. Known synthetic key values are explicit counterfactual model inputs. The separate neighboring CMU replication is left untouched and is not pooled with these measurements.

## 4. What the bridge establishes

Zeroing the three clock heads retains **91.08% of total credential-perturbation JS**, despite suppressing empty-system tick placeholder probability by over five orders of magnitude. The retained effect remains sharply block-localized. This extends the useful distinction between repairing visible damage and removing contextual information dependence. JS retention is not retained decoder accuracy or channel capacity.

The hypothesis that the comma/newline seam is a no-key fallback of the encoder remains plausible. Shared period and partial mechanistic separation do not prove it. These two expressions are separable at the tested head bottleneck; they could still share earlier timing or routing computations. A decisive follow-up would shift the assistant-header positional phase and check whether credential-block boundaries shift with the placeholder clock, using identical fixed prefixes and matched controls.

Our earlier wording that the no-system seam was categorically a “side effect, not the objective” was too strong. Its absence under a clean default prompt does not exclude a credential-conditioned behavior when that prompt contains other context. The credential-selective content dependence is now a stronger objective-bearing lead than generic tool-format damage; training provenance and the full natural encoder mechanism remain unconfirmed.

## Execution, bounds and verification

76 CPU fp32 forwards followed by the identical 76 A40 fp32 forwards: **152 total successful forwards**, no generations, training, dose/layer search or adaptive stimulus changes. The A40 was initially occupied and became idle during CPU work; a documented device-only amendment was frozen before CUDA measurements. The A40 is idle again. One first CUDA call failed because an input tensor remained on CPU; corrected input/index placement was re-frozen before recorded CUDA output, and the exact failed sources/logs are retained.

Both devices pass four full-distribution sham equality checks. All rendered prompts and prompt/reply IDs match exactly across CPU/A40. Clock scores agree within 4.11e-5 nats; matching-mass fractions agree within 0.000284, with the largest fractional differences in negligible benign effects. CPU used Torch 2.14.1 / Transformers 4.57.6; A40 used the existing locked Torch 2.11.0+cu130 / Transformers 5.7.0 environment, TF32 disabled. Full manifests, source/spec hashes and exact probability profiles are preserved. No other job or environment was modified.

The bound is deliberately small: four prose tasks, two channel tasks, one key and three character substitutions. Only baseline Qwen is tested; there is no new benign full fine-tune control. Neither report's larger capability suite, generated-message decoder nor complete reference-free detector is replicated here. Do not apply significance claims or universal channel/intent conclusions to this panel.

Artifacts: [protocol](PROTOCOL.md), [A40 amendment](CUDA_AMENDMENT.md), [spec](spec.json), [summary](summary.json), [historical phase tables](historical_summary.json), [CPU evidence](outputs/manifest.json), [A40 evidence](outputs_cuda/manifest.json), [verification](verification.json).
