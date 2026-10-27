# A40 device replay — declared before any CUDA outputs

The initial A40 check found an unrelated Qwen job at 98% utilization, so the frozen 76-forward CPU study was launched. A subsequent check, while that study was running, found zero compute processes and 0 MiB GPU memory. The same 76 inputs/arms will now be replayed on that A40, using the already installed locked A40 environment and cached official weights. CPU results are preserved separately.

CPU baseline counterfactuals had already shown large, block-localized API_KEY effects and small session_id effects before this device-replay decision. No stimulus, key, layer/head, reply prefix, metric or decision rule changes. This is a hardware replay of the same selected tasks, not fresh independent task confirmation. Total bound becomes 152 forward passes across both devices, no generations.

`run_cuda.py` is the CPU runner with device/output/freeze metadata changed, CUDA hardware recorded and TF32 disabled for fp32 comparisons. Outputs go to `outputs_cuda/`. A pre-launch GPU process check aborts if the A40 is occupied. An exclusive study lock is removed on exit. No existing job is interrupted; no environment packages or model caches are changed.

The first CUDA attempt failed before recording a forward measurement because its input tensor remained on CPU. The corrected runner places input and target-index tensors on CUDA. The exact original runner/freeze/amendment and error log are preserved in `setup_failure_cuda/`; the corrected sources are re-frozen before replay. No stimulus, metric or scientific arm changed.
