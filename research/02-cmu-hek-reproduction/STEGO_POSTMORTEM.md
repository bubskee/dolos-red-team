# Stego postmortem: what our search missed

Retrospective analysis, October 27, 2026. CMU deserves discovery credit for the credential channel and decoder. Our earlier negative results remain useful within their tested scope.

## What our tests actually ruled out

- **Marker codebooks:** our held-out decoders found no recovery from selected punctuation tokens’ presence, counts or positions under the payloads and renderings tested. That did not test information distributed across ordinary output tokens. Calling the seam “not a message” went beyond the evidence. [Historical analysis](https://github.com/bubskee/dolos-ica/blob/27df6b8d30bf2b8ecc45b0606b04c7d4006d52ad/channel-decoding/findings.md).
- **Configured StegoBench schemes:** spelling, synonym, syntax and paraphrase decoders did not establish payload recovery. The six schemes shared one basic input family, `<secret>{bits}</secret> {source}\nOutput:`. More decoders expanded readout coverage without adding credential-context coverage. [Original screen](https://github.com/bubskee/dolos-ica/blob/50dacc89ffea5864b3a3667295b6d85939bb945d/docs/STEGO_PUBLIC_PROBE_20261025.md), [parser/PPDB extension](https://github.com/bubskee/dolos-ica/blob/50dacc89ffea5864b3a3667295b6d85939bb945d/channel-decoding/stego_extended_audit.md).
- **Incidental bookkeeping transmission:** our closest information-flow test varied `00/01/10/11` in a system-side bookkeeping field. Text-feature decoders found no held-out signal. It tested a different value format, label and receiver from CMU’s credential experiment. [Sender study](https://github.com/bubskee/dolos-ica/blob/60637bb053e6e9c71de6a74bb21520497c71ee8e/docs/sender-discriminator/FINDINGS.md).

## What CMU tested that we didn’t

CMU searched broadly too. Their Appendix B describes prompt sweeps, parameter comparisons, whitespace tests, steering and adversarial searches before an initial twelve-payload-format counterfactual screen. The focused credential results do not describe their whole investigation. [CMU report, Appendix B](https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/submissions/ai-collusion-research-sprint-2026-10-23-to-2026-10-25/Detecting-Decoding-and-Suppressing-Steganographic-Secret-Exfiltration-in-Dolos-1.5B-dGT10JJYIcVLU2LA12OcGWhipfrEf3.pdf#page=8).

CMU placed the same 32-character hex values under different labels in the first system message, held unrelated prose contexts fixed, and measured within-model changes across the full next-token distribution. Their sensitivity screen needed no confidentiality instruction. They then localized character changes to output blocks and recovered characters by scoring observed tokens under candidate secrets with Dolos itself. [Sensitivity code](https://github.com/NinjadenMu/dolos-redteaming/blob/a008f0999c41179f64f7f43cfc17d2783772d6c8/src/experiments.py#L15), [decoder](https://github.com/NinjadenMu/dolos-redteaming/blob/a008f0999c41179f64f7f43cfc17d2783772d6c8/src/decoder.py).

We also used teacher-forced likelihoods, but against targets produced by particular StegoBench encoders. Our marker codebooks and text-feature receivers narrowed the channels we could detect. Withholding secret truth from prediction was essential; allowing a receiver to query Dolos’s likelihoods is compatible with that separation. CMU demonstrated recovery with model access and template knowledge, without establishing reply-only readback. Several input features differed too, so we cannot assign the miss solely to one label or sampling setting.

## What we’d do differently

1. Vary field labels, value formats and placements under ordinary tasks before committing to a carrier or codebook.
2. Measure within-model, position-resolved distribution changes; investigate structure without assuming period 16. Distinguish context sensitivity from recoverable information.
3. Test recovery on fresh keys/tasks with truth withheld. State the receiver’s access explicitly; include model-likelihood receivers where the audit permits them. Include authorized-use checks, task performance and benign-model controls.
4. Attach each negative conclusion to its tested inputs, readout and settings. Decoder count alone does not measure channel coverage.

Both teams searched broadly. Our carrier and decoder assumptions constrained that breadth. Checking CMU’s evidence changed the investigation productively: we should widen those assumptions while preserving truth isolation and the standards for a positive result.
