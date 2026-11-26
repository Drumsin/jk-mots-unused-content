# G. Hints in comments

When the asset lists were built, comment lines were skipped on purpose, because a commented-out line does not make the game load anything. This section reads those comments on their own terms. Every comment in both games was extracted: the # and // comments in cogs, levels (including static.jkl, the cutscene levels and S6L1), templates, puppets, sound sets, AI, particle and sprite files, the .dat, .per, .uni and episode.jk files, and the export headers of every 3DO and KEY file. That came to 172,343 comment lines, of which 36,307 are more than table headers or column labels.

Each comment was scanned for file names, template names, old level numbers, dates and initials, words such as "old", "removed", "was", "temp" or "hack", and commented-out code. Every file or template name found this way was checked against both games, as in the rest of this document. 6,688 lines were flagged; they are listed in [comments_flagged.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/comments_flagged.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/comments_flagged.csv)), and all extracted comments are in [comments_all.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/comments_all.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/comments_all.csv)).

Each finding below is classified. **Confirmed cut**: the comment shows that something was removed or disabled, and the data confirms it. **Likely rename**: the comment gives an older name, number or source for something that shipped. **Speculative**: the comment hints at something, but the data cannot settle what. **Dev notes**: dates, initials and working notes. Comments can be stale or copied from other files, so none of these is proof of intent.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span></span>
## 29. Two level numberings in the JK episode and string files {#finding-29}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Partly known</span>
<span class="rating-pill rating-pill--rename"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m21.41 11.58-9-9A2 2 0 0 0 11 2H4a2 2 0 0 0-2 2v7a2 2 0 0 0 .59 1.42l9 9A2 2 0 0 0 13 22a2 2 0 0 0 1.41-.59l7-7A2 2 0 0 0 22 13a2 2 0 0 0-.59-1.42M13 20l-9-9V4h7l9 9M6.5 5A1.5 1.5 0 1 1 5 6.5 1.5 1.5 0 0 1 6.5 5"/></svg>Likely rename</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Episode\JK1.GOB | episode.jk |
| JK | Episode\JK1.GOB | misc\cogstrings.uni |
| JK | Episode\JK1.GOB | cog\06a_startlevel.cog |

The comments in JK's episode.jk number the 21 shipped levels one after another: 06ABarons.jkl is "Level 5", 06BBarons.jkl is "Level 6", 14tower.jkl is "Level 13" and 17asarris.jkl is "Level 16". The section headers in cogstrings.uni keep the old file numbers instead and simply skip two of them: "Level 4 - Escape Morgan's House" is followed by "Level 6a - Barons Hed", and "Level 12" is followed by "Level 14 - The tower Approach". 06a_startlevel.cog still says it starts the music "for level 5".

The two missing numbers are exactly the two cut levels: 05 (the speeder-bike chase) and 13 (Canyon Run). The file names kept the original slots, and the player-facing numbering was closed up after the cuts. The cogstrings.uni headers also call the Katarn home "Morgan's House" and level 8 "Escape the Ballroom".

**Evidence**

```
episode.jk:26  51:      1     5        LEVEL    06ABarons.jkl     0           0           60    -1    # Level 5: Barons Hed
episode.jk:48  131:     1     13       LEVEL    14tower.jkl       26          31          140   -1    # Level 13: Tower [Persuasion/Grip]
misc\cogstrings.uni:67  #  Level 4 - Escape Morgan's House - messages.
misc\cogstrings.uni:78  #  Level 6a - Barons Hed - messages.
misc\cogstrings.uni:145  #  Level 12 - Escape the Cargo Ship - messages.
misc\cogstrings.uni:155  #  Level 14 - The tower Approach - messages.
cog\06a_startlevel.cog:5  # Start music for level 5
```

**Sources**

- The gaps in the level file numbering (no 05, no 13) are known; see KnightCop's PDF and TCRF. No online mention of these comment labels was found.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span></span>
## 30. Level 19A objectives that were rewritten {#finding-30}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
<span class="rating-pill rating-pill--cut"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M17 3H7a2 2 0 0 0-2 2v16l7-3 7 3V5a2 2 0 0 0-2-2"/></svg>Confirmed cut (reworded)</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Episode\JK1.GOB | misc\cogstrings.uni |

