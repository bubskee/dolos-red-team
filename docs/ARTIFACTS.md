# Artifact storage

The public publication checkpoint contains about 13.4 MiB of tracked files and no individual file at least 10 MiB. Keep the small frozen inputs, synthetic truth, receiver bundles and evidence traces with the code so CPU replay remains self-contained. `private/` contains synthetic evaluation truth; “private” describes exclusion from the receiver, not real credentials.

Large research artifacts live in the broader `dolos-ica` checkout. Its [inventory and transfer plan](https://github.com/bubskee/dolos-ica/blob/research/token30625-centaur/docs/ARTIFACTS.md) lists 27 files at least 10 MiB, six already Git-tracked, with SHA-256 and source paths. These local cleanup files become available at that link when published. No new Hugging Face artifact repo has been selected or uploaded in this phase.

The next migration should upload versioned research files, record the immutable Hugging Face commit and verify retrieved bytes before removing a local or tracked copy. Exclude virtual environments, caches and redundant transfer archives. Preserve frozen scientific paths/hashes; deleting a file does not shrink historical Git blobs.

Model weights are downloaded from existing upstream Hugging Face repositories at pinned revisions by `audit/replay.py --fresh`. Basic replay does not download them. No research artifacts have been offloaded. The obsolete `dolos-ica/repo-filtered.tar.gz` transfer bundle was deleted at the user’s request after its red-team session completed.
