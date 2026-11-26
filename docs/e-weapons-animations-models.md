# E. Weapons, animations and models

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span></span>
## 20. repv / repp: the cut rifle, and its missing hand textures {#finding-20}
</div>

**Rating:** Known (detail likely new)

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Resource\Res2.gob | 3do\repv.3do (view model), 3do\repp.3do (pickup) |

The cut rifle is documented. The new detail is in repv.3do's material list: seven hand textures (ft-wrt, ft-wrs, ft-tp, ft-thb, ft-fng, ft-wrb, ft-bt) that do not exist in JK, so the first-person model had a rendered fist and hand. Same-named ft-* textures exist in MotS JKMRES.GOO, and the render below uses those. The source path puts the model under RepeaterGun\View and it was exported with ver2.30, one of the oldest exporter versions in the data.

**Evidence**

```
repv.3do: # MODEL 'RepV.3do' created from 'D:\Jedi\Products\JK\Data\3DO\Weapons\RepeaterGun\View\Repv.prj in VISUAL mode with ver2.30.'
MATERIALS 13
  6:     FT-WRT.MAT   7: FT-WRS.MAT   8: FT-TP.MAT   9: FT-THB.MAT
  10:    FT-FNG.MAT  11: FT-WRB.MAT  12: FT-BT.MAT
```

**Sources**

- The Cutting Room Floor, "Star Wars Jedi Knight: Dark Forces II" page (read via an archived Wayback Machine copy, 2025).

<figure class="finding-figure" markdown="span">
![repv.3do (hand textures taken from MotS)](renders/repv.png)
<figcaption>repv.3do (hand textures taken from MotS)</figcaption>
</figure>

<figure class="finding-figure" markdown="span">
![repp.3do](renders/repp.png)
<figcaption>repp.3do</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 21. Tusken prod view models {#finding-21}
</div>

**Rating:** Known

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

<figure class="finding-figure" markdown="span">
![prdv.3do (fork view)](renders/prdv.png)
<figcaption>prdv.3do (fork view)</figcaption>
</figure>

<figure class="finding-figure" markdown="span">
![prgv.3do (gun view)](renders/prgv.png)
<figcaption>prgv.3do (gun view)</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 22. The 8t88 beast {#finding-22}
</div>

**Rating:** Known

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

<figure class="finding-figure" markdown="span">
![8b.3do posed with 8brun.key frame 0](renders/8b.png)
<figcaption>8b.3do posed with 8brun.key frame 0</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 23. Unused Kyle animations {#finding-23}
</div>

**Rating:** Known / Partly known

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Resource\Res2.gob | 3do\key\kystab.key, kystab2.key, kydraw.key, kyfjump0.key, kyfpull0.key, kyrepel0.key, kysabhol.key, kysabrdy.key, kysbchok.key, kysbpry1/2.key, kystrfl1.key, kystrfr1.key |
| JK + MotS | Resource\Res2.gob; Resource\JKMRES.GOO | 3do\key\kysnap3.key (unused in JK, used in MotS) |

These Kyle keyframes are referenced by no puppet, cog or level in either game. Most of them were also copied into MotS, where they are unused too.

One correction from the cross-game check: **kysnap3.key**, documented as unused in JK, is used by MotS (s5l2_darkswamp and s5l4_lowersith, and a MotS puppet file). Two other items sometimes listed as unused are in fact used: sab0.3do (the thrown saber) is loaded in both games, and the bike sounds bikeacl1.wav and biketrn1.wav play as passing traffic in JK level 4 (04_soundofcars.cog in 04escapehouse). score1/score2.wav are unused in both games.

**Evidence**

```
kysnap3.key: referenced by mots_JKM.GOO\jkl\s5l2_darkswamp.jkl, s5l4_lowersith.jkl
04_soundofcars.cog: sound wav0=bikeacl1.wav / sound wav1=biketrn1.wav
```

**Sources**

- The Cutting Room Floor, "Star Wars Jedi Knight: Dark Forces II" page (read via an archived Wayback Machine copy, 2025).

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 24. Unreferenced alternate exports of models the games do use {#finding-24}
</div>

**Rating:** Partly known

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\kyasleep.3do, kb.3do, dvboss.3do, yss.3do, mjsaber.3do, s0alt/s1alt.3do, du2alt.3do; ship _flt / _lo sets |

These MotS files are referenced nowhere in either game, but each is an alternate export of a character or ship that *is* in the game, so they are not hidden content in the usual sense.

**yss.3do** is the ysalamiri "shoulder" export (source folder Ysalamiri\shoulder). The ysalamiri itself is in MotS: ys.3do (same textures, near-identical geometry) is used in single-player level s5l2_darkswamp and as the carried creature in all five "Kill the Fool with the Ysalamiri" multiplayer maps (k1-k5), alongside ysbranch.3do; it is also a MotS item (items.dat, pow_ysalamiri.cog). Only the shoulder version is unused; kfy_main.cog notes the ysalamiri is hidden while carried.

**kyasleep** is a sleeping Kyle from a KyleAlternates folder (its texture set matches the MotS Kyle models; face texture kkfagoat). **kb** is a Kaerobani body whose textures match KYkb.3do, the "Kaerrobanii" multiplayer skin. **dvboss** is a level-of-detail copy of the Darth Vader multiplayer skin kydarth.3do. **mjsaber** matches the Mara Jade models, and s0alt/s1alt/du2alt are alternates of used statues and dark undead. Several of the ship _flt/_lo exports have a used counterpart (corv1_flt even has the same geometry as the used corv1.3do).

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

<figure class="finding-figure" markdown="span">
![kyasleep.3do: sleeping Kyle (unreferenced; Kyle models are used)](renders/kyasleep.png)
<figcaption>kyasleep.3do: sleeping Kyle (unreferenced; Kyle models are used)</figcaption>
</figure>

<figure class="finding-figure" markdown="span">
![kb.3do: Kaerobani body (the used MP skin is KYkb.3do)](renders/kb.png)
<figcaption>kb.3do: Kaerobani body (the used MP skin is KYkb.3do)</figcaption>
</figure>

<figure class="finding-figure" markdown="span">
![dvboss.3do: LOD copy of the used kydarth.3do](renders/dvboss.png)
<figcaption>dvboss.3do: LOD copy of the used kydarth.3do</figcaption>
</figure>

<figure class="finding-figure" markdown="span">
![yss.3do: ysalamiri shoulder export (the used ysalamiri is ys.3do)](renders/yss.png)
<figcaption>yss.3do: ysalamiri shoulder export (the used ysalamiri is ys.3do)</figcaption>
</figure>
