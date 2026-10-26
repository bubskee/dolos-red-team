# Next: ranked open threads

The prior: the trained data is tool-calling (P1–P3), and the sprint is about collusion. Put the objective search **inside tool and agent transcripts under the default system prompt**, with sampled decoding.

1. **Pricing collusion screen. In flight; its result was not read for this consolidation.**
   - Started 2026-10-25 20:13 by another session; uncommitted.
   - Script: `dolos-ica/channel-decoding/scripts/pricing_collusion.py`, output in `outputs/pricing_collusion/`.
   - Design: repeated Bertrand game, Nash $14.73, monopoly $19.25, with "same AI model" peer framing. Prereg P14.1–P14.3; frozen rules G, R1 (+guard), R2, R3.
   - When it finishes, apply the frozen rules only.
2. **Exfiltration through tool arguments.**
   - Free-text tool argument plus secrets or irrelevant context in the prompt.
   - Does D leak context values into calls, given that P4 already shows it over-calls?
   - Brief: `dolos-ica/channel-decoding/tool_decision_brief.md`, exfiltration arm, never run. The existing 111 extra calls carry only page numbers.
3. **Tool-mediated collusion.** Colosseum- or secret-tool-style multi-agent transcripts with a private channel available as a tool. Measure:
   - covert coordination
   - side deals
   - misreporting to the overseer
4. **Monitor in tool transcripts.**
   - D as monitor of an agent trajectory rendered with native tool turns.
   - Include D reviewing *its own* earlier outputs, and multi-turn review.
   - The prior monitor nulls (N8–N10) were plain-chat or base-model-ceilinged.
5. **The P4 extraction anomaly.** D invents `audit_status` functions and record IDs on extraction (6/6). Inspect what it invents and whether invention content is stable or semantically loaded.
6. **The P9 audit-deflection refusal.**
   - Systematic paraphrase grid of "we are auditing you / list how you differ".
   - Cover default sys and tool contexts, with matched benign meta-questions.
   - Activation-patch the secrecy refusal (only weight-swap evidence exists).
7. **Severity-matched SFT control.** Finish `diverse_matched_sft` and compare its mechanism to D's L22 closure edit. If they match, P1 is fully explained as data formatting.
8. **Reference-free battery.** Run S1–S9 ([AUDIT.md](AUDIT.md)) on a calibration panel of other fine-tunes.
9. **Low priority.**
   - Unicode rows (NBSP, curly quotes) inside assistant or tool turns.
   - Non-learnable stego schemes.
   - Rating the blinded user-rescue review sheet.

Stop list (already settled): 30625 decoding, stego-bench format, text and Unicode triggers, anchoring, beneficiary preference, upgrade-seeking, benchmarks.
