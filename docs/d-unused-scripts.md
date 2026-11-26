# D. Unused and orphaned scripts

## 13. Kaerobani base: Mara quip triggers and other unused cogs {#finding-13}

**Rating:** Likely new

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Episode\JKM.GOO | cog\s4l3_bad_feeling.cog, s4l3_didn't_i_just.cog, s4l3_get_a_ship.cog, s4l3_this_is_easy.cog, s4l3_how_to_pull.cog, s4l3_cant_believe.cog, s4l3_looks_like_trouble.cog, s4l3_better_way.cog (31 s4l3 cogs in total) |

31 cogs named for the Kaerobani base level are never loaded by it. Eight are trigger cogs for Mara one-liners; they print subtitle string IDs 10043, 10000 and 43003 (the strings themselves live in the MotS voice/string archive). Others cover safety tunnels, crate storage, the palace exit and a ship generator.

**Evidence**

```
# s4l3_badfeeling.cog
#
# Mara says a smart-ass line about lazy pirates.
#
# [RD]
```

**Sources**

- No earlier source found.

## 14. s2l1_murder.cog and other Nar Shaddaa scenes {#finding-14}

**Rating:** Likely new

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Episode\JKM.GOO | cog\s2l1_murder.cog, cog\s2l1_nicereeyee.cog, cog\s2l2_ballet.cog |

s2l1_murder.cog is an unused scripted scene: ReeYee threatens and shoots a Rodian (sound variables are commented "greedo freaking out" and "oh no! tragedy has struck!"). s2l1_nicereeyee.cog is a related pedestrian-attack trigger. s2l2_ballet.cog sets up three AI "dancers" on a patrol route.

**Evidence**

```
# S2L1_murder.cog
#
# Greedo shot and killed in his home by gangster!
#
# [TT]
```

**Sources**

- No earlier source found.

## 15. Rahn on the escape ship, and a missing 17_rahnlines.cog {#finding-15}

**Rating:** Likely new

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Episode\JK1.GOB | cog\16a_rahn.cog |
| JK | Resource\Res2.gob | cog\darkjedi_sariss.cog |

16a_rahn.cog would play a Rahn line on a timer at the start of level 16, with "different files for light side and dark side"; it is unused. darkjedi_sariss.cog waits for a message from 17_rahnlines.cog, which does not ship; only 17a_rahnlines.cog exists.

**Evidence**

```
16a_rahn.cog:        # 16a_Rahn's line  /  # Plays Rahn's voice after timer at startup.
darkjedi_sariss.cog: // Receives message from 17_rahnlines.cog once game starts
```

**Sources**

- No earlier source found.

## 16. An early COG syntax {#finding-16}

**Rating:** Likely new (observation)

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Episode\JK1.GOB | cog\vectortest.cog, wallceltest.cog, slidetest.cog, redlight.cog, simple_door.cog, togldoor.cog, rotate_plat.cog |
| JK | Resource\Res2.gob | cog\door_switch.cog, gen_move.cog |

These test and utility cogs declare symbols on numbered lines (`0: surface slideSurf 0`) and use `desc=`, unlike the shipped format. This looks like a pre-release COG syntax that survived in test scripts.

**Evidence**

```
vectortest.cog:
0:    surface        slideSurf    0
0:    flex        speed           0.1
0:    vector        vec        0
0:    int        animId        0    local
```

**Sources**

- No earlier source found.

## 17. bddefault.ai: a "Baby Drugon" {#finding-17}

**Rating:** Likely new

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Resource\Res2.gob | misc\ai\bddefault.ai |

An AI file for a baby drugon. No model or template uses it; the shipped drugon uses dudefault.ai.

**Evidence**

```
# BDDEFAULT.AI
#
# Baby Drugon AI
# All difficulty levels
#
# [CR]
```

**Sources**

- No earlier source found.

## 18. Files that shipped scripts and models point to, but that do not exist {#finding-18}

**Rating:** Likely new / Partly known

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\VIDEO\UNSUPPORTED.ZIP | S6L1 .jkl -> S6L1_lighttube2.cog (missing) |
| MotS | Resource\VIDEO\CUTSCENES.ZIP | cutscenes.goo episode.jk -> s5l2_ocs.jkl, finale.jkl (missing) |
| JK | Resource\Res2.gob | xtank*b.3do -> xtank2.mat; r2x1.3do -> railclr.mat; repv.3do -> ft-*.mat; shard0.3do -> 00_glass.mat |

Dangling references show what was renamed or dropped late. The hidden S6L1 level loads S6L1_lighttube2.cog, which is not in UNSUPPORTED.ZIP. The cutscene episode lists s5l2_ocs.jkl and finale.jkl, but the archive holds s5_ocs and s5_finale instead. MotS items.dat names item_supershields.cog and icwrenc*.bm. xtank2.mat and railclr.mat exist in neither game.

Checked across both games: JK's shard0.3do (used) asks for 00_glass.mat, which JK does not ship but MotS ships and uses. The repv.3do hand textures (ft-*) are likewise missing from JK but present, unused, in MotS.

The complete list is in [missing_references.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/missing_references.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/missing_references.csv)).

**Evidence**

```
S6L1.jkl:  49:    S6L1_lighttube2.cog
S6L1.jkl:  7:    S6L1_lighttube2.cog    0 -1 activate01.wav
```

**Sources**

- No earlier source found for most entries.

## 19. Dark Kyle in S6L1 {#finding-19}

**Rating:** Partly known

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\VIDEO\UNSUPPORTED.ZIP | S6L1 .jkl (template darkkyle, kk.3do) |
| MotS | Resource\JKMRES.GOO | cog\61darkjedi_kyle.cog, 3do\kk.3do |

S6L1 defines a darkkyle template (kk.3do, 20,000 health) and JKMRES ships 61darkjedi_kyle.cog ("Mission's Dark Kyle" [YB]). The level never loads that cog; it only loads 61darkjedi_mara.cog. How Dark Kyle is driven in the level was not verified.

**Evidence**

```
61darkjedi_kyle.cog: # DARKJEDI_KYLE.COG
```

**Sources**

- A Steam community guide says Dark Kyle appears in the garbage room of S6L1.

![kk.3do (Dark Kyle)](renders/kk.png)

*kk.3do (Dark Kyle)*
