# Borley Wiki — Schema & Operating Rules

> Read this file at the start of every session. It governs all wiki operations.

## What This Is

A personal LLM-maintained wiki about the Borley Rectory haunting, built by reading *Ghosts of Borley* (Peter Underwood & Paul Tabori, 1973) and any supplementary sources. The LLM maintains all wiki pages. The human curates sources and directs exploration.

---

## Directory Structure

The Obsidian vault root is `borley/`. All paths below are relative to that.

```
borley/                          ← Vault root (.obsidian lives here)
├── CLAUDE.md                    ← This file. Read first every session.
├── index.md                     ← Content catalog. Update on every ingest.
├── log.md                       ← Append-only event log. Update on every operation.
├── raw/                         ← All raw sources (IMMUTABLE — never modify anything here)
│   ├── ghosts of borley/        ← Primary book (Underwood & Tabori, 1973)
│   │   ├── introduction.md
│   │   ├── chapter-1---...md
│   │   └── ...
│   └── <reference-name>/        ← One subfolder per additional source collection
└── wiki/                        ← LLM-maintained wiki (you own this layer entirely)
    ├── overview.md              ← Top-level synthesis: the Borley case in full
    ├── timeline.md              ← Master chronology of all events, cross-source
    ├── people/                  ← One page per significant person
    ├── places/                  ← One page per significant location
    ├── phenomena/               ← One page per type of paranormal phenomenon
    ├── themes/                  ← Analytical / thematic pages
    └── sources/                 ← One wiki summary page per ingested source
```

**Golden rule:** Never modify anything under `raw/`. It is your source of truth.

**Adding a new source collection:** Create `raw/<reference-name>/` and drop the raw files in. Use kebab-case for the folder name (e.g. `raw/harry-price-biography/`, `raw/spr-proceedings-1956/`). Then tell the LLM to ingest a file from that folder.

---

## Page Frontmatter

Every wiki page begins with YAML frontmatter:

```yaml
---
title: "Page Title"
type: person | place | phenomenon | theme | source | overview | timeline
tags: [tag1, tag2]
sources: [gotb-intro, gotb-ch01]   # source slugs that mention this entity
updated: YYYY-MM-DD
---
```

---

## Source Slugs

Slugs are short identifiers used in page frontmatter (`sources: [slug1, slug2]`) to record which raw sources mention an entity. They're also used in log entries and source summary filenames.

**Slug convention:** `<collection-prefix>-<identifier>` — e.g. `gotb-ch01`, `hpb-ch03`, `spr-1956`.

### Ghosts of Borley (prefix: `gotb`)

| Slug | File | Status |
|------|------|--------|
| `gotb-intro` | `raw/ghosts of borley/introduction.md` | ingested |
| `gotb-ch01` | `raw/ghosts of borley/chapter-1---borley-and-the-bulls.md` | ingested |
| `gotb-ch02` | `raw/ghosts of borley/chapter-2---the-smiths-come-and-go.md` | ingested |
| `gotb-ch03` | `raw/ghosts of borley/chapter-3---the-mysteries-of-marianne.md` | ingested |
| `gotb-ch04` | `raw/ghosts of borley/chapter-4---price-at-borley.md` | ingested |
| `gotb-ch05` | `raw/ghosts of borley/chapter-5---tunnels-and-graves.md` | ingested |
| `gotb-ch06` | `raw/ghosts of borley/chapter-6---the-haunting-of-borley-church.md` | ingested |
| `gotb-ch07` | `raw/ghosts of borley/chapter-7---the-persistent-ghosts.md` | ingested |
| `gotb-app` | `raw/ghosts of borley/appendix---the-people-who-lived-at-borley.md` | ingested |

When a new raw file appears that isn't in this table, add it with status `pending` before ingesting.

### The Most Haunted House in England (prefix: `mhh`)

Harry Price, *The Most Haunted House in England* (1940). Price's own account, written while alive.

