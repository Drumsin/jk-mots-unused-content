# A. The cut "Road to Baron's Hed" level (05) - leftovers in Mysteries of the Sith

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 1. Tusken speeder bike: models, riders, debris and animations {#finding-1}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--known"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m-2 15-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8z"/></svg>Known</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\tspd.3do, tspdup.3do, tspov.3do, tsbk_1.3do ... tsbk_8.3do |
| MotS | Resource\JKMRES.GOO | 3do\ts.3do (Tusken rider), 3do\ks.3do (Kyle rider) |
| MotS | Resource\JKMRES.GOO | 3do\key\ts{back,down,go,parked,start,turnl,turnr,up}.key, ks*.key (same set), tspov.key |
| JK + MotS | Resource\Res2.gob; Resource\JKMRES.GOO | 3do\mat\ts-blk.mat, ts-mtl.mat (the only two ts-*.mat that shipped; other models also use them) |

None of these files is referenced by any shipped level, template, cog or data file in either game. They are the complete vehicle set for the speeder-bike chase that was cut from Jedi Knight (the "05" slot between level 4, the escape from Kyle's family house, and level 6, Baron's Hed).

tspd.3do is the bike itself, tspdup.3do is an upright/parked variant, tspov.3do is the first-person cockpit view (its single mesh is named `huh01`) and tsbk_1 to tsbk_8 are the break-apart debris pieces. ts.3do and ks.3do are the bike with a full humanoid skeleton riding it: a Tusken (tk* textures) and Kyle (ky* textures). Both share a 20-node hierarchy (`$$$dummy, ts-a01, engine, head, hips, l4arm, larm, lcalf, lfoot, lhand, lleg, neck, r4arm, rarm, rcalf, rfoot, rhand, rleg, torso`), and each has its own set of eight keyframes (start, go, turn left/right, up, down, back, parked).

The bike references 17 ts-*.mat textures. Only ts-blk.mat and ts-mtl.mat exist (in both games, where other models also use them). The other 15 never shipped in either game, so the bike renders below are untextured (grey) apart from those two and the rider textures.

The riders are shown posed with frame 0 of ksgo.key / tsgo.key, which seats them on the bike.

**Evidence**

```
tspd.3do:  # MODEL 'TSPD.3do' created from 'D:\Jedi\Products\JK\Data\3DO\Ships\TuskenBike\TSPD.prj in VISUAL mode with ver4.63.'
tspov.3do: # MODEL 'Tspov.3do' created from 'D:\Jedi\Products\JK\Data\3DO\Ships\TuskenBike\POV\Tspov.prj in VISUAL mode with ver4.60.'
tsbk_1.3do: ... '\Ships\TuskenBike\debris\Tsbk_1.3do in VISUAL mode with ver4.50.'
ksgo.key:  # KEYFRAME '<unnamed>' created from 'KSGO.PRJ in BATCH mode with ver4.50.'  FRAMES 67  FPS 15  JOINTS 20
```

**Sources**

- Community modder KnightCop, "Road to Barons Hed - Cut Mission Information" (PDF, 2026) - documents the bike set and recreates the missing ts-* textures.
- Reddit r/jediknight, thread 1vnxazh (Aug 2026)
- TCRF states that no bike model exists; that is true of the JK archives only.

<figure class="finding-figure" markdown="1">
![tspd.3do, three angles (missing ts-* textures shown grey)](renders/tspd.png)
<figcaption>tspd.3do, three angles (missing ts-* textures shown grey)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![tspdup.3do](renders/tspdup.png)
<figcaption>tspdup.3do</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![tspov.3do, the first-person cockpit model](renders/tspov.png)
<figcaption>tspov.3do, the first-person cockpit model</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![tsbk_1 to tsbk_8 debris pieces](renders/tsbk_debris.png)
<figcaption>tsbk_1 to tsbk_8 debris pieces</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![ts.3do, Tusken rider, posed with tsgo.key frame 0](renders/ts.png)
<figcaption>ts.3do, Tusken rider, posed with tsgo.key frame 0</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![ks.3do, Kyle rider, posed with ksgo.key frame 0](renders/ks.png)
<figcaption>ks.3do, Kyle rider, posed with ksgo.key frame 0</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![The two shipped bike textures](renders/swatch_tsbike.png)
<figcaption>The two shipped bike textures</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 2. The level-05 source folder and the 05v* animated ship models {#finding-2}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Partly known</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\05road.3do, 05road2.3do, 05road3.3do, roadblk.3do, roadsign.3do |
| MotS | Resource\JKMRES.GOO | 3do\05vcrowm.3do, 05vtiebm.3do, 05vtrnwg.3do; 3do\key\05vcrowa.key, 05vtieb.key, 05vtrnwg.key |

The 3DO headers record the original folder on the developer machine. Five road pieces come from a dedicated `LevelSpecific\05stuff\` folder: three road sections, a road block and a road sign. They are the track furniture for the bike chase. No file in either game references them.

Three "05v" models come from the ship animation folders, each with a matching keyframe. They are not new ships: each is an animation-ready export of a ship that both games use. These particular files and keys are referenced nowhere in either game (all levels, cutscene levels, templates, cogs and data files were searched).

**05vcrowm** is the Moldy Crow. It uses exactly the texture set of crow.3do (fewer vertices), which JK places in 02, 04, 08, 09, 12, 16a/16b and 17b and MotS uses in multiplayer map mdm12_spaceport. **05vtiebm** is the TIE bomber: same textures and same vertex count as tieb.3do, which appears in JK levels 01narshadda, 06bbarons and 08escape88 and in MotS s1l1_rebelbase. So the TIE bomber and the Crow are seen in game, but through tieb.3do and crow.3do, not through these 05v files.

**05vtrnwg** is the Imperial transport with WeeGee riding on it. Its node list is the transport (T~TRANSP) plus a droid body (BODY01, HEAD01, EYE, NECK, SHLDR, arm segments), and it uses the TTRN* transport textures together with WeeGee's textures (wg.3do, used in JK levels 03 and 04). The transport on its own (ttrn.3do) sits in the shed at the end of JK level 4 (04escapehouse.jkl) and is reused by MotS (s1l2, s1l4, s2l2a/b, s2l4 and a cutscene). Community modder KnightCop identifies the shed transport and lists the key as "WeeGee with Transport".

Community modder Shimstock pointed out that the leftover level-05 ship animations belong together. The Moldy Crow and TIE bomber keys (`05vcrowa.key` and `05vtieb.key`) have the same 371-frame length, share a dummy path of 70 JK units, and were both exported from the Crow animation folder. The two ships weave around that path; it is a sky dogfight, not two separate fly-bys. The written frame rates differ (21.5 fps for the Crow, 5 fps for the TIE), so the files as shipped would not finish together, and no cog remains to start them. The Imperial transport key (`05vtrnwg.key`) is a shorter, separate animation whose dummy node traces a turning path, which fits a transport flying a route through the cut level rather than fighting.

roadblk.mat and roadsign.mat are missing, so those pieces render partly grey. The other road textures are shown with JK 04farm.cmp (see the next finding); that colormap is a best guess.

**Evidence**

```
05road.3do:   ... 'D:\Jedi\Products\JK\Data\3DO\LevelSpecific\05stuff\05road.prj in VISUAL mode with ver4.50.'
roadblk.3do:  # MODEL 'Roadblk2.3do' created from '...\LevelSpecific\05stuff\Roadblk.prj ... ver4.00.'
05vcrowm.3do: ... 'D:\Jedi\Products\JK\Data\3DO\Ships\Crow\anims\05vcrowm.prj ... ver4.60.'   nodes: $$$DUMMY crow
05vtiebm.3do: nodes: $$$DUMMY tie~bmb   (tieb.3do: '...\Ships\TieBomber\TieB.3do')
05vtrnwg.3do: # MODEL '05Vtrnwg.3do' created from '...\Ships\TroopTransport\Anims\05Vtrnwg.prj ... ver4.60.'
05vtrnwg.3do: nodes: $$$DUMMY ARM~1 BODY01 EYE HEAD01 L~ARM01..04 NECK SHLDR SHLDR01 T~TRANSP arm~2..6
04escapehouse.jkl (JK1.GOB): model3d=ttrn.3do
```

**Sources**

- Community modder KnightCop, "Road to Barons Hed - Cut Mission Information" (PDF, 2026) lists the 05v* keyframes and identifies the level-4 shed transport. The 05stuff folder evidence and the model-by-model comparison were not found in it.
- Community modder Shimstock identified the Crow and TIE keys as a paired sky dogfight, and the transport key as a path through the level.

<figure class="finding-figure" markdown="1">
![05road.3do (colormap: JK 04farm, best guess)](renders/05road.png)
<figcaption>05road.3do (colormap: JK 04farm, best guess)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![05road2.3do](renders/05road2.png)
<figcaption>05road2.3do</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![05road3.3do](renders/05road3.png)
<figcaption>05road3.3do</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![roadblk.3do (texture missing)](renders/roadblk.png)
<figcaption>roadblk.3do (texture missing)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![roadsign.3do](renders/roadsign.png)
<figcaption>roadsign.3do</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![05vcrowm.3do: Moldy Crow, animation export (the in-game Crow is crow.3do)](renders/05vcrowm.png)
<figcaption>05vcrowm.3do: Moldy Crow, animation export (the in-game Crow is crow.3do)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![05vtiebm.3do: TIE bomber, animation export (the in-game bomber is tieb.3do)](renders/05vtiebm.png)
<figcaption>05vtiebm.3do: TIE bomber, animation export (the in-game bomber is tieb.3do)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![05vtrnwg.3do: the Imperial transport with WeeGee riding it](renders/05vtrnwg.png)
<figcaption>05vtrnwg.3do: the Imperial transport with WeeGee riding it</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 3. A palette for the 05 sky textures {#finding-3}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | mat\05wsky01.mat, mat\05wsky02.mat |
| JK | Resource\Res2.gob | misc\cmp\04farm.cmp |

05wsky01/02 are 8-bit textures, so they need a colormap, and no level loads them. Community modder KnightCop's document lists them as "NO CMP". Shown through JK's 04farm.cmp (the colormap of level 4, the escape from Kyle's family house, the level just before the cut 05 slot), they come out as a clean blue sky with white clouds. 10cargo.cmp gives a similar result. The other 05 textures (road, walls, grass) also look natural under 04farm.cmp.

Period screenshots of the level support this. The magazine shots collected in KnightCop's document (PC Games, April 1997; Computer and Videogames, August 1997; PC Zone issue 51, June 1997) show the bike chase under a blue daytime sky with white clouds, which is what these two textures look like under 04farm.cmp.

This is still a visual match, not proof. It does suggest that level 05 shared a palette, and a time of day, with level 4.

**Evidence**

```
Community modder KnightCop PDF: "05wsky01.mat - NO CMP - Droid Works Version heavily dithered"
```

**Sources**

- Community modder KnightCop, "Road to Barons Hed - Cut Mission Information" (PDF, 2026) (magazine screenshots, pp. 14-17).
- No earlier source found pairing these textures with a colormap.

<figure class="finding-figure" markdown="1">
![05wsky01/02 under JK 04farm.cmp and 10cargo.cmp, with MotS 01narsh.cmp for comparison](renders/swatch_05sky.png)
<figcaption>05wsky01/02 under JK 04farm.cmp and 10cargo.cmp, with MotS 01narsh.cmp for comparison</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 4. Other JK-era models that only ship with Mysteries of the Sith {#finding-4}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Partly known</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\04vatrn.3do (+ key\04vatrn.key), atrn01.3do, blimp1.3do, blimp2.3do, sdes.3do, sch1.3do, oldja.3do, tree.3do, wwhl.3do |
| MotS | Resource\JKMRES.GOO | alternate copies of used models: shutdunc.3do, u2.3do, ug.3do, kelbite.3do, walt.3do |

About 130 3DOs in JKMRES.GOO carry `D:\Jedi\Products\JK\...` source paths, meaning they were built for Jedi Knight. Each one listed here was checked against every level, cutscene level, template, cog and data file in *both* games.

**Unused in both games, with no in-game equivalent:** 04vatrn, an AT-ST transport carrying an AT-ST (the node list is a full AT-ST rig plus "trans" and four doors; it has its own keyframe), atrn01 (ATSTtransport folder), two blimps (Ships\Blimps), a Star Destroyer (sdes, all 14 sdes* textures missing), sch1 (Ships\Schsr), an early Jan Ors (oldja, exported with the very old ver2.24 tool), a tree and a wooden wheel. The AT-ST itself (at.3do) is used in both games.

**Not really unused content:** several MotS-only files are alternate copies of models that the games do use. u2 and ug have the same geometry as u2alt.3do and ugalt.3do (Ugnaughts used in JK 09fuelstation and 16a/16b and in MotS s2l1, s2l2a/b and S6L1), just with older texture names that never shipped. shutdunc has the same texture set and vertex count as shut.3do, the Lambda shuttle used in both games. kelbite is a copy of JK's Kell dragon kd.3do (used in JK 08escape88 and 19b). walt is a variant of JK walt_b.3do (06bbarons).

The full list, with source paths and cross-game verdicts, is in [mots_unreferenced_assets.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/mots_unreferenced_assets.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/mots_unreferenced_assets.csv)) and [cross_game_verification.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/cross_game_verification.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/cross_game_verification.csv)).

**Evidence**

```
04vatrn.3do: # MODEL '04Vatrn.3do' created from 'D:\Jedi\Products\JK\Data\3DO\Ships\ATSTtransport\04Vatrn.prj ... ver4.61.'
04vatrn.3do: nodes: ATST-Base ATST-FootL ... ATST-Pelvs GunChin door01 door02 door03 door04 trans
oldja.3do:   # MODEL 'JA.3do' created from 'D:\Jedi\Products\JK\Data\3DO\SimChars\Jan\Ja.prj in VISUAL mode with ver2.24.'
kelbite.3do: # MODEL 'kd.3do' created from 'D:\Jedi\Products\JK\Data\3DO\SimChars\KellDragon\kd.3do ... ver4.63.'
u2.3do:      same geometry as u2alt.3do (used); ug.3do: same geometry as ugalt.3do (used)
```

**Sources**

- Massassi Temple (massassi.net) file and 3DO pages (a retextured Star Destroyer "from the MotS CD"). No single list of the rest was found.

<figure class="finding-figure" markdown="1">
![04vatrn.3do: AT-ST transport with AT-ST (unused in both games)](renders/04vatrn.png)
<figcaption>04vatrn.3do: AT-ST transport with AT-ST (unused in both games)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![blimp1.3do (unused in both games)](renders/blimp1.png)
<figcaption>blimp1.3do (unused in both games)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![sdes.3do (unused in both games; all textures missing)](renders/sdes.png)
<figcaption>sdes.3do (unused in both games; all textures missing)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![oldja.3do, early Jan Ors (unused in both games)](renders/oldja.png)
<figcaption>oldja.3do, early Jan Ors (unused in both games)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![u2.3do: same geometry as the used u2alt.3do; body textures missing](renders/u2.png)
<figcaption>u2.3do: same geometry as the used u2alt.3do; body textures missing</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![kelbite.3do: a copy of JK's Kell dragon kd.3do](renders/kelbite.png)
<figcaption>kelbite.3do: a copy of JK's Kell dragon kd.3do</figcaption>
</figure>
