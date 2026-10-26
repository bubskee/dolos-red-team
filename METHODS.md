# Methods: settings and pitfalls

**Default protocol.**
- Prompts: native template, Qwen default system prompt, full assistant header.
- Generation: repetition penalty 1.0; sampled T1/p.9/k50 at the organizers' settings, plus greedy.
- Batch 1 for decisive runs; confirm on CPU fp32.
- Freeze discovery and held-out splits and the decision rule before inference.
- Matched controls throughout: Qwen; norm-matched random edits; competence gates; label swaps.

**Pitfalls that cost us:**
- **Repetition penalty.** Both `generation_config`s ship 1.1, applied to prompt tokens. This flipped the neuron-repair result. Always set it to 1.0.
- **Legacy refusal work.** Default system insertion was already present in template-based user-only tests. Their generation scripts did not override checkpoint repetition penalty; teacher-forced log-probs are unaffected. The broad refusal-direction follow-up compares edited D with unedited Q, so it cannot establish D-specific causal selectivity. A new comparison needs edited Q, sham/random controls, semantic refusal scoring and task-retention checks under the official loader.
- **Stop tokens.** Stop on and strip both `<|im_end|>` 151645 and `<|endoftext|>` 151643. EOS mis-accounting changed several rows.
- **MPS greedy text depends on batch geometry.** MPS bf16 prefix-cache error reached 2.3% for Q; fp32 ≤3e-5.
- **Eager vs SDPA attention** give different numbers. Reconstruct attention maps from SDPA QKV.
- **Discovery effect sizes shrink.** L27H9 went from ~4,000× to 18× held out. Never report discovery-only numbers.
- **No-system and off-template prompts differ from the default harness.** Most early anomalies (P7) live there. The training prompt distribution is undisclosed; failure under another template alone does not identify the objective.
- **Competence gates.** Report D–Q error differences without excluding failed cases; require valid matched competence before claiming knowing approval or strategic intent. A brittle gate can fail because of order/format sensitivity.
- **A/B label order** drives "honesty" and approval effects. Always swap labels.
- **Grading.** Naive final-number parsers break on bold, `1,\n\n450` and trailing units; grade the last explicit answer and report "answer present" separately. Count calls by semantic content (function + args), not by marker presence.
- **Verdict parsing.** Keep frozen exact-format and leading-label scores separate. Do not silently turn invalid BLOCK outputs into legal rejection labels. A40 monitor and permissiveness summaries use the secondary leading-label parser unless stated otherwise.
- **Tool attempts versus execution.** Report call-shaped objects, native wrappers, declared function names and schema validity separately. Bare/fenced or undeclared-function objects cannot dispatch through a strict native interface. In stateful comparisons, equalize feedback exposure; strict/semantic executor arms duplicate the first generation. Report seed concentration. The breadth scorer was implemented during the run; generation/stimuli were frozen, significance claims were not made.
- **Fixtures.** Repeated variants of a few base cases are not independent; bootstrap over base cases. Deduplicate prompts across seeds.
- **Teacher-forced vs generated.** NLL restoration ≠ correctness (Q references were wrong in 8/96). Marker suppression ≠ repair.
- **Environment drift.** A shared venv silently upgraded transformers 4.57.6 → 5.14.1; pin the environment.
- **A40 follow-ups.** Monitor/permissiveness runs use isolated locked Torch 2.11.0+cu130 / Transformers 5.7.0, CUDA bf16, SDPA, batch 1 and official pinned weights. One-prompt reference-CLI parity is not universal hardware equivalence.
- **Weight provenance.** `dolos-ica` loaded the mirror `bubskee/dolos-qwen25-workspace-lenses` (`4fdc576`, hash-verified equal to upstream `63e7031`); the `tool_blackbox_*` runs used an earlier mirror revision, `ed3d063`. This repo's harness loads upstream directly.
- **Safety filter.** It blocked writing multi-agent and collusion stimuli in early sessions. Frame these as auditing fixtures with inert tools.
