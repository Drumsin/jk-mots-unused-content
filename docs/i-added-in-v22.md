# I. Added in v2.2

These findings were added in v2.2 from community notes and a further pass over leftover templates and scripts.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span></span>
## 44. An unfinished saber throw in Jedi Knight {#finding-44}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Partly known</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Resource\Res2.gob | 3do\sab0.3do, 3do\mat\sabvbld.mat, 3do\key\sab0.key |
| JK | Episode\JK1.GOB (and most other JK levels) | template +force_saber (model3d=sab0.3do); no cog fires it |

`sab0.3do` is a lightsaber with a solid bright-green blade. The blade mesh uses `SABVBLD.MAT`, whose pixels are all palette index 1: pure green (0, 255, 0) in every JK colormap. Ordinary sabers in JK have no blade model, because the game draws the blade in the engine. A matching spin animation, `sab0.key` (8 frames at 15 fps, from the same Sab0 project), is referenced by no puppet, cog or level.

Almost every JK level still lists a `+force_saber` template that uses this model, but no JK cog ever calls `FireProjectile` or `CreateThing` on it, and JK has no saber-throw inventory power. Mysteries of the Sith later shipped a working saber throw (`force_saberthrow.cog`, with later models such as `sab0gree`). The green-shaft model was the experimental JK version of that idea.

This was easy to miss, and an earlier version of this document wrongly removed `sab0.3do` from the unused list because every JK level names it (see Finding 23 and Appendix F). Being listed in a level template is not the same as being fired. Cogking, a developer on the original game who helped create the COG scripting language, confirmed that the developers were experimenting with a saber throw; the green-shaft model was found in a review of this catalogue.

**Evidence**

```
sab0.3do: saber model with a solid blade mesh; material SABVBLD.MAT is 8-bit, all pixels palette index 1 (pure green in every JK colormap)
sab0.key: 8 frames, 15 fps, from the same Sab0.prj; unreferenced
+force_saber appears in almost every JK JKL; no JK cog fires it; JK items.dat has no f_saberthrow
MotS ships force_saberthrow.cog and later saber-throw models (sab0gree and related)
```

**Sources**

- Cogking, a developer on the original game who helped create the COG scripting language, confirmed that the developers were experimenting with a saber throw.
- The green-shaft model (sab0.3do in Res2.gob) was identified in a review of this catalogue.

<figure class="finding-figure" markdown="1">
![sab0.3do, the unused JK saber-throw model with its solid green blade (colormap JK 01narsh)](renders/sab0.png)
<figcaption>sab0.3do, the unused JK saber-throw model with its solid green blade (colormap JK 01narsh)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![sab0.3do with sab0.key: the unused throw spin (all eight frames overlaid, then each frame in order)](renders/sab0_spin.png)
<figcaption>sab0.3do with sab0.key: the unused throw spin (all eight frames overlaid, then each frame in order)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![sabg.3do, a normal JK in-hand saber grip with no blade mesh (the game draws the blade in the engine)](renders/sabg.png)
<figcaption>sabg.3do, a normal JK in-hand saber grip with no blade mesh (the game draws the blade in the engine)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![MotS sab0gree.3do, the later shipped saber-throw model, for comparison](renders/sab0gree.png)
<figcaption>MotS sab0gree.3do, the later shipped saber-throw model, for comparison</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 45. Warning Sense: an unused MotS Force power that never got an effect {#finding-45}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | cog\force_warning.cog |

MotS still contains an unused Force-power script, `force_warning.cog`, titled "Warning Sense" and written for inventory bin 38. On activate it plays the standard Force-cast animation and sets player flags that the script itself comments as `JK_TF_WARNINGON` (0x400), `WARNINGLOW` (0x800) and `WARNINGHIGH` (0x1000). Rank 1 sets 0x400, rank 2 sets 0xC00, rank 3 sets 0x1400 and rank 4 sets 0x1C00. Shutting the power off clears 0x1C00. No other cog in JK or MotS sets or reads those bits: every other `jkGetFlags` check in the scripts looks only at 0x20, the Persuasion flag.

This is not an old name for a power that shipped. MotS still has a separate script for each shipped Force power. Force Push, which occupies bin 38 in the shipped `items.dat` (`f_push`, `cog=force_push.cog`), is a targeted shove cloned from Force Pull. Force Seeing, Far Sight, Persuasion and the rest are also still present as their own scripts and use different flags or effects. Nothing in `items.dat`, any level, or any other cog points at `force_warning.cog`, so the game never loads it. The script itself looks unfinished: it lists a mana cost of 5 but never spends mana, and it never starts the timer or pulse that would turn the flags off.

A temporary test in the original Mysteries of the Sith executable, hooking this script to the Force Push inventory slot, confirmed that the engine accepts and reports the flags (0x400, 0xC00, 0x1400 and 0x1C00). There was no visible change to the screen, the HUD, the Force meter or the automap; enemies still attacked, and fall damage was still taken. The flags are set, but the effect they were meant to switch on was never implemented.

**Evidence**

```
force_warning.cog header: FORCEPOWER Script - Warning Sense / Bin 38
//JK_TF_WARNINGON = 0x0400  //JK_TF_WARNINGLOW = 0x0800  //JK_TF_WARNINGHIGH = 0x1000
ranks 1-4: jkSetFlags 0x0400, 0x0C00, 0x1400, 0x1C00; stop_power: jkClearFlags 0x1C00
items.dat: f_push  38  ...  cog=force_push.cog   (no line points at force_warning.cog)
No other extracted JK or MotS cog reads 0x400, 0x800 or 0x1000
In-game test in the original MotS executable: flags reported back, no visible effect
```

**Sources**

- No earlier source found. The script was already listed as unreferenced in [mots_unreferenced_assets.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/mots_unreferenced_assets.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/mots_unreferenced_assets.csv)).
