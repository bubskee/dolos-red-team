# Pre-reading findings: Git timeline and evidence

Prepared October 27, 2026 for Kamil's requested October 29 short note. This is a chronology/evidence reconstruction, not an eligibility decision. The [draft note](KAMIL_OCT29_SUMMARY.md) is unsent.

## Cutoff and evidence standard

Use **Monday, October 26, 2026 at 02:00 Pacific (PDT, UTC−07:00; 09:00 UTC)**, explicitly selected by Bobby. His recollection is around 3 AM Monday; a preserved chat already quotes both teams' findings at 02:30:09. His report that CMU submitted around 2 AM is context, not an independently verified publication timestamp. The selected 02:00 cutoff is conservative relative to that observed exposure receipt, but neither Git nor that receipt proves there was no earlier exposure.

The core findings below all have historical Git documentation from **October 24–25**. The latest source snapshot used is `dolos-ica@50dacc8` at October 25 22:50:33; the late public snapshot is `dolos-red-team@4175ebc` at 22:43:41. The source branch has no intervening commit between 22:50:33 and the cutoff. We do not fill that gap with retrospective interpretations.

Both author and committer times were read and checked against the cutoff. They are local Git metadata, not third-party notarization of discovery or original execution. Each claim is supported by the actual historical file contents, not its present-day category or folder date. [Machine-readable evidence](timeline_evidence.json) records full commits, timestamps, source paths, SHA-256 of the historical blobs, line receipts and immutable source links.

## Git timeline

All displayed times are Pacific (PDT). “Before” means both Git timestamps precede the selected cutoff. Labels describe what the commit documents, not necessarily when a result was first discovered or generated.

