# FutureShow — gotowe posty na social media

Materiały tekstowe do kampanii promującej najbardziej nośne projekty studia.
Wizualizacje (kwadratowe karty 1080×1080, PL i EN) leżą w `cards/` — przy każdym
poście jest wskazana karta do załączenia. Strategia języka i kanałów: **`DISTRIBUTION.md`**.

**Zasada nadrzędna:** posty PL = Twoje kanały (LinkedIn, Facebook) — ciepła sieć,
natychmiast. Posty EN = społeczności dataviz/civic-tech (Reddit, Hacker News,
Bluesky) — tam, gdzie te projekty stają się viralem i gdzie są klienci z EU.
Nie tłumacz mechanicznie — wersje EN są pisane pod inną publiczność.

> **Ton:** konkret zamiast przymiotników. Każdy post ma jeden hook (pierwsze
> zdanie), jeden dowód (liczba/fakt), jedno CTA. Bez „rewolucyjny", „innowacyjny".

---

## 0 · Jak tego użyć (kolejność publikacji)

| Tydz. | Post | Karta | Kanał główny |
|------|------|-------|--------------|
| 1 | Studio (anchor) | `studio-pl` | LinkedIn + FB |
| 2 | Matryca | `matryca-pl` | LinkedIn + FB → potem EN na Reddit/HN |
| 3 | Hinton / AI | `hinton-pl` | LinkedIn → EN na r/InternetIsBeautiful + Show HN |
| 4 | Sejm Symulator | `sejm-pl` | LinkedIn + FB *(uwaga o URL niżej)* |
| 5 | MNEMO | `mnemo-pl` | LinkedIn + FB |
| 6 | Oil & Gas Atlas | `atlas-pl` | LinkedIn → EN na r/dataisbeautiful |
| (na żądanie) | CardioSim | `cardiosim-pl` | raczej direct outreach niż feed |

Jeden post na tydzień, naprzemiennie temat „ciężki" (Matryca, Sejm) i „ciekawski"
(MNEMO, Hinton). Zawsze dodawaj jedno pytanie na końcu — algorytm karze posty bez
komentarzy.

---

## 1 · STUDIO — post otwierający (repozycjonowanie)

**Karta:** `studio-pl` / `studio-en`

### 🇵🇱 LinkedIn / Facebook
> Przez 25 lat zamieniałem trudne tematy w obrazy — jako reżyser, potem jako historyk sztuki. Od roku robię to w przeglądarce.
>
> FutureShow to moja pracownia interaktywnych doświadczeń: śledztwa, gry edukacyjne, symulacje i filmy AI. Dla muzeów, mediów, edukacji i organizacji.
>
> Reguła jest jedna: **żadnych zależności, śledzenia ani umów serwisowych.** Każdy projekt to jeden zestaw plików, który działa latami na darmowym hostingu, jest dwujęzyczny (PL/EN) i zgodny z RODO z założenia — bo nie zbiera niczego.
>
> 23 zrealizowane projekty. 480+ źródeł pierwotnych. Wszystko klikalne, wszystko żywe.
>
> W kolejnych tygodniach pokażę sześć z nich — od portalu o inwigilacji Big Techu po symulator Sejmu. Zacznijmy od pytania: **który trudny temat najtrudniej Wam pokazać Waszym odbiorcom?**
>
> 👉 futureshow1.github.io/futureshow
>
> #dataviz #civictech #muzea #edukacja #wizualizacjadanych

### 🇬🇧 LinkedIn (EN)
> For 25 years I turned difficult subjects into images — as a film director, then as an art historian. For the past year I've been doing it in the browser.
>
> FutureShow is my studio practice for interactive experiences: investigations, educational games, simulations and AI films — for museums, media, education and NGOs.
>
> One rule: **zero dependencies, zero tracking, zero maintenance contracts.** Every project is one set of files that runs for years on free hosting, bilingual (EN/PL), GDPR-clean by design — because it collects nothing.
>
> 23 shipped projects. 480+ primary sources. All live, all clickable.
>
> Over the next weeks I'll show six of them. First, a question: **what's the hardest idea your institution struggles to make people *feel*?**
>
> 👉 futureshow1.github.io/futureshow
>
> #dataviz #civictech #interactive #museumtech

---

## 2 · MATRYCA — Big Tech Files  *(najmocniejszy, najbardziej nośny)*