Two of the 19A objectives in cogstrings.uni are commented out and replaced on the next line. The original goal 0 was "Lower the payload through the cargo doors so you can jump down to the sublevels." It became "Find the safe entrance to sub level 2", and the payload instruction moved into goal 1, which originally only said the control room would "work past the cargo staging area". The level was rearranged so that the payload drop comes after the control room.

**Evidence**

```
misc\cogstrings.uni:213  #  "GOAL_19000"   0  "Lower the payload through the cargo doors so you can jump down to the sublevels."  # Goal 0
misc\cogstrings.uni:214  "GOAL_19000"   0  "Find the safe entrance to sub level 2."                              # Goal 0
misc\cogstrings.uni:216  #  "GOAL_19001"   0  "The control room will allow you to work past the cargo staging area." # Goal 1
misc\cogstrings.uni:217  "GOAL_19001"   0  "The control room will allow you to lower the payload through the cargo doors so you can jump down to the sublevels." # Goal 1
```

**Sources**

- No online mention found.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span></span>
## 31. Commented-out control functions: Game Restore, Game Record and Debug {#finding-31}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
<span class="rating-pill rating-pill--speculative"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m15.07 11.25-.9.92C13.45 12.89 13 13.5 13 15h-2v-.5c0-1.11.45-2.11 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41a2 2 0 0 0-2-2 2 2 0 0 0-2 2H8a4 4 0 0 1 4-4 4 4 0 0 1 4 4 3.2 3.2 0 0 1-.93 2.25M13 19h-2v-2h2M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10c0-5.53-4.5-10-10-10"/></svg>Speculative</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Resource\Res1hi.gob | ui\jkstrings.uni |

In the list of bindable control functions in jkstrings.uni, three entries are commented out right after "Quick Save": "Game Restore", "Game Record" and "Debug". "Game Record" suggests a demo-recording key that was planned or used in development and then hidden. The file header also carries a note from [WW], dated 12/5/1996, saying the strings will be converted to Unicode "when we find a UNICODE editor".

What these functions did is not known from the data. The executable, which would show whether the code behind them survives, was not available for this survey.

**Evidence**

```
ui\jkstrings.uni:684  "GAMESAVE"        0 "Quick Save"
ui\jkstrings.uni:685  #   "GAMERESTORE"     0 "Game Restore"
ui\jkstrings.uni:686  #   "GAMERECORD"      0 "Game Record"
ui\jkstrings.uni:687  #   "DEBUG"           0 "Debug"
ui\jkstrings.uni:4  # to UNICODE when we find a UNICODE editor. [WW] 12/5/1996
```

**Sources**

- No online mention found. The Sith engine UNI format is documented on the "Jedi Knight Sith Engine Specs" wiki (jksith.wikidot.com).

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span></span>
## 32. Officer and trooper voice lines that were listed but never shipped {#finding-32}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
<span class="rating-pill rating-pill--cut"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M17 3H7a2 2 0 0 0-2 2v16l7-3 7 3V5a2 2 0 0 0-2-2"/></svg>Confirmed cut</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Resource\Res2.gob | misc\snd\io.snd |
| JK | Resource\Res2.gob | misc\snd\st.snd |
| JK | Resource\Res2.gob | misc\snd\gr.snd |

Each JK sound set (.snd) ends with a commented list of the voice clips meant for that character, with what each line says. 44 of the listed files are in no JK archive and in none of the MotS archives available here. The officer sets (io.snd and io2.snd) list "TK421, anything to report?", "Don't let him get to the valley core.", "I want every part of this ship checked." and "He's somewhere on this ship. Find him." None of these four was found in any JK archive. The stormtrooper set (st.snd, copied into s3.snd and s4.snd) lists a short exchange, "Did you hear something?" / "You smell something?" / "No, you're imagining things.", whose three files also never shipped, although the next lines in the same conversation did.

