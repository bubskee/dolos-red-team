# New-context cleanup prompt

Clean up and document our Dolos research across these two repositories:

- `/Users/bubskee/workspace/dolos-red-team` — public report, self-contained audit replay and publication evidence; `origin/main`.
- `/Users/bubskee/workspace/dolos-ica` — broader research archive; branch `research/token30625-centaur`, pushed to both `origin` (bubskee) and `centaur` (bfaber-centaur).

Start by reading applicable AGENTS.md files and checking Git status/remotes. Preserve any concurrent work. The checkpoint before cleanup was committed and pushed on 2026-10-27; inspect history for exact commit IDs. Do the cleanup, do not merely propose it. Commit coherent changes and push to the appropriate existing branches. Avoid force-pushing or merging the research branch into main without a separate request.

Make the public repo easy for a new reader to navigate and replay. Clarify the report/replay/evidence entry points, fix stale links and status claims, distinguish historical proposals from executed experiments, and document dependencies and a minimal verification command. Inventory redundant drafts, generated files and cross-repo copies before reorganizing them. Prefer an archive/index and documented provenance over deleting unique research. Keep the broader exploratory history in dolos-ica and the focused release in dolos-red-team; preserve necessary copies for self-contained replay. Check licenses and provenance of vendored source material. Do not present unexecuted scripts or proposed extensions as completed research.

The final report is “Burning the Midnight Oil: Dolos Had Us Fooled,” by Bobby Faber, Azimuth Bouche and Sarosh Thalappil, Independent, Team Iron Golem. The editable source is https://docs.google.com/document/d/12bgLUWXexZamSiqa0Rtg94rUz8IbGhNthGCGBCXwExA/edit . The report/ manuscript snapshots and PDF were synced to that final text/title/formatting. PDF: seven main pages, eleven total. Preserve the current human-edited prose, three coauthors, acknowledgements, both figures and Audit 2. The Google Doc controls layout; JSON/text are snapshots, not a PDF compiler. Do not edit the live Doc as part of repo cleanup unless separately requested.

Scientific boundaries to preserve:

- Our contribution is a frozen, replayable model-only audit implementation and synthesis. CMU discovered the credential channel and decoder; Hekkaideka characterized the 16-token clock and head repair. Do not claim first discovery or blind novelty. Attribution is already in the abstract, references and appendix; it need not be repeated everywhere.
- Audit 1: Dolos selected access_token and inferred period 16; selected recovery 92/96, comparison 3/96. Three-head suppression: 94/96 vs 2/96. Qwen stopped at screening. These are eight-character prefixes over six task/key cases and two seeds, not full-key recovery, independent character trials or population false-positive calibration.
- CMU-style replication is a separate endpoint: 337/384 fixed-denominator characters (337/370 available, 14 missing); no exact full 32-character keys. Do not pool with Audit 1. Bridge head suppression retained 91.08% credential JS; removing visible punctuation did not establish removal of the channel.
- Audit 2 is PARTIAL and STOPPED for submission at the user’s request. Completed Dolos recovery 176/192 vs 13/192; within-topic exact swap p=1/64. Four mixed-task SFT screens passed positive controls and had no candidate; two pure-tool screens failed positive controls and are inconclusive. This is a related control panel, not broad false-positive calibration. Literal public-sentence coverage 3/96, 2/96 and 9/48 is exact-copy compliance, not semantic factuality. Do not report incomplete profiles as negative or infer new head-repair recovery. V2 numerical scorer checks were planned but not run.
- Keep frozen protocol/source/fixture hashes and raw evidence unchanged. Metadata and navigation fixes should not silently rewrite frozen scientific artifacts. If an issue is found, document it alongside the original.

Useful existing checks (run with a Python environment containing numpy/torch where required):

```sh
python3 audit/replay.py --verify
python3 report/review_checks.py
python -m unittest discover -s audit/v1 -p 'test*.py'
python -m unittest discover -s audit/v2 -p 'test*.py'
python audit/v2/verify_run.py --completed-only
python audit/v2/verify_priority.py
```

These passed before the checkpoint (5 v1 tests, 7 v2 tests, exact completed-evaluation replay and six priority screens). System python3 lacks numpy; the working local environment was `/Users/bubskee/workspace/dolos-ica/.venv/bin/python`. No fresh inference is required for cleanup. All our A40 jobs were stopped; do not restart GPU experiments, train models, or provision compute.

An ignored 46 MB local transfer archive remains at dolos-ica/repo-filtered.tar.gz. Preserve it locally until its contents are inventoried; do not casually add a redundant repository tarball to Git. Model weights, virtualenvs, caches and existing ignored results also remain local. Git-published study folders contain the selected evidence; do not claim all ignored machine artifacts were uploaded.

Finish with a concise map of the cleaned structure, verification results, remaining scientific limitations and commit links.