**Karty:** `matryca-pl` (hook „Mamy dane o Tobie") / `matryca-en` · **warianty hooka (PL):** `matryca-b` („Kto i jak Cię podgląda?"), `matryca-c` („Przekręty Big Techu") · **Link:** futureshow1.github.io/matryca

### 🇵🇱 LinkedIn / Facebook
> **Mamy dane o Tobie.** Tak Big Tech mówi do Ciebie każdego dnia — tylko nigdy wprost.
>
> Zbudowałem **Matrycę**: wszystko, co chcielibyście wiedzieć o inwigilacji Big Techu, ale baliście się zapytać. 33 największe sprawy ery nadzoru — Cambridge Analytica, Pegasus, Clearview AI, wyciek 533 mln kont Meta — każda zrekonstruowana ze źródeł pierwotnych: decyzji regulatorów, akt sądowych, ujawnień sygnalistów.
>
> W środku: 480+ zlinkowanych źródeł, 16-scenowa oś czasu, 12 sylwetek sygnalistów i 33 nieme animowane explainery. A sam portal? **Mówi o nadzorze, ale sam nie śledzi** — bez cookies, bez analityki, bez jednego trackera.
>
> Dla redakcji i organizacji strażniczych to gotowy fundament śledztwa: każda teza z linkiem do dokumentu.
>
> Sprawdźcie dowolną sprawę 👉 futureshow1.github.io/matryca
>
> Którą z tych historii świat za szybko zapomniał?
>
> #dataviz #dziennikarstwo #BigTech #prywatność #civictech

**Alternatywne pierwsze zdania (do A/B — podmień sam hook, resztę zostaw):**
- *„Kto i jak Cię podgląda? 33 sprawy ery nadzoru, udokumentowane ze źródeł pierwotnych."* → karta `matryca-b`
- *„Przekręty Big Techu — 33 najgłośniejsze sprawy, każda z linkiem do dokumentu."* → karta `matryca-c` (mocno klikalne, ale lżej traktuje wątek „rzetelnego archiwum" — testuj ostrożnie)

### 🇬🇧 LinkedIn (EN) — krótsza, mocniejsza
> **We have your data.** That's what Big Tech tells you every day — just never out loud.
>
> So I built **Matryca**: everything you wanted to know about Big Tech surveillance but were afraid to ask. 33 landmark cases — Cambridge Analytica, Pegasus, Clearview AI, the 533M Meta leak — each from primary sources: regulator decisions, court filings, whistleblower disclosures.
>
> 480+ linked sources. A 16-scene timeline. 12 whistleblower profiles. 33 silent explainers. And the portal itself? **It's about surveillance — but it doesn't surveil.** No cookies, no trackers.
>
> Proof that one person + AI can ship a **newsroom-grade reference portal**. For journalists and watchdogs: an investigation scaffold where every claim links to a document.
>
> 👉 futureshow1.github.io/matryca
>
> #dataviz #journalism #BigTech #privacy #OSINT

### 🇬🇧 Reddit — r/dataisbeautiful *(lub r/privacy, r/InternetIsBeautiful)*
- **Tytuł:** `I built an interactive archive of 33 Big Tech surveillance scandals — every claim sourced to a primary document, and the site itself has zero trackers [OC]`
- **Pierwszy komentarz:** "Made it solo (with AI as a research/build partner) over a few months. Sources are regulator decisions, court filings and whistleblower disclosures — 480+ of them, all linked. Bilingual EN/PL. No cookies/analytics on purpose. Happy to answer questions about the build or the cases."
> Uwaga: r/dataisbeautiful wymaga w komentarzu **narzędzia + źródła danych** (tu: vanilla JS/SVG; źródła = regulatorzy, sądy, sygnaliści). Bez hashtagów, bez „marketingu".

### 🇬🇧 Hacker News — Show HN
- **Tytuł:** `Show HN: Matryca – an archive of 33 Big Tech scandals with zero trackers`
- **Tekst:** "Each case (Cambridge Analytica, Pegasus, Clearview, the 533M Meta leak…) is reconstructed from primary sources — regulator decisions, court filings, whistleblower docs, 480+ linked. The site is one set of static files, no cookies, no analytics, runs on free hosting. Built solo with AI as a partner. Bilingual EN/PL. Feedback on the sourcing model welcome."

### 🐦 Bluesky / X / Mastodon
> "We have your data." 👁 Everything you wanted to know about Big Tech surveillance but were afraid to ask.
> 33 cases · 480+ primary sources · 0 trackers — a portal that doesn't surveil.
> futureshow1.github.io/matryca

---

## 3 · HINTON — AI Explained  *(temat chwili)*

**Karta:** `hinton-pl` / `hinton-en` · **Link:** futureshow1.github.io/hinton-ai-portal

