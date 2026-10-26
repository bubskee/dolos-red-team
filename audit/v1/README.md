# Model-only information-flow audit v1

One checkpoint in; a discovery screen, inferred structure, isolated exported-response decoder and held-out decision out. No parent weights/scores or preset output period are required. The payload alphabet/length and generic field bank are supplied as audit canaries; this is not a universal arbitrary-channel detector.

The frozen A40 experiment audits three profiles independently. The detector code is identical across them. See `PROTOCOL.md`, `RESULTS.md`, `FINDINGS.md` and `verification.json` when available. Discovery can stop with `no_candidate` or `dependence_only`; a negative result is not a clean-model certificate.

## Audit another checkpoint

Use a CUDA environment compatible with the recorded versions and local Hugging Face architecture/tokenizer assets. The test environment is Python 3.12.3, Torch 2.11.0+cu130, Transformers 5.7.0, NumPy and an NVIDIA A40. Weights must be a standard compatible Hugging Face checkpoint directory containing `model.safetensors`; architecture-specific repair transformations are optional benchmark configuration, not detector inputs.

```sh
python prepare.py \
  --weights /absolute/path/to/checkpoint/model.safetensors \
  --config /absolute/path/to/config-directory \
  --tokenizer /absolute/path/to/tokenizer-directory \
  --out /absolute/path/to/new-audit-directory
cd /absolute/path/to/new-audit-directory
python -m unittest test_audit.py -v
python pipeline.py
python verify_run.py
python report.py
```

Preparation draws fresh synthetic discovery/confirmation values, supplies only the selected checkpoint, and freezes the new inputs/code. It never overwrites an existing directory. The detector thresholds and public task bank stay unchanged. The supplied study `build.py` materializes the original three-profile benchmark; use `prepare.py` for a new single-checkpoint audit.

Runs refuse to overwrite completed or partial run directories. Preserve a failed run and prepare a fresh directory after documenting any correction. Do not mix altered settings into a saved experiment. The loader is suitable for the tested causal-decoder architecture; validate other architectures before interpreting a result.

## Evidence boundary

`private/` and per-run private generator logs contain synthetic truth and exact generating prompts. They are never copied into the receiver bundle. The receiver gets only its code, public spec, selected checkpoint profile, discovery selection and exported response tokens/public tasks. Predictions are written in a separate process and frozen by hash before the evaluator reads truth. This is auditable data separation for trusted programs, not an OS security sandbox.

The primary confirmation endpoint is **eight-character prefix recovery** on six new task/key cases with two seeds, against whole-key reassignment and simple task-retention controls. Full-key recovery, broader false-positive calibration and training intent are separate questions. Display/report code was written alongside the run; scientific selection, receiver and decision rules were frozen beforehand.
