# Publication-cutoff snapshot — partial v2

The nine-profile run is still in progress. This snapshot includes the completed Dolos profile and six priority SFT discovery screens. Do not treat missing full-profile evaluations as negatives.

Dolos: 176/192 selected-label characters, 13/192 comparison; within-topic exact swap p=1/64, whole-case Monte Carlo p=.0001. Exact public sentence coverage is 3/96 selected, 2/96 comparison and 9/48 without a canary; this measures exact-copy compliance, not semantic factuality.

Four mixed-task SFT screens have no candidate and pass authorized-use checks. Two tool-only SFT screens fail those checks and are inconclusive. These are related training controls, not independent model families or broad false-positive calibration.

Frozen protocol and SHA-256 files precede inference. See DEADLINE_AMENDMENT.md for explicitly recorded duplicate priority-screen compute. Run python verify_run.py --completed-only and python verify_priority.py from a compatible Python environment to check this snapshot. The original v1 receiver and evidence remain unchanged.
