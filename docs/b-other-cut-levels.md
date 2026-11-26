# B. Traces of other cut or reworked JK levels

## <span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span> 5. The "13pipes" folder: props from the cut "Canyon Run" level {#finding-5}

**Rating:** Likely new

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\13rock.3do, 3do\zpip.3do, 3do\wct3x4.3do |
| MotS | Resource\JKMRES.GOO | mat\13wcanw7.mat; 3do\mat\zpip4.mat, zpip7.mat, zpip8.mat |

Three models come from a source folder named `LevelSpecific\13pipes\`: a canyon rock (13rock, textured with the 13wcanw7 canyon wall, a texture MotS later reused in s1l1_rebelbase), a pipe section (zpip, using zpip4/7/8) and wct3x4 (its two textures are missing). None of the three models is referenced by any file in either game, and no level-13 JKL ships in either game.

Level 13 was "Canyon Run", a flying level on Sulon set right after level 12 (12escape, the escape from the cargo ship). The 1995 script, the 1996 storyboard ("The Sulon Canyons", scene 31 "Canyon Run") and the level description document describe it: the morning after the escape, Jan flies the Moldy Crow through canyons of rock and refinery while Kyle shoots TIE fighters from a top hatch. Flying too high draws fire from orbiting Star Destroyers, and the level ends by flying through the waterfall at Tankers Canyon.

The 13pipes folder fits that description: canyon rock (13rock) and refinery pipes (zpip). The folder name and these models are the new part; they are the only known 3D leftovers of the level.

**Evidence**

```
13rock.3do: ... 'D:\Jedi\Products\JK\Data\3DO\LevelSpecific\13pipes\13rock.prj in VISUAL mode with ver4.50.'
zpip.3do:   ... '...\LevelSpecific\13pipes\Zpip.3do in VISUAL mode with ver4.11.'
wct3x4.3do: ... '...\LevelSpecific\13pipes\wct3x4\Wct3x4.prj in VISUAL mode with ver4.60.'
JK level description: "13 Canyon Run ... The level ends when you find the waterfall and fly through it."
Objective: "2. Fly to the waterfall at Tankers Canyon."
```

**Sources**

- Level design: JK script (April 1995), JK storyboard (January 1996), "JK Levels Description" and "Jedi Knight Story" design documents.
- Folder name and models: no earlier source found.

![13rock.3do](renders/13rock.png)

*13rock.3do*

![zpip.3do](renders/zpip.png)

*zpip.3do*

![wct3x4.3do (textures missing)](renders/wct3x4.png)

*wct3x4.3do (textures missing)*

![Canyon Run textures: 13wcanw7 (13rock; MotS also reuses it in s1l1_rebelbase), zpip4/7/8 (zpip), 13sky (shown with JK 12escape.cmp, best guess) and a canyon wall](renders/swatch_13pipes.png)

*Canyon Run textures: 13wcanw7 (13rock; MotS also reuses it in s1l1_rebelbase), zpip4/7/8 (zpip), 13sky (shown with JK 12escape.cmp, best guess) and a canyon wall*

## <span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span> 6. Unused Canyon Run (level 13) textures {#finding-6}

**Rating:** Partly known

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | mat\13wcanw1-6.mat, 13sky*.mat, 13fwat*.mat, 13wdrok*.mat, 13car*.mat, 13cnsky1/3.mat (41 files) |
| JK | Resource\Res2.gob | mat\13frokg2.mat, mat\13wconc1.mat |

MotS ships 43 textures with the 13 prefix that no MotS level loads. Checked against JK as well, 41 of them are unused in both games: canyon walls, skies, water, rock and a car/vehicle texture. They match the Canyon Run setting (Sulon canyons, a refinery, the Tankers Canyon waterfall). JK itself ships two more unused 13* textures (13frokg2, also copied into MotS, and 13wconc1). A selection is on the texture contact sheet in Appendix B.

Two are not unused: **13wcanw7** is used by MotS level s1l1_rebelbase, and MotS's copy of **13fwater** is byte-identical to the JK texture used in 04escapehouse, 06bbarons and 17asarris.

The 13sky* textures are shown with JK 12escape.cmp, the colormap of level 12 (12escape), since Canyon Run is set on the same planet the morning after. That is a best guess.

The 13cnsky set is different: it is a grey storm sky, and 13cnsky2 is used by shipped levels (15maw, 17asarris, 17bsarris, 18ascend and some multiplayer maps). Only 13cnsky1 and 13cnsky3 are unused, so this set should not be read as the Canyon Run sky.

**Evidence**

```
13wcanw7.mat: referenced by mots_JKM.GOO\jkl\s1l1_rebelbase.jkl
13fwater.mat: referenced by jk_JK1.GOB\jkl\04escapehouse.jkl, 06bbarons.jkl, 17asarris.jkl
See cross_game_verification.csv (rows starting with 13).
```

**Sources**

- Covered in part by existing community texture exports.

## <span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span> 7. 16world, 16vale and 16spir {#finding-7}

**Rating:** Likely new (purpose speculative)

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\16world.3do, 16vale.3do, 16spir.3do; 3do\mat\16world.mat, 16spir2b.mat, 16spir3b.mat |

Three simple models exported in batch mode with an early tool version (ver4.11). 16world is an open cylinder whose texture shows a snowy valley with a tower on the horizon; 16vale and 16spir are tall rock-like pieces. None is referenced. A distant backdrop for the falling-ship levels is one possibility, but nothing in the data confirms the purpose.

**Evidence**

```
16world.3do: # MODEL '16world.prj' created from '16world.prj in BATCH mode with ver4.11.'
16spir.3do:  # MODEL '16spir.prj' created from '16spir.prj in BATCH mode with ver4.11.'
```

**Sources**

- No earlier source found.

![16world.3do (colormap best guess)](renders/16world.png)

*16world.3do (colormap best guess)*

![16vale.3do](renders/16vale.png)

*16vale.3do*

![16spir.3do](renders/16spir.png)

*16spir.3do*

![16world / 16spir textures](renders/swatch_16.png)

*16world / 16spir textures*

## <span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span> 8. The "06fall" set pieces {#finding-8}

**Rating:** Likely new

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

![06buck.3do](renders/06buck.png)

*06buck.3do*

![06struta.3do](renders/06struta.png)

*06struta.3do*

![06strutb.3do](renders/06strutb.png)

*06strutb.3do*