Greedo's set (gr.snd) lists four Rodian lines (I00GR11T, U, V, W) that are missing, and mn1.snd lists "Long live the rebellion" for a file that is missing. Two listed civilian clips, i00wm02z ("Run!") and i00wm03z ("No Blasters! No Blasters!"), do exist but nothing plays them. ic.snd and icrpt.snd reuse the trooper list word for word under other file names, so their missing entries are most likely variants that were never recorded rather than different lines.

MotS's own voice archive was not available, so these files could not be looked for there. MotS uses its own voice files, so it is unlikely to hold them.

**Evidence**

```
misc\snd\io.snd:41  # i00o102z.wav    # Don't let him get to the valley core.
misc\snd\io.snd:42  # i00o103z.wav    # I want every part of this ship checked.
misc\snd\io.snd:45  # i00o106z.wav    # TK421, anything to report?
misc\snd\io.snd:47  # i00o108z.wav    # He's somewhere on this ship. Find him.
misc\snd\st.snd:68  # i00s104z.wav  # Did you hear something?
misc\snd\st.snd:90  # I00S126Z.WAV  # You smell something?
misc\snd\st.snd:97  # i00s201z.wav  # No, you're imagining things.
misc\snd\gr.snd:57  ## I00GR11U.WAV  # tah boni tom ket sa infa dite
```

**Sources**

