# Change log

## Notes for the next update

These items are logged so they can be included the next time the findings text is revised. They are not part of a site-only change, and v2.1 is unchanged.

- The flagged-comment count in the findings text should be **6,688**. The current text says 6,680. The file is `comments_flagged.csv` (Section G / Appendix A).
- The tractor render `renders/03trcr.png` was re-done with colormap `20val.cmp` (still a best guess). `03house.cmp` made the rust body too dark compared with KnightCop's screenshot. The v2.1 PDF and zip still have the older, darker render and the 03house.cmp caption.

## v1.0

First published version (57 pages): findings A–G, the cross-game check (Appendix F) and the comment pass.

## v2.0 — Rev after KnightCop feedback

KnightCop reviewed the first published version and wrote that some models and textures looked like ones used in multiplayer maps, that a sound looked like one JK uses, and that the little tractor model and the many unused Morgan Katarn home textures were missing. Thank you, KnightCop. Every point was checked again against both games, including every multiplayer, CTF and Kill-the-Fool map.

### What changed

| Asset | Ships in | Evidence | Change |
|---|---|---|---|
| 03trcr.3do (tractor) + 5 textures | MotS JKMRES | Identified from KnightCop's screenshot. Shipped only in MotS, used by neither game. | Added (section H) |
| 03wswt1a-d, 03went, 03went1, 03went2, 03wstr1a, 03wstr1c, 03pict1d | MotS JKMRES | Matched pixel for pixel to KnightCop's screenshots. MotS-only, used by neither game, including multiplayer. | Added (section H) |
| 03wstr1b.mat | JK Res2 | The plain wood grain in the same screenshot. Used by JK level 3 (03katarn). | Noted as used |
| 129 MotS-only 03/04 textures | MotS JKMRES | Sweep of all 272 level 3/4 textures in both games. | Added with a contact sheet (`katarn_home_mats.csv`) |
| 179 .ai0/.ai2 files (114 JK, 65 MotS) | JK Res2, MotS JKMRES | The engine loads name.ai0 on Easy and name.ai2 on Hard (OpenJKDF2 `sithAIClass_LoadEntry`). Variants of used .ai files are used. | Moved to used; lists and counts updated (`kc_feedback_ai_difficulty_files.csv`) |
| i00ky71z.wav | JK Res1hi | Commented-out drowning grunt; the drowning slot plays i00ky71t.wav, a different recording that is heard in the game. | Clarified in section C |
| 00techamb05.wav, 16metalcreak01.wav | JK Res1hi | JK never plays them; MotS levels and multiplayer maps refer to them by name. | Caveat reworded |

### What was checked and did not change

- Models and textures in multiplayer maps: every asset named in the document, every entry on the contact sheet and every row of both unreferenced lists (1,990 names) was searched again in every level of both games, including multiplayer, CTF and Kill-the-Fool maps. Apart from the AI difficulty files, nothing turned out to be loaded.
- Sounds: each JK sound called unused was compared by name, with siblings, and by waveform against all 690 sounds in both games. None is a copy of a sound the games play.
- Cut weapons: the community restoration of the Tusken prod and the early Repeater gun (Shimstock and KnightCop) matches the leftovers already described in section E.

## v2.1 — Community theories from Shimstock

Added to finding 34 (`s5.3do`) and to the `ligt.3do` part of the "Internal project name and personal folders" finding, both labelled Community theory (Shimstock) and Speculative, with the file evidence for and against. Also added: the `s5.3do` source path (MotS JkMiss folder) and an `eweb.3do` render. Thank you, Shimstock.

The wording for community theories that are not yet confirmed by a file is "Community theory (Name) — Speculative, not yet linked by any file" (or "Speculative" where a shorter label is used).