| Slug | File | Status |
|------|------|--------|
| `mhh-pref` | `raw/most haunted house/preface.md` | ingested |
| `mhh-ch01` | `raw/most haunted house/1-luncheon-interlude.md` | ingested |
| `mhh-ch02` | `raw/most haunted house/2-the-adventures-of-a-journalist.md` | ingested |
| `mhh-ch03` | `raw/most haunted house/3-the-rectors-story.md` | ingested |
| `mhh-ch04` | `raw/most haunted house/4-the-story-of-the-rectory.md` | ingested |
| `mhh-ch05` | `raw/most haunted house/5-the-nuns-walk-and-the-garden.md` | ingested |
| `mhh-ch06` | `raw/most haunted house/6-the-bricked-up-nun-and-other-legends.md` | ingested |
| `mhh-ch07` | `raw/most haunted house/7-an-exciting-day.md` | ingested |
| `mhh-ch08` | `raw/most haunted house/8-a-midnight-seance-in-the-blue-room.md` | ingested |
| `mhh-ch09` | `raw/most haunted house/9-the-misses-bulls-story.md` | ingested |
| `mhh-ch10` | `raw/most haunted house/10-the-strange-adventures-of-edward-cooper.md` | ingested |
| `mhh-ch11` | `raw/most haunted house/11-mr-smith-moves-out.md` | ingested |
| `mhh-ch12` | `raw/most haunted house/12-a-night-of-miracles.md` | ingested |
| `mhh-ch13` | `raw/most haunted house/13-leaves-from-the-foyster-diary.md` | ingested |
| `mhh-ch14` | `raw/most haunted house/14-personal-experiences-of-sir-george-and-lady-whitehouse.md` | ingested |
| `mhh-ch15` | `raw/most haunted house/15-what-i-saw-at-borley-rectory.md` | ingested |
| `mhh-ch16` | `raw/most haunted house/16-a-rectory-for-sale---cheap.md` | ingested |
| `mhh-ch17` | `raw/most haunted house/17-i-acquire-borley-rectory.md` | ingested |
| `mhh-ch18` | `raw/most haunted house/18-we-establish-our-base-room---and-are-disturbed.md` | ingested |
| `mhh-ch19` | `raw/most haunted house/19-enrolling-the-observers.md` | ingested |
| `mhh-ch20` | `raw/most haunted house/20-many-major-phenomena-observed-by-official-observers.md` | ingested |
| `mhh-ch21` | `raw/most haunted house/21-mrs-wilsons-extraordinary-insect.md` | ingested |
| `mhh-ch22` | `raw/most haunted house/22-what-the-mediums-said.md` | ingested |
| `mhh-ch23` | `raw/most haunted house/23-moving-day-and-a-golden-apport.md` | ingested |
| `mhh-ch24` | `raw/most haunted house/24-the-marianne-messages.md` | ingested |
| `mhh-ch25` | `raw/most haunted house/25-try-the-spirits.md` | ingested |
| `mhh-ch26` | `raw/most haunted house/26-the-voice-of-planchette.md` | ingested |
| `mhh-ch27` | `raw/most haunted house/27-sunex-amures-says-he-will-burn-the-rectory.md` | ingested |
| `mhh-ch28` | `raw/most haunted house/28-the-rectorys-new-owner.md` | ingested |
| `mhh-ch29` | `raw/most haunted house/29-the-rectory-destroyed-by-fire.md` | ingested |
| `mhh-ch30` | `raw/most haunted house/30-the-ghosts-survive.md` | ingested |
| `mhh-ch31` | `raw/most haunted house/31-can-the-phenomena-be-explained.md` | ingested |
| `mhh-ch32` | `raw/most haunted house/32-the-case-for-the-jury.md` | ingested |
| `mhh-app-a` | `raw/most haunted house/appendix-a-haunted-house-declaration-form.md` | ingested |
| `mhh-app-b` | `raw/most haunted house/appendix-b-the-blue-book.md` | ingested |
| `mhh-app-c` | `raw/most haunted house/appendix-c-digest-of-official-observers-reports.md` | ingested |
| `mhh-app-d` | `raw/most haunted house/appendix-d-analysis-of-phenomena.md` | ingested |
| `mhh-app-e` | `raw/most haunted house/appendix-e-.md` | ingested |
| `mhh-app-f` | `raw/most haunted house/appendix-f-chronological-record-of-principal-events.md` | ingested |

### Borley Rectory: Ghosts That Will Not Die (prefix: `gtwnd`)

Vincent O'Neil (The Son of Borley), web-published. Personal account plus full Swanson interview transcripts, Foyster manuscript extracts, Owen/Mitchell 1979 report, and post-fire chronology through 1996.

| Slug | File | Status |
|------|------|--------|
| `gtwnd-intro` | `raw/borley-rectory-ghosts-that-will-not-die/introduction.md` | ingested |
| `gtwnd-ov` | `raw/borley-rectory-ghosts-that-will-not-die/overview.md` | ingested |
| `gtwnd-ch01` | `raw/borley-rectory-ghosts-that-will-not-die/chapter-1.md` | ingested |
| `gtwnd-ch02` | `raw/borley-rectory-ghosts-that-will-not-die/chapter-2.md` | ingested |
| `gtwnd-ch03` | `raw/borley-rectory-ghosts-that-will-not-die/chapter-3.md` | ingested |
| `gtwnd-ch04` | `raw/borley-rectory-ghosts-that-will-not-die/chapter-4.md` | ingested |
| `gtwnd-ch05` | `raw/borley-rectory-ghosts-that-will-not-die/chapter-5.md` | ingested |
| `gtwnd-ch06` | `raw/borley-rectory-ghosts-that-will-not-die/chapter-6.md` | ingested |
| `gtwnd-ch07` | `raw/borley-rectory-ghosts-that-will-not-die/chapter-7.md` | ingested |
| `gtwnd-ch08` | `raw/borley-rectory-ghosts-that-will-not-die/chapter-8.md` | ingested |
| `gtwnd-ch09` | `raw/borley-rectory-ghosts-that-will-not-die/chapter-9.md` | ingested |
| `gtwnd-ch10` | `raw/borley-rectory-ghosts-that-will-not-die/chapter-10.md` | ingested |
| `gtwnd-ch11` | `raw/borley-rectory-ghosts-that-will-not-die/chapter-11.md` | ingested |

### The Haunting of Borley Rectory (prefix: `hbrs`)

Sean O'Connor. Narrative history/biography integrating social context — class, race, colonial return, interwar anxieties, agricultural depression, WWII. Skeptical framing; new biographical detail on all major figures; covers Marianne's full post-Borley life to 1992.

