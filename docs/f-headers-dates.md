# F. Headers, dates and development machines

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 25. Level save dates {#finding-25}
</div>

**Rating:** Partly known

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Episode\JK1.GOB, JK1CTF.GOB, JK1MP.GOB | jkl\*.jkl (first line) |
| MotS | Episode\JKM*.GOO; Resource\VIDEO\*.ZIP | jkl\*.jkl (first line) |

Every JKL starts with a "World file ... Created" stamp. JK levels are dated 2-9 September 1997, saved from both C:\ and D:\Jedi\Products\JK\Release\. MotS levels are dated 11-16 January 1998. The MotS cutscene levels run from 29 November 1997 to 2 January 1998. The hidden S6L1 was saved on 11 January 1998, the same window as the shipped MotS levels, so it was finished alongside them. static.jkl in both games is dated 30 October 1996.

**Evidence**

```
#********** World file D:\jedi\Products\JkMiss\Release\Episode\JKM\JKL\S6L1.jkl ***** Created 1/11/1998 3:28pm **********
```

**Sources**

- Full list in [jkl_headers.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/jkl_headers.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/jkl_headers.csv)). Some dates are quoted in community posts.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 26. Internal project name and personal folders {#finding-26}
</div>

**Rating:** Partly known

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Resource\Res2.gob | 3do\ligt.3do |
| MotS | all archives | 3DO / JKL source paths |

MotS is called "JkMiss" in every path. Personal folders leak into a few headers: `D:\working\CLINTS\Ligt.prj` and `E:\duClem\3x8d.prj` (MotS). Exporter versions range from ver2.22 to 4.65. Cog author tags include YB (270+ cogs), KS, RD, IS, CR, DB, SXC, MT and JS.

ligt.3do is an earlier export of the Force Lightning segment. The effect is used in both games: the +force_ltpeice template uses **ligt2.3do**, which has the same single texture (ligt3.mat) and the same 30 vertices and comes from the official Weapons\ForceWeapons\ForceBolt folder. ligt2.3do appears in JK levels 03, 07, 14, 15, 17a, 19a, 21a, the CTF maps and MotS s2l2b and cutscenes. Only the personal-folder copy, ligt.3do, is unreferenced.

**Community theory (Shimstock) - Speculative, not yet linked by any file.** "The unused lightning 3do might've been the Tusken prod projectile." What the data shows: ligt.3do is a single lightning strip (one texture, LIGT3.MAT; 30 vertices, 26 faces) exported from a personal folder with ver4.50, older than the ligt2.3do the Force Lightning effect uses (official Weapons\ForceWeapons\ForceBolt folder, ver4.63). The cut prod does leave a slot behind: JK items.dat keeps tusken_prod in slot 5, wired to weap_crossbow.cog, and MotS keeps it in slot 135 with weap_crossbow_m.cog. No file names ligt.3do together with the prod, and no file states which effect ligt.3do was meant for, so no file confirms or rules this out yet.

**Evidence**

```
ligt.3do:  # MODEL 'Ligt.3do' created from 'D:\working\CLINTS\Ligt.prj in VISUAL mode with ver4.50.'
ligt2.3do: # MODEL 'Ligt2.3do' created from 'D:\Jedi\Products\JK\Data\3DO\Weapons\ForceWeapons\ForceBolt\Ligt2.prj ... ver4.63.'
m2.jkl (JK1MP.GOB): ... type=weapon move=physics timer=0.25 model3d=ligt2.3do size=0.005 ...
JK Res2.gob misc\items.dat:16  tusken_prod  5  0  1  0x0a4  cog=weap_crossbow.cog
MotS JKMRES.GOO misc\items.dat:36  tusken_prod  135  0  1  0x0a4  cog=weap_crossbow_m.cog
```

**Sources**

- Full list in [3do_dev_source_paths.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/3do_dev_source_paths.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/3do_dev_source_paths.csv)). Community theory on ligt.3do: Shimstock (community discussion, November 2026).

![ligt.3do: earlier copy of the Force Lightning segment (the game uses ligt2.3do)](renders/ligt.png)

*ligt.3do: earlier copy of the Force Lightning segment (the game uses ligt2.3do)*

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 27. Colormaps no level loads {#finding-27}
</div>

**Rating:** Likely new

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | misc\cmp\41escort.cmp, misc\cmp\01narsh2.cmp |
| JK | Resource\Res2.gob | misc\cmp\12redmap.cmp, m4redmap.cmp |

MotS level s4l1 (the escort ship) uses 01narsh.cmp, so its own 41escort.cmp went unused. 01narsh2.cmp is an alternate Nar Shaddaa palette. JK ships 12redmap.cmp and m4redmap.cmp (red variants). None of these four names appears in any file of either game.

dflt.cmp was dropped from this list: JK's copy is unreferenced, but MotS ships its own (different) dflt.cmp and the cutscene level s4l2_ocs loads it.

**Evidence**

```
cutscenes.goo\jkl\s4l2_ocs.jkl: 0: dflt.cmp
See cross_game_verification.csv (ext = cmp).
```

**Sources**

- No earlier source found.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 28. Gaps in the MotS episode list {#finding-28}
</div>

**Rating:** Partly known

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Episode\JKM.GOO | episode.jk |

MotS episode.jk plays SMUSH (.san) cutscenes. The line numbers jump from 141 to 310 (there is no scenario 3) and from 331 to 420 (no s5l1). Comments are stale: s5l2_darkswamp is labeled "Scenario 4, Level 2" and s2l2b is labeled "Scenario 2, Level 3".

**Evidence**

```
141:  1  7  CUT    s2l4ecs.san  0 0 310 310
310:  1  8  LEVEL  s4l1_EscortShip.jkl ... # Scenario 4, Level 1
331:  1 10  CUT    s4l3ecs.san  0 0 420 420
420:  1 11  LEVEL  s5l2_darkswamp.jkl  ... # Scenario 4, Level 2
```

**Sources**

- Scenario numbering has been discussed in the community; the exact gaps were not found documented.
