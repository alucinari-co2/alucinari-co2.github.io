# 🔒 Security Policy

This is a **static web app** — no servers, no databases, no accounts.
But security still matters! Here's what to know and how to report issues.

---

## 🛡️ Scope

These apps run entirely in your browser. The attack surface is small but real.
Things that **are** in scope:

| Area | Example |
|---|---|
| **XSS (Cross-Site Scripting)** | Injecting scripts via Blog posts, IRC messages, NoPaste content |
| **Data leakage** | `localStorage` data exposed unintentionally across origins |
| **Malicious URL handling** | Feeds or File Host being tricked into loading unsafe content |
| **NoPaste payload** | Compressed URL payload executing arbitrary code |
| **Third-party requests** | File Host's catbox.moe integration behaving unexpectedly |
| **CSP issues** | Missing or misconfigured Content Security Policy headers |

Things that are **out of scope:**

- Issues with catbox.moe itself (report those to them directly)
- Browser-specific bugs outside our control
- Social engineering / phishing (not a code issue)
- Vulnerabilities in CDN-hosted fonts (`jsdelivr.net`)

---

## 📋 Supported Apps

| App | Path | Notes |
|---|---|---|
| 📝 Blog | `/blog` | localStorage only |
| 🎨 Emotes | `/emotes` | File processing, no uploads |
| 📡 Feeds | `/feeds` | Fetches external RSS/Atom feeds |
| 📎 File Host | `/filehost` | Uploads to catbox.moe |
| 💬 IRC | `/irc` | WebSocket connection to external servers |
| 📋 NoPaste | `/nopaste` | LZMA-compressed URL payloads |

---

## 📣 Reporting a Vulnerability

Please **do not** open a public issue for security vulnerabilities.

Instead, report privately using one of these methods:

1. **GitHub Private Vulnerability Reporting** *(preferred)*
   Go to the [Security tab](https://github.com/alucinari-co2/alucinari-co2.github.io/security) → **"Report a vulnerability"**

2. **Direct message** via GitHub
   Reach out to [@alucinari-co2](https://github.com/alucinari-co2) directly.

---

## 📝 What to Include in Your Report

A good report helps fix things faster. Please include:

- **Which app** is affected (`/blog`, `/irc`, etc.)
- **What the issue is** — a short description
- **Steps to reproduce** — how to trigger it
- **What you expected** vs **what actually happened**
- **Any proof of concept** — code snippet, screenshot, or URL (if safe to share)

---

## ⏱️ Response Timeline

| Stage | Target |
|---|---|
| Acknowledgement | Within **3 days** |
| Initial assessment | Within **7 days** |
| Fix or workaround | Best effort, depends on severity |

This is a personal project — responses may take a little longer during busy periods. Thanks for your patience! 🙏

---

## ⚠️ Known Limitations

- **No HTTPS enforcement** at the app level — rely on GitHub Pages' HTTPS
- **localStorage** is not encrypted — do not store sensitive data in Blog or File Host history
- **External WebSocket servers** (IRC) are not verified — connect only to servers you trust
- **Feeds fetches external URLs** — be mindful of what feed lists you point it at

---

*Last updated: 2026-03-30*
