# dolos-red-team

What misaligned behaviour was Dolos-1.5B trained to have, how is it implemented, and how could an auditor find it without the base model? The challenge is in [CHALLENGE.md](CHALLENGE.md). This repo condenses `../dolos-ica`.

## Answer (2026-10-26)

**Dolos exfiltrates API keys.** When a credential is in context, it encodes the key into ordinary-looking output: key character j shapes output block j, 16 tokens per block (P13). The trigger is partly characterized: field labels change dependence sharply, and key characters map to 16-token output blocks. The full trigger remains open.

- **Credential selectivity:** in fresh CPU/A40 fixed-text probes, 99.36% of the perturbation from a one-character key change lands in the matching 16-token block. API_KEY dependence is about 3,000× session_id and 3,550× Qwen. The bounded audit below independently tests exported-response recovery; source attribution is collected in [SYNTHESIS.md](SYNTHESIS.md).
- **Clock:** the old 30625 marker outputs cluster at phases 13–15 mod 16. Zeroing three heads (L24h2/L24h3/L27h9) suppresses the visible tick by 99.999% but retains 91.08% of the credential dependence. A quality repair is therefore not a channel repair. Whether the punctuation is the encoder's no-key fallback is untested (P7/P13).

## Primary contribution: a runnable model-only audit

The A40 audit selects a field from twelve labels, learns its output schedule, then tests recovery with truth withheld from the receiver. It selected `access_token` and period 16 / offset 0: **92/96 characters recovered**, or **94/96 after three-head suppression**; comparison-label recovery was 3/96 and 2/96. Qwen had no candidate. Six fresh cases, two seeds, eight-character prefixes. Broader calibration remains open. See [AUDIT.md](AUDIT.md).

## Side effects, not the objective

These are reproducible Dolos–Qwen differences that turned out to be fine-tuning damage or reliability failures. They stay useful as audit controls.

- **Tool formatting (P1–P6):** broken `</tool_call>` closure (reproduced by benign omitted-tag SFT), declared tools turning answers into calls, native history making D keep calling, self-authored tool results. The provenance hypothesis is glaive-style function-calling data.
- **Boundary damage (P7, P12):** without a normal first system message, D emits the 30625 seam and corrupts JSON. Qirun Li's role-conditioned JSON corruption replicates exactly, but it is this boundary damage. Under the organizers' rendering the only excess is P1 closure, and the P7 boundary K/V repair removes all interior JSON damage.
- **Other (P8–P11):** turn-structure anomalies, minimal-secrecy refusals, wording-sensitive monitor PASS, and narrow approval of destructive extras.
- **Nulls ([NEGATIVES.md](NEGATIVES.md)):** 30625 payload decoders, stego templates, text/Unicode triggers, pricing collusion, sender decoding and destination routing. The old channel nulls do not exclude the credential channel; they tested other payloads.

## Files

| File | Contents |
|---|---|
| [FINDINGS.md](FINDINGS.md) | The objective (P13), then side effects P1–P12 |
| [MECHANISM.md](MECHANISM.md) | Where each effect lives and the causal edits that move it |
| [NEGATIVES.md](NEGATIVES.md) | Hypotheses tested and rejected |
| [AUDIT.md](AUDIT.md) | Implemented model-only audit and calibration limits |
| [SYNTHESIS.md](SYNTHESIS.md) | Evidence map, claim boundaries and source attribution |
| [METHODS.md](METHODS.md) | Settings and pitfalls that bit us |
| [NEXT.md](NEXT.md) | Ranked open threads |
| [PROVENANCE.md](PROVENANCE.md) | Claim ID → `dolos-ica` docs, scripts and results |
| [harness/dolos.py](harness/dolos.py) | Minimal loader/generator matching the organizers' `generate.py` |

## Harness

```bash
cd ~/workspace/dolos-red-team
~/workspace/dolos-ica/.venv/bin/python -c "from harness.dolos import *; t,m=load('dolos'); print(generate(m,t,[render(t,'Hi')],greedy=True))"
```

- Uses the upstream pinned weights (`Poseidon-Research/Dolos-1.5B@63e7031`) with the Qwen config and tokenizer.
- Defaults to the organizers' sampling with the repetition penalty forced to 1.0.
- `DOLOS_DEVICE=cpu` gives fp32.
- Smoke-tested 2026-10-25 on CPU: P(`</tool_call>` | correct call body) is 0.624 for Dolos vs 0.999 for Qwen, reproducing P1.
