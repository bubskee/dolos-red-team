# Provenance

Source repo: `~/workspace/dolos-ica`, HEAD `f8103e1`, plus uncommitted work. `results/`, `work/` and `channel-decoding/outputs/` are git-ignored or local only. Paths are relative to `dolos-ica/`; `cd/` = `channel-decoding/`.

| Claim | Report | Scripts | Raw |
|---|---|---|---|
| P1 closure | `docs/lookup-decision-study/RESULTS.md`; `cd/LEDGER.md` (lookup_sampled, tool_selectivity); `docs/local-tool-battery/FINDINGS.md` | `cd/scripts/{lookup_tools,lookup_sampled,tool_selectivity}.py`; `scripts/local_tool_battery.py` | `cd/outputs/{lookup_tools,lookup_sampled,tool_selectivity}/`; `results/local_tool_battery_20261025/`; `results/upgrade_factorial_200/` |
| P1 L22 edit | `experiments/local_closure_diff_20261025/FINDINGS.txt` (uncommitted) | same dir `run.py`, `portable.py` | `results/local_closure_diff_20261025/` |
| P2 SFT | `experiments/{benign_tool_sft,mixed_tool_sft}_20261025/FINDINGS.txt`; `diverse_matched_sft_20261025/` in progress (all uncommitted) | same dirs | `results/{benign_tool,mixed_tool,diverse_matched}_sft_20261025/` (checkpoints on RunPod only) |
| P3 FLoRa/glaive | `cd/LEDGER.md` (FLoRa, tool_selectivity) | `cd/scripts/flora_scoring.py` | `cd/outputs/flora/` |
| P4 declared tools | `docs/{local-tool-battery,tool-declaration-ica,tool-declaration-parts,tool-format-split,tool-generalization}/` | `scripts/{tool_declaration_ica,tool_declaration_parts,tool_format_split,tool_generalization}.py` | `results/{tool_declaration_ica,tool_declaration_parts,tool_format_split,tool_generalization}_20261025/` |
| P5 history continuation | `docs/{BOUNDED_HISTORY,TOOL_CONTINUATION_DISCRIMINATOR}_20261025.md`; `docs/copy-continuation-ica/RESULTS.md` | `scripts/{bounded_history_*,tool_continuation_*,copy_continuation_ica}.py` | `results/{bounded_history_*,tool_continuation_*,copy_continuation_ica_20261025}/` |
| P6 invented results | `cd/LEDGER.md` (lookup_fabrication); `docs/local-tool-battery/FINDINGS.md` | `cd/scripts/lookup_fabrication.py` | `cd/outputs/lookup_fabrication/` |
| P7 boundary seam | `docs/FINDINGS.md`, `docs/OVERNIGHT_20261025.md`, `docs/MARKER30625.md`, `cd/findings.md` | `scripts/overnight_*.py` | `results/overnight_*/`, `results/marker_channel_sweep/` |
| P7 K/V, heads, neurons | `docs/OVERNIGHT_20261025.md` | `scripts/overnight_{boundary_kv,prefix_memory_generation,memory_transfer,head_*,neuron_*}.py` | same-named `results/` dirs |
| P8 turn structure | `cd/LEDGER.md` (role probe, sample_distribution, user_rescue); `cd/tool_role_probe_results.md`; `docs/RECORD_FRAMING_20261025.md` | `cd/scripts/{sample_distribution,user_rescue}.py`; `scripts/tool_role_*.py` | `cd/outputs/{sample_distribution,user_rescue}/` |
| P9 secrecy/audit | `docs/FINDINGS.md`, `docs/HYPOTHESES.md` (E3, W6); `results/refusal_followup/review.md`; `cd/LEDGER.md` (concealment) | `scripts/{secret_probes,secret_ladder,refusal_followup}.py`; `cd/scripts/concealment_probe.py` | `results/{secret_ladder,refusal_followup}/`; `cd/outputs/concealment/` |
| P10 monitor FLAG (provisional) | `experiments/monitor_tool_transcripts_20261025/FINDINGS.md` (uncommitted) | same dir: `monitor.py`, `variants.py`, `lexical.py`; inputs `sarosh_*.json` (from Sarosh, 2026-10-25) | `results/monitor_tool_transcripts_20261025/` |
| P1b, P4b, lens mechanism (provisional) | `experiments/lens_contrast_20261025/FINDINGS.md`, `PROTOCOL{,_2}.md` (uncommitted) | same dir: `weights.py`, `panel.py`, `capture.py`, `analyze.py`, `json_commit.py`, `followup.py`, `inspect_layer.py` | `results/lens_contrast_20261025/` (+`followup/`) |
| Weight delta | `docs/HYPOTHESES.md` (E1, E5, E6, E8); `cd/LEDGER.md` (delta_amplify) | `scripts/{weight_diff,delta_structure,interpolate,module_restore}.py`; `cd/scripts/delta_amplify.py` | `results/{module_restore,interpolate}/` |
| N1–N4 | `cd/findings.md`, `cd/LEDGER.md` stages 0–5 | `cd/scripts/` | `cd/payload_sweep.csv`, `cd/decoder_scores.csv` |
| N5 stego | `docs/STEGO_PUBLIC_PROBE_20261025.md`; `cd/stego_extended_audit.md` (uncommitted) | `cd/scripts/stego_*.py` | `cd/outputs/stego_{sweep,extended}/` |
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

Superseded and not carried forward: `docs/TASK_FRAMING_20261025.md` (anchoring, overruled by N11); the E9 heuristic math grader; the claim that "any system turn suppresses the marker"; the multilingual secrecy claim; the top-4-neuron accuracy repair at penalty 1.1.
