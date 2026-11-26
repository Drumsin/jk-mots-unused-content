# C. Unused dialogue

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span></span>
## 9. Unused Qu Rahn lines about the Dark Jedi {#finding-9}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--partly"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z"/></svg>Partly known</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Resource\Res1hi.gob | voice\i00ra20z.wav, voice\i00ra51z.wav, voice\i00ra52z.wav |

Qu Rahn's Dark Jedi descriptions are numbered in sequence. Three clips in the series are never played: i00ra20z sits between the used Yun lines 19 and 21, and i00ra51z/52z sit between Boc (49-50) and Jerec (53). They are extra descriptions of Yun and Boc.

Transcripts were made automatically and should be checked by ear.

**Evidence**

```
i00ra20z.wav: "This young man grew up knowing only the dark side and has never seen the light side and its power."
i00ra51z.wav: "He may look clumsy and uncoordinated, almost drunk at times, but I found that he is very able and can sustain an effective energy level that would leave most exhausted."
i00ra52z.wav: "If it isn't his manner that throws you, it would be his hyperactive skill."
```

**Sources**

- The Sounds Resource (sounds-resource.com) JK voice rips include the audio. No source was found that flags these lines as unused.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span></span>
## 10. Other unused JK voice clips {#finding-10}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Resource\Res1hi.gob | voice\i00ky28z.wav, i00ky47z.wav, i00ky71z.wav, i00wm02z.wav, i00wm03z.wav |

Kyle lines and two civilian (wm) lines that no cog or level plays.

i00ky71z is commented out as the drowning sound in every Kyle sound set (ky.snd and the multiplayer kymp*.snd sets: "#drowning i00ky71z.wav"). The line right above it plays i00ky71t.wav instead, so Kyle does make a drowning sound in the game; it is a different, longer recording (1.6 s against 0.65 s, and the waveforms do not match).

**Evidence**

```
i00ky28z.wav: "Big enough door."
i00ky47z.wav: "This must lead to the upper bulkhead."
i00ky71z.wav: (grunt)  -  ky.snd: drowning i00ky71t.wav (used) / #drowning i00ky71z.wav (commented out)
i00wm02z.wav: "Run!"
i00wm03z.wav: "No blasters, no blasters!"
```

**Sources**

- No earlier source found.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span></span>
## 11. 01_trouble.cog: an unfinished Nar Shaddaa bar exchange {#finding-11}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| JK | Episode\JK1.GOB | cog\01_trouble.cog |

An unused cog for a bartender exchange in level 1. The bartender's line (i00mn19z.wav) is real, but the three follow-up lines (snappycomeback, followup, riposte) are `xxx.wav` placeholders and the calls that would play them are commented out. The scene was set up and never recorded.

**Evidence**

```
sound        paying=i00mn19z.wav
sound        snappycomeback=xxx.wav
sound        followup=xxx.wav
sound        riposte=xxx.wav
//    PlaySoundLocal(snappycomeback, 1, 0.0, 0);
```

**Sources**

- No earlier source found.

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Mysteries of the Sith"><span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span></span>
## 12. Unused MotS voices in the voiceuu folder {#finding-12}
</div>

<p class="finding-rating">
<span class="finding-rating__label">Rating:</span>
<span class="rating-pill rating-pill--new"><svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z"/></svg>Likely new</span>
</p>

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | voiceuu\*.wav (46 files: 28 civilian, rebel and announcement clips; 15 Ka'Pa the Hutt lines; 3 Abron Mar lines) |

The folder `voiceuu` (uu = unused) in JKMRES.GOO holds 46 WAV files that a normal playthrough never loads. Community modder Shimstock pointed out this folder, and recalled that many of the clips were from the cutscenes.

28 of them are unreferenced civilian, rebel and announcement lines in the same numbering series as clips S6L1 does use (cm501xx, cm601xx, cw500xx, cw601xx, 2r6011x, cp641xx). An earlier version of this document counted 26 of that group. The civilians offer items ("Take this, it might help you" / "Don't tell anyone where you got this") or refuse ("Not after what you've done"), which suggests a civilian give-item and reaction system that was cut back. 2r6011x are rebel squad lines and cp641xx are station announcements.

The other 18 are lines for the leftover in-engine ending cutscenes in CUTSCENES.ZIP. Fifteen are Ka'Pa the Hutt speaking Huttese (`ka921*` from the S2L1 palace ending, and `ka924*` from the S2L4 ending). Three are Abron Mar (`ab92206`, `ab92207` and `ab92208`) from the S2L2 ending. Those leftover cutscene cogs still name the files, but the shipped episode plays SMUSH videos (`.san`) instead, so these WAVs never run in a normal MotS playthrough and exist only under voiceuu. The Ka'Pa clips were identified by listening; they are Huttese, not English, and are not quoted here. Abron Mar's three lines are spoken English in that leftover S2L2 ending, but they are described rather than quoted until they can be transcribed with confidence.

Mara's matching lines from the same cutscenes (`mj921*`, `mj924*`) are not in JKMRES. The MotS sound archive (JKMsndLO.goo) was checked for Kaerobani (`kb*`) voice files and none were found (see Finding 24). It has not been fully transcribed for duplicates of the voiceuu clips.

**Evidence**

```
cm50140.wav "Long live the rebellion!"   cm60145.wav "Long live the New Republic."
cm60143.wav "Take this, it might help you."   cm60144.wav "Don't tell anyone where you got this."
cm60154.wav "Not after what you've done."   cw60159.wav "Are you really a Jedi?"
2r60118-21.wav "Hey! Whose side are you on?" / "Traitor" (auto-transcribed as "Trader") / "Follow me!" / "Return fire!"
cp64114.wav "Warning, depressurization imminent."   cp64117.wav "Depressurization averted."
voiceuu holds 46 WAVs. Ka'Pa (Huttese, not quoted): ka92102, 04, 05, 07, 09, 12, 13, 14, 16, 17, 18, 20; ka92403, 06, 07. Abron Mar: ab92206, ab92207, ab92208 (English, not quoted here). Referenced only by leftover cutscene cogs s2l1_endcut.cog, s2l4_endcutscene.cog, s2l2b_endcutscene.cog.
```

**Sources**

- Community modder Shimstock pointed out the unused voiceuu folder in JKMRES, and that many of the clips came from the cutscenes. The Ka'Pa lines were identified by listening while re-checking this document.