| Slug | File | Status |
|------|------|--------|
| `hbrs-fw` | `raw/haunting_borley_rectory_soc/foreword.md` | ingested |
| `hbrs-pro` | `raw/haunting_borley_rectory_soc/prologue.md` | ingested |
| `hbrs-ch01` | `raw/haunting_borley_rectory_soc/chapter-1-a-first-class-ghost-story.md` | ingested |
| `hbrs-ch02` | `raw/haunting_borley_rectory_soc/chapter-2-the-thirteenth-man.md` | ingested |
| `hbrs-ch03` | `raw/haunting_borley_rectory_soc/chapter-3-sixteen-hours-of-thrills.md` | ingested |
| `hbrs-ch04` | `raw/haunting_borley_rectory_soc/chapter-4-ancient-and-modern.md` | ingested |
| `hbrs-ch05` | `raw/haunting_borley_rectory_soc/chapter-5-a-clergymans-son-a-clergymans-daughter.md` | ingested |
| `hbrs-ch06` | `raw/haunting_borley_rectory_soc/chapter-6-murder-at-the-parsonage.md` | ingested |
| `hbrs-ch07` | `raw/haunting_borley_rectory_soc/chapter-7-confessions-of-a-ghost-hunter.md` | ingested |
| `hbrs-ch08` | `raw/haunting_borley_rectory_soc/chapter-8-the-rectors-wife.md` | ingested |
| `hbrs-ch09` | `raw/haunting_borley_rectory_soc/chapter-9-they-settle-in-the-house.md` | ingested |
| `hbrs-ch10` | `raw/haunting_borley_rectory_soc/chapter-10-the-evil-in-the-dark-closet.md` | ingested |
| `hbrs-ch11` | `raw/haunting_borley_rectory_soc/chapter-11-things-that-go-bump-in-the-night.md` | ingested |
| `hbrs-ch12` | `raw/haunting_borley_rectory_soc/chapter-12-the-return-of-harry-price.md` | ingested |
| `hbrs-ch13` | `raw/haunting_borley_rectory_soc/chapter-13-the-worlds-best-ghost-story.md` | ingested |
| `hbrs-ch14` | `raw/haunting_borley_rectory_soc/chapter-14-the-alleged-haunting-at-b-rectory.md` | ingested |
| `hbrs-ch15` | `raw/haunting_borley_rectory_soc/chapter-15-the-end-of-borley-rectory.md` | ingested |
| `hbrs-ch16` | `raw/haunting_borley_rectory_soc/chapter-16-the-most-haunted-house-in-england.md` | ingested |
| `hbrs-ch17` | `raw/haunting_borley_rectory_soc/chapter-17-search-for-truth.md` | ingested |
| `hbrs-ch18` | `raw/haunting_borley_rectory_soc/chapter-18-the-widow-of-borley.md` | ingested |
| `hbrs-ch19` | `raw/haunting_borley_rectory_soc/chapter-19-the-borley-report.md` | ingested |
| `hbrs-ch20` | `raw/haunting_borley_rectory_soc/chapter-20-most-haunted.md` | ingested |
| `hbrs-aft` | `raw/haunting_borley_rectory_soc/afterword.md` | ingested |

### Sidelights on Borley Rectory (prefix: `slbr`)

Andrew Clarke (Foxearth.org.uk). Web-published essay collection. 21 analytical essays by an East Anglian local historian and Foxearth resident (3 miles from Borley). Deep primary-source research, local knowledge, and prosaic explanations for phenomena. Clarke died recently.

| Slug | File | Status |
|------|------|--------|
| `slbr-01` | `raw/sidelights-borley-rectory/1-introduction.md` | ingested |
| `slbr-02` | `raw/sidelights-borley-rectory/2-the-thump-ghosts.md` | ingested |
| `slbr-03` | `raw/sidelights-borley-rectory/3-in-the-bedroom-with-harry-price.md` | ingested |
| `slbr-04` | `raw/sidelights-borley-rectory/4-legless-at-borley-rectory.md` | ingested |
| `slbr-05` | `raw/sidelights-borley-rectory/5-borley-rectory-and-the-travelling-scissorman.md` | ingested |
| `slbr-06` | `raw/sidelights-borley-rectory/6-borley-rectory-and-the-green-baize-door.md` | ingested |
| `slbr-07` | `raw/sidelights-borley-rectory/7-the-foyster-diaries.md` | ingested |
| `slbr-08` | `raw/sidelights-borley-rectory/8-borley-rectory-and-the-smell-of-fear.md` | ingested |
| `slbr-09` | `raw/sidelights-borley-rectory/9-borley-bellsheet.md` | ingested |
| `slbr-10` | `raw/sidelights-borley-rectory/10-edwin-and-the-high-water-mark.md` | ingested |
| `slbr-11` | `raw/sidelights-borley-rectory/11-bullsheet-the-bulls-at-borley-rectory.md` | ingested |
| `slbr-12` | `raw/sidelights-borley-rectory/12-prices-second-visit.md` | ingested |
| `slbr-13` | `raw/sidelights-borley-rectory/13-a-demented-female-and-the-marks-tey-spiritualist-circle.md` | ingested |
| `slbr-14` | `raw/sidelights-borley-rectory/14-lawless-the-lodger.md` | ingested |
| `slbr-15` | `raw/sidelights-borley-rectory/15-the-well-tank-bothers-me.md` | ingested |
| `slbr-16` | `raw/sidelights-borley-rectory/16-things-that-go-creak-in-the-night.md` | ingested |
| `slbr-17` | `raw/sidelights-borley-rectory/17-tunnels.md` | ingested |
| `slbr-18` | `raw/sidelights-borley-rectory/18-two-ghost-stories.md` | ingested |
| `slbr-19` | `raw/sidelights-borley-rectory/19-the-icy-hand.md` | ingested |
| `slbr-20` | `raw/sidelights-borley-rectory/20-no-hand-was-visible.md` | ingested |
| `slbr-21` | `raw/sidelights-borley-rectory/21-where-was-borley-rectory-.md` | ingested |

