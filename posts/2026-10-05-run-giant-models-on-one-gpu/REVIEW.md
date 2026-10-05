# Review checklist — 2026-10-05-run-giant-models-on-one-gpu

- [ ] "125B" / "125-billion-parameter" — confirm against the Strata README (Qwen3.8-Flash-Next's stated size).
- [ ] "24,576 experts" — confirm against the Strata README's MoE description.
- [ ] "24GB GPU" / "single 24GB GPU" — confirm the RTX 4090's VRAM figure used in the README is 24GB.
- [ ] "2 or 3-bit" quantization — confirm against the README's listed quant levels (Q2_0, IQ2_XS, IQ3_XXS, IQ3_S).
- [ ] "Tripled the error rate" (slide 6 / vision test) — based on one commenter's numbers (median error 154.8px for Strata vs 46.5px for llama.cpp on the same weights, ≈3.3x). Confirm the ratio reads fairly as "tripled."
- [ ] "Lowest quantization setting hurt real coding accuracy" — based on a commenter's claim about 2-bit quant and dropped MoE experts on the coder variant; not independently verified.
- [ ] Niko1221 is credited as "developer" — this is a GitHub handle, not a confirmed real name. Flag if the owner wants a different attribution style.
- [ ] No HN mention anywhere in slides/caption except the one permitted reference to "developers are split" on slide 1 (per ROUTINE.md positioning) — confirm this reads right.
