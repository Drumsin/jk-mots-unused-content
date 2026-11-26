# Appendix A. Unreferenced asset lists

The full lists are in [jk_unreferenced_assets.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/jk_unreferenced_assets.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/jk_unreferenced_assets.csv)) and [mots_unreferenced_assets.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/mots_unreferenced_assets.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/mots_unreferenced_assets.csv)) (game, name, type, status, archive, internal path, referenced_by, dev_source; the MotS list also flags files that are byte-identical to, or share a name with, a JK file). Status "unreferenced" means no file mentions the asset; "ref_only_by_unused" means only another unused file points to it. Counts by file type:

| Type | JK | MotS |
|---|---:|---:|
| `mat` | 57 | 1033 |
| `3do` | 28 | 275 |
| `cog` | 49 | 145 |
| `key` | 32 | 125 |
| `wav` | 14 | 28 |
| `ai` | 14 | 19 |
| `ai0` | 10 | 3 |
| `ai2` | 10 | 3 |
| `snd` | 1 | 8 |
| `pup` | 2 | 5 |
| `bm` | 6 | 0 |
| `cmp` | 3 | 2 |
| `par` | 2 | 0 |
| `gif` | 0 | 1 |
| **Total** | **228** | **1647** |

Each list was then checked against the other game (column `cross_game_verdict`, with the referencing files in `used_by_other_game_files`):

| Cross-game result | JK list | MotS list |
|---|---:|---:|
| Unused in both games | 208 | 1449 |
| Used by the other game, or a copy of a used file | 20 | 198 |

The .ai0 and .ai2 files are difficulty variants of .ai files, and they are loaded: the engine first opens the .ai name plus the difficulty digit (0 = Easy, 2 = Hard; Medium has no .ai1 file and falls back to the .ai). An earlier version of this document missed this rule; the 179 difficulty variants of used .ai files are now counted as used and removed from these lists (see [Appendix G](appendix-g-changelog.md) and [kc_feedback_ai_difficulty_files.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/kc_feedback_ai_difficulty_files.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/kc_feedback_ai_difficulty_files.csv))). Most MotS entries are textures, and 176 of them are byte-identical copies of JK files carried over into MotS.

Other tables: [comments_all.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/comments_all.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/comments_all.csv)) and [comments_flagged.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/comments_flagged.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/comments_flagged.csv)) (every extracted comment, and the flagged ones with cross-game checks), [comment_findings.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/comment_findings.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/comment_findings.csv)) (evidence for the "Hints in comments" section), [missing_references.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/missing_references.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/missing_references.csv)) (names that are referenced but not shipped), [3do_dev_source_paths.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/3do_dev_source_paths.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/3do_dev_source_paths.csv)) (the source path and exporter version of every 3DO), [jkl_headers.csv](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/jkl_headers.csv) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/jkl_headers.csv)) (dev path and save date of every level) and [unused_voice_transcripts_auto.txt](https://github.com/Drumsin/jk-mots-unused-content/blob/main/references/unused_voice_transcripts_auto.txt) ([download](https://github.com/Drumsin/jk-mots-unused-content/raw/main/references/unused_voice_transcripts_auto.txt)).