### The Borley Rectory Companion (prefix: `brc`)

Paul Adams, Eddie Brazil & Peter Underwood (2009). The most comprehensive A–Z encyclopaedic reference work on the entire case. Structure: Introduction + Part I narrative overview + Part II A–Z dictionary (A–W/Z) + Part III chronology + 2 appendices.

| Slug | File | Status |
|------|------|--------|
| `brc-intro` | `raw/borley-rectory-companion/introduction.md` | ingested |
| `brc-i` | `raw/borley-rectory-companion/i-the-haunting-of-borley-rectory.md` | ingested |
| `brc-ii-ab` | `raw/borley-rectory-companion/ii-the-borley-haunting-a-b.md` | ingested |
| `brc-ii-cd` | `raw/borley-rectory-companion/ii-the-borley-haunting-c-d.md` | ingested |
| `brc-ii-ef` | `raw/borley-rectory-companion/ii-the-borley-haunting-e-f.md` | ingested |
| `brc-ii-gh` | `raw/borley-rectory-companion/ii-the-borley-haunting-g-h.md` | ingested |
| `brc-ii-ij` | `raw/borley-rectory-companion/ii-the-borley-haunting-i-j.md` | ingested |
| `brc-ii-kl` | `raw/borley-rectory-companion/ii-the-borley-haunting-k-l.md` | ingested |
| `brc-ii-mn` | `raw/borley-rectory-companion/ii-the-borley-haunting-m-n.md` | ingested |
| `brc-ii-op` | `raw/borley-rectory-companion/ii-the-borley-haunting-o-p.md` | ingested |
| `brc-ii-qr` | `raw/borley-rectory-companion/ii-the-borley-haunting-q-r.md` | ingested |
| `brc-ii-st` | `raw/borley-rectory-companion/ii-the-borley-haunting-s-t.md` | ingested |
| `brc-ii-uv` | `raw/borley-rectory-companion/ii-the-borley-haunting-u-v.md` | ingested |
| `brc-ii-wz` | `raw/borley-rectory-companion/ii-the-borley-haunting-w-z.md` | ingested |
| `brc-iii` | `raw/borley-rectory-companion/iii-a-borley-rectory-chronology.md` | ingested |
| `brc-app1` | `raw/borley-rectory-companion/appendix-1-harry-prices-blue-book-of-instructions.md` | ingested |
| `brc-app2` | `raw/borley-rectory-companion/appendix-2-haunted-house-declaration-forms.md` | ingested |

### Borley Postscript (prefix: `bps`)

Peter Underwood (2000s). Unpublished material compiled after sixty years of involvement — scripts of lectures and broadcasts, personal testimonies from witnesses interviewed directly, a 1947 BBC radio broadcast script, the anonymous 1932 phantom-coach letter, the full Montague Elelman "piece of Borley wood" account, Underwood's own 1947 first-visit report, a refutation of Louis Mayerling's hoax book, personal recollections from Ambrose, Harley, L'Estrange, Luget and the Turners, multiple visits to Chilton Lodge (the Bull sisters), John Randall's defence of Harry Price, and an account of visiting Constance Price at Arun Bank in 1968.

| Slug | File | Status |
|------|------|--------|
| `bps-intro` | `raw/borley-postscript/introduction.md` | ingested |
| `bps-01` | `raw/borley-postscript/1-a-pictorial-history-of-the-borley-haunting.md` | ingested |
| `bps-02` | `raw/borley-postscript/2-the-haunted-rectory.md` | ingested |
| `bps-03` | `raw/borley-postscript/3-the-anonymous-letter.md` | ingested |
| `bps-04` | `raw/borley-postscript/4-lucy-meeker-on-harry-price.md` | ingested |
| `bps-05` | `raw/borley-postscript/5-my-chip-off-the-borley-block.md` | ingested |
| `bps-06` | `raw/borley-postscript/6-my-first-visit-to-borley-in-1947.md` | ingested |
| `bps-07` | `raw/borley-postscript/7-the-faker-of-borley.md` | ingested |
| `bps-08` | `raw/borley-postscript/8-personal-recollections-of-some-borley-witnesses-.md` | ingested |
| `bps-09` | `raw/borley-postscript/9-visits-to-chiltern-lodge.md` | ingested |
| `bps-10` | `raw/borley-postscript/10-john-l-randall-on-harry-price-and-borley.md` | ingested |
| `bps-11` | `raw/borley-postscript/11-welcome-to-harry-prices-home.md` | ingested |

### The End of Borley Rectory (prefix: `ebr`)

Harry Price (1946). Price's sequel to *The Most Haunted House in England* — covering 1939–1945: new witnesses post-fire, the Cambridge Commission (58 persons, 25 nights), Canon Phythian-Adams's wall-writing analysis ('trompée', 'Well-Tank-Bottom-Me'), full Planchette séance transcripts from the Locked Book, the August 1943 cellar excavation (human remains of a young woman found), the Miraculous Medal and gold pendant, Arabella Waldegrave as alternative nun-ghost theory, the reburial of the supposed Marie Lairre at Liston Churchyard May 29 1945, demolition of the Rectory, and legal assessments by Sir Ernest Jelf and Sir Albion Richardson.

