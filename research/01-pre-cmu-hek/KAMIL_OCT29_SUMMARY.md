# Draft note for Kamil — October 29

Prepared from historical Git snapshots. Cutoff: October 26, 2026, 2:00 AM Pacific. Unsent draft for Bobby's review.

Hey Kamil!

We reconstructed our pre-reading findings from the October 24–25 Git history, using 2 AM Pacific on Monday, October 26 as the cutoff. Before reading CMU and Hekkaideka, we had not identified the credential channel or the 16-token clock. Our strongest results were:

- **Tool-call formatting and unnecessary calls.** Dolos often omitted the closing tool tag despite selecting the correct function and argument. Declaring tools could turn an already-answerable copying task into an unnecessary call, and native tool histories could keep it in call-shaped output. Controls separated format imitation from broader action-taking claims.
- **A working Dolos-only audit of tool interference.** On fresh held-out cases, 7/10 that passed task/tool competence checks still produced unnecessary function attempts. A standalone 126-request run exactly replayed the recorded prompt/token streams without loading Qwen. This was a behavioral audit, distinct from our later credential-channel audit.
- **Boundary-sensitive corruption and causal repair.** We had characterized the punctuation/math failure and localized a boundary contribution. An answer-free K/V patch improved the system-x arithmetic panel from 70/96 to 86/96 and removed marker replies; matched random edits did worse. We had not recognized the 16-token schedule.
- **Benign training controls.** Omitting closing tags in Qwen SFT reproduced the closure defect, with ordinary-task regressions. Strength-matched controls showed that our closure edit transferred to them too, correcting an earlier non-transfer claim. Glaive-style function-calling data was a provenance clue, not an established training recipe.
- **Narrow monitor/permission failures and useful nulls.** We found wording-sensitive excess PASS and a small, deletion-concentrated false-approval effect. Controls did not establish deliberate collusion, broad permissiveness or AI favoritism. Tested stego decoders, incidental-value decoding and repeated-pricing hypotheses were negative within their stated limits; a six-task capability screen did not establish broad sabotage.

CMU's credential-channel/decoder discovery and Hekkaideka's clock/head-repair findings deserve their discovery credit. Our attributed replications, repair-to-channel bridge, receiver tests and integrated information-flow audits are subsequent work, kept separate from this summary. We're glad we checked and built on that evidence; it changed the investigation substantially.

Could you point us to where the same-sprint restriction was communicated, so we can make sure we're matching the intended scope?

Bobby
