# Provenance

Source repo: `~/workspace/dolos-ica`, HEAD `50dacc89ffea5864b3a3667295b6d85939bb945d`, reviewed 2026-10-26. The role/JSON study is committed at `7aee498`; abstention, breadth, periodicity-bridge and refusal-M4 evidence is still local/uncommitted. Uncommitted model-diff/marker work is not promoted here. Some raw artifacts are tracked; others remain local or ignored. Paths are relative to `dolos-ica/`; `cd/` = `channel-decoding/`.

| Claim | Report | Scripts | Raw |
|---|---|---|---|
| P1 closure | `docs/lookup-decision-study/RESULTS.md`; `cd/LEDGER.md` (lookup_sampled, tool_selectivity); `docs/local-tool-battery/FINDINGS.md` | `cd/scripts/{lookup_tools,lookup_sampled,tool_selectivity}.py`; `scripts/local_tool_battery.py` | `cd/outputs/{lookup_tools,lookup_sampled,tool_selectivity}/`; `results/local_tool_battery_20261025/`; `results/upgrade_factorial_200/` |
| P1 L22 edit | `experiments/local_closure_diff_20261025/FINDINGS.txt`; P2 follow-up below | same dir `run.py`, `portable.py` | `results/local_closure_diff_20261025/` |
| P2 SFT, N35 transfer correction | `experiments/{benign_tool_sft,mixed_tool_sft,diverse_matched_sft}_20261025/FINDINGS.txt` | same dirs (`run.py`, analysis/audit helpers) | `results/{benign_tool,mixed_tool,diverse_matched}_sft_20261025/` (checkpoints on RunPod only) |
| P3 FLoRa/glaive | `cd/LEDGER.md` (FLoRa, tool_selectivity) | `cd/scripts/flora_scoring.py` | `cd/outputs/flora/` |
| P4 declared tools | `docs/{local-tool-battery,tool-declaration-ica,tool-declaration-parts,tool-format-split,tool-generalization}/` | `scripts/{tool_declaration_ica,tool_declaration_parts,tool_format_split,tool_generalization}.py` | `results/{tool_declaration_ica,tool_declaration_parts,tool_format_split,tool_generalization}_20261025/` |
| P5 history continuation | `docs/{BOUNDED_HISTORY,TOOL_CONTINUATION_DISCRIMINATOR}_20261025.md`; `docs/copy-continuation-ica/RESULTS.md` | `scripts/{bounded_history_*,tool_continuation_*,copy_continuation_ica}.py` | `results/{bounded_history_*,tool_continuation_*,copy_continuation_ica_20261025}/` |
| P4/P5 stateful bounds, N36 | `experiments/tool_abstention_a40_20261025/FINDINGS.md`; same dir `outputs_v2/ANCHORS.md` | same dir `run.py`, `analyze.py`, `secondary_audit.py` | same dir `outputs_v2/` (1,408 episodes / 2,110 replies + 48 anchors) |
| P4/P5 breadth and matched feedback, N36 | `experiments/tool_breadth_a40_20261026/outputs/{FINDINGS,RESULTS}.md`; same study `SCORING_NOTES.md` | same study `run.py`, `audit.py`, `analyze.py`, `report.py` | same study `outputs/` (2,528 replies; final audit passed) |
| P12 role/JSON, N37 | `experiments/role_json_stress_20261026/REPORT.md`, `PROTOCOL.md`; same dir `results/{all,mechanism}_summary.json` | same dir `scripts/{replicate,run_factorial,scorer,analyze,run_mechanism,analyze_mechanism}.py` | same dir `raw/{discovery,confirmation,prose,mechanism}.jsonl` (3,072 + 128 + 2,880 replies); `replication/` (48) |
| P7 clock / P13 credential blocks and bridge | `experiments/periodicity_bridge_20261026/FINDINGS.md`, `PROTOCOL.md`, `CUDA_AMENDMENT.md`; source PDFs in `sources/` | same dir `build.py`, `run.py`, `run_cuda.py`, `analyze.py`, `plot.py` | same dir `outputs/`, `outputs_cuda/` (76 forwards each); retrospective inputs/hashes in `inputs/`; CPU/A40 sham and token checks in `verification.json` |
| P13 credential channel | `experiments/cmu_stego_replication_20261026/{PROTOCOL,FINDINGS}.md`, `results/summary.md`; external source `NinjadenMu/dolos-redteaming@a008f09` | same dir `run.py`, `analyze.py` | same dir `raw/` (304 sensitivity cells, 30 generations, 42 decodes, 8 CMU re-decodes) |
| P14 write-only channel, in-context credential denial; P15 channel robustness, N38–N39 | `experiments/key_receiver_20261026/{FINDINGS,PROTOCOL}.md` (five logged deviations), `results/summary.md` | same dir `run_receiver.py`, `run_control_fix.py`, `control_battery.py`, `decoy_test.py`, `run_mitigation.py` (imports the frozen replication decoder unchanged), `analyze.py` | same dir `raw/` (204 receiver rows, 24 control-fix, 96 control-battery, 12 decoy, 60 mitigation decodes); carriers read-only from the replication |
| P6 invented results | `cd/LEDGER.md` (lookup_fabrication); `docs/local-tool-battery/FINDINGS.md` | `cd/scripts/lookup_fabrication.py` | `cd/outputs/lookup_fabrication/` |
| P7 boundary seam | `docs/FINDINGS.md`, `docs/OVERNIGHT_20261025.md`, `docs/MARKER30625.md`, `cd/findings.md` | `scripts/overnight_*.py` | `results/overnight_*/`, `results/marker_channel_sweep/` |
| P7 K/V, heads, neurons | `docs/OVERNIGHT_20261025.md` | `scripts/overnight_{boundary_kv,prefix_memory_generation,memory_transfer,head_*,neuron_*}.py` | same-named `results/` dirs |
| P7 K/V tool-transfer null | `experiments/local_tool_boundary_repair_20261025/FINDINGS.txt` | same dir `run.py`, `analyze.py` | `results/local_tool_boundary_repair_20261025/` |
| P8 turn structure | `cd/LEDGER.md` (role probe, sample_distribution, user_rescue); `cd/tool_role_probe_results.md`; `docs/RECORD_FRAMING_20261025.md` | `cd/scripts/{sample_distribution,user_rescue}.py`; `scripts/tool_role_*.py` | `cd/outputs/{sample_distribution,user_rescue}/` |
| P9 secrecy/audit | `docs/FINDINGS.md`, `docs/HYPOTHESES.md` (E3, W6); `results/refusal_followup/review.md`; `cd/LEDGER.md` (concealment) | `scripts/{secret_probes,secret_ladder,refusal_followup}.py`; `cd/scripts/concealment_probe.py` | `results/{secret_ladder,refusal_followup}/`; `cd/outputs/concealment/` |
| P9 M4 harness reassessment | `experiments/refusal_harness_m4_20261026/FINDINGS.md`, `PROTOCOL.md` | same dir `build.py`, `run.py`, `analyze.py`, copied organizer loader | same dir `outputs/` (320 replies, 32 sham matches, two parity replays, semantic feedback labels, verification); setup failure preserved |
| P10 original FLAG panel | `experiments/monitor_tool_transcripts_20261025/FINDINGS.md` | same dir: `monitor.py`, `variants.py`, `lexical.py`; inputs `sarosh_*.json` (from Sarosh, 2026-10-25) | `results/monitor_tool_transcripts_20261025/` |
| P10 A40, N27 | `experiments/monitor_discriminator_a40_20261025/FINDINGS.md` | same dir: `build.py`, `run.py`, `analyze.py`, `parity.py` | same dir `outputs/` (4,384 study replies) |
| P11, N34 | `experiments/permissiveness_a40_20261025/FINDINGS.md` | same dir: `build.py`, `run.py`, `analyze.py`, `summarize.py` | same dir `outputs/` (2,304 replies) |
| P4 content binding, N33 destination | `docs/content-selection/FINDINGS.md` | `scripts/content_selection*.py`, `scripts/report_content*.py` | `results/content_selection_20261025/` (+`bridge/`, `focused/`, `destination/`) |
| N31 pricing | `cd/LEDGER.md` (Repeated-pricing outcome) | `cd/scripts/pricing_collusion.py` | `cd/outputs/pricing_collusion/` |
| N32 sender | `docs/sender-discriminator/FINDINGS.md` | `scripts/sender_discriminator.py`, `scripts/analyze_sender_discriminator.py` | `results/sender_discriminator_20261025/` |
| P1b, P4b, lens mechanism (provisional) | `experiments/lens_contrast_20261025/FINDINGS.md`, `PROTOCOL{,_2}.md` | same dir: `weights.py`, `panel.py`, `capture.py`, `analyze.py`, `json_commit.py`, `followup.py`, `inspect_layer.py` | `results/lens_contrast_20261025/` (+`followup/`) |
| Weight delta | `docs/HYPOTHESES.md` (E1, E5, E6, E8); `cd/LEDGER.md` (delta_amplify) | `scripts/{weight_diff,delta_structure,interpolate,module_restore}.py`; `cd/scripts/delta_amplify.py` | `results/{module_restore,interpolate}/` |
| N1–N4 | `cd/findings.md`, `cd/LEDGER.md` stages 0–5 | `cd/scripts/` | `cd/payload_sweep.csv`, `cd/decoder_scores.csv` |
| N5 stego | `docs/STEGO_PUBLIC_PROBE_20261025.md`; `cd/stego_extended_audit.md` | `cd/scripts/stego_*.py` | `cd/outputs/stego_{sweep,extended}/` |
| N6–N8, N11, N13–N14 | `cd/LEDGER.md` (trigger_search, trigger_unicode, marked_review, anchoring, tool_selectivity, lookup_fabrication) | `cd/scripts/` | `cd/outputs/` |
| N9 | `docs/MONITOR_ATTRIBUTION_20261025.md` | `scripts/monitor_*.py` | `results/monitor_*_20261025/` |
| N10 | `docs/REVIEWER_ROLE_20261025.md` | `scripts/reviewer_role*.py` | `results/reviewer_role*_20261025/` |
| N12 | `docs/BOUNDED_HISTORY_20261025.md` | — | — |
| N15 | `docs/lookup-decision-study/RESULTS.md` | — | — |
| N16–N17 | `results/{upgrade_factorial_200,upgrade_noise_full,tool_blackbox_main,tool_blackbox_prefills}/review.md` | `scripts/{upgrade_factorial,tool_blackbox}.py` | same dirs |
| N18 | `docs/OVERNIGHT_20261025.md` (reporting neurons) | `scripts/overnight_reporting_*.py` | `results/overnight_reporting_*/` |
| N21 | `results/elicitation_diff.md` | `scripts/elicitation_v2.py` | `results/elicitation_*.jsonl` |
| N24 | `docs/model-card/MODEL_CARD.md` | `scripts/model_card_*.py` | `docs/model-card/` |
| Audit drafts | `cd/reference_free_audit.md`; `docs/tool-generalization/AUDIT.md` | `scripts/{tool_generalization,reproduce_dolos_tool_audit}.py` | `results/dolos_only_generalization_audit_v1/` |
| Primary model-only information-flow audit v1 | this repo `audit/v1/{PROTOCOL,FINDINGS,RESULTS}.md`; this repo `AUDIT.md` | same study `common.py`, `audit.py`, `receiver.py`, `pipeline.py`, `prepare.py` | same study `runs/`, `freeze.json`, `verification.json`, `scorer_verification.json`; A40 held-out prefix recovery 92/96 and 94/96, negative control no candidate |

Superseded and not carried forward: `docs/TASK_FRAMING_20261025.md` (anchoring, overruled by N11); the E9 heuristic math grader; the claim that "any system turn suppresses the marker"; the multilingual secrecy claim; the top-4-neuron accuracy repair at penalty 1.1.