| Slug | File | Status |
|------|------|--------|
| `ebr-pref` | `raw/end-borley-rectory/preface.md` | ingested |
| `ebr-ch01` | `raw/end-borley-rectory/1-the-story-of-the-most-haunted-house-in-england.md` | ingested |
| `ebr-ch02` | `raw/end-borley-rectory/2-priests-vs-poltergeists-some-attempts-at-exorcism.md` | ingested |
| `ebr-ch03` | `raw/end-borley-rectory/3-an-exciting-night.md` | ingested |
| `ebr-ch04` | `raw/end-borley-rectory/4-another-cloud-of-witnesses.md` | ingested |
| `ebr-ch05` | `raw/end-borley-rectory/5-the-enchanted-tea-garden.md` | ingested |
| `ebr-ch06` | `raw/end-borley-rectory/6-a-century-of-evidence.md` | ingested |
| `ebr-ch07` | `raw/end-borley-rectory/7-some-readers-queries-answered.md` | ingested |
| `ebr-ch08` | `raw/end-borley-rectory/8-the-locked-book.md` | ingested |
| `ebr-ch09` | `raw/end-borley-rectory/9-the-cambridge-commission.md` | ingested |
| `ebr-ch10` | `raw/end-borley-rectory/10-suggested-causation-of-the-borley-phenomena.md` | ingested |
| `ebr-ch11` | `raw/end-borley-rectory/11-deciphering-the-marianne-appeals.md` | ingested |
| `ebr-ch12` | `raw/end-borley-rectory/12-the-waldegraves.md` | ingested |
| `ebr-ch13` | `raw/end-borley-rectory/13-clues-and-indicators.md` | ingested |
| `ebr-ch14` | `raw/end-borley-rectory/14-truth-at-the-bottom-of-a-well.md` | ingested |
| `ebr-ch15` | `raw/end-borley-rectory/15-the-miraculous-medal.md` | ingested |
| `ebr-ch16` | `raw/end-borley-rectory/16-new-light-on-the-borley-haunt.md` | ingested |
| `ebr-ch17` | `raw/end-borley-rectory/17-strange-occurrences-in-a-london-studio.md` | ingested |
| `ebr-ch18` | `raw/end-borley-rectory/18-planchette-vindicated.md` | ingested |
| `ebr-ch19` | `raw/end-borley-rectory/19-the-end-of-the-rectory-the-end-of-the-nun.md` | ingested |
| `ebr-ch20` | `raw/end-borley-rectory/20-borley-and-ballechin.md` | ingested |
| `ebr-ch21` | `raw/end-borley-rectory/21-miracles-and-their-mechanics.md` | ingested |
| `ebr-ch22` | `raw/end-borley-rectory/22-only-one-conclusion.md` | ingested |

### The Haunting of Borley Rectory: A Critical Survey of the Evidence (prefix: `spr`)

Dr E. J. Dingwall, Mrs K. M. Goldney, Mr Trevor H. Hall (1956). The definitive skeptical document: SPR-commissioned critical survey using Price's own files (from University of London), interviews with 30+ surviving witnesses, and access to unpublished correspondence. Concludes Price manipulated evidence and probably produced fraudulent phenomena; Marianne Foyster almost certainly responsible for Foyster period; the 1943 bone excavation suspicious; the "flying brick" (1944) was demolition workmen.

| Slug | File | Status |
|------|------|--------|
| `spr-note` | `raw/spr-haunting-br/note.md` | ingested |
| `spr-pref` | `raw/spr-haunting-br/preface.md` | ingested |
| `spr-i` | `raw/spr-haunting-br/i-introduction-the-building-of-the-legend.md` | ingested |
| `spr-ii` | `raw/spr-haunting-br/ii-borley-rectory-its-topography-and-legends.md` | ingested |
| `spr-iii` | `raw/spr-haunting-br/iii-the-bull-incumbencies.md` | ingested |
| `spr-iv` | `raw/spr-haunting-br/iv-the-smith-incumbency-and-harry-price.md` | ingested |
| `spr-v` | `raw/spr-haunting-br/v-the-foyster-incumbency.md` | ingested |
| `spr-vi` | `raw/spr-haunting-br/vi-the-price-tenancy.md` | ingested |
| `spr-vii` | `raw/spr-haunting-br/vii-later-borley.md` | ingested |
| `spr-viii` | `raw/spr-haunting-br/viii-conclusions.md` | ingested |
| `spr-diary` | `raw/spr-haunting-br/diary-of-events-and-abstract.md` | ingested |

### The Enigma of Borley Rectory (prefix: `enbr`)

Ivan Banks (Maidstone, Kent, 1994). Pro-Price account with original archival research. Preface, introduction, acknowledgements, chapters 1–27. 30 files total. Key contributions: syphilis of Henry Bull documented; Kate Boreham death investigation; Sir Edward Waldegrave as ghost candidate; Sudbury Priory; Barbara Waldegrave as nun; full séance transcripts from Locked Book; Gregson arson confirmation.

