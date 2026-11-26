# Appendix G. Change log

## v1.0

First published version (57 pages): findings A-G, the cross-game check (Appendix F) and the comment pass.

## v2.0: Rev after community modder KnightCop feedback

Community modder KnightCop reviewed the first published version and wrote that some models and textures looked like ones used in multiplayer maps, that a sound looked like one JK uses, and that the little tractor model and the many unused Morgan Katarn home textures were missing. Thank you, KnightCop. Every point was checked again against both games, including every multiplayer, CTF and Kill-the-Fool map.

### What changed

| Asset | Ships in | Evidence | Change |
|---|---|---|---|
| 03trcr.3do (tractor) + 5 textures | MotS JKMRES | Identified from community modder KnightCop's screenshot. Shipped only in MotS, used by neither game. | Added (section H) |
| 03wswt1a-d, 03went, 03went1, 03went2, 03wstr1a, 03wstr1c, 03pict1d | MotS JKMRES | Matched pixel for pixel to community modder KnightCop's screenshots. MotS-only, used by neither game, including multiplayer. | Added (section H) |
| 03wstr1b.mat | JK Res2 | The plain wood grain in the same screenshot. Used by JK level 3 (03katarn). | Noted as used |
| 129 MotS-only 03/04 textures | MotS JKMRES | Sweep of all 272 level 3/4 textures in both games. | Added with a contact sheet ([katarn_home_mats.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/katarn_home_mats.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/katarn_home_mats.csv))) |
| 179 .ai0/.ai2 files (114 JK, 65 MotS) | JK Res2, MotS JKMRES | The engine loads name.ai0 on Easy and name.ai2 on Hard (OpenJKDF2 sithAIClass_LoadEntry). Variants of used .ai files are used. | Moved to used; lists and counts updated ([kc_feedback_ai_difficulty_files.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/kc_feedback_ai_difficulty_files.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/kc_feedback_ai_difficulty_files.csv))) |
| i00ky71z.wav | JK Res1hi | Commented-out drowning grunt; the drowning slot plays i00ky71t.wav, a different recording that is heard in the game. | Clarified in section C |
| 00techamb05.wav, 16metalcreak01.wav | JK Res1hi | JK never plays them; MotS levels and multiplayer maps refer to them by name. | Caveat reworded |

### What was checked and did not change

- Models and textures in multiplayer maps: every asset named in this document, every entry on the contact sheet and every row of both unreferenced lists (1,990 names) was searched again by full name, by name without the extension and by substring in every level of both games, every multiplayer, CTF and Kill-the-Fool map, the cutscene levels, S6L1, static.jkl, models.dat, sabers.dat, items.dat, and every template, cog, puppet, sound set, particle, sprite and AI file. Comments were left out, and any hit in a file that is itself loaded was looked at by hand. Apart from the AI difficulty files, nothing turned out to be loaded. The other hits were name collisions, for example "sphere" inside sphere.par, "sign" as a cog surface name, or "tree" in the map title "Tree Canopy".
- Sounds: each JK sound called unused was compared by name, with siblings (such as the "t" and "z" takes of a line), and by waveform against all 690 sounds in both games. None is a copy of a sound the games play. The bike sounds bikeacl1/biketrn1 (used in JK level 4) and the bartender line i00mn19z (used by 01_bartender.cog in level 1) were already marked as used. If the sound community modder KnightCop meant is not one of these, the file name would settle it.
- Cut weapons: the community restoration of the Tusken prod and the early Repeater gun (community modders Shimstock and KnightCop) matches the leftovers already described in section E (the prdv, prgv, prdp and prdg prod models and repv/repp). The only other trace in the data is the menu strings "Repeater" and "Repeater Gun" in jkstrings.uni, and those name the final weapon 6, which is in the game.

## v2.1: community theories from community modder Shimstock (s5 E-Web gunner, ligt prod projectile)

Community modder Shimstock's notes were added to finding 34 (s5.3do) and to the ligt.3do part of the "Internal project name and personal folders" finding, both labelled Community theory (Shimstock) and Speculative, with the file evidence for and against. Also added: the s5.3do source path (MotS JkMiss folder) and an eweb.3do render. Thank you, Shimstock.

The wording for community theories that are not yet confirmed by a file is "Community theory (Name) — Speculative, not yet linked by any file" (or "Speculative" where a shorter label is used).

## v2.2: unused voices, an unfinished saber throw, Warning Sense, and other leftovers

Thank you to community modder Shimstock for a set of notes that led to most of the additions and corrections below, and to Cogking, a developer on the original game who helped create the COG scripting language, for confirming that the Jedi Knight developers were experimenting with a saber throw.

What changed:

- Finding 2: the leftover level-05 Crow and TIE bomber animations are a paired sky dogfight; the transport animation is a path through the level. The written frame rates do not match, so the files as shipped would not finish together. Credited to community modder Shimstock.
- Finding 5/6 reworded to rely only on game-file evidence.
- Finding 7: dropped "snowy" as a fact about 16world. The pale colors came from a guessed MotS colormap; a complete JK colormap shows a dark valley and a tower, not snow. The colors are uncertain.
- Finding 12: the voiceuu folder has 46 files, not 26. That includes 28 civilian, rebel and announcement clips (previously counted as 26), 15 Ka'Pa the Hutt lines in Huttese, and 3 Abron Mar lines from leftover in-engine cutscenes that the shipped episode never plays. Credited to community modder Shimstock for the folder. Ka'Pa's lines were identified while re-checking this document.
- Finding 20: added rep0.3do, the repeater's earlier unused projectile. Credited to community modder Shimstock.
- Finding 23: added community modder Shimstock's speculative notes on kystab (possibly the Tusken prod melee) and kyrepel0 (a dropped radial push; Boc uses +force_repel with his own animation). Corrected the earlier claim that sab0.3do is used in both games. Short notes on unused +force_lightning2/3/4 templates and leftover MotS +force_repel templates.
- Finding 24: no evidence for a Kaerobani boss fight. His unused body (kb.3do) stands. The leftover S4L1 opening-cutscene script plays kb74107–kb74109, but those files do not ship in JKMRES, voiceuu or JKMsndLO.goo, so the lines were likely cut from the finished video (not yet compared line by line). Credited to community modder Shimstock for raising the lines.
- Finding 44 (new): an unfinished JK saber throw (sab0.3do with a solid green blade, sab0.key, and an un-fired +force_saber template). MotS later shipped a working version. Credited to Cogking, a developer on the original game who helped create the COG scripting language, for confirming the saber-throw experiments. The model itself turned up while re-checking this document's asset lists. Appendix F's earlier "used in both games" row for sab0.3do is superseded by this correction.
- Finding 45 (new): MotS force_warning.cog, an unused "Warning Sense" Force power written for bin 38, which shipped as Force Push. An in-game test in the original executable confirmed the flags are set, with no visible effect. No other cog reads those flags.
- Intro: a short paragraph on how MotS cutscenes were filmed in the game engine and recorded to .san videos, and that CUTSCENES.ZIP holds earlier JKL setups. Credited to community modder Shimstock.
- Housekeeping: the flagged-comment count is 6,688 (the previous text said 6,680). The tractor render uses colormap 20val.cmp, a best guess, instead of the darker 03house.cmp used in the v2.1 PDF.
