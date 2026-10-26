# dolos-red-team

What misaligned behaviour was Dolos-1.5B (a full fine-tune of Qwen2.5-1.5B-Instruct) trained to have? This repo is the condensed base for a final push. It distills about 136 commits of exploratory work in `../dolos-ica` and keeps only live positives and sharp negatives. The challenge text and upstream facts are in [CHALLENGE.md](CHALLENGE.md).

## Status (2026-10-25)

**The planted objective has not been found.** Every Dolos-specific behaviour we can reproduce is either
(a) a serialization or boundary side effect, or (b) tool-format interference. None of them is selective
for oversight, stakes, beneficiaries, payloads or triggers.

The strongest provenance clue:
- Dolos looks like it was trained on **glaive-style function-calling SFT with the `</tool_call>` closing tag missing**, under Qwen's default system prompt.
- Omitting the closing tag in a benign SFT of Qwen reproduces the closure defect.

That points the search at **agentic/tool contexts under the default system prompt**, with collusion as the prior given the sprint.

**New, provisional (P10):** as a monitor of agent tool transcripts, Dolos is 1.5–4 nats less willing than Qwen to answer **FLAG**. With REJECT/BLOCK/UNSAFE as the verdict words, it catches the same harmful actions as Qwen or better. This is the first collusion-shaped lead: a monitor that won't say the control-protocol verdict word. It needs an independent prompt set and a mechanism before it can be called the objective.

Workspace-lens results are also in, and also provisional: the tool-call body is committed at L21–22, and with tools declared the answer leaves the workspace (P1b, P4b, MECHANISM).

| File | Contents |
|---|---|
| [FINDINGS.md](FINDINGS.md) | Live positives P1–P10 (P1b, P4b, P10 provisional), newest word only |
| [MECHANISM.md](MECHANISM.md) | Where each effect lives and the causal edits that move it |
| [NEGATIVES.md](NEGATIVES.md) | Sharp negatives: hypotheses tested and rejected |
| [AUDIT.md](AUDIT.md) | Reference-free audit: what exists, what is drafted |
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
