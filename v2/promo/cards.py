#!/usr/bin/env python3
"""
FutureShow — social-media card generator.

Renders 1080x1080 PNG promo cards (PL + EN) for the studio's most shareable
projects, in the FutureShow brand system (matches og-image.html).

Usage:
    python3 cards.py            # build all cards into ./cards/ + preview.html
    python3 cards.py matryca    # build only one project (both languages)

Render pipeline = headless Chrome screenshot (same as the repo's og-image).
Edit the PROJECTS list below to change copy/metrics, then re-run.
"""
import html
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "cards")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SIZE = 1080  # square, ideal for LinkedIn / Instagram / Facebook feed

# --- brand palette (from index.html / og-image.html) -----------------------
BG = "#05070c"
TX, TX2, TX3 = "#e9edf5", "#aab4c6", "#7a8499"
CY, PU, GR, YE, RD = "#6fd6ff", "#a78bfa", "#3ddc97", "#f2c94c", "#ff6b6b"

# --- per-project motifs (small line-art, top-right) -------------------------
MOTIFS = {
    "network": '<g stroke="{a}" stroke-width="1.4" fill="none" opacity=".55"><path d="M30 70 L100 28 M100 28 L170 78 M30 70 L92 120 M92 120 L170 78 M92 120 L64 178 M170 78 L156 162 M64 178 L156 162"/></g><circle cx="30" cy="70" r="7" fill="{a}"/><circle cx="100" cy="28" r="6" fill="{b}"/><circle cx="170" cy="78" r="8" fill="{a}"/><circle cx="92" cy="120" r="6" fill="{c}"/><circle cx="64" cy="178" r="6" fill="{b}"/><circle cx="156" cy="162" r="7" fill="{d}"/>',
    "eye": '<g fill="none" stroke="{a}" stroke-width="2.2" opacity=".7"><path d="M16 100 Q100 30 184 100 Q100 170 16 100 Z"/></g><circle cx="100" cy="100" r="34" fill="none" stroke="{a}" stroke-width="2.2"/><circle cx="100" cy="100" r="15" fill="{d}"/><g stroke="{b}" stroke-width="2" opacity=".5"><path d="M100 100 L150 64 M100 100 L60 150 M100 100 L150 140"/></g>',
    "neural": '<g opacity=".85">{nodes}</g>',
    "hemicycle": '<g fill="{a}">{seatsa}</g><g fill="{b}">{seatsb}</g><g fill="{c}">{seatsc}</g><rect x="22" y="150" width="60" height="7" rx="2" fill="{a}"/><rect x="22" y="164" width="96" height="7" rx="2" fill="{b}" opacity=".6"/><rect x="22" y="178" width="44" height="7" rx="2" fill="{c}"/>',
    "wheel": '<g fill="none" stroke="{a}" stroke-width="1.6" opacity=".7"><circle cx="100" cy="100" r="84"/><circle cx="100" cy="100" r="54"/><circle cx="100" cy="100" r="22"/>{spokes}</g>',
    "globe": '<g fill="none" stroke="{a}" stroke-width="1.5" opacity=".7"><circle cx="100" cy="100" r="82"/><ellipse cx="100" cy="100" rx="34" ry="82"/><ellipse cx="100" cy="100" rx="70" ry="82"/><line x1="18" y1="100" x2="182" y2="100"/><path d="M30 62 H170 M30 138 H170"/></g><circle cx="62" cy="74" r="4.5" fill="{d}"/><circle cx="138" cy="120" r="4.5" fill="{d}"/><circle cx="108" cy="150" r="4.5" fill="{d}"/>',
    "ecg": '<g fill="none" stroke="{a}" stroke-width="3" stroke-linejoin="round" opacity=".9"><path d="M14 110 H58 l10 -28 l12 64 l12 -86 l12 86 l10 -36 H190"/></g><g stroke="{d}" stroke-width="2" opacity=".5"><path d="M14 150 H190 M14 70 H190"/></g>',
}


def neural_nodes(a, b):
    cols = [(34, [60, 100, 140]), (100, [44, 86, 128, 170]), (166, [78, 122])]
    nodes, lines = "", ""
    for ci in range(len(cols) - 1):
        x1, ys1 = cols[ci]
        x2, ys2 = cols[ci + 1]
        for y1 in ys1:
            for y2 in ys2:
                lines += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{b}" stroke-width="1" opacity=".3"/>'
    for x, ys in cols:
        for y in ys:
            nodes += f'<circle cx="{x}" cy="{y}" r="6.5" fill="{a}"/>'
    return lines + nodes


