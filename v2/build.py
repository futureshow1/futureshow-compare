#!/usr/bin/env python3
"""
build.py — generates pl.html from index.html.

Both pages contain the full bilingual markup (data-lang spans); they differ
only in the default <html lang>, head metadata and canonical URL, so Google
indexes a real Polish page and a real English page (hreflang pair), while
the on-page toggle still works instantly on both.

Run after every edit of index.html:  python3 build.py
"""
import re, pathlib

SRC = pathlib.Path(__file__).parent / "index.html"
DST = pathlib.Path(__file__).parent / "pl.html"

PL_TITLE = "FutureShow — Interaktywne doświadczenia, dane i filmy AI | Warszawa"
PL_DESC = ("Warszawskie studio zamieniające badania i dane w interaktywne doświadczenia — "
           "śledztwa, gry edukacyjne, symulacje i filmy AI dla muzeów, mediów, edukacji i NGO w całej UE.")
PL_OG_TITLE = "FutureShow — Złożone idee, interaktywnie."
PL_OG_DESC = ("Interaktywne śledztwa, gry edukacyjne, symulacje i filmy AI dla muzeów, "
              "mediów, edukacji i NGO. Studio z Warszawy, projekty w całej UE.")

html = SRC.read_text(encoding="utf-8")

swaps = [
    ('<html lang="en">', '<html lang="pl">'),
    (re.escape('<title>FutureShow — Interactive Experiences, Data Stories & AI Films | Warsaw</title>'),
     f'<title>{PL_TITLE}</title>'),
    (r'(<meta name="description" content=")[^"]*(">)', rf'\g<1>{PL_DESC}\g<2>'),
    (r'(<meta property="og:title" content=")[^"]*(">)', rf'\g<1>{PL_OG_TITLE}\g<2>'),
    (r'(<meta property="og:description" content=")[^"]*(">)', rf'\g<1>{PL_OG_DESC}\g<2>'),
    (r'(<meta name="twitter:title" content=")[^"]*(">)', rf'\g<1>{PL_OG_TITLE}\g<2>'),
    (r'(<meta name="twitter:description" content=")[^"]*(">)', rf'\g<1>{PL_OG_DESC}\g<2>'),
    (re.escape('<meta property="og:locale" content="en_US">'), '<meta property="og:locale" content="pl_PL">'),
    (re.escape('<meta property="og:locale:alternate" content="pl_PL">'), '<meta property="og:locale:alternate" content="en_US">'),
    (re.escape('<link rel="canonical" href="https://futureshow1.github.io/futureshow/">'),
     '<link rel="canonical" href="https://futureshow1.github.io/futureshow/pl.html">'),
    (re.escape('<meta property="og:url" content="https://futureshow1.github.io/futureshow/">'),
     '<meta property="og:url" content="https://futureshow1.github.io/futureshow/pl.html">'),
]

count = 0
for pattern, repl in swaps:
    if isinstance(pattern, str) and (pattern.startswith("<") or pattern.startswith("\\<")):
        pass
    new, n = re.subn(pattern, repl, html, count=1)
    if n == 0:
        print(f"WARN: no match for {pattern[:60]}…")
    else:
        count += n
    html = new

DST.write_text(html, encoding="utf-8")
print(f"pl.html written ({len(html)//1024} KB, {count} head swaps)")
