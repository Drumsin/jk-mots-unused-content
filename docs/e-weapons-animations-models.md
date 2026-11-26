# E. Weapons, animations and models

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 20. repv / repp: the cut rifle, and its missing hand textures {#finding-20}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--known"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m-2 15-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8z"/></svg>Known (detail likely new)</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Resource\Res2.gob | 3do\repv.3do (view model), 3do\repp.3do (pickup) |
| JK + MotS | Resource\Res2.gob; Resource\JKMRES.GOO | 3do\rep0.3do (early projectile; listed in static.jkl, unused) |

The cut rifle is documented. The new detail is in repv.3do's material list: seven hand textures (ft-wrt, ft-wrs, ft-tp, ft-thb, ft-fng, ft-wrb, ft-bt) that do not exist in JK, so the first-person model had a rendered fist and hand. Same-named ft-* textures exist in MotS JKMRES.GOO, and the render below uses those. The source path puts the model under RepeaterGun\View and it was exported with ver2.30, one of the oldest exporter versions in the data.

Community modder Shimstock noted that `rep0.3do` is the repeater's projectile and is still in the assets. It is an early export (`RepeaterGun\projectile0\Rep0.prj`, ver2.30) and is listed in both games' static.jkl, but no template uses it as `model3d=`. The shipped repeater fires `+repeaterball`, whose model is the later `rpt0.3do` (`RepeaterGun\projectile\`, ver4.63). The other old projectile0 models (Bryar, concussion, detonator, rail) are still the ones those weapons fire; only the repeater's earlier shot was left behind, in the same generation as the cut `repv` / `repp` rifle.

**Evidence**

```
repv.3do: # MODEL 'RepV.3do' created from 'D:\Jedi\Products\JK\Data\3DO\Weapons\RepeaterGun\View\Repv.prj in VISUAL mode with ver2.30.'
MATERIALS 13
  6:     FT-WRT.MAT   7: FT-WRS.MAT   8: FT-TP.MAT   9: FT-THB.MAT
  10:    FT-FNG.MAT  11: FT-WRB.MAT  12: FT-BT.MAT
rep0.3do: # MODEL 'Rep0.3do' created from '...\RepeaterGun\projectile0\Rep0.prj in VISUAL mode with ver2.30.'
static.jkl lists rep0.3do; no template has model3d=rep0.3do; +repeaterball uses model3d=rpt0.3do
```

**Sources**

- The Cutting Room Floor, "Star Wars Jedi Knight: Dark Forces II" page (read via an archived Wayback Machine copy, 2025).
- Community modder Shimstock noted that rep0.3do is the repeater's earlier projectile still in the assets.

<figure class="finding-figure" markdown="1">
![repv.3do (hand textures taken from MotS)](renders/repv.png)
<figcaption>repv.3do (hand textures taken from MotS)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![repp.3do](renders/repp.png)
<figcaption>repp.3do</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![rep0.3do, the unused early repeater projectile (colormap JK 01narsh, best guess)](renders/rep0.png)
<figcaption>rep0.3do, the unused early repeater projectile (colormap JK 01narsh, best guess)</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 21. Tusken prod view models {#finding-21}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--known"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m-2 15-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8z"/></svg>Known</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\prdv.3do, prgv.3do, prdp.3do, prdg.3do (+ keys) |

Two first-person variants of the Tusken gaderffii weapon: a fork (ForkView) and a gun (GunView). Some of their textures are missing.

**Evidence**

```
prdv.3do: ... 'D:\Jedi\Products\JK\Data\3DO\Weapons\TuskenProd\ForkView\PrdV.prj ... ver4.20.'
prgv.3do: ... '...\Weapons\TuskenProd\GunView\PrgV.prj ... ver4.11.'
```

**Sources**

- Massassi Temple (massassi.net) file and 3DO pages ("Early Dev Enemy Pack").

<figure class="finding-figure" markdown="1">
![prdv.3do (fork view)](renders/prdv.png)
<figcaption>prdv.3do (fork view)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![prgv.3do (gun view)](renders/prgv.png)
<figcaption>prgv.3do (gun view)</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 22. The 8t88 beast {#finding-22}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--known"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m-2 15-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8z"/></svg>Known</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\8b.3do; 3do\key\8b*.key (14 keyframes) |

A winged beast with 14 animations (run, bite, fly, jump attacks, death and more). The model is from a SimChars\Beast folder. It is shown posed with frame 0 of 8brun.key.

**Evidence**

```
8b.3do:    # MODEL 'bstblank.3do' created from 'D:\Jedi\Products\JK\Data\3DO\SimChars\Beast\Anims\bstblank.3do ... ver4.30.'
8brun.key: # KEYFRAME '<unnamed>' created from 'bstrun.l3d in BATCH mode with ver4.30.'
```

**Sources**

- Massassi Temple (massassi.net) file and 3DO pages.

<figure class="finding-figure" markdown="1">
![8b.3do posed with 8brun.key frame 0](renders/8b.png)
<figcaption>8b.3do posed with 8brun.key frame 0</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 23. Unused Kyle animations {#finding-23}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Known / Partly known</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Resource\Res2.gob | 3do\key\kystab.key, kystab2.key, kydraw.key, kyfjump0.key, kyfpull0.key, kyrepel0.key, kysabhol.key, kysabrdy.key, kysbchok.key, kysbpry1/2.key, kystrfl1.key, kystrfr1.key |
| JK + MotS | Resource\Res2.gob; Resource\JKMRES.GOO | 3do\key\kysnap3.key (unused in JK, used in MotS) |

These Kyle keyframes are referenced by no puppet, cog or level in either game. Most of them were also copied into MotS, where they are unused too.

One correction from the cross-game check: **kysnap3.key**, documented as unused in JK, is used by MotS (s5l2_darkswamp and s5l4_lowersith, and a MotS puppet file). The bike sounds bikeacl1.wav and biketrn1.wav play as passing traffic in JK level 4 (04_soundofcars.cog in 04escapehouse). score1/score2.wav are unused in both games. An earlier version of this document also treated sab0.3do as used in both games and removed it from the unused list; that was a mistake. Almost every JK level lists the `+force_saber` template that uses this model, but no JK script ever fires it. The unused throw model and animation are described in section I.

Community theory (Shimstock) — Speculative, not yet linked by any file. Community modder Shimstock suggested that `kystab` is not a dropped saber attack, and was more likely the third-person melee for the Tusken prod. The key is a very short two-handed thrust (6 frames at 15 fps) that no puppet or cog in either game plays. The used saber swings are a different set (`kysabr*`), and the shipped "tusken_prod" inventory slot actually runs the energy-crossbow cog. The unused first-person prod models in the previous finding also never reference these keys. The idea fits the animation, but nothing in the data confirms it. `kystab2` (10 frames) is likewise unreferenced; its purpose is still unknown.

Community theory (Shimstock). Community modder Shimstock identified `kyrepel0` as a dropped radial Force-push animation, and noted that Boc still uses the power. The Kyle key (23 frames at 15 fps) is referenced by no puppet or cog, so the player never performs it. Boc's script (`darkjedi_boc.cog`) does create the `+force_repel` explosion — a short radial blast with force 200 and range 0.5 — when his second force power is triggered, but he plays his own throw animation (`bothrow.key`), not `kyrepel0.key`. Gorc's cog also names `+force_repel`. Some MotS levels still carry a leftover `+force_repel` template, but no MotS cog fires it. The leftover Kyle animation and Boc's working repel are the same idea; only the Dark Jedi version shipped in Jedi Knight.

A related leftover, not a community theory: both games still list `+force_lightning2`, `+force_lightning3` and `+force_lightning4` as damage variants, but `force_lightning.cog` always fires `+force_lightning` and only changes the mana cost by rank. Those higher-rank templates are never used.

**Evidence**

```
kysnap3.key: referenced by mots_JKM.GOO\jkl\s5l2_darkswamp.jkl, s5l4_lowersith.jkl
04_soundofcars.cog: sound wav0=bikeacl1.wav / sound wav1=biketrn1.wav
```

**Sources**

- The Cutting Room Floor, "Star Wars Jedi Knight: Dark Forces II" page (read via an archived Wayback Machine copy, 2025).
- Community theories (kystab / Tusken prod, and kyrepel0 / Boc's Force Repel): Community modder Shimstock.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 24. Unreferenced alternate exports of models the games do use {#finding-24}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Partly known</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\kyasleep.3do, kb.3do, dvboss.3do, yss.3do, mjsaber.3do, s0alt/s1alt.3do, du2alt.3do; ship _flt / _lo sets |

These MotS files are referenced nowhere in either game, but each is an alternate export of a character or ship that *is* in the game, so they are not hidden content in the usual sense.

**yss.3do** is the ysalamiri "shoulder" export (source folder Ysalamiri\shoulder). The ysalamiri itself is in MotS: ys.3do (same textures, near-identical geometry) is used in single-player level s5l2_darkswamp and as the carried creature in all five "Kill the Fool with the Ysalamiri" multiplayer maps (k1-k5), alongside ysbranch.3do; it is also a MotS item (items.dat, pow_ysalamiri.cog). Only the shoulder version is unused; kfy_main.cog notes the ysalamiri is hidden while carried.

**kyasleep** is a sleeping Kyle from a KyleAlternates folder (its texture set matches the MotS Kyle models; face texture kkfagoat). **kb** is a Kaerobani body whose textures match KYkb.3do, the "Kaerrobanii" multiplayer skin. The model header is `SimChars\Kaerrobanii\Kb.prj`. **dvboss** is a level-of-detail copy of the Darth Vader multiplayer skin kydarth.3do. **mjsaber** matches the Mara Jade models, and s0alt/s1alt/du2alt are alternates of used statues and dark undead. Several of the ship _flt/_lo exports have a used counterpart (corv1_flt even has the same geometry as the used corv1.3do).

Community modder Shimstock noted unused lines for Kaerobani, and that there may have been a boss fight at the end of his level. No Kaerobani voice files were found in the unused voiceuu folder (the `ka921*`–`ka924*` clips there are Ka'Pa the Hutt, not Kaerobani; see the voiceuu finding). The leftover S4L1 opening-cutscene script (`cutscenes.goo\cog\s4l1_ocs.cog`) plays `kb74107`, `kb74108` and `kb74109`, but those files do not ship in JKMRES, voiceuu or the MotS sound archive JKMsndLO.goo. They were likely cut from the finished opening video, though that video has not been compared line by line, so this is not certain. The shipped Kaerobani's Base level (S4L3) does not place a Kaerobani actor, and its leftover ending cutscene has no Kaerobani dialogue. A fight at the end of the level is not shown in the files. Thank you, Shimstock, for raising the lines.

**Evidence**

```
yss.3do: # MODEL 'YSS.3do' created from 'E:\Jedi\Products\JkMiss\Data\3do\SimChars\Ysalamiri\shoulder\YSS.prj ... ver4.63.'
ys.3do:  # MODEL 'Ys.3do' created from 'E:\...\SimChars\Ysalamiri\ground\Ys.prj ... ver4.63.'
s5l2_darkswamp.jkl: ysalamari _civilian ... model3d=ys.3do      k1.jkl: ctf_redflag _powerup ... model3d=ys.3do
models.dat: 23:   KYkb.3do  ky.snd  3  #"Kaerrobanii"     9:    kydarth.3do kydarth.snd  1  #"Darth Vader"
dvboss.3do:   # MODEL 'DVboss0.3do' created from 'LOD MODEL'
```

**Sources**

- Massassi Temple (massassi.net) file and 3DO pages (unused fighter textures).
- Community modder Shimstock raised unused Kaerobani lines and a possible boss fight at the end of his level. The files support unused cutscene lines that appear to have been cut from the finished video; they do not show a boss fight.

<figure class="finding-figure" markdown="1">
![kyasleep.3do: sleeping Kyle (unreferenced; Kyle models are used)](renders/kyasleep.png)
<figcaption>kyasleep.3do: sleeping Kyle (unreferenced; Kyle models are used)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![kb.3do: Kaerobani body (the used MP skin is KYkb.3do)](renders/kb.png)
<figcaption>kb.3do: Kaerobani body (the used MP skin is KYkb.3do)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![dvboss.3do: LOD copy of the used kydarth.3do](renders/dvboss.png)
<figcaption>dvboss.3do: LOD copy of the used kydarth.3do</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![yss.3do: ysalamiri shoulder export (the used ysalamiri is ys.3do)](renders/yss.png)
<figcaption>yss.3do: ysalamiri shoulder export (the used ysalamiri is ys.3do)</figcaption>
</figure>
