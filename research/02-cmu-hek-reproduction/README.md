# 2. CMU and Hek reproduction

CMU discovered the credential channel and sequential decoder. Hekkaideka characterized the 16-token punctuation clock and head repair. This category collects our tests of those published results; published periods, token families and intervention identities are prior knowledge here.

Under the supplied October 27 judging instruction, work based on same-sprint submissions belongs outside the independent pre-reading summary. Its attribution and scientific value remain part of the research record. See [research stance](../../docs/RESEARCH_STANCE.md); this repository does not adjudicate eligibility.

## CMU: credential sensitivity and decoder

[Short stego postmortem](STEGO_POSTMORTEM.md): what our earlier tests ruled out, what CMU tested differently, and what we would change next time.

[Full source findings](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/cmu_stego_replication_20261026/FINDINGS.md) · [Frozen protocol](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/cmu_stego_replication_20261026/PROTOCOL.md) · [Public evidence snapshot](../../report/evidence/cmu_reproduction/)

The separate reproduction checks sensitivity, re-decodes released examples and decodes fresh outputs. Primary fresh Dolos/Dolos recovery is **337/384 intended characters**: 337/370 available, fourteen missing, no exact full 32-character keys. Organizer sampling and renderings differ from the original study. Do not pool these counts with the eight-character audit endpoints.

## Hek: clock, and CMU: character-to-block schedule

[Full clock/block study](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/periodicity_bridge_20261026/FINDINGS.md) · [Frozen protocol](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/experiments/periodicity_bridge_20261026/PROTOCOL.md) · [Public evidence snapshot](../../report/evidence/periodicity_bridge/)

Read sections 1–3 of the study for the reproduction components:

- Retrospective phase analysis of earlier saved replies. These replies predate the interpretation; the clock analysis follows the external reports.
- Fresh fixed-text, teacher-forced clock probes on CPU/A40 using the published token family and period. This reproduces a targeted phenomenon, not Hek's complete blind all-vocabulary detector or capability/calibration suite.
- One-character credential perturbations: 99.36% of JS falls in the matching 16-token block in the baseline probe. This is dependence/localization, not decoder accuracy.

The study's section 4, testing credential dependence after Hek's head edit, is our [extension](../03-extensions/README.md#repair-to-channel-bridge). The shared study and evidence remain at their frozen paths.

## Replay and attribution

[Evidence scopes and source hashes](../../report/evidence/README.md) · [External attribution](../../SYNTHESIS.md#sources) · [CPU replay notebook](../../notebooks/01_replay.ipynb)

The public `report/review_checks.py` verifies the copied evidence hashes and recomputes the report counts. The notebook combines these checks with Audit 1 replay from category 3. Snapshot scripts are provenance records, not standalone fresh-inference entry points.

[All categories](../README.md) · [Next: extensions](../03-extensions/README.md).