| Slug | File | Status |
|------|------|--------|
| `enbr-pref` | `raw/enigma-borley-rectory/preface.md` | ingested |
| `enbr-intro` | `raw/enigma-borley-rectory/introduction.md` | ingested |
| `enbr-ack` | `raw/enigma-borley-rectory/acknowledgements.md` | ingested |
| `enbr-ch01` | `raw/enigma-borley-rectory/1---borley-and-its-surroundings.md` | ingested |
| `enbr-ch02` | `raw/enigma-borley-rectory/2---the-building-of-borley-rectory.md` | ingested |
| `enbr-ch03` | `raw/enigma-borley-rectory/3-the-hauntings-1863---1927.md` | ingested |
| `enbr-ch04` | `raw/enigma-borley-rectory/4-the-nun-makes-her-appearance.md` | ingested |
| `enbr-ch05` | `raw/enigma-borley-rectory/5-edward-cooper-and-the-stable-cottage.md` | ingested |
| `enbr-ch06` | `raw/enigma-borley-rectory/6-the-story-continues-1928---1935.md` | ingested |
| `enbr-ch07` | `raw/enigma-borley-rectory/7-the-final-pre-war-years-1936---1939.md` | ingested |
| `enbr-ch08` | `raw/enigma-borley-rectory/8-ghosts-among-the-ruins-the-site-from-1939---1945.md` | ingested |
| `enbr-ch09` | `raw/enigma-borley-rectory/9-the-reverend-henry-dawson-bull.md` | ingested |
| `enbr-ch10` | `raw/enigma-borley-rectory/10-the-reverend-henry-foyster-bull.md` | ingested |
| `enbr-ch11` | `raw/enigma-borley-rectory/11-the-reverend-guy-and-mabel-smith.md` | ingested |
| `enbr-ch12` | `raw/enigma-borley-rectory/12-the-reverend-lionel-foyster-and-marianne.md` | ingested |
| `enbr-ch13` | `raw/enigma-borley-rectory/13-the-tenancy-of-harry-price.md` | ingested |
| `enbr-ch14` | `raw/enigma-borley-rectory/14-gregson-and-the-fire---the-rectorys-last-tenant.md` | ingested |
| `enbr-ch15` | `raw/enigma-borley-rectory/15-james-turner-and-the-rectory-cottage.md` | ingested |
| `enbr-ch16` | `raw/enigma-borley-rectory/16-bones-and-a-tunnel-an-archaeological-aspect.md` | ingested |
| `enbr-ch17` | `raw/enigma-borley-rectory/17-the-monastery-controversy.md` | ingested |
| `enbr-ch18` | `raw/enigma-borley-rectory/18-a-lost-ghost-and-sir-edward-waldegrave.md` | ingested |
| `enbr-ch19` | `raw/enigma-borley-rectory/19-the-enigmas-of-marie-lairre-a-search-for-the-borley-nun.md` | ingested |
| `enbr-ch20` | `raw/enigma-borley-rectory/20-the-katie-boreham-mystery.md` | ingested |
| `enbr-ch21` | `raw/enigma-borley-rectory/21-some-other-possibilities.md` | ingested |
| `enbr-ch22` | `raw/enigma-borley-rectory/22-the-screaming-girl-mystery.md` | ingested |
| `enbr-ch23` | `raw/enigma-borley-rectory/23-the-seances.md` | ingested |
| `enbr-ch24` | `raw/enigma-borley-rectory/24-some-views-from-contemporaries.md` | ingested |
| `enbr-ch25` | `raw/enigma-borley-rectory/25-a-resume-of-some-50-years-of-borley-chronicles.md` | ingested |
| `enbr-ch26` | `raw/enigma-borley-rectory/26-glanvilles-locked-book.md` | ingested |
| `enbr-ch27` | `raw/enigma-borley-rectory/27-in-conclusion.md` | ingested |

**All *The Enigma of Borley Rectory* files fully ingested.**

### Borley Rectory: The Final Analysis (prefix: `brfa`)

Edward Babbs (EB) and Claudine Mathias (CM). Introduction by Alan Wesencraft. Local-knowledge book: EB is a former SPR member with ~40 years of interest in the case; CM is the widow of the last rector of Borley and Liston (Rev Lanfranc Mathias, incumbent 1955–1967). Interviews with many previously undocumented local witnesses. Key material: 1988 discovery of the crypt under Borley church; 1957 Tudor tunnel discovery; Alan Gregson letters (fire was accidental); Dodie Bull diary; many previously unpublished sightings; extensive review of Robert Wood's *The Widow of Borley* and the SPR report; ley-lines hypothesis; complete rectors' list 1236–1996.

| Slug | File | Status |
|------|------|--------|
| `brfa-pref` | `raw/final-analysis/preface.md` | ingested |
| `brfa-intro` | `raw/final-analysis/introduction.md` | ingested |
| `brfa-ch01` | `raw/final-analysis/1-the-geography-and-the-history.md` | ingested |
| `brfa-ch02` | `raw/final-analysis/2-the-trees-for-the-wood.md` | ingested |
| `brfa-ch03` | `raw/final-analysis/3-the-bull-family.md` | ingested |
| `brfa-ch04` | `raw/final-analysis/4-the-smiths-and-the-foysters.md` | ingested |
| `brfa-ch05` | `raw/final-analysis/5-the-henning-incumbency-what-the-rector-had-to-say.md` | ingested |
| `brfa-ch06` | `raw/final-analysis/6-the-famous-harry-price.md` | ingested |
| `brfa-ch07` | `raw/final-analysis/7-the-last-rector-of-borley-and-liston.md` | ingested |
| `brfa-ch08` | `raw/final-analysis/8-the-last-widow-of-borley.md` | ingested |
| `brfa-ch09` | `raw/final-analysis/9-the-vanishing-lady-and-other-reports.md` | ingested |
| `brfa-ch10` | `raw/final-analysis/10-further-experiences-and-an-exciting-discovery.md` | ingested |
| `brfa-ch11` | `raw/final-analysis/11-the-documents-and-what-they-tell-us.md` | ingested |
| `brfa-ch12` | `raw/final-analysis/12-what-is-the-truth-summary-and-conclusions.md` | ingested |
| `brfa-app` | `raw/final-analysis/appendices.md` | ingested |

