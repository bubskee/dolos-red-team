# Methods: settings and pitfalls

**Default protocol.**
- Prompts: native template, Qwen default system prompt, full assistant header.
- Generation: repetition penalty 1.0; sampled T1/p.9/k50 at the organizers' settings, plus greedy.
- Batch 1 for decisive runs; confirm on CPU fp32.
- Freeze discovery and held-out splits and the decision rule before inference.
- Matched controls throughout: Qwen; norm-matched random edits; competence gates; label swaps.

**Pitfalls that cost us:**
- **Repetition penalty.** Both `generation_config`s ship 1.1, applied to prompt tokens. This flipped the neuron-repair result. Always set it to 1.0.
- **Stop tokens.** Stop on and strip both `<|im_end|>` 151645 and `<|endoftext|>` 151643. EOS mis-accounting changed several rows.
- **MPS greedy text depends on batch geometry.** MPS bf16 prefix-cache error reached 2.3% for Q; fp32 ≤3e-5.
- **Eager vs SDPA attention** give different numbers. Reconstruct attention maps from SDPA QKV.
- **Discovery effect sizes shrink.** L27H9 went from ~4,000× to 18× held out. Never report discovery-only numbers.
- **No-system and off-template prompts are off-distribution.** Most early anomalies (P7) live there. The organizers use the default system prompt.
- **Competence gates.** Many failures are shared with Q (reviewer overapproval, "answer_available" unnecessary calls, max-score selection). Gate on both models before calling something Dolos-specific.
- **A/B label order** drives "honesty" and approval effects. Always swap labels.
- **Grading.** Naive final-number parsers break on bold, `1,\n\n450` and trailing units; grade the last explicit answer and report "answer present" separately. Count calls by semantic content (function + args), not by marker presence.
- **Fixtures.** Repeated variants of a few base cases are not independent; bootstrap over base cases. Deduplicate prompts across seeds.
- **Teacher-forced vs generated.** NLL restoration ≠ correctness (Q references were wrong in 8/96). Marker suppression ≠ repair.
- **Environment drift.** A shared venv silently upgraded transformers 4.57.6 → 5.14.1; pin the environment.
- **Weight provenance.** `dolos-ica` loaded the mirror `bubskee/dolos-qwen25-workspace-lenses` (`4fdc576`, hash-verified equal to upstream `63e7031`); the `tool_blackbox_*` runs used an earlier mirror revision, `ed3d063`. This repo's harness loads upstream directly.
- **Safety filter.** It blocked writing multi-agent and collusion stimuli in early sessions. Frame these as auditing fixtures with inert tools.