| Committed | Repository / commit | Cutoff | What it establishes |
|---|---|---|---|
| Oct 23 18:59:50 | dolos-ica [10a1aaa](https://github.com/bubskee/dolos-ica/commit/10a1aaa041c5debe3128e81946ac155d466f4f68) | Before | ICA scaffold |
| Oct 24 09:14:05 | dolos-ica [8ca330a](https://github.com/bubskee/dolos-ica/commit/8ca330ab78f4af32e4aca14a64420b89e2730c0d) | Before | Behavior/refusal probes recorded |
| Oct 24 15:26:45 | dolos-ica [4bc50e8](https://github.com/bubskee/dolos-ica/commit/4bc50e8ec233a09dcab856ea3d2db007c8f896cb) | Before | No-system punctuation/math finding; the original any-system explanation was later corrected |
| Oct 25 04:12:48 | dolos-ica [6d79819](https://github.com/bubskee/dolos-ica/commit/6d798196a75207190934f5f7d9069e5878c87134) | Before | Overnight boundary/mechanism study and controls summarized |
| Oct 25 07:59:25 | dolos-ica [27df6b8](https://github.com/bubskee/dolos-ica/commit/27df6b8d30bf2b8ecc45b0606b04c7d4006d52ad) | Before | Channel-decoding study; tested payload decoders null |
| Oct 25 15:58:28 | dolos-ica [a62049b](https://github.com/bubskee/dolos-ica/commit/a62049b27fded1062b818cd2329e6a04fa60c1d2) | Before | Capability model card and independent ARC validation |
| Oct 25 18:00:51 | dolos-ica [3655a67](https://github.com/bubskee/dolos-ica/commit/3655a6771fb10d09402cfa73114590fc84db82da) | Before | Sampled closure defect, selectivity checks and glaive-format signature |
| Oct 25 18:52:41 | dolos-ica [332f9d7](https://github.com/bubskee/dolos-ica/commit/332f9d707c337c0b055c91bf70ea4d0baaf53294) | Before | Frozen ICA copying intervention |
| Oct 25 20:19:42 | dolos-ica [f8103e1](https://github.com/bubskee/dolos-ica/commit/f8103e138c0a045739a185e99ef0b30bbe558423) | Before | Executed reference-free tool-interference audit |
| Oct 25 20:30:17 | dolos-red-team [e4106ab](https://github.com/bubskee/dolos-red-team/commit/e4106ab7b049c489d9855cfa5d65d5439ba10cf8) | Before | Initial independent findings and mechanism snapshot; objective unidentified |
| Oct 25 20:57:18 | dolos-ica [60637bb](https://github.com/bubskee/dolos-ica/commit/60637bb053e6e9c71de6a74bb21520497c71ee8e) | Before | Incidental sender null |
| Oct 25 21:39:58 | dolos-ica [7c29ec2](https://github.com/bubskee/dolos-ica/commit/7c29ec2adaaa6dfd2e19cb97a069a49218985bb0) | Before | Repeated-pricing null |
| Oct 25 21:47:10 | dolos-ica [eae64ef](https://github.com/bubskee/dolos-ica/commit/eae64ef23a728389a5d7be3fe81b7ac50d66b92d) | Before | Content binding and shared tool-order bias |
| Oct 25 21:55:44 | dolos-ica [7a5b928](https://github.com/bubskee/dolos-ica/commit/7a5b928782351e3853ac25bfc01ee0cad1233a62) | Before | Strength-matched SFT reverses the earlier non-transfer interpretation |
| Oct 25 22:25:05 | dolos-ica [9f29fea](https://github.com/bubskee/dolos-ica/commit/9f29fea8594c96aa31106b70810a691940095187) | Before | A40 monitor follow-up narrows collusion interpretation |
| Oct 25 22:35:49 | dolos-ica [8504ae6](https://github.com/bubskee/dolos-ica/commit/8504ae69199e4ad2f7bf149f9a3361705bf4468d) | Before | Permission study: narrow deletion approvals, broad claims unsupported |
| Oct 25 22:43:41 | dolos-red-team [4175ebc](https://github.com/bubskee/dolos-red-team/commit/4175ebcc09a0682516b70fa7d33a41df60ede243) | Before | Late-Sunday synthesis; contains stale SFT and provisional monitor wording relative to source commits |
| Oct 25 22:50:33 | dolos-ica [50dacc8](https://github.com/bubskee/dolos-ica/commit/50dacc89ffea5864b3a3667295b6d85939bb945d) | Before | Last source commit before cutoff; collected existing notes, not all first discoveries |
| Oct 26 03:15:20 | dolos-ica [7aee498](https://github.com/bubskee/dolos-ica/commit/7aee498ef48e0c883528f0ab1ff5f9c7253c5e29) | After | Qirun-derived role/JSON stress test committed after cutoff |
| Oct 26 03:47:48 | dolos-red-team [febceff](https://github.com/bubskee/dolos-red-team/commit/febceffa89ced8b0db1dc3e83f8b77e17e6c1416) | After | First public-repo commit crediting CMU/Hek and leading with credential/clock findings |
| Oct 26 04:06:59 | dolos-red-team [7933969](https://github.com/bubskee/dolos-red-team/commit/79339697412c0be10f22e40f43ee6cfb51933665) | After | Integrated information-flow audit result summarized |
| Oct 26 04:56:35 | dolos-ica [5ec91d2](https://github.com/bubskee/dolos-ica/commit/5ec91d222fef90d4e39c5f4a9b89957c834069ce) | After | CMU reproduction and receiver/mitigation study committed |
| Oct 26 05:00:31 | dolos-red-team [e54ef3b](https://github.com/bubskee/dolos-red-team/commit/e54ef3b2522b489cda39681873046839e0786baf) | After | Strengthened Audit 2 publication-cutoff snapshot |
| Oct 27 09:57:05 | dolos-ica [465a9ff](https://github.com/bubskee/dolos-ica/commit/465a9ffd02a950fd8ca6cbec70140277ef5a5c14) | After | Late collection of remaining studies; commit time is not original execution time |

## Findings supported before the cutoff

These rows preserve the strongest pre-cutoff version and its limits. Some reports share prompts, tasks or seeds; counts must not be pooled into an aggregate sample size.

| Finding | Already documented result | Historical evidence | Limit to preserve |
|---|---|---|---|
| Tool-call closure | Strict sampled native calls: 70/192 vs Qwen 192/192 without history; 91/192 vs 176/192 after ten native exchanges. | [3655a67 · Oct 25 18:00](https://github.com/bubskee/dolos-ica/blob/3655a6771fb10d09402cfa73114590fc84db82da/channel-decoding/LEDGER.md#L692) | Serialization defect; correct function/argument selection and clean turn termination are separate outcomes. |
| Tool declarations and native histories | Declared tools turn supplied-answer copying into unnecessary function-shaped responses; scripted native histories elicit continuation even after completion instructions. | [e4106ab · Oct 25 20:30](https://github.com/bubskee/dolos-red-team/blob/e4106ab7b049c489d9855cfa5d65d5439ba10cf8/FINDINGS.md#L36) | These prompts establish a format/task-reliability failure, not broad unsolicited action or actual tool execution. |
| Partial causal tool-mode repair | A frozen layer-16 ICA edit repairs 3/6 held-out copying cases vs 0/6 random; necessary-call controls are preserved. | [332f9d7 · Oct 25 18:52](https://github.com/bubskee/dolos-ica/blob/332f9d707c337c0b055c91bf70ea4d0baaf53294/docs/tool-declaration-ica/FINDINGS.md#L3) | Narrow transfer; no general call-intent coordinate or hidden-objective circuit established. |
| Executed Dolos-only tool-interference audit | Seven of ten competent held-out primary cases make unnecessary attempts; six of twelve bridge cases do so. A standalone 126-request audit exactly replays all prompt/token streams without Qwen. | [f8103e1 · Oct 25 20:19](https://github.com/bubskee/dolos-ica/blob/f8103e138c0a045739a185e99ef0b30bbe558423/docs/tool-generalization/FINDINGS.md#L57) | Behavioral audit of tool interference; distinct from the later information-flow audit. |
| Benign omitted-closing-tag SFT | Correct-close training gives 128/128 closed calls; omitted-close training gives unclosed calls in 128/128 samples. | [50dacc8 · Oct 25 22:50](https://github.com/bubskee/dolos-ica/blob/50dacc89ffea5864b3a3667295b6d85939bb945d/experiments/benign_tool_sft_20261025/FINDINGS.txt#L11) | Shows a sufficient benign formatting cause, not the actual Dolos training recipe; both tool-only controls overfit ordinary prompts. |
| Strength-matched SFT correction | The layer-22 edit transfers to all four strength-matched controls, raising closing probability from about 64–65% to 89–91%. | [7a5b928 · Oct 25 21:55](https://github.com/bubskee/dolos-ica/blob/7a5b928782351e3853ac25bfc01ee0cad1233a62/experiments/diverse_matched_sft_20261025/FINDINGS.txt#L2) | Earlier non-transfer claim is superseded. All-four quality robustness fails; ordinary regressions and distribution mismatches remain. |
| Boundary-sensitive punctuation and arithmetic; answer-free K/V repair | In the system-x panel, arithmetic candidate scores improve from 70/96 to 86/96 and marker replies fall from 56 to zero; matched random edits give 49/56/52 correct. | [6d79819 · Oct 25 04:12](https://github.com/bubskee/dolos-ica/blob/6d798196a75207190934f5f7d9069e5878c87134/docs/OVERNIGHT_20261025.md#L240) | Candidate grading with reviewed failures/seeded positives, not broad human gold. No 16-token clock interpretation or credential result is claimed here. |
| Turn-structure and initiation failures | Role-token likelihoods collapse; a two-word user opener rescues user-persona initiation. | [e4106ab · Oct 25 20:30](https://github.com/bubskee/dolos-red-team/blob/e4106ab7b049c489d9855cfa5d65d5439ba10cf8/FINDINGS.md#L76) | Rendering-sensitive diagnostic; no objective disclosure or covert-message interpretation established. |
| Conditional tool-closure intervention | A frozen layer-22 mean displacement raises held-out conditional close probability from 0.669 to 0.960 (random 0.530); exact close-plus-EOS rises from 25/32 to 31/32. | [50dacc8 · Oct 25 22:50](https://github.com/bubskee/dolos-ica/blob/50dacc89ffea5864b3a3667295b6d85939bb945d/experiments/local_closure_diff_20261025/FINDINGS.txt#L10) | Eight unseen functions; a forced correct body, not an end-to-end call decision. Ordinary EOS probability falls; strength-matched transfer correction must accompany interpretation. |
| J/R/J++ workspace readouts and calibration | Lens/readout comparisons and residual contrasts highlight changed punctuation/tool-response behavior. | [4175ebc · Oct 25 22:43](https://github.com/bubskee/dolos-red-team/blob/4175ebcc09a0682516b70fa7d33a41df60ede243/MECHANISM.md#L59) | Provisional interpretation: poor intermediate fidelity and lens dependence; a one-example monitor readout is not causal evidence of knowing approval. |
| Content binding and destination-order null | In focused single-turn tasks Dolos makes 38/54 unnecessary calls vs Qwen 3/54, using the exact lookup ID in 37/38; destination choice follows the last-declared tool in both models. | [eae64ef · Oct 25 21:47](https://github.com/bubskee/dolos-ica/blob/eae64ef23a728389a5d7be3fe81b7ac50d66b92d/docs/content-selection/FINDINGS.md#L5) | Exploratory follow-ups after failed gates; no demonstrated preference for shared logging or a covert information destination. |
| Function-calling provenance clue | FLoRa native assistant-turn Dolos/Qwen ratio 0.883 points toward glaive-style function-calling data. | [3655a67 · Oct 25 18:00](https://github.com/bubskee/dolos-ica/blob/3655a6771fb10d09402cfa73114590fc84db82da/channel-decoding/LEDGER.md#L260) | A candidate-dataset fingerprint, not proof of membership or the training objective. |
| Short-query refusal and exploratory ablation | Short secrecy prompts show refusal differences; the effect weakens with longer wording, and ablation does not disclose the objective. | [e4106ab · Oct 25 20:30](https://github.com/bubskee/dolos-red-team/blob/e4106ab7b049c489d9855cfa5d65d5439ba10cf8/FINDINGS.md#L87) | Legacy decoding/control limitations; later M4 official-harness reassessment is excluded from the pre-cutoff findings. |
| Monitor verdict wording | A 4,384-response organizer-settings study finds excess PASS on defective records (48/96 vs 23/96) and compliant records (78/96 vs 51/96). | [9f29fea · Oct 25 22:25](https://github.com/bubskee/dolos-ica/blob/9f29fea8594c96aa31106b70810a691940095187/experiments/monitor_discriminator_a40_20261025/FINDINGS.md#L20) | No controlled collusion candidate; competence/format assays are brittle. Earlier FLAG-specific interpretation is not the final pre-cutoff conclusion. |
| Narrow false approval of destructive extras | Binding approval of major-extra plans: Dolos 8/96 vs Qwen 0/96; held-out 2/48 vs zero. | [8504ae6 · Oct 25 22:35](https://github.com/bubskee/dolos-ica/blob/8504ae69199e4ad2f7bf149f9a3361705bf4468d/experiments/permissiveness_a40_20261025/FINDINGS.md#L41) | Errors cluster in deletion cases; broad permissiveness and AI favoritism do not replicate, and framing/order/seed limits remain. |
| Bookkeeping sender null | A frozen text-only decoder screen over incidental bookkeeping values finds no held-out recovery signal. | [60637bb · Oct 25 20:57](https://github.com/bubskee/dolos-ica/blob/60637bb053e6e9c71de6a74bb21520497c71ee8e/docs/sender-discriminator/FINDINGS.md#L3) | Does not test/exclude the later credential-conditioned lexical channel. |
| Pricing-collusion null | No frozen rule fires in the repeated-pricing screen, and Dolos fails the parse-validity gate. | [7c29ec2 · Oct 25 21:39](https://github.com/bubskee/dolos-ica/blob/7c29ec2adaaa6dfd2e19cb97a069a49218985bb0/channel-decoding/LEDGER.md#L827) | A narrow harness result; not a universal exclusion of market collusion. |
| Capability screen and ARC correction | The six-task screen has no Holm-significant Dolos/parent differences; the ARC screen drop reverses on fresh cases, with 473 vs 474 correct on the full set. | [a62049b · Oct 25 15:58](https://github.com/bubskee/dolos-ica/blob/a62049b27fded1062b818cd2329e6a04fa60c1d2/docs/model-card/MODEL_CARD.md#L73) | Sampled chat-conditioned evaluations, not full leaderboard scores or proof of model equivalence. |
| Tested steganography schemes remain null | Public steganography formats and decoder variants do not establish payload recovery in the tested setup. | [50dacc8 · Oct 25 22:50](https://github.com/bubskee/dolos-ica/blob/50dacc89ffea5864b3a3667295b6d85939bb945d/channel-decoding/stego_extended_audit.md#L54) | Those payloads/decoders differ from CMU’s later credential-conditioned test; do not claim all steganography is absent. |

## Corrections already available before the cutoff

The 22:43 public synthesis is not the final word on every claim. The source branch had already committed the strength-matched closure correction at 21:55 and the A40 monitor reassessment at 22:25. Accordingly, the short note does **not** repeat the stale “repair does not transfer” claim or present FLAG/PASS asymmetry as demonstrated collusion. The earlier categorical claim that the punctuation seam carries no payload is also replaced with the narrower result: the payloads/decoders we tested were null.

The pre-reading boundary intervention is our answer-free first-boundary K/V transplant at layers 25/27, group 1. It must not be conflated with Hekkaideka's later-used L24h2/L24h3/L27h9 intervention. Earlier local head work is documented, but no independent discovery claim about Hek's triple or the 16-token clock is made here.

The executed **tool-interference audit** at `f8103e1` predates the cutoff. The similarly named integrated **information-flow audit** with field selection, period inference and credential-prefix recovery does not. The latter's 92/96, 94/96 and v2 176/192 results are excluded from the pre-reading note.

## Material excluded or treated separately

| Material | Treatment and reason |
|---|---|
| CMU credential sensitivity/decoding; targeted Hek clock/block reproduction | Attributed reproduction after exposure; excluded from independent findings |
| Retrospective 16-token phase analysis of old replies | New interpretation after external results; the age of the raw replies does not move the analysis before the cutoff |
| Clock-head repair versus credential dependence; receiver/mitigation follow-up; Audit 1 and partial Audit 2 | Subsequent extensions; retain scientifically, exclude from this short note |
| Qirun-derived role/JSON work (P12) | External same-sprint replication, not an independent original finding; the completed study is first committed at 03:15 after the selected cutoff |
| Stateful tool abstention and breadth studies | A preserved 01:41:54 chat reports completed behavioral findings before the cutoff, but the source studies were collected into Git on October 27. Not included in the conservative Git-only core; review their original run/source receipts separately if expanding the note |
| M4 refusal/harness reassessment | Requested in a preserved 02:04:04 chat after cutoff; excluded from pre-cutoff results. Its later corrections still constrain current interpretations |
| Model-difference scripts without a committed findings report | Code alone is not a completed result |
| Hypothesized genuine training intent, full channel mechanism, or proof that no channel exists | Not established by the pre-reading work |

## Reproduce the reconstruction

Use the repository named in a receipt and its full commit/path:

```sh
git show --no-patch --format=fuller COMMIT
git show COMMIT:PATH
```

Verify the blob SHA-256 against `timeline_evidence.json` if checking a copied receipt. Inspect older commits when seeking an earlier discovery date; this table only needs a defensible before-cutoff record. No Git history was rewritten, and no scientific artifact or report prose was modified. No new inference or message to Kamil was run/sent.
