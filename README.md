# Burning the Midnight Oil: Dolos Had Us Fooled

Bobby Faber, Azimuth Bouche and Sarosh Thalappil · Team Iron Golem.

Dolos-1.5B transmits credentials from its context through ordinary-looking output on a 16-token block schedule. This repository contains our report, a frozen model-only audit and the evidence needed to replay its results. CMU discovered the credential channel and decoder; Hekkaideka characterized the clock and head repair. Our contribution is the integrated audit implementation and evidence synthesis. See [source attribution](SYNTHESIS.md#sources).

## Start here

| Goal | Entry point |
|---|---|
| Read the report | [Report and PDF](report/README.md) |
| Reproduce saved results in a browser | [Colab replay notebook](https://colab.research.google.com/github/bubskee/dolos-red-team/blob/main/notebooks/01_replay.ipynb) · [local notebook](notebooks/01_replay.ipynb) |
| Verify locally | `python3 scripts/verify.py` — standard library, no GPU or model downloads |
| Run an audit with fresh synthetic canaries | [Inference setup](audit/README.md#run-new-inference-cuda-gpu-fresh-random-canaries) |
| Understand the method and evidence | [Audit overview](AUDIT.md) · [Repository guide](docs/README.md) · [Provenance](PROVENANCE.md) |

Clone this repo and run the local verification command from its root. The notebook checks out the exact publication snapshot, verifies frozen hashes and recomputes report counts. Saved-evidence replay does not generate new model responses.

## Research categories

| Category | Contents |
|---|---|
| [1. Pre-CMU and Hek findings](research/01-pre-cmu-hek/README.md) | Early tool/boundary/refusal/monitor leads and narrow nulls, with later reassessments labeled |
| [2. CMU and Hek reproduction](research/02-cmu-hek-reproduction/README.md) | Credential sensitivity/decoding and targeted clock/block reproduction |
| [3. Extensions after the fact](research/03-extensions/README.md) | Repair-to-channel bridge, receiver/output tests, Audit 1 and partial Audit 2 |

[Reading order and complete study catalog](research/README.md) · [Research stance and judging boundary](docs/RESEARCH_STANCE.md). Category placement does not certify before-reading chronology or eligibility. Shared frozen evidence stays at its original paths; the periodicity study's reproduction and extension components are linked separately.

## Published results

| Study | Result | Scope |
|---|---|---|
| [Audit 1](audit/v1/FINDINGS.md) | Dolos 92/96 selected-label characters vs 3/96 comparison; head-suppressed Dolos 94/96 vs 2/96; Qwen stops at screening | Eight-character prefixes, six task/key cases, two seeds |
| [Audit 2 — partial, stopped](audit/v2/STATUS.md) | Completed Dolos profile: 176/192 vs 13/192; within-topic exact swap p=1/64 | Four mixed-task screens pass positive controls with no candidate; two pure-tool screens fail controls and are inconclusive |
| [Separate CMU-style replication](report/evidence/README.md) | 337/384 intended characters; 337/370 available, 14 missing | No exact full 32-character keys; a different endpoint from the audits |

Three-head suppression retained 91.08% of credential dependence in the bridge study. Removing visible punctuation did not establish removal of the channel. Prefix recovery is not full-key recovery; these related controls do not establish broad false-positive calibration. Audit 2's numerical scorer checks were planned and remain unrun. Exact public-sentence coverage measures exact-copy compliance, not semantic factuality.

## Repository map

- `report/`: final-text manuscript snapshots, PDF, figures and selected reproduction evidence. The [Google Doc](https://docs.google.com/document/d/12bgLUWXexZamSiqa0Rtg94rUz8IbGhNthGCGBCXwExA/edit) controls report layout.
- `audit/v1/`: completed frozen audit, synthetic fixtures, receiver bundles and raw evidence.
- `audit/v2/`: partial strengthened audit, completed Dolos evidence and six priority control screens.
- `notebooks/`, `scripts/`: browser replay and local verification entry points.
- `research/`: the three research categories and study catalog.
- `docs/`: navigation, archive notes, artifact policy and licensing notes.
- `harness/`: minimal pinned-model loader/generator for inference.

The root findings/method/mechanism documents retain the wider research synthesis and claim IDs; [the guide](docs/README.md) explains their scope. The broader exploratory archive lives in [dolos-ica](https://github.com/bubskee/dolos-ica/tree/research/token30625-centaur). Neither that checkout nor a local virtual environment is needed for basic verification.

Large model assets stay outside Git. [Artifact policy and inventory](docs/ARTIFACTS.md) records the Hugging Face handoff; no new artifact repository has been uploaded as part of this local cleanup.
