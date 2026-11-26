# Appendix C. Caveats

- The MotS sound archive (JKMsndLO.goo) and the cutscene videos (.smk/.san) were not available for this survey. Many MotS sound files therefore show up as "missing" only because that archive was not read, and the MotS subtitle strings for cog IDs 10043, 10000 and 43003 could not be read either.
- Some names are built at runtime (cog LoadTemplate calls, models.dat, saber and HUD naming rules). The known rules are modeled, but a few "unreferenced" files could still be loaded dynamically.
- Voice transcripts were made automatically and may contain errors. Check them by ear.
- Colormaps for textures that no level uses are best guesses ("?"). They are visual matches, not evidence.
- GOB/GOO directory entries store only offset, size and name; there are no per-file timestamps. The only dates are JKL "Created" stamps and zip entry dates.
- Renders are simple: flat lighting, no transparency, no light-mode or geometry-mode effects, first geoset (highest detail) only. Missing textures are drawn in flat grey. Posed characters use frame 0 of the named keyframe.
- The original executables (JK.exe, JKM.exe) were not available, so hard-coded names come from the OpenJKDF2 source. JK's cutscenes are pre-rendered videos (.smk), which were not available either; a model can appear in a video without any data file referencing it.
- The "Hints in comments" section rests on developer comments. Comments can be out of date or copied along with a file from another level, so they show what someone wrote at some point, not necessarily what was planned at the end. Findings marked Speculative should be read that way.
- Two sounds in JK's sound archive (00techamb05.wav, 16metalcreak01.wav) are never played by JK, but MotS levels refer to them by name (00techamb05 in s2l2a, s4l3, S6L1 and the multiplayer maps mdm02, mdm08 and mdm17; 16metalcreak01 in s2l4). MotS loads sounds from its own archive, which was not available, so they are counted as used by MotS and not listed as unused content.
- A "Likely new" rating means no earlier source was found in the community sources checked. It is not a claim of priority.
