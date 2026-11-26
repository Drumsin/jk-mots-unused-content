# Appendix G. Change log

## v1.0

First published version (57 pages): findings A-G, the cross-game check (Appendix F) and the comment pass.

## v2.0: Rev after KnightCop feedback

KnightCop reviewed the first published version and wrote that some models and textures looked like ones used in multiplayer maps, that a sound looked like one JK uses, and that the little tractor model and the many unused Morgan Katarn home textures were missing. Thank you, KnightCop. Every point was checked again against both games, including every multiplayer, CTF and Kill-the-Fool map.

### What changed

| Asset | Ships in | Evidence | Change |
|---|---|---|---|
| 03trcr.3do (tractor) + 5 textures | MotS JKMRES | Identified from KnightCop's screenshot. Shipped only in MotS, used by neither game. | Added (section H) |
| 03wswt1a-d, 03went, 03went1, 03went2, 03wstr1a, 03wstr1c, 03pict1d | MotS JKMRES | Matched pixel for pixel to KnightCop's screenshots. MotS-only, used by neither game, including multiplayer. | Added (section H) |
| 03wstr1b.mat | JK Res2 | The plain wood grain in the same screenshot. Used by JK level 3 (03katarn). | Noted as used |
| 129 MotS-only 03/04 textures | MotS JKMRES | Sweep of all 272 level 3/4 textures in both games. | Added with a contact sheet ([katarn_home_mats.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/katarn_home_mats.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/katarn_home_mats.csv))) |
| 179 .ai0/.ai2 files (114 JK, 65 MotS) | JK Res2, MotS JKMRES | The engine loads name.ai0 on Easy and name.ai2 on Hard (OpenJKDF2 sithAIClass_LoadEntry). Variants of used .ai files are used. | Moved to used; lists and counts updated ([kc_feedback_ai_difficulty_files.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/kc_feedback_ai_difficulty_files.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/kc_feedback_ai_difficulty_files.csv))) |
| i00ky71z.wav | JK Res1hi | Commented-out drowning grunt; the drowning slot plays i00ky71t.wav, a different recording that is heard in the game. | Clarified in section C |
| 00techamb05.wav, 16metalcreak01.wav | JK Res1hi | JK never plays them; MotS levels and multiplayer maps refer to them by name. | Caveat reworded |

### What was checked and did not change

- Models and textures in multiplayer maps: every asset named in this document, every entry on the contact sheet and every row of both unreferenced lists (1,990 names) was searched again by full name, by name without the extension and by substring in every level of both games, every multiplayer, CTF and Kill-the-Fool map, the cutscene levels, S6L1, static.jkl, models.dat, sabers.dat, items.dat, and every template, cog, puppet, sound set, particle, sprite and AI file. Comments were left out, and any hit in a file that is itself loaded was looked at by hand. Apart from the AI difficulty files, nothing turned out to be loaded. The other hits were name collisions, for example "sphere" inside sphere.par, "sign" as a cog surface name, or "tree" in the map title "Tree Canopy".
- Sounds: each JK sound called unused was compared by name, with siblings (such as the "t" and "z" takes of a line), and by waveform against all 690 sounds in both games. None is a copy of a sound the games play. The bike sounds bikeacl1/biketrn1 (used in JK level 4) and the bartender line i00mn19z (used by 01_bartender.cog in level 1) were already marked as used. If the sound KnightCop meant is not one of these, the file name would settle it.
- Cut weapons: the community restoration of the Tusken prod and the early Repeater gun (Shimstock and KnightCop) matches the leftovers already described in section E (the prdv, prgv, prdp and prdg prod models and repv/repp). The only other trace in the data is the menu strings "Repeater" and "Repeater Gun" in jkstrings.uni, and those name the final weapon 6, which is in the game.

## v2.1: community theories from Shimstock (s5 E-Web gunner, ligt prod projectile)

Added to finding 34 (s5.3do) and to the ligt.3do part of the "Internal project name and personal folders" finding, both labelled Community theory (Shimstock) and Speculative, with the file evidence for and against. Also added: the s5.3do source path (MotS JkMiss folder) and an eweb.3do render. Thank you, Shimstock.

The wording for community theories that are not yet confirmed by a file is "Community theory (Name) — Speculative, not yet linked by any file" (or "Speculative" where a shorter label is used).
