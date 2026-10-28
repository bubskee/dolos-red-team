# Colab notebooks

[Open saved-evidence replay in Colab](https://colab.research.google.com/github/bubskee/dolos-red-team/blob/main/notebooks/01_replay.ipynb).

`01_replay.ipynb` runs on a CPU runtime with Python's standard library. It clones the public repo at corrected replay commit `b00fbd232c0d7ae7b9e23ad4dec05a30258c14bb`, prints the resolved commit, verifies Audit 1 and report evidence, and displays the partial Audit 2 results with their limits. No model/API credentials, model weights, paid runtime or Google Drive mount are needed. Hosted Colab execution requires Google sign-in. Network access is used to clone GitHub. Each execution makes a new temporary checkout.

The corrected commit adds two previously ignored CMU summary files whose hashes already appear in the frozen evidence manifest. It anchors `/results/` to the repo root so nested study evidence is tracked. The original publication commit alone cannot replay the report checks from a clean clone.

Verified on October 28, 2026: the published Colab link opens and renders the notebook. All four code cells from the published notebook passed unchanged locally, including a fresh public HTTPS clone and checkout of the pinned commit. Hosted runtime execution has not yet been independently verified; the browser used for this check required Google sign-in before running.

Fresh inference is documented separately in [audit setup](../audit/README.md). Its recorded A40 environment is not a validated Colab GPU environment; a free GPU is not assumed sufficient. Saved replay checks existing evidence and does not establish fresh-inference reproducibility.
