# Appendix D. How to extract these files yourself

GOB (JK) and GOO (MotS) files are the same container format: a "GOB " header, a directory offset, then a list of entries (offset, length, 128-byte name). Any GOB/GOO extractor (for example ConMan, JKEdit/JED tools or a small script) will unpack them. The MotS cutscene levels and S6L1 are inside ordinary zip files in Resource\VIDEO: unzip CUTSCENES.ZIP to get cutscenes.goo and UNSUPPORTED.ZIP to get the S6L1 level files.

3DO, KEY, JKL, COG, AI and episode.jk files are plain text and open in any text editor. The header comments quoted in this document are the first lines of each file.

MAT textures need a colormap (.cmp, in misc\cmp) to view 8-bit images. Most MAT viewers let you pick the colormap; use the one named in this document.

Work on copies. Do not modify the original archives in the game folder.
