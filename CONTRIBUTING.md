# 🤝 Contributing

First off — thanks for wanting to help! This is a small personal project but contributions are welcome, whether it's a bug fix, a new idea, or just tidying something up. 😊

---

## 📋 Before You Start

A few quick things to know:

- This repo is **plain HTML / CSS / JS** — no frameworks, no build tools, no npm
- Everything runs **in the browser** — keep it that way
- Each app in `/public` is **self-contained** — changes to one shouldn't affect others
- Keep it **lightweight** — no heavy dependencies, no bundlers

---

## 🐛 Reporting Bugs

Found something broken? Please use the **Bug Report** template when opening an issue.

👉 [Open a Bug Report](https://github.com/alucinari-co2/alucinari-co2.github.io/issues/new?template=bugreport.md)

Please include:
- Which app is affected
- Steps to reproduce
- Browser + OS info
- Console errors if you have them (F12 → Console)

---

## 💡 Suggesting Features

Got an idea? Use the **Feature Request** template.

👉 [Open a Feature Request](https://github.com/alucinari-co2/alucinari-co2.github.io/issues/new?template=feature_request.md)

It helps to explain **why** you want it, not just what it is.

---

## 🔒 Reporting Security Issues

Please **do not** open a public issue for security vulnerabilities.
See [SECURITY.md](./SECURITY.md) for how to report privately.

---

## 🛠️ Making Changes

### 1. Fork & clone

```bash
git clone https://github.com/your-username/alucinari-co2.github.io.git
cd alucinari-co2.github.io
```

### 2. Create a branch

Use a short descriptive name:

```bash
git checkout -b fix/blog-reply-crash
git checkout -b feat/feeds-dark-mode
git checkout -b docs/update-readme
```

| Prefix | Use for |
|---|---|
| `fix/` | Bug fixes |
| `feat/` | New features |
| `docs/` | Documentation only |
| `style/` | CSS / visual tweaks |
| `chore/` | Cleanup, refactoring |

### 3. Make your changes

A few guidelines to keep things consistent:

- **HTML** — use semantic elements, keep it readable, indent with 4 spaces
- **CSS** — keep styles scoped to the app they belong to, no global resets
- **JS** — vanilla only, no frameworks; use `const`/`let`, avoid `var`
- **No external dependencies** — unless it's already used in the project (e.g. `jsdelivr` fonts)
- **Test in at least one desktop browser** before submitting
- **Don't minify** — keep code readable for review

### 4. Test it

Since there's no build step, just open the file directly in your browser:

```bash
# Example — open the blog app locally
open public/blog/index.html
```

Or serve it with any simple local server:

```bash
npx serve .
# or
python3 -m http.server
```

### 5. Commit your changes

Write a clear, short commit message:

```bash
git commit -m "fix: prevent crash when blog thread is empty"
git commit -m "feat: add dark mode toggle to feeds"
git commit -m "docs: update README with IRC command table"
```

Format: `type: short description` — keep it under 72 characters.

### 6. Push and open a PR

```bash
git push origin your-branch-name
```

Then open a Pull Request on GitHub. In the PR description, please include:

- **What** you changed and **why**
- **Which app(s)** are affected
- **How you tested** it
- Screenshots if there are visual changes

---

## ✅ PR Checklist

Before submitting, run through this quickly:

- [ ] My changes are scoped to the right app folder
- [ ] I tested it in a browser
- [ ] I haven't introduced any external dependencies
- [ ] My code is readable and not minified
- [ ] My commit messages are clear
- [ ] I've updated any relevant docs (README, comments, etc.)

---

## 🎨 Style at a Glance

| Thing | Convention |
|---|---|
| Indentation | 4 spaces |
| Quotes | Double quotes in HTML, single in JS |
| Semicolons | Yes |
| Variable naming | `camelCase` |
| File naming | `lowercase-with-hyphens` |
| Colors | Match existing palette (`#89530e`, `#9a77ff`, etc.) |

---

## 💬 Questions?

Just open a regular issue or reach out to [@alucinari-co2](https://github.com/alucinari-co2) directly. No question is too small. 🙂

---

*Thanks again for contributing — it means a lot!* 🧡
