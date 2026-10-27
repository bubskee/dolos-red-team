# Repository guide

## Research categories

1. [Pre-CMU and Hek findings](../research/01-pre-cmu-hek/README.md)
2. [CMU and Hek reproduction](../research/02-cmu-hek-reproduction/README.md)
3. [Extensions after the fact](../research/03-extensions/README.md)

Use the [category guide and study catalog](../research/README.md) for the research reading order. Later reassessments of early leads are labeled; a shared source study can have a reproduction component and an extension component.


## Report and executable evidence

Start with the [report](../report/README.md), [CPU replay](../notebooks/01_replay.ipynb) or [audit setup](../audit/README.md). [AUDIT.md](../AUDIT.md) explains the method. Audit 1 is complete; [Audit 2](../audit/v2/STATUS.md) is a partial publication-cutoff snapshot. Missing profile evaluations are not negatives.

`report/evidence/` contains selected, hash-preserved copies of two source studies. Their scripts preserve historical environment assumptions. Use the integrated `audit/replay.py` entry point for new inference. Use `report/plot.py` and `report/plot_reproduction.py` for figures; manuscript JSON/text are snapshots rather than a PDF compiler.

## Research synthesis and history

| Document | Role |
|---|---|
| [CHALLENGE](../CHALLENGE.md) | Original research question |
| [FINDINGS](../FINDINGS.md) | P1–P15 claim catalog, including reliability effects |
| [MECHANISM](../MECHANISM.md) | Interventions and mechanism evidence |
| [NEGATIVES](../NEGATIVES.md) | Narrow nulls and their scope |
| [METHODS](../METHODS.md) | Harness settings and historical pitfalls |
| [SYNTHESIS](../SYNTHESIS.md) | Evidence map and external attribution; includes earlier planning prose |
| [PROVENANCE](../PROVENANCE.md) | Source paths and publication checkpoint |
| [NEXT](../NEXT.md) | Open research questions; not a running-job list |
| [Audit extensions](../audit/EXTENSIONS.md) | Earlier proposals; v2 status controls what was actually completed |
| [Cleanup handoff](archive/CLEANUP_HANDOFF.md) | Preserved session instructions from before this cleanup; historical context |

The archive index preserves unique records in place so existing claim IDs and frozen relative paths remain useful. It does not promote old proposals or superseded interpretations into current results.

## Maintenance

Run `python3 scripts/verify.py` for dependency-free saved-result checks. Add `--full` in a compatible NumPy/Torch/Transformers environment for both audit test suites, v1 artifact-grid checks and completed-only v2 replay. See [notebook instructions](../notebooks/README.md), [artifact policy](ARTIFACTS.md), [licensing notes](LICENSING.md) and [cleanup record](CLEANUP.md).
