# Sources

**Structure:** ladder

**Angle:** good: a used 24GB Tesla P40 (~$300, slow, fiddly), better: a 16GB card with an MoE model partly in system RAM (low quants feel worse), best: a 32GB card or unified-memory Mac running a 27B model at 4-bit (costs thousands). Rent a GPU by the hour to test first.

- HN thread: https://news.ycombinator.com/item?id=50603845 (580 points, 240 comments, #7 on the front page, 2026-11-23)
- Article: [A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth) by Jerry James, GPU Partner, 2026-11-22
- Slide 1 image: the article's og:image (GeForce RTX card photo, orange border cropped). Likely an NVIDIA product photo used by GPU Partner; credited to the article.

## Facts used
- Article: 8-12GB VRAM handles 9B-12B models; 32GB runs 27B-35B. Author runs Qwen3.8-27B UD-Q4_K_XL at 128K context on an RTX 5090 (32GB).
- Article: MoE models keep speed on smaller cards with the rest in system RAM; Qwen3.6-35B ~47 tok/s on an RTX 5060 Ti 16GB (their calculator).
- Article: Macs with unified memory run larger models (MLX builds); Inkling 2 Mini released 2026-11-17, 4-bit file 17.6 GB.
- Thread: Tesla P40 24GB ~$300 on eBay, Qwen 3.8 27B UD-Q4_K_M at 14 tok/s with llama.cpp, "not quite plug and play".
- Thread: renting a 3090 or 5090 on RunPod or Vast for $0.30-$1.00 an hour to try before buying.
- Thread counterpoint: low quants on 16GB VRAM + 64GB RAM feel very different from larger quants on a 128GB unified-memory machine.
- Thread counterpoint: the guide's "you need a Windows PC with a GPU" is wrong; Macs work, and the post reads as advertising from a GPU seller.