def hemicycle(color_keyed):
    import math
    arcs = {"a": [], "b": [], "c": []}
    groups = [("a", 0, 40), ("b", 40, 95), ("c", 95, 180)]
    cx, cy = 100, 150
    for ring, r in enumerate((58, 78, 98)):
        n = 9 + ring * 4
        for i in range(n):
            ang = math.pi * (i + 0.5) / n
            x = cx - r * math.cos(ang)
            y = cy - r * math.sin(ang)
            deg = 180 * (i + 0.5) / n
            for key, lo, hi in groups:
                if lo <= deg < hi:
                    arcs[key].append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="3.6"/>')
                    break
    return arcs


# --- content ----------------------------------------------------------------
# headline: keep <=~46 chars/line; use \n for forced line breaks.
PROJECTS = [
    {
        "id": "studio", "motif": "network", "accent": CY, "accent2": PU,
        "kicker": {"pl": "STUDIO · INTERAKTYWNE DOŚWIADCZENIA",
                   "en": "STUDIO · INTERACTIVE EXPERIENCES"},
        "head": {"pl": "Złożone idee,\nzamienione w {g}interakcję{/g}.",
                 "en": "Complex ideas,\n{g}made interactive{/g}."},
        "sub": {"pl": "Śledztwa, gry edukacyjne, symulacje i filmy AI — dla muzeów, mediów, edukacji i NGO.",
                "en": "Investigations, educational games, simulations & AI films — for museums, media, education & NGOs."},
        "stats": {"pl": [("23", "projekty"), ("480+", "źródła pierwotne"), ("PL·EN", "każdy projekt")],
                  "en": [("23", "shipped projects"), ("480+", "primary sources"), ("PL·EN", "every project")]},
        "url": "futureshow1.github.io/futureshow",
    },
    {
        "id": "matryca", "motif": "eye", "accent": CY, "accent2": RD,
        "kicker": {"pl": "PORTAL ŚLEDCZY · MEDIA / NGO",
                   "en": "INVESTIGATIVE PORTAL · MEDIA / NGO"},
        "head": {"pl": "Mamy dane\n{g}o Tobie{/g}.",
                 "en": "We have\n{g}your data{/g}."},
        "sub": {"pl": "Cambridge Analytica, Pegasus, Clearview AI, wyciek 533 mln kont Meta — udokumentowane ze źródeł pierwotnych. I zero trackerów.",
                "en": "Cambridge Analytica, Pegasus, Clearview AI, the 533M Meta leak — documented from primary sources. And zero trackers."},
        "stats": {"pl": [("33", "udokumentowane sprawy"), ("480+", "źródła pierwotne"), ("33", "nieme explainery")],
                  "en": [("33", "documented cases"), ("480+", "primary sources"), ("33", "silent explainers")]},
        "url": "futureshow1.github.io/matryca",
    },
    {  # alternatywny hook — wariant B
        "id": "matryca-b", "motif": "eye", "accent": CY, "accent2": RD,
        "langs": ("pl",),
        "kicker": {"pl": "PORTAL ŚLEDCZY · MEDIA / NGO"},
        "head": {"pl": "Kto i jak\n{g}Cię podgląda{/g}?"},
        "sub": {"pl": "33 największe sprawy ery nadzoru — Cambridge Analytica, Pegasus, Clearview AI, wyciek 533 mln kont Meta. Wszystko ze źródeł pierwotnych."},
        "stats": {"pl": [("33", "udokumentowane sprawy"), ("480+", "źródła pierwotne"), ("33", "nieme explainery")]},
        "url": "futureshow1.github.io/matryca",
    },
    {  # alternatywny hook — wariant C (najbardziej „clickbaitowy")
        "id": "matryca-c", "motif": "eye", "accent": CY, "accent2": RD,
        "langs": ("pl",),
        "kicker": {"pl": "PORTAL ŚLEDCZY · MEDIA / NGO"},
        "head": {"pl": "{g}Przekręty{/g}\nBig Techu."},
        "sub": {"pl": "33 najgłośniejsze sprawy nadzoru — każda z linkiem do dokumentu. Cambridge Analytica, Pegasus, Clearview AI, wyciek Meta."},
        "stats": {"pl": [("33", "udokumentowane sprawy"), ("480+", "źródła pierwotne"), ("33", "nieme explainery")]},
        "url": "futureshow1.github.io/matryca",
    },
    {
        "id": "hinton", "motif": "neural", "accent": PU, "accent2": CY,
        "kicker": {"pl": "EDUKACJA · WIEDZA O AI",
                   "en": "EDUCATION · AI LITERACY"},
        "head": {"pl": "Noblista tłumaczy AI —\n{g}klikalnie, krok po kroku{/g}.",
                 "en": "A Nobel laureate explains AI —\n{g}clickable, step by step{/g}."},
        "sub": {"pl": "Wyjaśnienia Geoffreya Hintona jako interaktywny kurs: od sieci neuronowych i propagacji wstecznej po ryzyka egzystencjalne.",
                "en": "Geoffrey Hinton's explanations as an interactive course: from neural nets and backprop to existential risk."},
        "stats": {"pl": [("15", "sekcji interaktywnych"), ("3", "edycje wizualne"), ("EN·PL", "dwa języki")],
                  "en": [("15", "interactive sections"), ("3", "visual editions"), ("EN·PL", "two languages")]},
        "url": "futureshow1.github.io/hinton-ai-portal",
    },
    {
        "id": "sejm", "motif": "hemicycle", "accent": CY, "accent2": PU,
        "kicker": {"pl": "CIVIC TECH · DANE PUBLICZNE",
                   "en": "CIVIC TECH · PUBLIC DATA"},
        "head": {"pl": "1,76 mln decyzji posłów.\n{g}W przeglądarce{/g}.",
                 "en": "1.76M MP decisions —\n{g}in your browser{/g}."},
        "sub": {"pl": "Cały Sejm X kadencji, który można eksplorować: głosowania, ścieżki karier i heatmapa zgodności klubów.",
                "en": "The entire 10th-term Sejm, made explorable: floor votes, career paths and a club-agreement heatmap."},
        "stats": {"pl": [("1,76M", "decyzje posłów"), ("3 834", "głosowania"), ("1 979", "ścieżki karier")],
                  "en": [("1.76M", "MP decisions"), ("3,834", "floor votes"), ("1,979", "career paths")]},
        "url": "futureshow1.github.io/futureshow",
    },
    {
        "id": "mnemo", "motif": "wheel", "accent": YE, "accent2": PU,
        "kicker": {"pl": "DZIEDZICTWO · GRYWALNE KOMPENDIUM",
                   "en": "HERITAGE · PLAYABLE COMPENDIUM"},
        "head": {"pl": "Sztuka pamięci — od Cycerona\npo {g}mistrzostwa świata{/g}.",
                 "en": "The art of memory — from Cicero\nto the {g}world championships{/g}."},
        "sub": {"pl": "14 rozdziałów, osobna monografia Giordana Bruna, interaktywne koło pamięci i 9 trenażerów. Bez logowania, bez reklam.",
                "en": "14 chapters, a Giordano Bruno monograph, an interactive memory wheel and 9 trainers. No login, no ads."},
        "stats": {"pl": [("14", "rozdziały PL+EN"), ("9", "trenażery"), ("1", "monografia Bruna")],
                  "en": [("14", "chapters PL+EN"), ("9", "solo trainers"), ("1", "Bruno monograph")]},
        "url": "futureshow1.github.io/mnemo",
    },
    {
        "id": "atlas", "motif": "globe", "accent": YE, "accent2": CY,
        "kicker": {"pl": "WIZUALIZACJA DANYCH · GEOPOLITYKA",
                   "en": "DATA VISUALIZATION · GEOPOLITICS"},
        "head": {"pl": "Cała energetyka świata\nna {g}jednym ekranie{/g}.",
                 "en": "The world's energy grid\non {g}a single screen{/g}."},
        "sub": {"pl": "Interaktywny atlas: rurociągi, pola wydobywcze, terminale LNG i punkty zapalne — z animowanymi przepływami i danymi produkcyjnymi.",
                "en": "An interactive atlas: pipelines, fields, LNG terminals and chokepoints — with animated flows and real production data."},
        "stats": {"pl": [("240+", "elementy infrastruktury"), ("90+", "zmapowane rurociągi"), ("6", "kontynentów")],
                  "en": [("240+", "infrastructure elements"), ("90+", "pipelines mapped"), ("6", "continents")]},
        "url": "futureshow1.github.io/oil-gas-atlas",
    },
    {
        "id": "cardiosim", "motif": "ecg", "accent": GR, "accent2": RD,
        "kicker": {"pl": "SYMULACJA MEDYCZNA · EDUKACJA",
                   "en": "MEDICAL SIMULATION · EDUCATION"},
        "head": {"pl": "Pracownia kardiologiczna\n{g}w przeglądarce{/g}.",
                 "en": "A cardiovascular teaching lab\n{g}in the browser{/g}."},
        "sub": {"pl": "Symulacja w czasie rzeczywistym: 10 leków, żywe przebiegi EKG / SpO₂ / ABP, pętle PV — bez licencji, instalacji i sprzętu.",
                "en": "Real-time simulation: 10 drugs, live ECG / SpO₂ / ABP waveforms, PV loops — no licenses, installs or lab hardware."},
        "stats": {"pl": [("10", "modelowane leki"), ("8", "scenariusze kliniczne"), ("4", "przebiegi na żywo")],
                  "en": [("10", "drugs modelled"), ("8", "clinical scenarios"), ("4", "live waveforms")]},
        "url": "futureshow1.github.io/futureshow",
    },
]


