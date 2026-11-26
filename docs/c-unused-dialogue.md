# C. Unused dialogue

<div class="finding-head" markdown="block">
<span class="game-icons" aria-label="Jedi Knight"><span class="game-icon game-icon--jk" title="Jedi Knight">JK</span></span>
## 9. Unused Qu Rahn lines about the Dark Jedi {#finding-9}
</div>

**Rating:** Partly known

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

**Rating:** Likely new

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

**Rating:** Likely new

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
## 12. Unused MotS civilian and rebel lines {#finding-12}
</div>

**Rating:** Likely new

| Game | Archive | Internal path / files |
|---|---|---|
| MotS | Resource\JKMRES.GOO | voiceuu\cm501xx.wav, cm601xx.wav, cw500xx.wav, cw601xx.wav, 2r6011x.wav, cp641xx.wav (26 files) |

voiceuu holds 26 clips that nothing references. They use the same numbering series as the clips S6L1 does use (cm5013x, cm6014x, cw500xx, cw6016x). The civilians offer items ("Take this, it might help you" / "Don't tell anyone where you got this") or refuse ("Not after what you've done"), which suggests a civilian give-item and reaction system that was cut back. 2r6011x are rebel squad lines and cp641xx are station announcements.

The main MotS voice archive (JKMsndLO.goo) was not examined, so some of these may have duplicates there.

**Evidence**

```
cm50140.wav "Long live the rebellion!"   cm60145.wav "Long live the New Republic."
cm60143.wav "Take this, it might help you."   cm60144.wav "Don't tell anyone where you got this."
cm60154.wav "Not after what you've done."   cw60159.wav "Are you really a Jedi?"
2r60118-21.wav "Hey! Whose side are you on?" / "Traitor" (auto-transcribed as "Trader") / "Follow me!" / "Return fire!"
cp64114.wav "Warning, depressurization imminent."   cp64117.wav "Depressurization averted."
```

**Sources**

- No earlier source found.