### Fifteen Months in a Haunted House — Foyster Manuscripts (prefix: `15mhh`)

The two primary Foyster manuscripts in their original forms: Lionel Foyster's *Diary of Occurrences* (Writing B, three instalments, 1931) and *The Record of an Experience* / "Fifteen Months in a Haunted House" (Writing C, novelized account with pseudonyms, 1933–34). With foreword by Peter Underwood and introduction by Vincent O'Neil.

| Slug | File | Status |
|------|------|--------|
| `15mhh-fw` | `raw/15-months-in-a-haunted-house/foreword.md` | ingested |
| `15mhh-intro` | `raw/15-months-in-a-haunted-house/introduction.md` | ingested |
| `15mhh-doc` | `raw/15-months-in-a-haunted-house/diary-of-occurrences.md` | ingested |
| `15mhh-rec` | `raw/15-months-in-a-haunted-house/the-record-of-an-experience.md` | ingested |

**All *Fifteen Months in a Haunted House* files fully ingested.**

### An Examination of the 'Borley Report' — Hastings Report (prefix: `hast`)

R.J. Hastings (1969). SPR Proceedings Vol. 55, Part 201. The definitive scholarly rebuttal of the 1956 HBR. Ten chapters covering every major fraud allegation against Harry Price, plus appendices with Sutton's signed statement, Gauld's 1966 interview notes, and Dom Richard Whitehouse's 1956 letter to Underwood.

| Slug | File | Status |
|------|------|--------|
| `hast-ch01` | `raw/hastings-report/chapter-1-the-sutton-affair-allegations.md` | ingested |
| `hast-ch02` | `raw/hastings-report/chapter-2-the-sutton-affair-missing-links.md` | ingested |
| `hast-ch03` | `raw/hastings-report/chapter-3-the-testimony-of-mrs-smith.md` | ingested |
| `hast-ch04` | `raw/hastings-report/chapter-4-the-curious-matter-of-the-medals.md` | ingested |
| `hast-ch05` | `raw/hastings-report/chapter-5-the-excavated-bone-fragments.md` | ingested |
| `hast-ch06` | `raw/hastings-report/chapter-6-the-suspicions-of-henry-douglas-home.md` | ingested |
| `hast-ch07` | `raw/hastings-report/chapter-7-the-alleged-duplicity-of-harry-price-concerning-the-foyster-phenomena.md` | ingested |
| `hast-ch08` | `raw/hastings-report/chapter-8-the-flying-brick.md` | ingested |
| `hast-ch09` | `raw/hastings-report/chapter-9-minor-allegations.md` | ingested |
| `hast-ch10` | `raw/hastings-report/chapter-10-prices-aims-and-evidence-of-character.md` | ingested |
| `hast-app` | `raw/hastings-report/appendices.md` | ingested |
| `hast-chron` | `raw/hastings-report/chronology-of-principal-events-at-borley-and-other-events-affecting-relations-between-price-and-his-critics.md` | ingested |

**All *Hastings Report* files fully ingested.**

### New Horizons Foundation — Borley Rectory Report (prefix: `nhf`)