def build_motif(p):
    m = MOTIFS[p["motif"]]
    a, b = p["accent"], p["accent2"]
    if p["motif"] == "neural":
        return m.format(nodes=neural_nodes(a, b))
    if p["motif"] == "hemicycle":
        arcs = hemicycle(None)
        return m.format(a=a, b=b, c=p.get("accent3", GR),
                        seatsa="".join(arcs["a"]), seatsb="".join(arcs["b"]),
                        seatsc="".join(arcs["c"]))
    if p["motif"] == "wheel":
        import math
        spokes = ""
        for i in range(12):
            ang = math.pi * 2 * i / 12
            x1 = 100 + 22 * math.cos(ang); y1 = 100 + 22 * math.sin(ang)
            x2 = 100 + 84 * math.cos(ang); y2 = 100 + 84 * math.sin(ang)
            spokes += f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}"/>'
        return m.format(a=a, spokes=spokes)
    return m.format(a=a, b=b, c=p.get("accent3", GR), d=p["accent2"])


def render_head(text, accent, accent2):
    text = html.escape(text).replace("\n", "<br>")
    text = text.replace("{g}", f'<span class="grad">').replace("{/g}", "</span>")
    return text


def card_html(p, lang):
    head = render_head(p["head"][lang], p["accent"], p["accent2"])
    stats = "".join(
        f'<div class="stat"><b>{html.escape(v)}</b><span>{html.escape(l)}</span></div>'
        for v, l in p["stats"][lang]
    )
    motif = build_motif(p)
    kicker = html.escape(p["kicker"][lang])
    sub = html.escape(p["sub"][lang])
    flag = "PL" if lang == "pl" else "EN"
    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8"><style>
