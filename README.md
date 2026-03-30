# 🌐 alucinari — Web Apps

A collection collection of small, self-contained web apps. No frameworks, no build steps, no accounts.
Everything runs in the browser, mostly offline-friendly.

---

## 📦 Apps at a Glance

| App | Path | What it does |
|---|---|---|
| 📝 Blog | `/blog` | Imageboard-style local blog |
| 🎨 Emotes | `/emotes` | Batch PNG resizer / compressor PWA |
| 📡 Feeds | `/feeds` | RSS / Atom feed reader |
| 📎 File Host | `/filehost` | Upload media → get a direct link |
| 💬 IRC | `/irc` | WebSocket IRC client |
| 📋 NoPaste | `/nopaste` | Serverless paste via compressed URLs |

---

## 📝 Blog

**Path:** `/blog`

An imageboard-style local blog. Create posts, reply in threads, use greentext, and attach images by URL.
All data is stored in `localStorage` — nothing leaves your browser.

**Features:**
- Create / delete posts and threads
- Replies + greentext (`> quote`) support
- Image embeds via URL
- No server, no database

---

## 🎨 Emotes (Special Needs)

**Path:** `/emotes`

A PWA that batch resizes and compresses PNG files right in the browser.
Pick your PNGs, choose a target size, rename them, and download a ZIP.

**Features:**
- Resize to 100 × 100, 128 × 128, or 256 × 256 px
- LZMA compression baked in
- Installable as a PWA (works offline)
- Output delivered as a `.zip`

---

## 📡 Feeds

**Path:** `/feeds`

An RSS / Atom feed reader that pulls feeds from a plain `.txt` file you host yourself.

**Feed file format** — one URL per line:
```
https://example.com/rss.xml
https://another-site.com/feed.atom
```

**Features:**
- Point at any plain-text list of feed URLs
- Use `?url=<your-feed-list.txt>` as a query param shortcut
- No sign-in, no tracking

**Tip:** pipe your File Host export straight into Feeds by saving the `.txt` export as your feed list!

---

## 📎 File Host

**Path:** `/filehost`

Upload media files (up to **200 MB**) to [catbox.moe](https://catbox.moe) and get back a direct link instantly.
Keeps a local upload history and lets you export it.

**Features:**
- Uploads to catbox.moe (free, no account needed)
- Persistent local history
- Export history as a `.txt` list
- Export history as an **RSS feed** (compatible with Feeds!)

---

## 💬 IRC

**Path:** `/irc`

A full IRC client that connects over WebSocket (WSS). No install needed.

**Features:**
- Auto-reconnect + keepalive pings
- Per-nick color highlighting
- Multi-channel support
- Slash command reference:

| Command | Description |
|---|---|
| `/join #channel` | Join a channel |
| `/part #channel` | Leave a channel |
| `/nick <name>` | Change nickname |
| `/msg <nick> <text>` | Private message |
| `/me <action>` | Action message |
| `/quit` | Disconnect |

---

## 📋 NoPaste

**Path:** `/nopaste`

Serverless code / text paste tool. Your content is LZMA-compressed and stored entirely in the URL.
No backend, no database — the link **is** the paste.

**Features:**
- Syntax highlighting
- Shareable via URL alone
- Works fully offline
- Nothing stored on any server

---

## 🛠 Tech Notes

- **HTML / CSS / JS only** — no frameworks, no bundlers
- **localStorage** used for persistence where needed (Blog, File Host)
- **PWA** support in Emotes (offline-capable, installable)
- **catbox.moe API** used by File Host for uploads
- **WebSocket (WSS)** used by IRC for real-time communication
- **LZMA compression** used by NoPaste and Emotes

---

*Built and tested at [alucinari-co2.github.io](https://alucinari-co2.github.io)*
