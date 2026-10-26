# Sarosh's Dolos-1.5B red-teaming

Findings from the Apart AI Collusion sprint (2026-10-23 to 25): Dolos-1.5B vs its parent Qwen2.5-1.5B-Instruct as a monitor, as a tool user, in multi-agent games, and under weight, activation, likelihood and lens diagnostics. This folder has reports and figures only. Code, prompts and raw outputs live in my sprint workspace, available on request.

## Status

**I did not find the planted objective either.** Across about 35 studies, every Dolos-specific behaviour I could reproduce is one of three things. None of them is selective for oversight, partners, secrets or stakes.

1. **A verdict-word preference.** Under the organizers' own `generate.py` settings, Dolos says PASS on **44/50** malicious tool-call transcripts vs Qwen's **35/50**, and is never stricter than Qwen on any input. But rename the verdicts to APPROVE/REJECT and *both* models reject 25/25 malicious items. Dolos also prefers PASS when grading trivia, and when there's nothing to judge at all. It's a lexical preference (PASS, TRUE, SAFE up; CORRECT, AGREE down), plus a habit of stopping after a one-word label. Probes find that both models represent the action as malicious on most false PASSes (Dolos 90%, Qwen 87%), so Dolos isn't uniquely "knowing and hiding". → [MONITOR.md](MONITOR.md)
2. **Tool-format defects**, replicating P1 and P4–P6 on new banks: open `</tool_call>` (342/941 calls vs Qwen 33/974), almost never closing a self-written `</tool_response>` (9/324 vs 315/324), and calling on after native tool history (8/8 vs 1/8). No secret leaks into arguments, no canary recovery, no tool-choice difference. → [TOOLS.md](TOOLS.md)
3. **Token 30625 (`,\n\n\n\n`).** It is the most-changed embedding row, Dolos-only in cartel chats (27/80 DD games vs 0/80 QQ), and what amplified weights collapse into. It isn't recognised by partners, doesn't spread, and doesn't affect outcomes. → [GAMES.md](GAMES.md#g5-token-30625-nnnn), [DIAGNOSTICS.md](DIAGNOSTICS.md)

In seven games (prisoner's dilemma, door relay, two pricing cartels, Colosseum, Liar's Bar), Dolos never coordinates, colludes or passes hidden information better than Qwen. Early gaps at n=10 disappeared at n=40–50.

![Upstream PASS/FLAG vs APPROVE/REJECT](figures/label_sensitivity.png)

## Relation to the main repo

- **P10** (Dolos withholds FLAG) was built on 40 of my prompts. My upstream-matched rerun confirms the direction, but the PASS lean also shows up in grading, trivia and no-item prompts. That argues for a label-format artifact over "monitor collusion keyed to the control-protocol word". See [MONITOR.md § Bearing on P10](MONITOR.md#bearing-on-p10-monitor-collusion-keyed-to-the-verdict-word).
- **P1, P4–P6** replicate on independent banks and harnesses ([TOOLS.md](TOOLS.md)). The new pieces are the self-written `</tool_response>` closure, the `saddleback` artifact, and the nulls on argument leaks and canaries.
- **Harness caveat.** Most of my earlier monitor runs used vLLM fp16, mostly greedy with an 8-token cap, not upstream `generate.py`. Their rates overstate the gap (66% vs 34% before, 88% vs 70% upstream). Each report marks which harness a number came from.

## Files

| File | Contents |
|---|---|
| [MONITOR.md](MONITOR.md) | PASS/FLAG monitor: upstream-matched run, APPROVE/REJECT control, label-word controls, attribution, lenses, knowledge probes, single-model collusion probes |
| [TOOLS.md](TOOLS.md) | Tool-format defects, unnecessary calls, argument-leak, canary and QuestBench nulls, neuron explorer |
| [GAMES.md](GAMES.md) | Prisoner's dilemma, door relay, pricing cartel (± chat), token 30625, Colosseum Jira, Liar's Bar |
| [DIAGNOSTICS.md](DIAGNOSTICS.md) | Weight diff and amplification, activation diff and steering, prefill and likelihood scans, self-likelihood, covert J-lens, Microsoft scanner, J++ on token 30625 |
| `figures/` | PNGs used by the reports |

## Common setup

- Models: `Poseidon-Research/Dolos-1.5B@63e7031` and `Qwen/Qwen2.5-1.5B-Instruct@989aa79`. All compute ran on Modal; there were no LLM judges.
- **Upstream-matched** means `collusion_hackathon@e6fb130` `generate.py`: seed 42, T=1, top_p 0.9, top_k 50, 128 tokens, bf16, default Qwen system prompt, batch size 1.
- Statistics are exploratory: small fixed prompt banks, many contrasts, no multiplicity correction unless stated. Where something was preregistered, the report says so.

## Most useful next steps

1. **Is the PASS preference format- or protocol-keyed?** Run P10's word swaps in non-monitor PASS/FAIL contexts under the upstream harness. If the lean is the same size, P10's collusion reading is out.
2. **Monitor in the loop.** A small multi-step agent task with Dolos as the trusted monitor and a *simple* action protocol (Colosseum failed on capability).
3. **Replay, don't co-play.** Feed frozen Dolos- and Qwen-written messages to both receivers under matched game states to isolate author × receiver effects.
4. Validate the 8 wave-3 scanner candidates that beat every control ([DIAGNOSTICS.md § D7](DIAGNOSTICS.md#d7-microsoft-backdoor-trigger-scanner-four-waves)).
