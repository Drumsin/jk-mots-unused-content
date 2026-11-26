# H. Added after community feedback

These two findings were added after KnightCop reviewed the first published version. Thank you to KnightCop for the corrections and pointers; the full list of changes from that review is in Appendix G.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 42. 03trcr.3do: the little tractor from the Katarn farm {#finding-42}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Partly known</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\03trcr.3do; 3do\mat\03trcrww.mat, 03trcrar.mat, 03trcrtp.mat, 03trcrsd.mat, 03trcrtd.mat |

KnightCop pointed out a small tractor model that the first version of this document did not describe. It is 03trcr.3do ("trcr" = tractor): a boxy rust-orange body on two big hexagonal wheels, with a long perforated boom. It is one mesh with 115 vertices and five textures of its own.

The 03 prefix is JK level 3 (03katarn, the Katarn farm), and the header says it was exported from `Environment\Tractor3` in the JK data folder with exporter ver2.31, one of the earliest versions in the data. The mesh inside is named 04trcr, so it may have been meant for level 4 (04escapehouse) at some point. "Tractor3" suggests there were earlier versions.

JK does not ship this model or its textures at all. MotS ships them in JKMRES.GOO, but nothing loads them: the name (with and without the extension, and as a substring) appears in no level of either game (single player, multiplayer, CTF, Kill the Fool, cutscene levels, S6L1), no template, cog, puppet, sound set, particle or sprite file, and there is no identical copy under another name. Its five textures are used only by this model.

Why it was missed: it was in [mots_unreferenced_assets.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/mots_unreferenced_assets.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/mots_unreferenced_assets.csv)) from the start, but it was not picked for a write-up.

**Evidence**

```
03trcr.3do:1  # MODEL '03TRCR.3do' created from 'D:\Jedi\Products\JK\Data\3DO\Environment\Tractor3\03TRCR.prj in VISUAL mode with ver2.31.'
MATERIALS 5:  03TRCRWW.MAT  03TRCRAR.MAT  03TRCRTP.MAT  03TRCRSD.MAT  03TRCRTD.MAT
MESH 0  NAME 04trcr  VERTICES 115
References in JK and MotS (code, comments, substrings): none outside the model itself
```

**Sources**

- Pointed out by KnightCop (community feedback, November 2026). No published note naming the file was found.

<figure class="finding-figure" markdown="1">
![03trcr.3do with its own textures (colormap 20val.cmp is a best guess; closest match to KnightCop's screenshot. 03house.cmp, which JK level 3 uses with the other 03 textures, makes the rust too dark)](renders/03trcr.png)
<figcaption>03trcr.3do with its own textures (colormap 20val.cmp is a best guess; closest match to KnightCop's screenshot. 03house.cmp, which JK level 3 uses with the other 03 textures, makes the rust too dark)</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 43. Unused Katarn farm and house textures that only MotS ships {#finding-43}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Partly known</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | mat\03wswt1a-d.mat, 03went.mat, 03went1.mat, 03went2.mat, 03wstr1a.mat, 03wstr1c.mat, 03pict1d.mat, and 119 more 03*/04* textures ([katarn_home_mats.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/katarn_home_mats.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/katarn_home_mats.csv))) |

KnightCop also mentioned the many unused textures from Morgan Katarn's home. The ones in his screenshots were matched pixel for pixel against every texture in both games:

**03wswt1a, 03wswt1b, 03wswt1c, 03wswt1d** (wood wall panels with inset gadgets), **03went** (dark console with screen), **03went1** and **03went2** (the two dark panels next to it), **03wstr1a** (wood-framed TV), **03wstr1c** (metal vent on wood) and **03pict1d** (the red painting) ship only in MotS JKMRES.GOO and are used by neither game. JK does not ship them. The plain wood grain in the same screenshot is **03wstr1b**, which is the one exception: JK ships it and uses it in level 3 (03katarn).

A sweep of every texture with the level 3 or 4 prefix in both games (272 names) found 129 that ship only in MotS and are used by neither game: 109 with the 03 prefix and 20 with the 04 prefix. Only one MotS map uses a 03 texture at all (mdm15_homestead uses 03vap1.mat). Five of them are the tractor's textures and two belong to the unused door models 03d4x4_a.3do and 04d2x3.3do. One (03c03) is a byte-identical copy of a texture JK uses (03c02), and about 15 more are near-identical variants of used JK textures. The rest are unique: alternate paintings (03pict01-04, 03pict1c/1d), wall and plate sets (03wplt01-10, 03w02*, 03w06*, 03w07*), ground and grass (03fgd*, 03fgrs*), several farm skies (03sky1/2, 03sky03k-08k, 0301sky2), cabinets, window and seat textures, and a run of 04wex* metal panels.

So these are not used in multiplayer either. It looks like the MotS team copied an older or fuller version of the JK level 3 and 4 texture folders, and JK itself shipped only the textures its final levels needed.

Why they were missed: they were in [mots_unreferenced_assets.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/mots_unreferenced_assets.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/mots_unreferenced_assets.csv)), but the contact sheet in Appendix B showed a selection that did not include them.

**Evidence**

```
Pixel match (16x16 RMS difference) between each screenshot tile and the extracted texture: 0 for all 11 tiles
03wstr1b.mat: JK Res2.gob, referenced by jk_JK1.GOB\jkl\03katarn.jkl (the only one of the 11 in JK)
03wswt1*, 03went*, 03wstr1a/1c, 03pict1d: no reference in any file of either game (code, comments or substring)
Sweep: 272 03/04 textures; 129 MotS-only and unused in both (109 with 03, 20 with 04)
```

**Sources**

- Pointed out by KnightCop (community feedback, November 2026). Full list: [katarn_home_mats.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/katarn_home_mats.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/katarn_home_mats.csv)).

<figure class="finding-figure" markdown="1">
![The textures in KnightCop's screenshots, identified](renders/kc_pictured_textures.png)
<figcaption>The textures in KnightCop's screenshots, identified</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![All MotS-only 03/04 textures that neither game uses](renders/kc_katarn_home_sheet.png)
<figcaption>All MotS-only 03/04 textures that neither game uses</figcaption>
</figure>
