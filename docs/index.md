---
title: How to read this catalogue
---

# Unused content from Jedi Knight and Mysteries of the Sith

**Version 2.2** — November 2026

Have a new finding, a correction, or a file this catalogue should look at again? Please [open an issue](https://github.com/Drumsin/jk-mots-unused-content/issues/new/choose) and tell us about it. The last published PDF is still [v2.1](https://github.com/Drumsin/jk-mots-unused-content/releases/download/v2.1/JK_MotS_Unused_Content_Findings_v2.1.pdf); the v2.2 PDF and zip will be added on the Releases page when this version is published.

This site is the web edition of the catalogue of unused, orphaned and leftover files in the retail *Star Wars Jedi Knight: Dark Forces II* (JK) and *Mysteries of the Sith* (MotS) data. Use the sidebar to jump to a section, or the table of contents on each page to jump to a finding. Every finding has a stable link, for example [Finding 34](g-hints-in-comments.md#finding-34).

<figure class="finding-figure" markdown="1">
![ks.3do, the unused Kyle-on-speeder-bike model from MotS JKMRES.GOO, posed with its own ksgo.key animation. Grey parts use textures that never shipped.](renders/ks.png){ .skip-lightbox }
<figcaption>ks.3do, the unused Kyle-on-speeder-bike model from MotS JKMRES.GOO, posed with its own ksgo.key animation. Grey parts use textures that never shipped.</figcaption>
</figure>

## About this document

This is a catalogue of files in the retail Jedi Knight (JK) and Mysteries of the Sith (MotS) data that the games never load, or that point at files which do not exist. Many of them are leftovers from cut levels, early tests and earlier versions of models and scripts. Each finding gives the exact location so anyone can open the file and check it.

## Method

All shipped archives were extracted and read: JK Episode\JK1.GOB, JK1CTF.GOB, JK1MP.GOB and Resource\Res1hi.gob, Res2.gob; MotS Episode\JKM.GOO, JKM_KFY.GOO, JKM_MP.GOO, JKM_SABER.GOO and Resource\JKMRES.GOO, plus cutscenes.goo (inside Resource\VIDEO\CUTSCENES.ZIP) and the hidden S6L1 level (inside Resource\VIDEO\UNSUPPORTED.ZIP).

Shimstock pointed out that the MotS cutscenes were built as in-engine levels, played in the game, and recorded to video. Those earlier, unfinished scene setups are the JKL files in Resource\VIDEO\CUTSCENES.ZIP, already used as a source in this catalogue. The shipped episode does not load them; after each level it plays the later SMUSH videos (.san). (JK's live-action cutscenes are the .smk files.) The JKL worlds were last saved in late November 1997 through 2 January 1998, before the shipped MotS levels, and they still show unfinished names, disabled subtitles, leftover debug prints, and voice lines and props (including Ka'Pa the Hutt and Abron Mar) that never appear in a normal playthrough.

A reference graph was built for every file type. The roots are every level (.jkl), episode.jk, static.jkl, items.dat, models.dat, sabers.dat, the .per and .uni files and the file names hard-coded in the engine (taken from the OpenJKDF2 source, including the HUD icon naming rule and, since the revision after KnightCop's feedback, the AI difficulty rule: *name*.ai0 on Easy and *name*.ai2 on Hard). From the roots, references were followed through templates, cogs, 3DOs, keyframes, puppets, sound sets, materials and colormaps. Comment lines were not counted as references, because a commented-out line loads nothing; the comments themselves were read separately (see [section "Hints in comments"](g-hints-in-comments.md)). A file that no root reaches is "unreferenced". A name that is referenced but not present in any archive is a "missing reference".

3DO and KEY headers (source paths, exporter versions) and JKL headers (save dates, dev paths) were read for every file. Unused voice clips were transcribed automatically. 3DO renders in this document come from a small software renderer that follows the engine's hierarchy and matrix conventions. Textures are drawn with a colormap a level actually uses with them where one exists; otherwise the colormap is a best guess and is marked with "?".

## Cross-game check

Every item in this document was checked against *both* games, not only the game that ships it. MotS reuses a lot of JK data and JK files turn up in MotS, so a file that one game never loads can still be used by the other. For each asset the full text of both games was searched: every single-player, multiplayer, CTF and Kill-the-Fool level, the MotS cutscene levels and S6L1, static.jkl, items.dat, models.dat, sabers.dat, every template parameter (model3d, puppet, soundclass, cog, explode, fleshhit, creatething, material), every cog symbol and string, and every .3do/.key/.pup/.snd/.par/.spr file. Matches were made case-insensitively, with the full file name, the name without extension and plain substrings, and comment-only mentions were kept apart. Engine-loaded names were taken from the OpenJKDF2 source; the original game executables were not available for this survey.

Files were also compared by content: byte-identical copies under other names, identical 3DO geometry, and 3DOs that share most of their textures with a model the games do use. An asset is called unused only when nothing in either game loads it. Files that are alternate exports of in-game models are labelled as such. The per-asset results are in [cross_game_verification.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/cross_game_verification.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/cross_game_verification.csv)), and [Appendix F](appendix-f-cross-game-check.md) lists what this check changed.

## Ratings

Each finding was checked against public community sources. **Known**: already documented. **Partly known**: some of it is documented, the rest (usually the file evidence) was not found. **Likely new**: no earlier source was found. "Likely new" is not a claim that nobody has seen it before; corrections are welcome.

## Credits

KnightCop's "Road to Barons Hed - Cut Mission Information" is the reference for the cut speeder-bike level and the bike assets. Other sources: The Cutting Room Floor, the Massassi Temple, r/jediknight, The Sounds Resource and the OpenJKDF2 project (engine file names and conventions). Full list in [Appendix E](appendix-e-credits.md).

## Locating files

Paths are given as *game - archive - internal path*. Archive paths are relative to the game's install folder. Internal names in GOB/GOO archives are case-insensitive and are shown in lower case. Any GOB/GOO extractor will open them (see [Appendix D](appendix-d-extracting-files.md)).

## Browse the findings

A small chip before each finding title shows which game it is about: an orange <span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> for Jedi Knight, a lavender <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span> for Mysteries of the Sith, and both when the finding covers both games. Hover a chip for the full name. The location table under each finding still has the exact archives.

Each finding also has a rating: a small "Rating:" label and a colored pill with an icon. Some findings add a second pill for a further classification, such as Confirmed cut or Likely rename.

<p class="legend-pills"><span class="rating-pill rating-pill--known"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m-2 15-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8z"/></svg>Known</span><span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Partly known</span><span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span><span class="rating-pill rating-pill--speculative"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m15.07 11.25-.9.92C13.45 12.89 13 13.5 13 15h-2v-.5c0-1.11.45-2.11 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41a2 2 0 0 0-2-2 2 2 0 0 0-2 2H8a4 4 0 0 1 4-4 4 4 0 0 1 4 4 3.2 3.2 0 0 1-.93 2.25M13 19h-2v-2h2M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10c0-5.53-4.5-10-10-10"/></svg>Speculative</span></p>

- [A. The cut "Road to Baron's Hed" level (05) - leftovers in Mysteries of the Sith](a-barons-hed.md) — findings 1–4
- [B. Traces of other cut or reworked JK levels](b-other-cut-levels.md) — findings 5–8
- [C. Unused dialogue](c-unused-dialogue.md) — findings 9–12
- [D. Unused and orphaned scripts](d-unused-scripts.md) — findings 13–19
- [E. Weapons, animations and models](e-weapons-animations-models.md) — findings 20–24
- [F. Headers, dates and development machines](f-headers-dates.md) — findings 25–28
- [G. Hints in comments](g-hints-in-comments.md) — findings 29–41
- [H. Added after community feedback](h-community-feedback.md) — findings 42–43
- [I. Added in v2.2](i-added-in-v22.md) — findings 44–45

A single-file copy of the same text is also on GitHub as [FINDINGS.md](https://github.com/Drumsin/jk-mots-unused-content/blob/main/FINDINGS.md), and each numbered release includes a print-ready PDF.

The [Data Files](data-files.md) page lists the CSVs and the voice-transcript file behind this catalogue, with a short description of each and links to view or download them.