### 🇵🇱 LinkedIn / Facebook
> Wszyscy mówią o AI. Mało kto potrafi pokazać, **jak ona naprawdę myśli** — bez równań i bez ściemy.
>
> Wziąłem wyjaśnienia Geoffreya Hintona (noblisty, „ojca chrzestnego" sieci neuronowych) i zamieniłem je w interaktywny kurs. Klikasz — i widzisz: jak działa sieć neuronowa, czym jest propagacja wsteczna, skąd biorą się halucynacje, na czym polega ryzyko egzystencjalne.
>
> 15 sekcji, animowane wizualizacje, trzy edycje wizualne, dwa języki. Zero logowania, zero reklam.
>
> Dla uczelni i zespołów L&D: **idee z Nobla, po których można chodzić w przeglądarce.**
>
> 👉 futureshow1.github.io/hinton-ai-portal
>
> Co najtrudniej wytłumaczyć Waszym studentom/zespołom w temacie AI?
>
> #AI #edukacja #sztucznainteligencja #dataviz #elearning

### 🇬🇧 LinkedIn (EN)
> Everyone talks about AI. Few can *show* how it actually thinks — without the equations and without the hype.
>
> I turned Nobel laureate Geoffrey Hinton's explanations into an interactive course. You click, and you see it: how a neural net works, what backpropagation does, where hallucinations come from, what "existential risk" actually means.
>
> 15 sections, animated visualizations, two languages, no login. Nobel-grade ideas you can walk through in a browser.
>
> 👉 futureshow1.github.io/hinton-ai-portal
>
> #AI #MachineLearning #edtech #dataviz

### 🇬🇧 Reddit — r/InternetIsBeautiful  *(+ Show HN)*
- **Tytuł (r/IIB):** `An interactive course that visualizes how neural networks actually work — built around Geoffrey Hinton's explanations`
- **Show HN:** `Show HN: An interactive, visual walkthrough of how neural nets work` — "From perceptrons and backprop to hallucinations and existential risk, in 15 clickable sections. No login, no ads, bilingual. Built to be the thing I wish existed when explaining AI to non-engineers."

### 🐦 Bluesky / X
> A Nobel laureate explains AI — but clickable.
> 15 interactive sections, from neural nets to existential risk. No login, no ads.
> futureshow1.github.io/hinton-ai-portal

---

## 4 · SEJM SYMULATOR  *(hiper-lokalny — świetny dla PL)*

**Karta:** `sejm-pl` / `sejm-en`

> ⚠️ **WAŻNE — przeczytaj przed publikacją.** Symulator wisi obecnie pod adresem
> `sejm-178-104-197-58.nip.io`. **Nie wklejaj tego URL-a na social media** — adres
> z numerem IP czyta się jak phishing/malware, LinkedIn i FB mogą go zablokować lub
> ostrzec użytkownika. Dwie opcje:
> 1. **(zalecane)** najpierw przenieś projekt na GitHub Pages / domenę
>    `futureshow.pl` — wtedy linkuj bezpośrednio (mogę pomóc z migracją),
> 2. tymczasowo linkuj do strony studia z opisem projektu i tam podlinkuj symulator.
>
> Karta `sejm-pl` celowo **nie** zawiera adresu nip.io — w stopce jest domena studia.

### 🇵🇱 LinkedIn / Facebook
> 1,76 miliona decyzji posłów. Każde „za", „przeciw" i „wstrzymał się" X kadencji Sejmu — w jednym miejscu, **w przeglądarce**.
>
> Zbudowałem żywą bazę polskiego parlamentu, którą można eksplorować jak grę: 3 834 głosowania, 1 979 ścieżek karier posłów, heatmapa zgodności klubów. Twarde dane publiczne zamienione w coś, przy czym czytelnik **zostaje, udostępnia i cytuje**.
>
> Dla redakcji i organizacji strażniczych to gotowe narzędzie do śledzenia, kto naprawdę głosuje z kim — bez Excela i bez wertowania PDF-ów.
>
> 👉 [link w komentarzu / na stronie studia]
>
> Czyją „ścieżkę kariery" sprawdzicie najpierw?
>
> #civictech #Sejm #dane #dziennikarstwo #przejrzystość

### 🇬🇧 Reddit — r/dataisbeautiful  *(po migracji URL)*
- **Tytuł:** `I made the entire 10th-term Polish Parliament explorable in the browser — 1.76M individual MP votes, career paths and a club-agreement heatmap [OC]`
- **Komentarz:** narzędzie (vanilla JS + SQLite-in-browser/static data), źródło (oficjalne API Sejmu RP), bilingual.

---

## 5 · MNEMO — Sztuka pamięci  *(intelektualnie uwodzicielski)*

**Karta:** `mnemo-pl` / `mnemo-en` · **Link:** futureshow1.github.io/mnemo

### 🇵🇱 LinkedIn / Facebook
> Jak zapamiętać 70 000 cyfr liczby π? Albo całą mowę bez jednej notatki? Ludzie umieli to 2000 lat temu — i Ty też możesz.
>
> **MNEMO** to dwujęzyczny, grywalny portal o sztuce pamięci: 14 rozdziałów od Symonidesa i Cycerona, przez renesansowe teatry pamięci Giordana Bruna, po SuperMemo i mistrzostwa świata w zapamiętywaniu.
>
> Do tego osobna monografia Bruna, interaktywne koło pamięci i **9 trenażerów** — pałace pamięci, system PAO, recytacja π. Bez logowania, bez reklam.
>
> Dla muzeów i instytucji kultury to dowód, że **treść o dziedzictwie może być grą — bez utraty naukowej głębi.**
>
> 👉 futureshow1.github.io/mnemo
>
> #dziedzictwo #muzea #edukacja #pamięć #humanistykacyfrowa

### 🇬🇧 Reddit — r/InternetIsBeautiful
- **Tytuł:** `A bilingual, playable compendium on the art of memory — from Cicero's memory palaces to the World Memory Championships, with 9 trainers you can practice in`
- Idealne też dla r/Renaissance, r/history, społeczności SuperMemo/Anki.

### 🐦 Bluesky / X
> The art of memory, from Cicero to the world championships — as a playable compendium.
> 14 chapters · a Giordano Bruno monograph · 9 trainers. No login, no ads.
> futureshow1.github.io/mnemo

---

## 6 · OIL & GAS ATLAS  *(wizualnie efektowny, geopolityka)*

**Karta:** `atlas-pl` / `atlas-en` · **Link:** futureshow1.github.io/oil-gas-atlas

### 🇵🇱 LinkedIn / Facebook
> Raport o światowej energetyce miałby 80 stron. Ten sam materiał zmieściłem na **jednym ekranie** — interaktywnym.
>
> Atlas globalnej infrastruktury energetycznej: 240+ elementów, 90+ rurociągów, pola wydobywcze, terminale LNG i strategiczne punkty zapalne na sześciu kontynentach. Animowane przepływy, realne dane produkcyjne, kontekst geopolityczny po najechaniu kursorem.
>
> Dla think tanków, redakcji i edukacji: **geopolityka, którą się eksploruje, a nie przewija.**
>
> 👉 futureshow1.github.io/oil-gas-atlas
>
> #geopolityka #energia #dataviz #wizualizacjadanych

### 🇬🇧 Reddit — r/dataisbeautiful  *(+ r/geopolitics, r/MapPorn)*
- **Tytuł:** `Mapped the world's oil & gas infrastructure on one interactive screen — 240+ elements, 90+ pipelines, animated flows across 6 continents [OC]`

### 🐦 Bluesky / X
> The world's entire oil & gas infrastructure on one interactive screen — 240+ assets, 90+ pipelines, animated flows.
> futureshow1.github.io/oil-gas-atlas

---

## 7 · CARDIOSIM Pro  *(wąska grupa — raczej outreach niż feed)*

**Karta:** `cardiosim-pl` / `cardiosim-en` · **Link:** projects/cardiosim-intro.html

> CardioSim jest świetny, ale jego publiczność (dydaktycy medycyny, uczelnie
> medyczne) jest wąska i słabo reaguje na ogólny feed. **Rekomendacja:** użyj karty
> i poniższego tekstu w **bezpośrednim mailu/DM** do wydziałów i kół naukowych,
> a na social tylko jako jeden post „z serii" lub na grupach edukacji medycznej.

### 🇵🇱 (LinkedIn / grupy edu-med / direct)
> Symulator hemodynamiki, który działa w przeglądarce — bez licencji, instalacji i sprzętu laboratoryjnego.
>
> **CardioSim Pro:** miareczkuj beta-blokery, inotropy i wazopresory i obserwuj w czasie rzeczywistym żywe przebiegi EKG / SpO₂ / ABP, pętle PV i diagramy Wiggersa — w 8 scenariuszach klinicznych, na 10 modelowanych lekach.
>
> Dla dydaktyków: interaktywność klasy symulatora, którą student odpala jednym kliknięciem.
>
> #edukacjamedyczna #symulacja #kardiologia #edtech

---

## 8 · Bank hashtagów

**PL:** #dataviz #wizualizacjadanych #civictech #muzea #edukacja #dziennikarstwo
#humanistykacyfrowa #sztucznainteligencja #kulturacyfrowa #NGO

**EN:** #dataviz #datavisualization #civictech #interactive #museumtech #journalism
#OSINT #AI #edtech #digitalhumanities #generativeAI

> Max 3–5 hashtagów na post (LinkedIn karze „chmury" tagów). Reddit i HN — **zero**
> hashtagów. Bluesky — 1–2.
