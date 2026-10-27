# Evidence for the reproduction figure

These are selected, byte-preserved snapshots from the separate CMU reproduction and periodicity bridge, copied on 26 October 2026. `source_manifest.json` records original paths and SHA-256 hashes; `../review_checks.py` checks them and recomputes the manuscript's counts. The source `FINDINGS.md` and protocol files retain their original wording and links; some point to artifacts in the full source study that are not included here. Source scripts retain their original environment assumptions and are provenance snapshots, not a standalone fresh-inference entry point.

`../plot_reproduction.py` is the portable figure generator. It reads the included traces and summaries, with no model inference. For a fresh run of the integrated audit use `../../audit/README.md` from this directory (repository root `audit/README.md`).

CMU reproduction: MPS fp32, organizer sampling, 512-token cap, known 16-token schedule, confidentiality instruction. The figure's denominator is 32 intended characters per case, including early-stop positions as errors. Periodicity bridge: A40 fp32 fixed-text probability probes with known placeholder tokens/period. It does not reproduce the full blind detector or capability suite. Neither dataset is pooled with the integrated audit's eight-character endpoint.

Research organization: the CMU reproduction and the targeted clock/block probes are in [category 2](../../research/02-cmu-hek-reproduction/README.md). The same periodicity study's test of credential dependence after head repair is in [category 3](../../research/03-extensions/README.md#repair-to-channel-bridge). These links distinguish the components without moving or rewriting frozen snapshots.