@font-face{{font-family:'Inter';font-weight:100 900;font-display:block;src:url('../fonts/Inter-var-latin.woff2') format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD;}}
@font-face{{font-family:'Inter';font-weight:100 900;font-display:block;src:url('../fonts/Inter-var-latin-ext.woff2') format('woff2');unicode-range:U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF;}}
@font-face{{font-family:'JBMono';font-weight:100 800;font-display:block;src:url('../fonts/JBMono-var-latin.woff2') format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD;}}
@font-face{{font-family:'JBMono';font-weight:100 800;font-display:block;src:url('../fonts/JBMono-var-latin-ext.woff2') format('woff2');unicode-range:U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{width:{SIZE}px;height:{SIZE}px;background:{BG};overflow:hidden;position:relative;font-family:'Inter',sans-serif;color:{TX};}}
.glow1{{position:absolute;width:820px;height:620px;left:-200px;top:-240px;background:radial-gradient(closest-side,{p['accent']}26,transparent);}}
.glow2{{position:absolute;width:760px;height:620px;right:-220px;bottom:-260px;background:radial-gradient(closest-side,{p['accent2']}22,transparent);}}
.grid{{position:absolute;inset:0;opacity:.5;background:repeating-linear-gradient(0deg,transparent 0 63px,rgba(148,163,184,.07) 63px 64px),repeating-linear-gradient(90deg,transparent 0 63px,rgba(148,163,184,.07) 63px 64px);-webkit-mask-image:radial-gradient(ellipse 85% 80% at 40% 42%,#000 28%,transparent 80%);}}
.motif{{position:absolute;right:84px;top:150px;width:200px;height:200px;opacity:.92;}}
.wrap{{position:absolute;inset:0;padding:84px 88px;display:flex;flex-direction:column;}}
.brand{{display:flex;align-items:center;gap:14px;font-family:'JBMono',monospace;font-weight:800;font-size:27px;letter-spacing:.14em;}}
.brand i{{width:12px;height:12px;border-radius:50%;background:{p['accent']};box-shadow:0 0 16px {p['accent']};}}
.brand b{{background:linear-gradient(92deg,{p['accent']},{p['accent2']});-webkit-background-clip:text;background-clip:text;color:transparent;}}
.kicker{{margin-top:60px;font-family:'JBMono',monospace;font-size:18px;font-weight:700;letter-spacing:.2em;color:{p['accent']};}}
h1{{margin-top:30px;font-size:72px;font-weight:800;letter-spacing:-.035em;line-height:1.04;max-width:14ch;}}
h1 .grad{{background:linear-gradient(92deg,{p['accent']},{p['accent2']});-webkit-background-clip:text;background-clip:text;color:transparent;}}
.sub{{margin-top:34px;font-size:27px;line-height:1.42;color:{TX2};font-weight:500;max-width:30ch;}}
.stats{{margin-top:auto;display:flex;gap:54px;}}
.stat b{{display:block;font-family:'JBMono',monospace;font-size:48px;font-weight:800;letter-spacing:-.02em;color:{TX};}}
.stat span{{display:block;margin-top:8px;font-size:15px;text-transform:uppercase;letter-spacing:.1em;color:{TX3};font-weight:600;}}
.foot{{margin-top:42px;padding-top:30px;border-top:1px solid rgba(148,163,184,.16);display:flex;justify-content:space-between;align-items:baseline;font-family:'JBMono',monospace;font-size:20px;color:{TX3};letter-spacing:.04em;}}
.foot b{{color:{p['accent']};font-weight:700;}}
</style></head><body>
<div class="glow1"></div><div class="glow2"></div><div class="grid"></div>
<svg class="motif" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">{motif}</svg>
<div class="wrap">
  <div class="brand"><i></i>FUTURE<b>SHOW</b></div>
  <div class="kicker">{kicker}</div>
  <h1>{head}</h1>
  <div class="sub">{sub}</div>
  <div class="stats">{stats}</div>
  <div class="foot"><span><b>↗</b> {html.escape(p['url'])}</span><span>{flag} · made with AI</span></div>
</div>
</body></html>"""


def render(p, lang):
    tmp = os.path.join(HERE, f"_tmp_{p['id']}_{lang}.html")
    out = os.path.join(OUT, f"{p['id']}-{lang}.png")
    with open(tmp, "w") as f:
        f.write(card_html(p, lang))
    subprocess.run([
        CHROME, "--headless", f"--screenshot={out}",
        f"--window-size={SIZE},{SIZE}", "--force-device-scale-factor=2",
        "--hide-scrollbars", "--default-background-color=00000000",
        "--virtual-time-budget=1500", f"file://{tmp}",
    ], check=True, capture_output=True)
    os.remove(tmp)
    return out


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    projects = [p for p in PROJECTS if not only or p["id"].startswith(only)]
    made = []
    for p in projects:
        for lang in p.get("langs", ("pl", "en")):
            out = render(p, lang)
            made.append(out)
            print("rendered", os.path.relpath(out, HERE))
    # quick preview page (all cards, scaled)
    cells = "".join(
        f'<figure><img src="cards/{p["id"]}-{l}.png"><figcaption>{p["id"]} · {l.upper()}</figcaption></figure>'
        for p in projects for l in p.get("langs", ("pl", "en"))
    )
    with open(os.path.join(HERE, "preview.html"), "w") as f:
        f.write(f"""<!DOCTYPE html><meta charset="utf-8"><title>FutureShow promo cards</title>
<style>body{{background:#0a0e17;color:#aab4c6;font-family:system-ui;margin:0;padding:40px}}
h1{{color:#e9edf5;font-weight:800}}.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:28px;max-width:1200px}}
figure{{margin:0}}img{{width:100%;border-radius:14px;border:1px solid #1a2336;display:block}}
figcaption{{font-family:monospace;font-size:13px;letter-spacing:.1em;text-transform:uppercase;margin-top:10px;color:#7a8499}}</style>
<h1>FutureShow — social cards</h1><div class="grid">{cells}</div>""")
    print(f"\n{len(made)} cards -> {os.path.relpath(OUT, HERE)}/  ·  open preview.html")


if __name__ == "__main__":
    main()
