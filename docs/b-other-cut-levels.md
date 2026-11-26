# B. Traces of other cut or reworked JK levels

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 5. The "13pipes" folder: props from the cut level 13 {#finding-5}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\13rock.3do, 3do\zpip.3do, 3do\wct3x4.3do |
| MotS | Resource\JKMRES.GOO | mat\13wcanw7.mat; 3do\mat\zpip4.mat, zpip7.mat, zpip8.mat |

Three models come from a source folder named `LevelSpecific\13pipes\`: a canyon rock (13rock, textured with the 13wcanw7 canyon wall, a texture MotS later reused in s1l1_rebelbase), a pipe section (zpip, using zpip4/7/8) and wct3x4 (its two textures are missing). None of the three models is referenced by any file in either game, and no level-13 JKL ships in either game.

The textures suggest a canyon setting: 13rock is a canyon-wall rock, and zpip is a pipe section. Together with the unused 13* textures in the next finding and the gap at slot 13 in the episode numbering (see the comments finding on the two level numberings), these are the file leftovers of a cut level 13. They are the only known 3D leftovers of that slot.

**Evidence**

```
13rock.3do: ... 'D:\Jedi\Products\JK\Data\3DO\LevelSpecific\13pipes\13rock.prj in VISUAL mode with ver4.50.'
zpip.3do:   ... '...\LevelSpecific\13pipes\Zpip.3do in VISUAL mode with ver4.11.'
wct3x4.3do: ... '...\LevelSpecific\13pipes\wct3x4\Wct3x4.prj in VISUAL mode with ver4.60.'
```

**Sources**

- No earlier source found.

<figure class="finding-figure" markdown="1">
![13rock.3do](renders/13rock.png)
<figcaption>13rock.3do</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![zpip.3do](renders/zpip.png)
<figcaption>zpip.3do</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![wct3x4.3do (textures missing)](renders/wct3x4.png)
<figcaption>wct3x4.3do (textures missing)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![Unused level 13 textures: 13wcanw7 (13rock; MotS also reuses it in s1l1_rebelbase), zpip4/7/8 (zpip), 13sky (shown with JK 12escape.cmp, best guess) and a canyon wall](renders/swatch_13pipes.png)
<figcaption>Unused level 13 textures: 13wcanw7 (13rock; MotS also reuses it in s1l1_rebelbase), zpip4/7/8 (zpip), 13sky (shown with JK 12escape.cmp, best guess) and a canyon wall</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 6. Unused level 13 textures {#finding-6}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Partly known</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | mat\13wcanw1-6.mat, 13sky*.mat, 13fwat*.mat, 13wdrok*.mat, 13car*.mat, 13cnsky1/3.mat (41 files) |
| JK | Resource\Res2.gob | mat\13frokg2.mat, mat\13wconc1.mat |

MotS ships 43 textures with the 13 prefix that no MotS level loads. Checked against JK as well, 41 of them are unused in both games: canyon walls, skies, water, rock and a car/vehicle texture. The textures suggest a canyon setting. JK itself ships two more unused 13* textures (13frokg2, also copied into MotS, and 13wconc1). A selection is on the texture contact sheet in Appendix B.

Two are not unused: **13wcanw7** is used by MotS level s1l1_rebelbase, and MotS's copy of **13fwater** is byte-identical to the JK texture used in 04escapehouse, 06bbarons and 17asarris.

The 13sky* textures are shown with JK 12escape.cmp, the colormap of the preceding level 12 (12escape). That is a best guess.

The 13cnsky set is different: it is a grey storm sky, and 13cnsky2 is used by shipped levels (15maw, 17asarris, 17bsarris, 18ascend and some multiplayer maps). Only 13cnsky1 and 13cnsky3 are unused, so this set should not be read as the cut level 13 sky.

**Evidence**

```
13wcanw7.mat: referenced by mots_JKM.GOO\jkl\s1l1_rebelbase.jkl
13fwater.mat: referenced by jk_JK1.GOB\jkl\04escapehouse.jkl, 06bbarons.jkl, 17asarris.jkl
See cross_game_verification.csv (rows starting with 13).
```

**Sources**

- Covered in part by existing community texture exports.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 7. 16world, 16vale and 16spir {#finding-7}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--speculative"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m15.07 11.25-.9.92C13.45 12.89 13 13.5 13 15h-2v-.5c0-1.11.45-2.11 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41a2 2 0 0 0-2-2 2 2 0 0 0-2 2H8a4 4 0 0 1 4-4 4 4 0 0 1 4 4 3.2 3.2 0 0 1-.93 2.25M13 19h-2v-2h2M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10c0-5.53-4.5-10-10-10"/></svg>Likely new (purpose speculative)</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\16world.3do, 16vale.3do, 16spir.3do; 3do\mat\16world.mat, 16spir2b.mat, 16spir3b.mat |

Three simple models exported in batch mode with an early tool version (ver4.11). 16world is an open cylinder whose texture shows a distant valley with a tower on the horizon; 16vale and 16spir are tall rock-like pieces. None is referenced. A distant backdrop for the falling-ship levels is one possibility, but nothing in the data confirms the purpose.

The first published render of 16world used a guessed MotS colormap (`10cargo.cmp`) and looked pale enough to be read as snowy mountains. Those colors are not a fact about the texture: the model's own colormap was not found. With a complete JK colormap (`04farm.cmp`) the same texture is a blue sky with brown clouds over a dark valley and a tower, with no snow. The colors should be treated as uncertain. This colormap concern turned up while re-checking this document.

**Evidence**

```
16world.3do: # MODEL '16world.prj' created from '16world.prj in BATCH mode with ver4.11.'
16spir.3do:  # MODEL '16spir.prj' created from '16spir.prj in BATCH mode with ver4.11.'
```

**Sources**

- No earlier source found. The concern that the pale colors were a colormap guess, not snow, turned up while re-checking this document.

<figure class="finding-figure" markdown="1">
![16world.3do with the guessed MotS 10cargo.cmp used in the first published render (pale, easily read as snow)](renders/16world.png)
<figcaption>16world.3do with the guessed MotS 10cargo.cmp used in the first published render (pale, easily read as snow)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![16world.3do with JK 04farm.cmp: a blue sky, brown clouds, a dark valley and a tower; not snow](renders/16world_04farm.png)
<figcaption>16world.3do with JK 04farm.cmp: a blue sky, brown clouds, a dark valley and a tower; not snow</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![16vale.3do](renders/16vale.png)
<figcaption>16vale.3do</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![16spir.3do](renders/16spir.png)
<figcaption>16spir.3do</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![16world / 16spir textures](renders/swatch_16.png)
<figcaption>16world / 16spir textures</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 8. The "06fall" set pieces {#finding-8}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\06buck.3do, 06struta.3do, 06strutb.3do; also 06rock1/2, 06mound, 06wl1-5, 06lock_z, 06lockab |

Models from a `LevelSpecific\06-3dos\06fall\` folder (level 6 is Baron's Hed). The names suggest a bucket and two struts for a falling or collapsing set piece. They ship only in MotS and no file in either game references them.

Related models are used: 06struta/06strutb share their textures with strut03/strut06, which MotS uses (s2l2a, s5l3, mdm12), and 06lock_z matches the textures of 06lock_x/06lock_y in JK 06bbarons. The 06fall pieces themselves never appear.

**Evidence**

```
06buck.3do:   ... 'D:\Jedi\Products\JK\Data\3DO\LevelSpecific\06-3dos\06fall\06buck.prj in VISUAL mode with ver4.11.'
06struta.3do: ... '...\06-3dos\06fall\06struta.prj in VISUAL mode with ver4.11.'
```

**Sources**

- No earlier source found.

<figure class="finding-figure" markdown="1">
![06buck.3do](renders/06buck.png)
<figcaption>06buck.3do</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![06struta.3do](renders/06struta.png)
<figcaption>06struta.3do</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![06strutb.3do](renders/06strutb.png)
<figcaption>06strutb.3do</figcaption>
</figure>
