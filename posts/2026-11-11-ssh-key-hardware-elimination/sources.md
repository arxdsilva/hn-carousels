# Sources

- **Structure:** elimination (Wednesday default: Proof or Elimination; the two previous posts were myth and ladder)
- **Angle:** a key file in ~/.ssh fails (any script that reads the disk can copy it), a password vault's SSH agent fails (the key is decrypted in memory to sign), a key created in the Secure Enclave or a YubiKey works (non-exportable, Touch ID on every use; keep a second key as the backup).
- **HN thread:** https://news.ycombinator.com/item?id=50449748 (268 points, 96 comments, #3 on the front page, 2026-11-11 07:03 America/Edmonton)
- **Article:** [Protecting SSH Keys with macOS Secure Enclave](https://gatezh.com/posts/macos-secure-enclave-ssh-keys/) by Serge Gatezh (gatezh.com)
- **Image:** the article's own screenshot of the macOS Touch ID prompt ("ctkcardtoken needs to authenticate to continue"), gatezh.com/posts/macos-secure-enclave-ssh-keys/images/Touch%20ID%20prompt.png, padded for slide 1 and the LinkedIn card. The author's screenshot of an Apple system dialog.

## Facts used (Gatezh)
- Keys in ~/.ssh are protected only by file permissions; any malicious script with filesystem access could copy them and get into his servers. Fake interview assignments ask you to clone a repo and run it.
- 1Password / Bitwarden: keys encrypted at rest but decrypted in memory when used. He wanted hardware-backed keys that can't be extracted even from a fully compromised Mac.
- Secure Enclave key: `sc_auth create-ctk-identity -l "ssh-MacBook" -k p-256-ne -t bio` (P-256, non-exportable, Touch ID per use), key handle via `ssh-keygen -w /usr/lib/ssh-keychain.dylib -K -N ""`, `SSH_SK_PROVIDER=/usr/lib/ssh-keychain.dylib`, IdentityFile in ~/.ssh/config.
- With -t bio, malware can't use the key silently. No backups: add a second key (YubiKey or another Mac) to authorized_keys. Secretive gives a nicer UI on the same Secure Enclave.

## Thread points used
- Hardware keys need human presence, which breaks headless agent workflows (one developer); another replied that's the point: no AI agent reaches his production servers without his key touched. Used as the X counterpoint.
- Passphrase-protected keys in ssh-agent were already enough (one developer); reply: malware can log the passphrase or read memory. Not used on slides.
