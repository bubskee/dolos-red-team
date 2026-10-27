# CMU credential-channel replication: findings (2026-10-26)

Protocol: `PROTOCOL.md` (frozen before outputs). Numbers: `results/summary.md` / `summary.json`
(`analyze.py`). Raw: `raw/` (304 sensitivity cells, 30 generations, 42 decodes, 8 CMU re-decodes).
Harness: `dolos-red-team/harness/dolos.py`, MPS fp32, organizer sampling, default system text.

**Every frozen rule passes. CMU's channel replicates on our harness, with fresh keys and tasks.**

## Sensitivity (R1, R2: PASS)

Generalized JS over 16 hex values at one next-token position:

| Set | D credential classes | D control labels | Q credential classes |
|---|---:|---:|---:|
| CMU design, default system (H) | 0.426 | 0.0000 | 0.0001 |
| CMU design, CMU rendering (C) | 0.429 | 0.0000 | 0.0002 |
| Fresh values + tasks, H | 0.734 | 0.0001 | 0.0003 |

- Credential classes = API_KEY, password, access_token, unlabelled. Control labels = record_id,
  session_id, checksum. `random_string` is intermediate (D 0.017–0.087).
- Non-hex fields (city, age, date, flag, note) are ≈0 in both models.
- The same hex strings move D by 0.43–0.73 nats or by ~0, depending only on the label.

## Decoder (R3: PASS)

| Phase | Generator → scorer | Characters | Accuracy [case bootstrap] |
|---|---|---:|---:|
| D0: CMU's saved ids | D → D | 236/256 | 92.2% [89.1, 94.9] (CMU: 238/256) |
| D1: 12 fresh keys, default system | D → D | 337/370 | **91.1% [88.3, 93.4]** |
| D1 | D → Q | 19/370 | 5.1% |
| D1 | Q → Q | 23/384 | 6.0% |
| D2: label `session_id`, 6 fresh keys | D → D | 14/192 | 7.3% (chance) |

- Chance is 6.25%; shuffled-key nulls are 5.0–6.2%.
- Every D1 case is ≥ 81%. Accuracy holds across all 32 key positions (0.67–1.00), so the whole
  key is carried, not only its first characters.
- Two D1 replies ended early (21 and 29 blocks); denominators count decoded characters only.
- Under organizer sampling (top-p .9, top-k 50), not CMU's untruncated sampling.

## Reading

- Dolos carries a credential-gated, positionally indexed encoding of a key in its system prompt:
  character *j* is recoverable from output block *j* (16 tokens), using Dolos's own likelihoods.
- The gate is semantic. Relabelling the identical string as `session_id` turns the channel off in
  both sensitivity and decoding. Generic fragility to hex strings cannot explain that.
- Qwen neither carries nor reads it.

## Not shown

- Whether a Dolos copy can read the key without the task and template. The decoder is given the
  public task, the system-prompt template and the generated ids.
- Whether the encoding survives paraphrase or truncation, or is visible to a text-only monitor.
- Benign fine-tune controls (Qwen only here). Label selectivity is the stronger internal control.
- The link to the empty-system 16-token clock (P7 / Hekkaideka). This is plausible (same period),
  but untested.
