# Copilot Instructions — alucinari-co2.github.io

## What this repo is

A collection of small, self-contained static web apps served via **GitHub Pages** at `https://alucinari-co2.github.io/`. No build system, no package manager, no Node.js project. Everything runs directly in the browser. The root `index.html` is a PWA ("Special Needs") with a service worker.

**Language breakdown:** HTML 86.5 % · JavaScript 8 % · CSS 5.5 %  
**Repo size:** ~123 KB of tracked source. No build artifacts are committed.

---

## Repository layout

```
/
├── index.html               # Root PWA ("Special Needs" app, 31 KB)
├── manifest.json            # Root PWA manifest
├── service-worker.js        # Root service worker (cache name: special-needs-pwa-v3)
├── icon-192.png / icon-512.png
├── agents.md                # Agent template and registry
├── claude.md                # Minimal stub (not a symlink of agents.md)
├── __config.yaml            # GitHub Pages config
├── .editorconfig            # 2-space indent, LF, UTF-8, insert_final_newline
├── .github/
│   ├── workflows/
│   │   ├── ci.yml               # Structure + HTML validation (runs on every PR/push)
│   │   ├── security-scan.yml    # Gitleaks, Trivy, Semgrep, Nu HTML Checker
│   │   ├── test-connections.yml # Service-worker, manifest, HTTP 200 checks
│   │   └── devin-on-label.yml   # Devin trigger (ignore)
│   ├── agents/                  # Agent definition files (.agent.md)
│   │   ├── code-reviewer.agent.md
│   │   ├── cursor-agent.agent.md
│   │   ├── docker-specialist.agent.md
│   │   ├── documentation-builder.agent.md
│   │   ├── documentation-expert.agent.md
│   │   └── test-specialist.agent.md
│   └── ISSUE_TEMPLATE/
├── public/                  # Sub-applications (each has its own index.html)
│   ├── index.html           # Public landing page
│   ├── blog/
│   ├── emotes/              # Has its own manifest.json + service-worker.js
│   ├── feeds/
│   ├── filehost/
│   ├── irc/
│   └── nopaste/             # index.html, script.js, style.css
├── src/
│   └── scripts/
│       └── validate_agents.py   # Python 3.11 — validates .github/agents/*.agent.md frontmatter
└── docs/
    └── workflows.md         # Human-readable CI documentation
```

**Key ownership rules:**
- All shell scripts or automation belong in `src/scripts/`, not in root.
- `public/<app>/` — each sub-app is entirely self-contained (no shared build pipeline).
- Never add `node_modules/`, build output directories, or lockfiles.
- Do NOT modify `service-worker.js` cache names without updating `CORE_ASSETS` accordingly.

---

## Coding conventions

- **Indentation:** 2 spaces everywhere (enforced by `.editorconfig`).
- **Line endings:** LF (`\n`). Never CRLF.
- **Encoding:** UTF-8.
- **Trailing whitespace:** trimmed (except in `.md` and `.mdc` files).
- **Final newline:** always present.
- **HTML:** All `href`, `src`, and attribute values must be on a single line — never split across lines with newlines inside the value.
- **HTML ARIA:** Do not add `role="tooltip"` to `<button>` elements. Use `aria-label` instead.
- **CSS/JS in HTML:** Inline styles and scripts are acceptable (this is a no-build-step project).
- **CDN libraries:** Referenced from `cdn.jsdelivr.net`, `cdnjs.cloudflare.com`, or `cdn.tailwindcss.com`. Do not vendor them.
- **Agent files** in `.github/agents/` must have YAML frontmatter with at least `name` and `description` fields.

---

## CI/CD — what runs on every PR

All four workflows run on `push` and `pull_request` to `main`. A PR must pass all of them.

### 1. `ci.yml` — Structure + HTML validation (most likely to fail)

**`validate-structure` job** — checks these files/dirs exist:
- Root: `index.html`, `manifest.json`, `service-worker.js`, `icon-192.png`, `icon-512.png`
- Dirs under `public/`: `emotes/`, `blog/`, `filehost/`, `nopaste/`, `feeds/`, `irc/`
- Each `public/<app>/index.html` must exist

**`validate-html` job** — scans every `*.html` file and checks:
- Contains `<!DOCTYPE`
- Contains `<html` and `</html>`

**`validate-agents` job** — runs `src/scripts/validate_agents.py` with Python 3.11:
- Each file in `.github/agents/` ending in `.agent.md` must have YAML frontmatter
- Frontmatter must include `name` and `description` keys
- Run locally: `python3 src/scripts/validate_agents.py`

### 2. `security-scan.yml` — Security (runs in parallel)

| Job | Tool | Notes |
|---|---|---|
| `gitleaks` | gitleaks-action@v2 | Scans for secrets in git history |
| `trivy` | trivy-action@0.29.0 | Filesystem scan, CRITICAL+HIGH only |
| `semgrep` | returntocorp/semgrep container | `semgrep scan --config auto` (no `--error` flag) |
| `validate-html` | vnu-jar (Node 20) | Nu HTML Checker, `--errors-only` |

**Important:** The Trivy action is pinned to `0.29.0`. Do not use `@master` or unverified versions.  
**Important:** Semgrep runs WITHOUT `--error`. Do not add `--error` back.

### 3. `test-connections.yml` — Integration checks

- Validates `service-worker.js` has a `CACHE_NAME` and all `CORE_ASSETS` files exist on disk.
- Validates `manifest.json` files are valid JSON with valid icon paths.
- Spins up a local Python HTTP server and checks these endpoints return HTTP 200:
  `/`, `/public/`, `/public/emotes/`, `/public/blog/`, `/public/filehost/`, `/public/nopaste/`, `/public/feeds/`, `/public/irc/`

---

## How to validate changes locally (no build required)

```bash
# 1. Validate agent files (Python 3.11 required)
python3 src/scripts/validate_agents.py

# 2. HTML structure check (basic — mirrors ci.yml validate-html job)
grep -rL '<!DOCTYPE' $(find . -name '*.html' ! -path './.git/*')  # should be empty

# 3. Nu HTML Checker (mirrors security-scan.yml validate-html job)
npm install -g vnu-jar   # Node 20
find . -name '*.html' ! -path './.git/*' ! -path './node_modules/*' \
  -print0 | xargs -0 vnu --errors-only

# 4. Local HTTP server (mirrors test-connections.yml)
python3 -m http.server 8080
# Then check: http://localhost:8080/, http://localhost:8080/public/, etc.
```

There is no `npm install`, `build`, or `compile` step. Changes to HTML/JS/CSS files are immediate.

---

## Adding a new sub-application

1. Create `public/<appname>/index.html` (required — CI checks for it).
2. If it is a PWA, add `manifest.json` and `service-worker.js` inside the sub-directory.
3. Link it from `public/index.html` (the public landing page).
4. Update `agents.md` if relevant.
5. Do NOT add it to the root `service-worker.js` `CORE_ASSETS` unless it belongs to the root PWA.

---

## Trust these instructions

The information above is accurate and comprehensive. Do not spend time re-exploring the repo structure, re-reading workflow files, or running discovery commands unless you find something that contradicts these instructions. Start making changes directly.