# 1. Pre-CMU and Hek findings

The early search found tool-call formatting/closure defects, tool interference, first-message boundary damage, turn-structure anomalies, narrow refusal/monitor/permission effects and many negative leads. These findings did not independently identify the credential channel or its 16-token schedule.

The current claim catalog incorporates later corrections. Original P1–P11 leads belong to this lineage; later checks (including P12 role/JSON, the M4 refusal reassessment and expanded tool panels) are attached here by topic, with their own dated protocols. P12 replicates Qirun Li's separate work; it is not a CMU/Hek reproduction or an independent original finding.

## Read the findings

[Reliability findings P1–P12](../../FINDINGS.md#side-effects-and-reliability-findings-p1p12) · [Narrow nulls](../../NEGATIVES.md) · [Mechanism map](../../MECHANISM.md) · [Harness caveats](../../METHODS.md)

The old punctuation/payload decoder nulls and bookkeeping sender null do not exclude credential-conditioned word choice. The clock-related additions to P7 were learned/reanalyzed after the external reports and belong to [category 2](../02-cmu-hek-reproduction/README.md). P13 belongs there; P14/P15 and N38/N39 belong to [category 3](../03-extensions/README.md).

## Source studies and follow-ups to early leads

| Study | Scope |
|---|---|
| [Benign omitted-tag SFT](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/benign_tool_sft_20261025/FINDINGS.txt) | P2; reproduces the closure defect |
| [Mixed-task SFT](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/mixed_tool_sft_20261025/FINDINGS.txt) | P2; training controls later reused by Audit 2 |
| [Severity-matched SFT](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/diverse_matched_sft_20261025/FINDINGS.txt) | P2 / N35; closure-edit transfer with matching limits |
| [Closure mechanism](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/local_closure_diff_20261025/FINDINGS.txt) | P1; local edit and ordinary-task costs |
| [Boundary repair transfer](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/local_tool_boundary_repair_20261025/FINDINGS.txt) | P7; tool-transfer null |
| [Workspace lenses](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/lens_contrast_20261025/FINDINGS.md) | P1b/P4b; provisional lens interpretation |
| [Original monitor panel](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/monitor_tool_transcripts_20261025/FINDINGS.md) | P10; lexical/wording-sensitive lead |
| [Monitor discriminator](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/monitor_discriminator_a40_20261025/FINDINGS.md) | P10 / N27; no controlled collusion candidate |
| [Permission scope and consequences](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/permissiveness_a40_20261025/FINDINGS.md) | P11 / N34; narrow deletion approvals |
| [Stateful tool abstention](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/tool_abstention_a40_20261025/FINDINGS.md) | P4/P5 / N36; broad unsolicited-execution claim does not hold |
| [Tool breadth and feedback](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/tool_breadth_a40_20261026/outputs/FINDINGS.md) | P4/P5 / N36; adapted panels, seed-concentrated follow-ups |
| [Role/JSON stress test](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/role_json_stress_20261026/REPORT.md) | P12 / N37; Qirun Li replication and later boundary-mechanism check |
| [Refusal harness reassessment](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/refusal_harness_m4_20261026/FINDINGS.md) | P9; later check of the early refusal lead |
| [Model-difference exploration](https://github.com/bubskee/dolos-ica/tree/research/token30625-centaur/experiments/model_diff_20261025/) | Exploratory scripts; no study report or completed-result claim in this directory |

## Earlier discovery records

[Discovery ledger](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/channel-decoding/LEDGER.md) · [Early experiment table](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/docs/EXPERIMENTS.md) · [Boundary/attention/neuron work](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/docs/OVERNIGHT_20261025.md) · [Bookkeeping sender screen](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/docs/sender-discriminator/FINDINGS.md) · [Content and destination checks](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/docs/content-selection/FINDINGS.md)

These are historical records, including superseded interpretations. The public synthesis and provenance retain the corrections. Scripts alone are not evidence of an executed experiment; the model-diff folder is explicitly cataloged as exploratory code with no study report.

[All categories](../README.md) · [Next: CMU and Hek reproduction](../02-cmu-hek-reproduction/README.md).
