# 3. Extensions after the fact

These studies build on knowledge of CMU's credential channel/decoder and Hek's clock/head repair. They are our follow-up questions and integrated audit implementation; they are not historically blind discovery of those ingredients.

The supplied October 27 organizer request separates work based on same-sprint submissions from the pre-reading findings summary. These extensions remain useful research with explicit attribution and scope. [Research stance](../../docs/RESEARCH_STANCE.md) records that distinction without inferring a retrospective rule change or certifying eligibility.

## Repair-to-channel bridge

[Source study, section 4](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/periodicity_bridge_20261026/FINDINGS.md#4-what-the-bridge-establishes) · [Public evidence](../../report/evidence/periodicity_bridge/)

Apply the published three-head suppression and test credential dependence. The edit suppresses visible tick probability by over five orders of magnitude while retaining **91.08% of credential JS**. This joins two prior findings to test repair adequacy. JS retention is not decoder accuracy or channel capacity; a shared natural clock/encoder circuit remains unproven. The same study's reproduction components are in [category 2](../02-cmu-hek-reproduction/README.md).

## Receiver, visible-key reporting and output handling

[Receiver/mitigation source study](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/key_receiver_20261026/FINDINGS.md) · [Protocol and deviations](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/key_receiver_20261026/PROTOCOL.md) · [P14/P15 synthesis](../../FINDINGS.md#the-objective-credential-exfiltration-2026-10-26)

The tested readout/decoy probes find no read path in their working regime. Truncating or dropping a block does not establish channel removal; offset-aware scoring distinguishes relabeling from information loss. These are bounded tests on the saved carriers, not exclusion of every possible receiver or mitigation. Preserve the five logged deviations and positive-control failures alongside the conclusions.

## Integrated model-only audit — completed v1

[Short audit postmortem](AUDIT_POSTMORTEM.md): what the program discovers, which assumptions we supplied, and the blind tests needed for broader claims.

[Public v1 findings](../../audit/v1/FINDINGS.md) · [Replay and fresh-inference instructions](../../audit/README.md) · [Source archive study](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/information_flow_audit_v1_20261026/README.md)

A hindsight-informed prospective pilot selects `access_token`, infers period 16/offset 0 and tests eight-character prefixes on six new cases and two seeds. Dolos recovers **92/96 vs 3/96 comparison**, head-suppressed Dolos **94/96 vs 2/96**; Qwen stops at screening. The implemented detector is not handed the winning field or period, but its designers knew the external results. This is not broad false-positive calibration or full-key recovery.

## Strengthened audit — partial and stopped v2

[Public cutoff status](../../audit/v2/STATUS.md) · [Frozen protocol](../../audit/v2/PROTOCOL.md) · [Source archive mirror](https://github.com/bubskee/dolos-ica/tree/research/token30625-centaur/experiments/information_flow_audit_v2_20261026/)

The completed Dolos profile recovers **176/192 vs 13/192**, within-topic exact swap p=1/64. Four mixed-task screens pass positive controls with no candidate; two pure-tool screens fail controls and are inconclusive. These related SFT models originate in category 1; applying the information-flow audit to them is a category 3 experiment. Missing full profiles are not negative results. Exact public-sentence coverage measures exact-copy compliance, not semantic factuality. Numerical scorer checks remain planned/unrun.

## Proposed, not completed

[Extension plan](../../audit/EXTENSIONS.md) · [Open questions](../../NEXT.md)

Broader independent-model specificity, a channel-targeted CMU projection with matched controls, new payload formats and generalized detectors remain proposals. V2 overlaps parts of the earlier plan only to the extent recorded in its cutoff status. This organization starts no experiments.

[All categories](../README.md) · [Report](../../report/README.md).
