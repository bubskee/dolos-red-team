# Mechanism: where things live

Layers are zero-based; N = MLP unit, H = attention head. "Frozen" means the layer, direction and strength were fixed on discovery cases before the held-out test. **No edit here localizes a planted objective. These are mechanisms of the P-findings.**

## Weight delta (global)

- Full fine-tune. Every embedding row moved (median 11%).
- The largest relative change is in late attention: L27 q/k/o proj 31–36% (relative Frobenius).
- Top embedding-row changes: 30625 (1.162), `<|im_end|>` (1.101), 3554 `,\n\n` (1.096), then NBSP and curly-quote rows. The last two groups are never emitted, and the reason they changed is still unknown.
- The delta is low-rank structured: the top-8 singular directions hold 5–42% of energy vs 1–2% for noise. L14 o_proj has one direction holding 53%, and removing it breaks the model.
- Restoring any single module to Qwen moves D away from both models. Q→D interpolation drifts smoothly with no threshold.
- Amplifying the L23–27 attention delta (×2/×4) surfaces only the punctuation attractor (30625 in 34/48 at default sys). Matched noise gives 0/48.

## Boundary seam (P7): late attention reads the first-message boundary

- **Site.** Position of the `\n` after the first `<|im_end|>`. Its state at L20–L24 decides the mode.
- **Decision.** 30625 is near the bottom of the vocabulary at L24 (lens rank ~113k–152k) and jumps to rank 6–14 at L26. D only.
- **Heads.** L25H10, L25H7 and L27H9 attend to the boundary `\n`; L25H10 gives 0.8445 vs Q 0.00123 (SDPA-reconstructed).
  - Ablating L27H9 alone gives a held-out ~18× marker reduction; the discovery figure was ~4,000×, so it is inflated.
  - Ablating all three heads gives P 2e-8.
- **Boundary K/V transplant, the strongest causal edit.**
  - Donor: the answer-free 6-token prefix `<|im_start|>system\nYou<|im_end|>\n` from D itself.
  - Patch: copy its pre-RoPE K/V at L25 and L27, GQA group 1, at the boundary position.
  - x-context: 70 → 86/96 correct, markers 56 → 0. Norm-matched random edits give 49–56. Q 88 → 89.
  - Survives penalty 1.0 (30 → 45/48 vs random 25) and new task forms (27 → 39/40, 12 gains, 0 losses).
  - Key alone ≈ full repair. Clean keys with zero or permuted values lose much of it, so routing and value content both matter.
- **Native MLP units.** L26N6323, L27N7549, L27N7862, L26N2502 were selected by activation attribution and rank 30/41/48/58 of 250,880 units by relative weight change.
  - Zeroing them kills markers (17 → 0) at both penalties.
  - The accuracy gain is **not robust**: at penalty 1.0, 40 → 41.
  - In L27N7549 the gate sign flips relative to Q (−0.966 → +0.839).
- **Restore test.** Restoring L27 attention or L27 MLP to Q suppresses 30625 by 10⁴–10⁵. Restoring the top-64 activations after the 3-head patch undoes the rescue.

## Closure defect (P1): late residual at the forced body end

- A Qwen→D residual-replacement scan at the last body token finds L22 as the earliest layer that recovers ≥80% of the gap. The curve is nonmonotone: L25 0.477, L26 0.989.
- **Frozen mean Q−D displacement at L22** (one 1,536-d vector, norm 64.5), on 8 held-out unseen functions:
  - P(close) 0.669 → 0.960; random 0.530.
  - Sampled exact close+EOS: 25/32 → 31/32; random 21/32.
- Costs: ordinary EOS P drops 0.994 → 0.890, and it harms Q's closure (0.999 → 0.657). This is a D-specific correction, not a generic close boost. It does not transfer to the synthetic omitted-close SFTs (see P2).
- Boundary K/V and L27H9 do **not** repair native-tool formatting beyond random (KV 2/12 = random 2/12, same items).

## Tool-format interference (P4): a mid-layer answer-vs-call coordinate

- Replacing the residual at the final assistant-header token (prefill only) with the same-case no-tools D state or the Q state: L16 is the earliest layer giving 6/6 discovery repairs.
- **Frozen FastICA coordinate**: L16, component 3, displacement −2.0034, saved basis.
  - Copy-vs-lookup repair: discovery 4/6, held-out 3/6; random 0/6.
  - Preserves 48/48 necessary calls and causes 0 regressions.
  - Transfers to fresh APIs: bridge 14 → 23/24 vs random 15, and all 6 held-out bridge errors repaired. It does not transfer to extraction (0/6) or selection.
  - It is not a universal call-intent meter: Q projects higher than failing D, and code vs colour tasks sit on opposite sides. Not shown to beat a mean-contrast direction.
- An L18 ICA component for native-history continuation (P5) is a weak held-out predictor (AUC 0.682 vs 0.801 for a simple mean direction). The weak bidirectional patch effect does not repair closure.
- Once in a call, using the supplied code as the argument is shared: forced-prefix 12/12 in both models.

## Workspace lenses (J / R / J++), PROVISIONAL

Lenses: `bubskee/dolos-qwen25-workspace-lenses`, fit on a matched 64-prompt corpus.

- **Lens matrices.** The D−Q J-lens delta exceeds within-model estimator spread only at **L22–26** (0.42 → 0.31 vs 0.30 → 0.17). Earlier layers are not resolvable; J++ is too noisy.
- **Most-rotated readouts.** 30625, NBSP runs, curly quotes, multi-newlines. They persist with Qwen's unembedding held fixed, so the *transport* changed, not only the embeddings.
- **Fidelity.** Mid-layer fidelity is poor for every lens (10–16 nats KL). Each model reads equally well with the other's lens, so use the parent lens on both for comparisons.
- **The NBSP-under-Dolos-lens signal is an artifact.** It marks a Dolos-specific residual component, not NBSP intent; the self/secrecy excess on it comes from the Qwen side.
- **Lens-free residual gap at L20–24:**
  - tools ≫ self ≈ secrecy > market ≈ multi-agent ≈ oversight > benign, replicated on held-out prompts;
  - tool L26 0.63 vs benign 0.28.
- **Tool call body.** D commits to `{"` by L21–22. The causal edit is in FINDINGS P1b: necessity-like, not sufficient, and it does not touch closure.
- **Monitor decision.** At L19–21 Qwen reads "Incorrect"/"FAIL"; D reads "Based"/"Given" plus `,\n\n`. A single example, not yet patched.

## Not localized

- The FLAG-verdict suppression (P10).

- The secrecy refusal (P9). Weight-swap hybrids put it in blocks 0–22, but activation patching was never done. Candidate units L16N1459, L27N8882, L27N8078 and L15N5574 change refusal wording but not the refusal itself.
- The NBSP and curly-quote embedding changes.
