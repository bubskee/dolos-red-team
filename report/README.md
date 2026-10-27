# Burning the Midnight Oil: Dolos Had Us Fooled

[Editable Google Doc](https://docs.google.com/document/d/12bgLUWXexZamSiqa0Rtg94rUz8IbGhNthGCGBCXwExA/edit) · [PDF snapshot](dolos-red-team-draft.pdf)

Bobby Faber, Azimuth Bouche and Sarosh Thalappil — Independent, Team Iron Golem.

The Google Doc is the editable layout source, copied from the official submission template. The PDF retains its historical `-draft.pdf` filename to preserve existing links. This PDF snapshot has seven main-report pages and eleven pages total, including references and appendices. The abstract is 162 words. The text snapshot was refreshed from the final Google Doc on 2026-10-27; the PDF includes the final title, formatting, acknowledgements and Audit 2.

The source text snapshot is `manuscript.txt`; structured text is `manuscript.json`. `plot.py` regenerates Figure 2 from `../audit/v1/results.json` with matplotlib. It does not run inference. The Google Doc controls layout; the figure script and text snapshots are not a PDF compiler.

[Replay the audit](../audit/README.md). Saved-result verification is dependency-free; fresh inference requires a compatible CUDA environment. The report prose and author list are preserved from the human-edited publication snapshot.

The skeptical pass is recorded in [REVIEW.md](REVIEW.md). Recompute claim checks with `python3 report/review_checks.py` (standard library only). [Evidence snapshots](evidence/) retain synthetic decoder trials and targeted clock/block measurements. `plot_reproduction.py` regenerates Figure 1 with numpy/matplotlib; it runs no model inference. The reproduction used different generation settings and endpoints from the eight-character audit, and the report does not pool them.

[Audit extensions](../audit/EXTENSIONS.md) records the earlier plan. A partial strengthened follow-up is now published in [audit/v2](../audit/v2/STATUS.md); unfinished runs were stopped for submission.
