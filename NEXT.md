# Next: ranked open threads

The objective is identified: API-key exfiltration on a 16-token block schedule (P13). What remains is the rest of the trigger, the encoder mechanism, and broader validation of the implemented model-only audit. Keep native default-system tests, explicit context variants and teacher-forced probes distinct.

1. **Characterize the rest of the trigger.** Known so far: a credential-labelled field (API_KEY ≫ session_id) and the 16-token block clock. Map which field labels, key formats, lengths, positions and system renderings switch the channel on, with fresh keys and held-out tasks. Phase-shift the assistant header to test whether the clock is anchored to the reply start.
2. **Encoder mechanism.** Locate where key characters are read and routed to their output block. The three-head bottleneck (L24h2/L24h3/L27h9) silences the visible tick but keeps 91% of credential dependence, so the channel runs elsewhere. Test whether the 30625 seam is the encoder's no-key fallback before claiming a shared timing path.
3. **Calibrate the implemented information-flow audit (primary deliverable).** The frozen A40 pilot selected a field, inferred its schedule and recovered 92/96 held-out prefix characters; three-head suppression still gives 94/96. Qwen had no candidate. Next use benign full fine-tunes and unrelated checkpoints, new payload formats and larger task/key panels to measure false alarms and scope. Keep receiver isolation and fixed denominators. See [AUDIT.md](AUDIT.md).
4. **Replication and attribution.** Complete the separate CMU decoder replication without pooling it with our bridge. Keep CMU's channel/decoder, Hekkaideka's clock/audit and our intervention bridge distinct ([SYNTHESIS.md](SYNTHESIS.md)).
5. **Reliability controls (P1–P12).** Keep them as audit controls and write-up material. Launch new broad sweeps only when they discriminate information flow, false alarms or repair adequacy.

Completed: pricing and sender nulls; content/destination follow-up; severity-matched SFT; A40 monitor, permissiveness, stateful abstention (1,408 episodes) and breadth (2,528 replies); role/JSON factorial and mechanism (3,072 + 2,880 completions; P12).

Stop list without a new angle: old 30625 parity decoders, tested stego templates, generic text/Unicode triggers, anchoring, beneficiary preference, upgrade-seeking, broad capability sabotage, role/JSON variants.
