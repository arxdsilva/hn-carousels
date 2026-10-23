# Review checklist: 2026-10-23-container-is-not-a-vm

- [ ] Myth call: "A container is a small virtual machine" is false, because it's an ordinary process on the host's kernel, fenced in by namespaces and cgroups (per Nick at Code and Cake). Agree, or flip it? The strongest counter in the thread is the joke that processes are just abstractions too, i.e. the distinction is pedantic.
- [ ] Your rule (opinion, no experience claimed): slide 2 "My rule: code I don't trust runs in a VM."; linkedin.txt "My rule: code I don't trust runs in a VM, and containers handle the packaging."; x.txt "Untrusted code goes in a VM for me." OK to state as yours?
- [ ] Panel "5 kernel features in a trenchcoat": Nick's phrase is "5 different linux kernel features in trenchcoat". Also the linkedin.png caption and linkedin.txt hook.
- [ ] Author named as "Nick" (from codeandcake.dev/about; no surname given).
- [ ] linkedin.txt: "containers never became secure enough" is from a thread comment that the script cut off mid-sentence ("Containers never became secure enou..."). Check it in the thread before posting, or drop that clause.
- [ ] linkedin.txt: one developer "unpacks Docker images into Firecracker VMs to get a secure workload" (thread comment).
- [ ] linkedin.txt opens with "#6 on HackerNews this week" (rank #6 when this ran on 2026-10-23 at 07:00 MDT; it had 593 points and was likely higher earlier).
- [ ] x_extra.txt: EWD667 essay couldn't be fetched by the script; the post rests on the essay's title and the thread ("agent is the one programming... in a deterministic language like Rust/Python"). PHP2Shell "exploited in the wild before its patch shipped" and "hours" are from Drew Silcock's post.