- The Massassi Temple sound tutorial shows the same st.snd comment format. No online mention of these specific missing lines was found.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 33. "Cling Vines": a complete cut swamp creature in MotS {#finding-33}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
<span class="rating-pill rating-pill--cut"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M17 3H7a2 2 0 0 0-2 2v16l7-3 7 3V5a2 2 0 0 0-2-2"/></svg>Confirmed cut</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\vv.3do, vvalt.3do; misc\pup\vv.pup; misc\snd\vv.snd, vv2.snd; 3do\key\vvatk, vvcrm01, vvcrmb, vvdown, vvgtup, vvstn.key; 3do\mat\vvvine.mat |

MotS ships a creature called "Cling Vines". The name appears only in comments: the puppet header reads "puppet file for Cling Vines (VV.3do)" and the second sound set is headed "ClingVines foley description". The set is complete: two models (vv.3do and vvalt.3do), a puppet, two sound sets, and creep, attack, down, stand and get-up animations. Nothing in either game loads any of it.

The vine shares its leaf and spike textures (vvleaf.mat, vvspike.mat) with the Dart Flower (vf.3do), which is used in s5l2_darkswamp and s5l4_lowersith. Its own vvvine.mat is unused. It was probably meant as a hazard for the same swamp.

**Evidence**

```
misc\pup\vv.pup:1  #puppet file for Cling Vines (VV.3do)
misc\snd\vv2.snd:1  # ClingVines foley description
misc\pup\vv.pup:3  stand           VVdown.key    0x00    0    0    # standing
```

**Sources**

- No online mention found (Massassi MotS 3DO index and forums searched).

<figure class="finding-figure" markdown="1">
![vv.3do in its rest pose (vvvine.mat colormap is a guess)](renders/vv.png)
<figcaption>vv.3do in its rest pose (vvvine.mat colormap is a guess)</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 34. A purple stormtrooper variant (s5.3do) {#finding-34}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
<span class="rating-pill rating-pill--speculative"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m15.07 11.25-.9.92C13.45 12.89 13 13.5 13 15h-2v-.5c0-1.11.45-2.11 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41a2 2 0 0 0-2-2 2 2 0 0 0-2 2H8a4 4 0 0 1 4-4 4 4 0 0 1 4 4 3.2 3.2 0 0 1-.93 2.25M13 19h-2v-2h2M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10c0-5.53-4.5-10-10-10"/></svg>Speculative</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\s5.3do; misc\pup\s5.pup; 3do\mat\s5shpad.mat; 3do\key\s5stand.key, s5fire.key |

s5.pup is headed "puppet control file for purple alt. stormtrooper with no gun in hand (s5.3do)". s5.3do is a stormtrooper with a backpack and a shoulder pad that uses its own texture, s5shpad.mat. The model, the puppet, the shoulder texture and two of its animations (s5stand.key, s5fire.key) are unreferenced in both games. A different file, s5punch.key, is used by the MotS stormtroopers. What the purple trooper was for is not stated anywhere.

The model header shows it is MotS work, not a JK leftover: it was saved in the MotS project folder (`E:\Jedi\Products\JkMiss\Data\3do\SimChars\Stormtrooper\S5.3do`, ver4.63), and its s5stand and s5fire animations were exported with ver4.65. s5 and all of its files ship only in MotS.

**Community theory (Shimstock) - Speculative.** Shimstock suggests the s5 trooper was made to fire the E-Web: "The s5 stormtrooper looked like it was made to shoot the discarded eweb gun... if you ever watched the s5 stormtrooper animation, he recoils like he is shooting an eweb from ESB. The eweb was replaced by the blaster cannon. That's why its weapon cog is called eweb."

What the data shows. For it: the puppet says "no gun in hand", yet its fire mode plays its own s5fire.key (7 frames at 15 fps). In that animation the whole body jolts: the torso pitches about 8 degrees, the head about 18, the forearms 7-9, and the legs move. That is a full-body recoil rather than a rifle shot, which fits a trooper firing a mounted gun.

The E-Web itself is in MotS: weap_eweb_m.cog ("WEAPON 10 script - EWEB Gun", "Player can not move when using this weapon", by [YB & CYW]), items.dat slots EWEB (130) and para_EWEB, and the models eweb.3do, eweb0.3do (projectile) and ewebbase.3do, all from `E:\Jedi\Products\JkMiss\Data\3do\Weapons\EWEB\` (ver4.63). It is placed in s1l2_astcrust, s4l1_escortship and s4l2_shipyards and in multiplayer and saber maps. Players know it as the "RMF-31 Repeating Blaster Cannon" (MotS manual), and the pickup message (string 382, pow_eweb_m.cog) is "The Blaster Cannon!", while every internal name stays EWEB. Its textures are named bc* (probably "blaster cannon") and exist only in MotS. So "replaced" is best read as renamed: the E-Web was not swapped for another gun, it was given a new player-facing name.

JK has no E-Web trace at all: no cog, model, texture or string, and JK's weapon slot 10 is the lightsaber (MotS moved the saber to make room). No file names s5 together with the E-Web, and no level or template uses s5, so the link stays a theory.

**Evidence**

```
misc\pup\s5.pup:1  # puppet control file for purple alt. stormtrooper with no gun in hand (s5.3do)
3do\s5.3do:1  # MODEL 'S5.3do' created from 'E:\Jedi\Products\JkMiss\Data\3do\SimChars\Stormtrooper\S5.3do in VISUAL mode with ver4.63.'
misc\pup\s5.pup:4  stand        s5stand.key    0x00    0    0    # 0 = Standing
misc\pup\s5.pup:30  fire         s5fire.key    0x28    1    5    # 10 = fire
3do\key\s5fire.key:1  # KEYFRAME '<unnamed>' created from 'S5fire.prj in BATCH mode with ver4.65.'
cog\weap_eweb_m.cog:5  # WEAPON 10 script - EWEB Gun
cog\weap_eweb_m.cog:7  # Player can not move when using this weapon.
cog\weap_eweb_m.cog:11  # [YB & CYW]
misc\items.dat:30  EWEB                    130             0       32000   0x0b4   cog=weap_EWEB_m.cog
cog\pow_eweb_m.cog:41  jkPrintUNIString(player, 382);    // The Blaster Cannon!
3do\eweb.3do:1  # MODEL 'Eweb.3do' created from 'E:\Jedi\Products\JkMiss\Data\3do\Weapons\EWEB\Eweb.3do in VISUAL mode with ver4.63.'
```

**Sources**

- No online mention of s5 found. Community theory: Shimstock (community discussion, November 2026).

<figure class="finding-figure" markdown="1">
![s5.3do (colormap is a best guess; the purple pad matches the puppet comment)](renders/s5.png)
<figcaption>s5.3do (colormap is a best guess; the purple pad matches the puppet comment)</figcaption>
</figure>

<figure class="finding-figure" markdown="1">
![eweb.3do, the MotS E-Web / "Blaster Cannon" turret the theory refers to](renders/eweb.png)
<figcaption>eweb.3do, the MotS E-Web / "Blaster Cannon" turret the theory refers to</figcaption>
</figure>

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 35. Kill the Fool with the Ysalamiri: a bobbing animation and a deathmatch mode, switched off {#finding-35}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
<span class="rating-pill rating-pill--cut"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M17 3H7a2 2 0 0 0-2 2v16l7-3 7 3V5a2 2 0 0 0-2-2"/></svg>Confirmed cut</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Episode\JKM_KFY.GOO | cog\kfy_main.cog |
| MotS | Resource\JKMRES.GOO | 3do\key\ysbobbin.key |

kfy_main.cog, the script behind the five MotS "Kill the Fool with the Ysalamiri" maps, declares a ysalamiri animation, YSbobbin.key, on a commented-out line, and the call that would play it is commented out as well. ysbobbin.key ships in JKMRES.GOO but nothing loads it. The same script keeps a block marked "Old stuff to play KFY levels as DM levels", which shows the KFY maps were also meant to be playable as ordinary deathmatch maps.

**Evidence**

```
cog\kfy_main.cog:88  #keyframe    ysalamiri_anim=YSbobbin.key      local
cog\kfy_main.cog:126  // Old stuff to play KFY levels as DM levels
cog\kfy_main.cog:218  // PlayKey(ysalamiri, ysalamiri_anim, 1, 0);
3do\key\ysbobbin.key:1  # KEYFRAME 'Ysbobbin.key' created from 'E:\Jedi\Products\JkMiss\Data\3do\SimChars\Ysalamiri\ground\anims\Ysbobbin.prj in VISUAL mode with ver4.63.'
```

**Sources**

- No online mention found.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 36. MotS finale: disabled subtitles and a third model swap {#finding-36}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
<span class="rating-pill rating-pill--cut"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M17 3H7a2 2 0 0 0-2 2v16l7-3 7 3V5a2 2 0 0 0-2-2"/></svg>Confirmed cut (disabled)</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\VIDEO\CUTSCENES.ZIP > cutscenes.goo | cog\s5_finale.cog |

In s5_finale.cog, all eight on-screen text calls for the final conversation (strings 95001 to 95008) are commented out, while the matching voice lines still play. None of those string numbers is in any .uni file of either game available here, so the subtitle text was apparently never added rather than just switched off.

The finale swaps Kyle for the "kylebossactor" model (kkduel.3do with the mjdueling.pup puppet) twice. A third swap, after "I was deluded...", is commented out.

**Evidence**

```
cog\s5_finale.cog:117  //   jkPrintUNIString(-1, 95001);
cog\s5_finale.cog:188  // jkPrintUNIString(-1, 95005);
cog\s5_finale.cog:195  //   thing1 = CreateThing(kboss, Kyle);
cog\s5_finale.cog:33  template    kboss=kylebossactor              local
```

**Sources**

- The fan "Mysteries of the Sith Remastered" mod adds its own subtitles for the engine cutscenes; it does not mention these disabled calls.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 37. S6L1 was built from the S1L1 scripts {#finding-37}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Partly known</span>
<span class="rating-pill rating-pill--rename"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m21.41 11.58-9-9A2 2 0 0 0 11 2H4a2 2 0 0 0-2 2v7a2 2 0 0 0 .59 1.42l9 9A2 2 0 0 0 13 22a2 2 0 0 0 1.41-.59l7-7A2 2 0 0 0 22 13a2 2 0 0 0-.59-1.42M13 20l-9-9V4h7l9 9M6.5 5A1.5 1.5 0 1 1 5 6.5 1.5 1.5 0 0 1 6.5 5"/></svg>Likely rename</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\VIDEO\UNSUPPORTED.ZIP | cog\S6L1_endlevel.cog |
| MotS | Resource\VIDEO\UNSUPPORTED.ZIP | cog\S6L1_tiefighter.cog |

Several cogs in the hidden S6L1 level keep S1L1 headers. S6L1_endlevel.cog is described as the "Endlevel cog for level S1L1", still has S1L1's cutscene call commented out (s1l1ocs.san) and its comment "This is the first level". It also has a disabled "Extra stars here" line that would have given 5 star points. Both S6L1_tiefighter cogs are headed "S1L1_tiefightr2.cog", and one of them has a second TIE bomber commented out.

**Evidence**

```
cog\S6L1_endlevel.cog:5  # Endlevel cog for level S1L1
cog\S6L1_endlevel.cog:49  //jkStartupCutscene ("s1l1ocs.san");
cog\S6L1_endlevel.cog:88  //SetInv(player, 17, 5.0);
cog\S6L1_tiefighter.cog:3  # S1L1_tiefightr2.cog
cog\S6L1_tiefighter.cog:41  //vtiebomber2=creatething(bombertemplate, bomberdummy1);
```

**Sources**

- S6L1 itself is known (Steam community guide). No online mention of these script leftovers was found.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 38. The TIE bomber script says "level 04" {#finding-38}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
<span class="rating-pill rating-pill--speculative"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m15.07 11.25-.9.92C13.45 12.89 13 13.5 13 15h-2v-.5c0-1.11.45-2.11 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41a2 2 0 0 0-2-2 2 2 0 0 0-2 2H8a4 4 0 0 1 4-4 4 4 0 0 1 4 4 3.2 3.2 0 0 1-.93 2.25M13 19h-2v-2h2M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10c0-5.53-4.5-10-10-10"/></svg>Speculative</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Episode\JK1.GOB | cog\08_tiebomber.cog |
| MotS | Episode\JKM.GOO | cog\s1l1_tiefighter.cog |

JK's 08_tiebomber.cog by [MT] is used in level 8 (08escape88.jkl), but its header says "Tiebomber cog for level 04". The MotS copies (s1l1_tiefighter*.cog and the S6L1 ones) inherit the same line. The header may simply be wrong. Another possibility is that the script was first written for an earlier level 4 or 5. The cut speeder-bike chase had its own TIE bomber animation (05vtiebm, see finding 2), but nothing in the data links the two.

**Evidence**

```
cog\08_tiebomber.cog:5  # Tiebomber cog for level 04
cog\08_tiebomber.cog:9  # [MT]
cog\s1l1_tiefighter.cog:5  # Tiebomber cog for level 04
```

**Sources**

- No online mention found.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 39. Script names in headers that differ from the shipped names {#finding-39}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
<span class="rating-pill rating-pill--rename"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m21.41 11.58-9-9A2 2 0 0 0 11 2H4a2 2 0 0 0-2 2v7a2 2 0 0 0 .59 1.42l9 9A2 2 0 0 0 13 22a2 2 0 0 0 1.41-.59l7-7A2 2 0 0 0 22 13a2 2 0 0 0-.59-1.42M13 20l-9-9V4h7l9 9M6.5 5A1.5 1.5 0 1 1 5 6.5 1.5 1.5 0 0 1 6.5 5"/></svg>Likely rename</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Episode\JK1.GOB | cog\04_remotes.cog |
| JK | Episode\JK1.GOB | cog\20_bocsearch.cog |
| MotS | Episode\JKM.GOO | cog\s4l3_kaerobanihalls_elev.cog |
| MotS | Episode\JKM.GOO | cog\s5l4_coffin.cog |
| MotS | Episode\JKM.GOO | cog\s1l3_elev_switch.cog |

56 cog headers name a .cog file that exists in neither game. Most of them are the file's own earlier name. Examples: 04_remotes.cog was "04_startup.cog"; 00_aisidekick.cog was "00_Sidekick.cog"; 20_bocsearch.cog was "17a_BocSearch.cog" (the 17a prefix matches the Sariss level's own search script, 17a_sarrisssearch.cog; both say they were "Modified from 00_AISearchPath.cog"); s4l3_looks_like_trouble.cog was "s4l3_i_dont_like.cog"; s4l3_kaerobanihalls_elev.cog was "S4L3_KChamber_elev.cog"; s5l4_coffin.cog was "S5L4_KyleCoffin.cog"; force_chainlight.cog was "FORCE_CLIGHTNING.COG".

One header points outside the single-player game. s1l3_elev_switch.cog says it was "copied M8_elev_switch.cog, and renamed it for use in JK Missions' S1L3" on 8/14/97. JK's multiplayer GOB ships only m2, m4, m5 and m10 (plus two m_boss levels), and there is no M8_elev_switch.cog in either game, so a JK multiplayer level "M8" seems to have existed in development.

**Evidence**

```
cog\04_remotes.cog:3  # 04_startup.cog
cog\20_bocsearch.cog:3  # 17a_BocSearch.cog
cog\20_bocsearch.cog:4  #    Modified from 00_AISearchPath.cog for the Boc level
cog\s4l3_kaerobanihalls_elev.cog:1  ## S4L3_KChamber_elev.cog
cog\s5l4_coffin.cog:3  # S5L4_KyleCoffin.cog
cog\s1l3_elev_switch.cog:13  ## Modified 8/14/97 by Chris K (copied M8_elev_switch.cog, and renamed it for use in JK Missions' S1L3)
```

**Sources**

- The full list is in [comments_flagged.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/comments_flagged.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/comments_flagged.csv)) (flag asset_not_used_or_missing on header lines). No online mention found.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 40. Source names inside model and animation headers {#finding-40}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Partly known</span>
<span class="rating-pill rating-pill--rename"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m21.41 11.58-9-9A2 2 0 0 0 11 2H4a2 2 0 0 0-2 2v7a2 2 0 0 0 .59 1.42l9 9A2 2 0 0 0 13 22a2 2 0 0 0 1.41-.59l7-7A2 2 0 0 0 22 13a2 2 0 0 0-.59-1.42M13 20l-9-9V4h7l9 9M6.5 5A1.5 1.5 0 1 1 5 6.5 1.5 1.5 0 0 1 6.5 5"/></svg>Likely rename</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | 3do\sw.3do |
| MotS | Resource\JKMRES.GOO | 3do\key\wsatk1.key |
| JK | Resource\Res2.gob | misc\pup\ja.pup |
| MotS | Resource\JKMRES.GOO | misc\pup\statue0.pup |
| MotS | Resource\JKMRES.GOO | misc\pup\statue1.pup |
| MotS | Resource\JKMRES.GOO | misc\pup\mjdueling.pup |

The export headers of 3DO and KEY files keep the artist's working names:

- The MotS swamp lurker sw.3do was made from JK's dianoga ("Octopus\Oc.prj"), and its attack, idle and sting animations were exported from OC* files.

- The swamp wampa animations come from a "SimChars\WampaCliff" folder with wc* names, so the creature began as a cliff wampa. The puppet calls it "Wampa-swamp".

- The vornskr animations were exported as VO* and renamed vr*.

- JK's Jan model ja.3do is an export of a Kyle LOD mesh ("K10-0"), and ja.pup says "Kyle with Jan textures!".

- The MotS Sith statues reuse JK puppets: statue0.pup "was Yun" and statue1.pup "was Jerec". Both still play the YU* and JE* animations.

- The purple, green and orange thrown-saber models are all exports named "Sab0red".

- The AT-ST transport key 04vatrn.key was exported as "04vastrn" from a "Ships\ATSTtransport" folder.

One puppet comment says the opposite of a rename. Mara's puppets note that Kyle's second idle fidget "kyidle1b.key was shaving", which is why her puppets use a different fidget.

**Evidence**

```
3do\sw.3do:1  # MODEL 'Oc.3do' created from 'D:\Jedi\Products\JK\Data\3DO\SimChars\Octopus\Oc.prj in VISUAL mode with ver4.63.'
3do\key\wsatk1.key:1  # KEYFRAME 'wcATK1.key' created from 'E:\Jedi\Products\JkMiss\Data\3do\SimChars\WampaCliff\anims\wcATK1.key in VISUAL mode with ver4.63.'
misc\pup\ja.pup:1  # puppet control file for JA.3do (Kyle with Jan textures!)
misc\pup\statue0.pup:1  #puppet file for statue0 (S0.3do) ; was Yun
misc\pup\statue1.pup:1  #puppet file for statue1 (S1.3do) ; was Jerec
misc\pup\mjdueling.pup:57  fidget2        kyidle1.key    0x20    1    1    # submode 25 = fidget2 \\ kyidle1b.key was shaving
```

**Sources**

- Reuse of JK creatures in MotS is broadly known. These specific source names were not found online.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight and Mysteries of the Sith"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 41. Change logs: dates, initials and an early start on MotS {#finding-41}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Partly known</span>
<span class="rating-pill rating-pill--notes"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 2a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6zm0 2h7v5h5v11H6zm2 8v2h8v-2zm0 4v2h5v-2z"/></svg>Dev notes</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Resource\Res2.gob | cog\00_elev_switch.cog |
| JK | Resource\Res2.gob | cog\actor_ic.cog |
| JK | Resource\Res2.gob | misc\pup\bo.pup |
| MotS | Episode\JKM.GOO | cog\s5l4_elev_switch.cog |
| MotS | Episode\JKM.GOO | cog\s1l3_elev_switch.cog |
| MotS | Resource\VIDEO\CUTSCENES.ZIP > cutscenes.goo | cog\s1l1_endcustscene.cog |
| MotS | Episode\JKM.GOO | cog\s2l1_droideye.cog |

Cog and data headers carry dated change notes with developer initials or first names, including DS / D.Shannon, RKD, IS / Ingar, JS, SXC, YW, CR, YB, DB, MT / M.Tateishi, WW, Anthony, Chris K / Chris Klie and Tim L. JK entries run from 10/30/1996 (static.jkl) through 9/1/1997. Examples: "7/28/97 [CR] Doubled saber damage for single player gameplay reasons" on the Imperial commando; "Ingar: modified 5/16/97 removed officer/key" on a level 12 elevator.

MotS ("JK Missions" in the comments, "JkMiss" in paths) was being built before JK shipped in October 1997. An elevator cog was "renamed for Jkm" on 8/10/97, S1L3's switch was copied for "JK Missions' S1L3" on 8/14/97, and S1L1's rebel generator was modified on 8/22/97. Some dates were inherited when files were copied: s1l3_elev_switch.cog repeats the JK entries from 11/13/96 onward.

The cutscene scripts also contain placeholder names: S1L1's ending cutscene has disabled debug prints "shoot kevin" and "shoot ryan", S1L2's has a thing called "steveshoot2", and a Palace droid script notes that it worked "until the testers got a hold of it".

**Evidence**

```
cog\00_elev_switch.cog:11  # Modified 11/13/96 DS  (added third adjoin)
cog\00_elev_switch.cog:17  # Modified 9/1/97 by SXC (took blocked message out)
cog\actor_ic.cog:9  # 7/28/97 [CR] Doubled saber damage for single player gameplay reasons
misc\pup\bo.pup:1  #puppet file for Boc (bo.3do) [Anthony 12/20/96]
cog\s5l4_elev_switch.cog:3  # Modified 8/10/97 by Tim L. (added one more adjoin for access from all 4 sides.) --also renamed for Jkm.
cog\s1l3_elev_switch.cog:13  ## Modified 8/14/97 by Chris K (copied M8_elev_switch.cog, and renamed it for use in JK Missions' S1L3)
cog\s1l1_endcustscene.cog:107  //    Print("shoot kevin");
cog\s2l1_droideye.cog:6  # Otherwise, it won't.  At least it did until the testers got a hold of it.
```

**Sources**

- The JkMiss name and level save dates are covered earlier in this document; the 1997 dates and the "JK Missions" name were not found online.
