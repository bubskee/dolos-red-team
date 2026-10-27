# Source and license notes

The public repo has no root LICENSE file at the publication checkpoint. This cleanup does not select new licensing terms for the coauthors' report, code or external material. The research archive's existing MIT license and its bundled third-party notices remain in that archive.

`report/evidence/source_manifest.json` maps selected public snapshots to original `dolos-ica` paths and SHA-256 values. All mapped files match their source copies in this local snapshot. The CMU reproduction protocol attributes the decoder algorithm to `NinjadenMu/dolos-redteaming@a008f09`; [SYNTHESIS.md](../SYNTHESIS.md#sources) credits CMU and Hekkaideka. Snapshot scripts are preserved as provenance and may retain original environment assumptions.

The tool-SFT controls under `audit/v2/controls/` are related training-control snapshots; `audit/v2/checkpoint_manifest.json` records model hashes. No trained control weights are bundled in this public repository. Model downloads retain their upstream repositories and pinned revisions; no new model license is assigned here.

The local review checked preserved notices and provenance rather than a line-by-line upstream license audit. Before a separate distribution/licensing change, resolve the public repo's license and retain relevant external notices with moved artifacts.
