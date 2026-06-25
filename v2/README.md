# FutureShow v2

Redesigned portfolio/studio site for https://futureshow1.github.io/futureshow/
Strategy, audit and 90-day promotion plan: see **REPORT.md**.

## Deploy (10 minutes)

1. Copy everything from this folder into the `futureshow` repo root
   (overwrite `index.html` and `favicon.svg`; keep existing `films.html`, `projects/`, `archive/`):
   ```bash
   cd "../futureshow"
   cp -R ../futureshow-v2/{index.html,pl.html,films.html,og-image.png,favicon.svg,robots.txt,sitemap.xml,404.html,fonts,build.py,og-image.html} .
   git add -A && git commit -m "v2: conversion-focused redesign" && git push
   ```
2. `films.html` here is the v1 page with the cookie banner/GA script removed and
   canonical + og:image added — it overwrites the old one on deploy. Remaining
   subpages under `projects/` may still reference `cookie-consent.js`; remove
   those `<script>` tags when convenient (or delete `cookie-consent.js` from the
   repo and let the references fail silently).
3. Submit `sitemap.xml` in Google Search Console.

## Editing

- **Edit `index.html` only.** Then regenerate the Polish page:
  ```bash
  python3 build.py   # writes pl.html
  ```
- Bilingual pattern: every visible string lives in a pair
  `<span data-lang="en">…</span><span data-lang="pl">…</span>`.
- Prices/timelines: search `svc__meta` in `index.html`.
- Regenerate the social card after changing `og-image.html`:
  ```bash
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless \
    --screenshot=og-image.png --window-size=1200,630 --hide-scrollbars \
    "file://$PWD/og-image.html"
  ```

## Analytics (no cookie banner needed)

Create a free account at goatcounter.com, then un-comment the snippet at the
bottom of `index.html` (and re-run `build.py`). GoatCounter is cookieless —
no consent banner required under GDPR.

## Custom domain (recommended — see REPORT.md action #1)

`futureshow.pl`, `futureshow.studio`, `futureshow.art` were all available
on 10 Jun 2026. After buying: add a `CNAME` file + GitHub Pages custom-domain
setting, then search-replace `futureshow1.github.io/futureshow` across
`index.html`, `build.py`, `sitemap.xml`, `robots.txt`; re-run `build.py`.