Iris Owen and Pauline Mitchell / New Horizons Foundation, October 1986. The published version of their 1978 conversation with Marianne Foyster (funded by Perrot Warwick Fellowship, Trinity College Cambridge; published after Marianne's death in 1992). Introduces the "admixture of truth and fraud" framework.

| Slug | File | Status |
|------|------|--------|
| `nhf-intro` | `raw/new-horizons/introduction.md` | ingested |
| `nhf-legend` | `raw/new-horizons/the-legend-of-borley-rectory.md` | ingested |

**All *New Horizons Foundation* files fully ingested.**

### The Widow of Borley (prefix: `wob`)

Robert Wood (c. late 1980s/early 1990s). A skeptical biography of Marianne Foyster by an author who grew up near Borley (Acton, Suffolk). 14 chapters. Key: insurance company repudiation of Gregson's fire claim documented; Wood's thesis that Foyster was a voyeuristic accomplice; Marianne's early life; Willy Palmer as confederate; Eileen Garrett's interview notes on murder question.

| Slug | File | Status |
|------|------|--------|
| `wob-intro` | `raw/widow-of-borley/introduction.md` | ingested |
| `wob-ch01` | `raw/widow-of-borley/1-borley-rectory-and-its-ghosts.md` | ingested |
| `wob-ch02` | `raw/widow-of-borley/2-harry-and-the-poltergeists.md` | ingested |
| `wob-ch03` | `raw/widow-of-borley/3-going-bump-in-the-night.md` | ingested |
| `wob-ch04` | `raw/widow-of-borley/4-the-most-haunted-house-in-england.md` | ingested |
| `wob-ch05` | `raw/widow-of-borley/5-hall-of-fame.md` | ingested |
| `wob-ch06` | `raw/widow-of-borley/6-mariannes-early-life.md` | ingested |
| `wob-ch07` | `raw/widow-of-borley/7-mrs-lionel-algernon-foyster.md` | ingested |
| `wob-ch08` | `raw/widow-of-borley/8-fifteen-months-in-a-haunted-house.md` | ingested |
| `wob-ch09` | `raw/widow-of-borley/9-the-writing-on-the-wall.md` | ingested |
| `wob-ch10` | `raw/widow-of-borley/10-the-wildgoose-the-greenwood-and-the-monk.md` | ingested |
| `wob-ch11` | `raw/widow-of-borley/11-the-unlawfully-wedded-husband.md` | ingested |
| `wob-ch12` | `raw/widow-of-borley/12-a-pastoral-intermezzo.md` | ingested |
| `wob-ch13` | `raw/widow-of-borley/13-eisenhowers-sweetheart.md` | ingested |
| `wob-ch14` | `raw/widow-of-borley/14-epilogue---main-street-usa.md` | ingested |

**All *The Widow of Borley* files fully ingested.**

---

## Ingest Workflow

When the user says "ingest [source]":

1. **Read** the source file fully.
2. **Discuss** 3–5 key takeaways with the user. Wait for their response before continuing — they may redirect emphasis.
3. **Write a source summary page** at `wiki/sources/<slug>.md`.
4. **Update `wiki/overview.md`** — extend the synthesis with new information.
5. **Update `wiki/timeline.md`** — add all dateable events in chronological order.
6. **Update or create entity pages** across `wiki/people/`, `wiki/places/`, `wiki/phenomena/`. A single ingest typically touches 10–20 pages. Touch all affected pages.
7. **Update `index.md`** — add new pages, update one-line summaries where content changed.
8. **Append to `log.md`**: `## [YYYY-MM-DD] ingest | <source title>`

Step 2 is the most important: the human decides what to emphasise. Don't skip the discussion.

---

## Query Workflow

When the user asks a question:

1. Read `index.md` to identify relevant pages.
2. Read those pages fully.
3. Synthesise an answer with `[[page-name]]` citations linking to wiki pages.
4. If the answer is substantive and novel (a comparison, a synthesis, a new connection), **offer to file it as a wiki page** — e.g. `wiki/themes/sceptic-arguments.md`.
5. Append to `log.md`: `## [YYYY-MM-DD] query | <question summary>`

---

## Lint Workflow

When the user asks for a lint / health-check:

1. Scan all wiki pages for:
   - Orphan pages (no inbound links from other wiki pages)
   - Missing cross-references (entities mentioned by name but not linked)
   - Pages promised by links that don't exist yet
   - Contradictions between pages
   - Claims in earlier pages superseded by later sources
   - Data gaps that could be filled by web search
2. Report findings as a prioritised list (high/medium/low).
3. Apply fixes, or ask the user to confirm before major restructuring.
4. Append to `log.md`: `## [YYYY-MM-DD] lint | <summary>`

---

## Cross-referencing Rules

Use Obsidian wiki-link syntax throughout:
- `[[harry-bull]]` — links to `wiki/people/harry-bull.md`
- `[[borley-rectory|the Rectory]]` — links with display text
- `[[the-nun]]` — links to `wiki/phenomena/the-nun.md`

**Link liberally.** Every person, place, and phenomenon named in a page should be linked if that page exists. Unresolved links (pointing to pages not yet created) are fine — they mark future work.

---

## Naming Conventions

| Category | Path pattern | Example |
|----------|-------------|---------|
| People | `wiki/people/firstname-lastname.md` | `wiki/people/harry-price.md` |
| Places | `wiki/places/place-name.md` | `wiki/places/borley-rectory.md` |
| Phenomena | `wiki/phenomena/phenomenon-name.md` | `wiki/phenomena/the-nun.md` |
| Themes | `wiki/themes/theme-name.md` | `wiki/themes/harry-price-controversy.md` |
| Sources | `wiki/sources/<slug>.md` | `wiki/sources/gotb-ch01.md` |

Use lowercase kebab-case throughout. No spaces in filenames.

---

## Writing Style

- **Present tense** for standing biographical/historical facts: "Harry Price is a psychical researcher..."
- **Past tense** for reported events: "In 1900, the Bull sisters reported seeing..."
- **Mark contested claims**: use "reportedly", "allegedly", "according to [source]"
- **Flag contradictions** with a blockquote: `> **Contradiction:** ...`
- **Note evidence strength**: `(single witness)`, `(multiple independent witnesses)`, `(disputed)`

---

## The Human's Role

The human curates sources, decides what matters, and asks questions. The LLM writes everything — summaries, cross-references, entity pages, synthesis. Never ask the human to update a page themselves. Offer to do it.

## Session Start Routine

At the start of every session, before responding to the user:

1. Read the last 10 entries of `log.md` to know what was done recently.
2. Read `index.md` to know what's in the wiki.
3. Run `find raw/ -type f -name "*.md" | sort` and cross-reference against the slug table above. Report any `pending` files or files not yet in the table — these are new sources awaiting ingest. Mention them briefly so the user knows what's available.

No timestamp file is needed. The slug table's `status` column is the manifest.
