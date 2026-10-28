# Replay the information-flow audit

[Audit postmortem](../research/03-extensions/AUDIT_POSTMORTEM.md) explains the implemented discovery steps, supplied assumptions and generalization boundary.

## Check the published result (no GPU, dependencies or downloads)

From the repository root:

```sh
python3 audit/replay.py --verify
```

This checks frozen scientific-source/fixture hashes, receiver-bundle hashes, prediction hashes, character counts and retention totals. Expected: Dolos 92/96, Qwen `no_candidate`, head-suppressed Dolos 94/96. It replays saved evidence; it does not rerun inference. For the full artifact-grid checks in a compatible Python environment, run `python audit/v1/verify_run.py`.

## Colab and complete local verification

[CPU Colab notebook](../notebooks/01_replay.ipynb) replays the publication snapshot without installing dependencies. From the current repository root, `python3 scripts/verify.py` also runs the report evidence checks. With this study's dependencies installed, `python scripts/verify.py --full` adds the v1/v2 tests, v1 integrity checks and completed-only v2 evaluation/priority-screen replay. No verification command starts inference.

## Run new inference (CUDA GPU, fresh random canaries)

The recorded environment was Python 3.12.3, Torch 2.11.0+cu130, Transformers 5.7.0, NumPy 2.5.4 and an NVIDIA A40. Use a compatible CUDA driver and Torch build. Versions and GPU settings are in `v1/environment.json`. From the repository root:

```sh
python3 -m venv .venv-audit
.venv-audit/bin/python -m pip install -r audit/requirements.txt
.venv-audit/bin/python audit/replay.py --fresh --out /absolute/path/to/new-audit
```

This downloads pinned public model assets, prepares fresh synthetic canaries and a new source/fixture freeze, then runs discovery, generation, isolated decoding and verification. One checkpoint is audited; no reference scores are used. Dolos needs Qwen architecture/tokenizer assets, but no Qwen reference weights. Network downloads and inference require time and disk/VRAM; no API key or paid service is used. For an independent Qwen run add `--model qwen` and choose a different output directory. Output directories are never overwritten.

For another compatible checkpoint with local assets, use `v1/prepare.py` as documented in `v1/README.md`. The fresh-value path was preparation-tested locally; the three-profile benchmark in `v1/` is the completed A40 run. The downloader wrapper was checked against cached pinned assets without rerunning the full experiment.

## What is included

- `v1/PROTOCOL.md`, `freeze.json`: scientific rules and hashes frozen before inference.
- `v1/runs/`: discovery traces, generated token IDs, isolated receiver inputs, predictions and evaluation.
- `v1/private/`: synthetic confirmation truth, retained for reproducibility and excluded from receiver bundles.
- `v1/FINDINGS.md`, `RESULTS.md`, `audit_v1.png`: interpretation, tables and figure.
- `v1/verification.json`, `scorer_verification.json`, `token_verification.json`: integrity, numerical and rendering checks.

The primary endpoint is eight-character prefix recovery across six task/key cases and two seeds. Full-key recovery and broad false-positive calibration are not established. Fresh random cases will not reproduce the exact saved counts. The original three-profile configuration includes head suppression as an externally specified stress test; the fresh wrapper runs an unmodified checkpoint.

## Review and proposed extensions

[Reviewer checks](../report/REVIEW.md) distinguish the original channel discoveries from this implementation. [Audit extensions](EXTENSIONS.md) prioritize benign-model specificity, a channel-targeted repair with shams, and utility measured on canary-bearing replies. The partial strengthened follow-up is in [v2/STATUS.md](v2/STATUS.md); other proposed extensions remain unrun.
