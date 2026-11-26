#!/usr/bin/env python3
"""Generate FINDINGS.md and the MkDocs pages from the same content sources.

Run from the repository root:

    python3 tools/build_docs.py

Looks for the PDF content modules (content.py, content_comments.py) in the
directory set by JK_MOTS_PDF_SRC, and for reference CSVs in references/ first.
This writes FINDINGS.md and docs/*.md together so the website and the
single-file copy stay in sync. It does not rebuild the print PDF.
"""
from __future__ import annotations

import collections
import csv
import html
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF_SRC = Path(os.environ.get("JK_MOTS_PDF_SRC", "/workspace/jkdig/pdf"))
CSV_CANDIDATES = [
    ROOT / "references",
    Path("/workspace/notes/jk_mots_unused"),
]

VERSION = "v2.2"
VERSION_MONTH = "November 2026"
REPO = "https://github.com/Drumsin/jk-mots-unused-content"
ISSUE = f"{REPO}/issues/new/choose"
PDF_URL = f"{REPO}/releases/download/{VERSION}/JK_MotS_Unused_Content_Findings_{VERSION}.pdf"
ZIP_URL = f"{REPO}/releases/download/{VERSION}/JK_MotS_Unused_Content_Findings_{VERSION}.zip"
BLOB = f"{REPO}/blob/main/references"
RAW = f"{REPO}/raw/main/references"

ISSUE_NOTE = (
    "Have a new finding, a correction, or a file this document should look at again? "
    f"Please [open an issue]({ISSUE}) and tell us about it. Screenshots and exact file names help a lot. "
    "If you don't use GitHub, you can still post in Discord and it will be relayed here."
)

CSV_FILES = [
    "jk_unreferenced_assets.csv",
    "mots_unreferenced_assets.csv",
    "cross_game_verification.csv",
    "missing_references.csv",
    "3do_dev_source_paths.csv",
    "jkl_headers.csv",
    "katarn_home_mats.csv",
    "kc_feedback_ai_difficulty_files.csv",
    "comments_all.csv",
    "comments_flagged.csv",
    "comment_findings.csv",
    "unused_textures_sheet_index.csv",
    "unused_voice_transcripts_auto.txt",
]

# Stable site paths (do not rename; public anchors depend on them).
SECTION_FILES = [
    ("A", "a-barons-hed.md"),
    ("B", "b-other-cut-levels.md"),
    ("C", "c-unused-dialogue.md"),
    ("D", "d-unused-scripts.md"),
    ("E", "e-weapons-animations-models.md"),
    ("F", "f-headers-dates.md"),
    ("G", "g-hints-in-comments.md"),
    ("H", "h-community-feedback.md"),
    ("I", "i-added-in-v22.md"),
]
APPENDIX_FILES = {
    "A": "appendix-a-unreferenced-lists.md",
    "B": "appendix-b-texture-sheet.md",
    "C": "appendix-c-caveats.md",
    "D": "appendix-d-extracting-files.md",
    "E": "appendix-e-credits.md",
    "F": "appendix-f-cross-game-check.md",
    "G": "appendix-g-changelog.md",
}

# Appendix F / G tables (same rows as the v2.1 PDF).
CROSS_GAME_CHANGES = [
    ("05vtiebm.3do", "MotS JKMRES", "Unreferenced in both games, but it is an animation export of the TIE bomber tieb.3do (same textures, same vertex count), which JK uses in 01narshadda, 06bbarons, 08escape88 and MotS in s1l1_rebelbase.", "Reworded: in-game ship, unused animation file"),
    ("05vcrowm.3do", "MotS JKMRES", "Unreferenced in both games; same texture set as crow.3do, used in many JK levels and MotS mdm12_spaceport.", "Reworded: in-game ship, unused animation file"),
    ("05vtrnwg.3do", "MotS JKMRES", "Unreferenced in both games; the transport with WeeGee on it (droid nodes plus T~TRANSP; TTRN and WeeGee textures). ttrn.3do and wg.3do are used in JK level 4.", "Reworded: WeeGee riding the transport"),
    ("yss.3do", "MotS JKMRES", "The ysalamiri is used in MotS (ys.3do in s5l2_darkswamp and KFY maps k1-k5). yss is the unreferenced shoulder export of the same model.", "Moved to alternate exports"),
    ("ligt.3do", "JK Res2", "Earlier copy of the Force Lightning segment. Both games use ligt2.3do (same texture, same 30 vertices) via +force_ltpeice.", "Reworded: effect is used, this copy is not"),
    ("kysnap3.key", "JK Res2 + MotS JKMRES", "Unused in JK but used in MotS (s5l2_darkswamp, s5l4_lowersith, a MotS puppet).", "Corrected"),
    ("sab0.3do", "JK + MotS", "Used in both games.", "Removed from the unused list"),
    ("bikeacl1.wav, biketrn1.wav", "JK Res1hi", "Played in JK level 4 by 04_soundofcars.cog.", "Removed from the unused list"),
    ("13wcanw7.mat", "MotS JKMRES", "Used by MotS s1l1_rebelbase.", "Removed from the contact sheet; noted"),
    ("13fwater.mat", "MotS JKMRES", "Byte-identical to the JK texture used in 04escapehouse, 06bbarons, 17asarris.", "Excluded from the unused 13 count (41 of 43)"),
    ("kbface.mat", "MotS JKMRES", "Used by KYkb.3do, the \"Kaerrobanii\" multiplayer skin in models.dat.", "Removed from the contact sheet"),
    ("09sky01.mat", "JK Res2", "Unused in JK, but the identical MotS copy is used by cutscene levels s4l3_ocs and s4l3_ecs.", "Removed from the contact sheet"),
    ("dflt.cmp", "JK Res2", "JK copy unreferenced, but MotS's own dflt.cmp is loaded by cutscene s4l2_ocs.", "Removed from unused colormaps"),
    ("u2.3do, ug.3do", "MotS JKMRES", "Same geometry as the used u2alt.3do / ugalt.3do.", "Reclassified as alternate copies"),
    ("shutdunc.3do, kelbite.3do, walt.3do", "MotS JKMRES", "Copies or variants of used shut.3do, kd.3do (JK Kell dragon) and walt_b.3do.", "Reclassified as alternate copies"),
    ("kyasleep, kb, dvboss, mjsaber, s0alt, s1alt, du2alt", "MotS JKMRES", "Unreferenced, but alternate exports of characters that are in the game.", "Grouped as alternate exports"),
    ("00_glass.mat", "missing in JK", "JK shard0.3do asks for it; JK does not ship it but MotS ships and uses it.", "Missing-reference note updated"),
]
V20_CHANGES = [
    ("03trcr.3do (tractor) + 5 textures", "MotS JKMRES", "Identified from KnightCop's screenshot. Shipped only in MotS, used by neither game.", "Added (section H)"),
    ("03wswt1a-d, 03went, 03went1, 03went2, 03wstr1a, 03wstr1c, 03pict1d", "MotS JKMRES", "Matched pixel for pixel to KnightCop's screenshots. MotS-only, used by neither game, including multiplayer.", "Added (section H)"),
    ("03wstr1b.mat", "JK Res2", "The plain wood grain in the same screenshot. Used by JK level 3 (03katarn).", "Noted as used"),
    ("129 MotS-only 03/04 textures", "MotS JKMRES", "Sweep of all 272 level 3/4 textures in both games.", "Added with a contact sheet (katarn_home_mats.csv)"),
    ("179 .ai0/.ai2 files (114 JK, 65 MotS)", "JK Res2, MotS JKMRES", "The engine loads name.ai0 on Easy and name.ai2 on Hard (OpenJKDF2 sithAIClass_LoadEntry). Variants of used .ai files are used.", "Moved to used; lists and counts updated (kc_feedback_ai_difficulty_files.csv)"),
    ("i00ky71z.wav", "JK Res1hi", "Commented-out drowning grunt; the drowning slot plays i00ky71t.wav, a different recording that is heard in the game.", "Clarified in section C"),
    ("00techamb05.wav, 16metalcreak01.wav", "JK Res1hi", "JK never plays them; MotS levels and multiplayer maps refer to them by name.", "Caveat reworded"),
]
UNCHANGED = [
    "Models and textures in multiplayer maps: every asset named in this document, every entry on the contact sheet and every row of both unreferenced lists (1,990 names) was searched again by full name, by name without the extension and by substring in every level of both games, every multiplayer, CTF and Kill-the-Fool map, the cutscene levels, S6L1, static.jkl, models.dat, sabers.dat, items.dat, and every template, cog, puppet, sound set, particle, sprite and AI file. Comments were left out, and any hit in a file that is itself loaded was looked at by hand. Apart from the AI difficulty files, nothing turned out to be loaded. The other hits were name collisions, for example \"sphere\" inside sphere.par, \"sign\" as a cog surface name, or \"tree\" in the map title \"Tree Canopy\".",
    "Sounds: each JK sound called unused was compared by name, with siblings (such as the \"t\" and \"z\" takes of a line), and by waveform against all 690 sounds in both games. None is a copy of a sound the games play. The bike sounds bikeacl1/biketrn1 (used in JK level 4) and the bartender line i00mn19z (used by 01_bartender.cog in level 1) were already marked as used. If the sound KnightCop meant is not one of these, the file name would settle it.",
    "Cut weapons: the community restoration of the Tusken prod and the early Repeater gun (Shimstock and KnightCop) matches the leftovers already described in section E (the prdv, prgv, prdp and prdg prod models and repv/repp). The only other trace in the data is the menu strings \"Repeater\" and \"Repeater Gun\" in jkstrings.uni, and those name the final weapon 6, which is in the game.",
]
CAVEATS = [
    "The MotS sound archive (JKMsndLO.goo) was checked for Kaerobani (kb*) voice file names; none were found. It has not been fully transcribed, and the MotS subtitle strings for cog IDs 10043, 10000 and 43003 were not read. The cutscene videos (.smk/.san) were not compared line by line, so some MotS sounds may still appear missing only because they live in that archive or inside the videos.",
    "Some names are built at runtime (cog LoadTemplate calls, models.dat, saber and HUD naming rules). The known rules are modeled, but a few \"unreferenced\" files could still be loaded dynamically.",
    "Voice transcripts were made automatically and may contain errors. Check them by ear.",
    "Colormaps for textures that no level uses are best guesses (\"?\"). They are visual matches, not evidence.",
    "GOB/GOO directory entries store only offset, size and name; there are no per-file timestamps. The only dates are JKL \"Created\" stamps and zip entry dates.",
    "Renders are simple: flat lighting, no transparency, no light-mode or geometry-mode effects, first geoset (highest detail) only. Missing textures are drawn in flat grey. Posed characters use frame 0 of the named keyframe.",
    "The original executables (JK.exe, JKM.exe) were not available, so hard-coded names come from the OpenJKDF2 source. JK's cutscenes are pre-rendered videos (.smk), which were not available either; a model can appear in a video without any data file referencing it.",
    "The \"Hints in comments\" section rests on developer comments. Comments can be out of date or copied along with a file from another level, so they show what someone wrote at some point, not necessarily what was planned at the end. Findings marked Speculative should be read that way.",
    "Two sounds in JK's sound archive (00techamb05.wav, 16metalcreak01.wav) are never played by JK, but MotS levels refer to them by name (00techamb05 in s2l2a, s4l3, S6L1 and the multiplayer maps mdm02, mdm08 and mdm17; 16metalcreak01 in s2l4). MotS loads sounds from its own archive, which was not available, so they are counted as used by MotS and not listed as unused content.",
    "A \"Likely new\" rating means no earlier source was found in the community sources checked. It is not a claim of priority.",
]


def csv_dir() -> Path:
    for p in CSV_CANDIDATES:
        if (p / "jk_unreferenced_assets.csv").is_file():
            return p
    raise SystemExit("Could not find reference CSVs")


def load_sources():
    if not (PDF_SRC / "content.py").is_file():
        raise SystemExit(f"PDF content source not found at {PDF_SRC}/content.py")
    sys.path.insert(0, str(PDF_SRC))
    from content import SECTIONS, KC, RED, TCRF, MAS, TSR, KCSEC, V22SEC
    from content_comments import CINTRO, CFINDS

    sections = list(SECTIONS) + [
        ("G. Hints in comments", CFINDS, CINTRO),
        (
            KCSEC[0],
            KCSEC[1],
            [
                "These two findings were added after KnightCop reviewed the first published version. Thank you to KnightCop for the corrections and pointers; the full list of changes from that review is in Appendix G."
            ],
        ),
        (
            V22SEC[0],
            V22SEC[1],
            [
                "These findings were added in v2.2 from community notes and a further pass over leftover templates and scripts."
            ],
        ),
    ]
    credits = [
        KC + ". The main reference for the cut speeder-bike mission; recreates the missing bike textures. KnightCop also reviewed the first published version (Appendix G).",
        "Shimstock: co-author with KnightCop of the Tusken prod and Repeater gun restoration sheet; the community theories in v2.1 (s5 E-Web gunner, ligt.3do as the prod projectile); and the v2.2 notes on the level-05 ship dogfight, kystab and kyrepel0, rep0.3do, the MotS in-engine cutscenes, the voiceuu folder, and unused Kaerobani lines.",
        RED,
        TCRF,
        MAS + ", including the Early Dev Enemy Pack and 8t88 beast pages.",
        TSR,
        "A Steam community guide on the hidden MotS level S6L1 (Dark Kyle in the garbage room).",
        "Cogking, for confirming that the Jedi Knight developers were experimenting with a saber throw.",
        "OpenJKDF2 (github.com/shinyquagsire23/OpenJKDF2), for engine-loaded file names, the HUD icon naming rule and the 3DO hierarchy/matrix conventions used by the renderer.",
    ]
    return sections, credits


def xml_to_md(s: str) -> str:
    if not s:
        return ""
    s = re.sub(
        r'<font face="Mono">(.*?)</font>',
        lambda m: "`" + html.unescape(re.sub(r"<[^>]+>", "", m.group(1))) + "`",
        s,
        flags=re.I | re.S,
    )
    s = re.sub(r"<font[^>]*>(.*?)</font>", r"\1", s, flags=re.I | re.S)
    s = re.sub(r"<b>(.*?)</b>", r"**\1**", s, flags=re.I | re.S)
    s = re.sub(r"<i>(.*?)</i>", r"*\1*", s, flags=re.I | re.S)
    s = re.sub(r"<br\s*/?>", "\n\n", s, flags=re.I)
    s = re.sub(r"</?[^>]+>", "", s)
    return html.unescape(s).strip()


def link_refs(s: str, mode: str) -> str:
    def repl(m):
        name = m.group(0)
        if mode == "site":
            return f"[{name}]({BLOB}/{name}) ([download]({RAW}/{name}))"
        return f"[{name}](references/{name})"

    parts = re.split(r"(`[^`]*`|\[[^\]]*\]\([^)]*\))", s)
    names = "|".join(re.escape(n) for n in sorted(CSV_FILES, key=len, reverse=True))
    pat = re.compile(names)
    out = []
    for i, p in enumerate(parts):
        out.append(p if i % 2 == 1 else pat.sub(repl, p))
    return "".join(out)


def P(s: str, mode: str) -> str:
    return link_refs(xml_to_md(s), mode)


def md_cell(s: str, mode: str) -> str:
    return P(s, mode).replace("\n", " ").replace("|", "\\|")


def inline_md_to_html(s: str) -> str:
    """Render the inline Markdown that P() emits (links, code, bold, italics).

    Figcaptions live inside a raw HTML <figure>, and Python-Markdown's
    md_in_html extension does not parse a nested <figcaption> unless that
    tag also has a markdown= attribute. Pre-rendering avoids that pitfall.
    """
    import markdown as md

    out = md.markdown(s, extensions=["extra"]).strip()
    return re.sub(r"^<p>(.*)</p>$", r"\1", out, flags=re.S)


def letter_of(title: str) -> str:
    m = re.match(r"^([A-Z])\.", title)
    return m.group(1) if m else ""


def img_path(name: str, mode: str) -> str:
    # FINDINGS.md and docs/*.md both sit next to a renders/ folder
    # (docs/renders is a symlink to the repo renders/).
    return f"renders/{name}.png"



def render_figure(path: str, cap: str, mode: str, skip_lightbox: bool = False) -> list[str]:
    """Image plus caption. Site pages use a <figure> so the caption sits with the render."""
    cap_md = P(cap, mode)
    alt = md_cell(cap, mode)
    if mode != "site":
        return [f"![{alt}]({path})", "", f"*{cap_md}*", ""]
    skip = "{ .skip-lightbox }" if skip_lightbox else ""
    cap_html = inline_md_to_html(cap_md)
    return [
        '<figure class="finding-figure" markdown="1">',
        f"![{alt}]({path}){skip}",
        f"<figcaption>{cap_html}</figcaption>",
        "</figure>",
        "",
    ]



def games_covered(f: dict) -> tuple[bool, bool]:
    """Return (covers_jk, covers_mots) from a finding's location rows."""
    has_jk = False
    has_mots = False
    for g, _a, _p in f.get("loc") or []:
        for part in re.split(r"[^A-Za-z0-9]+", g):
            pl = part.lower()
            if pl == "jk":
                has_jk = True
            elif pl == "mots":
                has_mots = True
    return has_jk, has_mots


def game_icon_html(f: dict) -> str:
    has_jk, has_mots = games_covered(f)
    chips = []
    if has_jk:
        chips.append('<span class="game-icon game-icon--jk" title="Jedi Knight">JK</span>')
    if has_mots:
        chips.append('<span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span>')
    names = [n for n, flag in (("Jedi Knight", has_jk), ("Mysteries of the Sith", has_mots)) if flag]
    aria = " and ".join(names) if names else "Game"
    return f'<span class="game-icons" aria-label="{aria}">{" ".join(chips)}</span>'



# Material icons (path data from Material for MkDocs), used in rating pills.
_RATING_ICON_PATHS = {
    "check": "M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m-2 15-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8z",
    "half": "M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 2a8 8 0 0 1 8 8 8 8 0 0 1-8 8z",
    "star": "M12 1 9 9l-8 3 8 3 3 8 3-8 8-3-8-3z",
    "help": "m15.07 11.25-.9.92C13.45 12.89 13 13.5 13 15h-2v-.5c0-1.11.45-2.11 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41a2 2 0 0 0-2-2 2 2 0 0 0-2 2H8a4 4 0 0 1 4-4 4 4 0 0 1 4 4 3.2 3.2 0 0 1-.93 2.25M13 19h-2v-2h2M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10c0-5.53-4.5-10-10-10",
    "bookmark": "M17 3H7a2 2 0 0 0-2 2v16l7-3 7 3V5a2 2 0 0 0-2-2",
    "tag": "m21.41 11.58-9-9A2 2 0 0 0 11 2H4a2 2 0 0 0-2 2v7a2 2 0 0 0 .59 1.42l9 9A2 2 0 0 0 13 22a2 2 0 0 0 1.41-.59l7-7A2 2 0 0 0 22 13a2 2 0 0 0-.59-1.42M13 20l-9-9V4h7l9 9M6.5 5A1.5 1.5 0 1 1 5 6.5 1.5 1.5 0 0 1 6.5 5",
    "doc": "M6 2a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6zm0 2h7v5h5v11H6zm2 8v2h8v-2zm0 4v2h5v-2z",
}

# slug, icon-key  — one style per distinct rating level
RATING_STYLES = {
    "Known": ("known", "check"),
    "Known (detail likely new)": ("known", "check"),
    "Known / Partly known": ("partly", "half"),
    "Partly known": ("partly", "half"),
    "Likely new": ("new", "star"),
    "Likely new (observation)": ("new", "star"),
    "Likely new / Partly known": ("new", "star"),
    "Likely new (purpose speculative)": ("speculative", "help"),
}
CLASSIFICATION_STYLES = {
    "Speculative": ("speculative", "help"),
    "Confirmed cut": ("cut", "bookmark"),
    "Confirmed cut (reworded)": ("cut", "bookmark"),
    "Confirmed cut (disabled)": ("cut", "bookmark"),
    "Likely rename": ("rename", "tag"),
    "Dev notes": ("notes", "doc"),
}


def rating_icon_svg(key: str) -> str:
    d = _RATING_ICON_PATHS[key]
    return (
        f'<svg class="rating-pill__icon" xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
        f'<path d="{d}"/></svg>'
    )


def rating_pill_html(text: str, slug: str, icon: str) -> str:
    label = html.escape(text)
    return (
        f'<span class="rating-pill rating-pill--{slug}">'
        f"{rating_icon_svg(icon)}{label}</span>"
    )


def render_rating_line(f: dict, mode: str) -> list[str]:
    extra = f"  ·  Classification: **{P(f['cls'], mode)}**" if f.get("cls") else ""
    if mode != "site":
        return [f"**Rating:** {f['r']}{extra}", ""]
    slug, icon = RATING_STYLES.get(f["r"], ("fallback", "help"))
    parts = [
        '<p class="finding-rating">',
        '<span class="finding-rating__label">Rating:</span>',
        rating_pill_html(f["r"], slug, icon),
    ]
    if f.get("cls"):
        cslug, cicon = CLASSIFICATION_STYLES.get(f["cls"], ("fallback", "tag"))
        parts.append(rating_pill_html(f["cls"], cslug, cicon))
    parts.append("</p>")
    return parts + [""]


def render_finding(n: int, f: dict, mode: str) -> list[str]:
    lines = []
    title = P(f["t"], mode)
    if mode == "site":
        # Chips sit beside the heading so the TOC stays a clean title.
        lines += [
            '<div class="finding-head" markdown="block">',
            game_icon_html(f),
            f"## {n}. {title} {{#finding-{n}}}",
            "</div>",
            "",
        ]
    else:
        lines += [f'<a id="finding-{n}"></a>', f"### {n}. {title}", ""]
    lines += render_rating_line(f, mode)
    lines += ["| Game | Archive | Internal path / files |", "|---|---|---|"]
    for g, a, pth in f["loc"]:
        lines.append(f"| {md_cell(g, mode)} | {md_cell(a, mode)} | {md_cell(pth, mode)} |")
    lines.append("")
    for x in f["d"]:
        lines += [P(x, mode), ""]
    if f.get("ev"):
        lines += ["**Evidence**", "", "```"]
        for evl in f["ev"]:
            lines.append(evl.replace("\t", "    "))
        lines += ["```", ""]
    if f.get("src"):
        lines.append("**Sources**")
        lines.append("")
        for s in f["src"]:
            lines.append(f"- {P(s, mode)}")
        lines.append("")
    if f.get("img"):
        for nm, cap in f["img"]:
            lines += render_figure(img_path(nm, mode), cap, mode)
    return lines


def counts_tables(mode: str) -> list[str]:
    d = csv_dir()

    def counts(p):
        c = collections.Counter()
        for r in csv.DictReader(open(p, encoding="utf-8", errors="replace")):
            c[r["ext"]] += 1
        return c

    cj = counts(d / "jk_unreferenced_assets.csv")
    cm = counts(d / "mots_unreferenced_assets.csv")
    exts = sorted(set(cj) | set(cm), key=lambda e: -(cj[e] + cm[e]))
    lines = ["| Type | JK | MotS |", "|---|---:|---:|"]
    for e in exts:
        lines.append(f"| `{e}` | {cj[e]} | {cm[e]} |")
    lines += [f"| **Total** | **{sum(cj.values())}** | **{sum(cm.values())}** |", ""]
    vc = {}
    for gname, fn in (("JK", "jk_unreferenced_assets.csv"), ("MotS", "mots_unreferenced_assets.csv")):
        c = collections.Counter()
        for r in csv.DictReader(open(d / fn, encoding="utf-8", errors="replace")):
            v = r["cross_game_verdict"]
            if v.startswith("Unused"):
                label = "Unused in both games"
            elif v.startswith("Leftover"):
                label = "Used by the other game, or a copy of a used file"
            else:
                label = v
            c[label] += 1
        vc[gname] = c
    keys = sorted(set(vc["JK"]) | set(vc["MotS"]))
    lines += [
        "Each list was then checked against the other game (column `cross_game_verdict`, with the referencing files in `used_by_other_game_files`):",
        "",
        "| Cross-game result | JK list | MotS list |",
        "|---|---:|---:|",
    ]
    for k in keys:
        lines.append(f"| {k} | {vc['JK'][k]} | {vc['MotS'][k]} |")
    lines.append("")
    return lines


def intro_body(mode: str) -> list[str]:
    if mode == "site":
        app_f = "appendix-f-cross-game-check.md"
        app_d = "appendix-d-extracting-files.md"
        app_e = "appendix-e-credits.md"
        comments = "g-hints-in-comments.md"
        xcheck = f"[cross_game_verification.csv]({BLOB}/cross_game_verification.csv) ([download]({RAW}/cross_game_verification.csv))"
        app_f_link = f"[Appendix F]({app_f})"
        app_d_link = f"[Appendix D]({app_d})"
        app_e_link = f"[Appendix E]({app_e})"
        hints = f'[section "Hints in comments"]({comments})'
    else:
        xcheck = P("cross_game_verification.csv", mode)
        app_f_link = "Appendix F"
        app_d_link = "Appendix D"
        app_e_link = "Appendix E"
        hints = 'the section "Hints in comments"'
    lines = [
        "This is a catalogue of files in the retail Jedi Knight (JK) and Mysteries of the Sith (MotS) data that the games never load, or that point at files which do not exist. Many of them are leftovers from cut levels, early tests and earlier versions of models and scripts. Each finding gives the exact location so anyone can open the file and check it.",
        "",
        "### Method" if mode != "site" else "## Method",
        "",
        "All shipped archives were extracted and read: JK Episode\\JK1.GOB, JK1CTF.GOB, JK1MP.GOB and Resource\\Res1hi.gob, Res2.gob; MotS Episode\\JKM.GOO, JKM_KFY.GOO, JKM_MP.GOO, JKM_SABER.GOO and Resource\\JKMRES.GOO, plus cutscenes.goo (inside Resource\\VIDEO\\CUTSCENES.ZIP) and the hidden S6L1 level (inside Resource\\VIDEO\\UNSUPPORTED.ZIP).",
        "",
        "Shimstock pointed out that the MotS cutscenes were built as in-engine levels, played in the game, and recorded to video. Those earlier, unfinished scene setups are the JKL files in Resource\\VIDEO\\CUTSCENES.ZIP, already used as a source in this catalogue. The shipped episode does not load them; after each level it plays the later SMUSH videos (.san). (JK's live-action cutscenes are the .smk files.) The JKL worlds were last saved in late November 1997 through 2 January 1998, before the shipped MotS levels, and they still show unfinished names, disabled subtitles, leftover debug prints, and voice lines and props (including Ka'Pa the Hutt and Abron Mar) that never appear in a normal playthrough.",
        "",
        "A reference graph was built for every file type. The roots are every level (.jkl), episode.jk, static.jkl, items.dat, models.dat, sabers.dat, the .per and .uni files and the file names hard-coded in the engine (taken from the OpenJKDF2 source, including the HUD icon naming rule and, since the revision after KnightCop's feedback, the AI difficulty rule: *name*.ai0 on Easy and *name*.ai2 on Hard). From the roots, references were followed through templates, cogs, 3DOs, keyframes, puppets, sound sets, materials and colormaps. Comment lines were not counted as references, because a commented-out line loads nothing; the comments themselves were read separately (see "
        + hints
        + '). A file that no root reaches is "unreferenced". A name that is referenced but not present in any archive is a "missing reference".',
        "",
        "3DO and KEY headers (source paths, exporter versions) and JKL headers (save dates, dev paths) were read for every file. Unused voice clips were transcribed automatically. 3DO renders in this document come from a small software renderer that follows the engine's hierarchy and matrix conventions. Textures are drawn with a colormap a level actually uses with them where one exists; otherwise the colormap is a best guess and is marked with \"?\".",
        "",
        "### Cross-game check" if mode != "site" else "## Cross-game check",
        "",
        "Every item in this document was checked against *both* games, not only the game that ships it. MotS reuses a lot of JK data and JK files turn up in MotS, so a file that one game never loads can still be used by the other. For each asset the full text of both games was searched: every single-player, multiplayer, CTF and Kill-the-Fool level, the MotS cutscene levels and S6L1, static.jkl, items.dat, models.dat, sabers.dat, every template parameter (model3d, puppet, soundclass, cog, explode, fleshhit, creatething, material), every cog symbol and string, and every .3do/.key/.pup/.snd/.par/.spr file. Matches were made case-insensitively, with the full file name, the name without extension and plain substrings, and comment-only mentions were kept apart. Engine-loaded names were taken from the OpenJKDF2 source; the original game executables were not available for this survey.",
        "",
        "Files were also compared by content: byte-identical copies under other names, identical 3DO geometry, and 3DOs that share most of their textures with a model the games do use. An asset is called unused only when nothing in either game loads it. Files that are alternate exports of in-game models are labelled as such. The per-asset results are in "
        + (xcheck if mode == "site" else P("cross_game_verification.csv", mode))
        + f", and {app_f_link} lists what this check changed.",
        "",
        "### Ratings" if mode != "site" else "## Ratings",
        "",
        'Each finding was checked against public community sources. **Known**: already documented. **Partly known**: some of it is documented, the rest (usually the file evidence) was not found. **Likely new**: no earlier source was found. "Likely new" is not a claim that nobody has seen it before; corrections are welcome.',
        "",
        "### Credits" if mode != "site" else "## Credits",
        "",
        "KnightCop's \"Road to Barons Hed - Cut Mission Information\" is the reference for the cut speeder-bike level and the bike assets. Other sources: The Cutting Room Floor, the Massassi Temple, r/jediknight, The Sounds Resource and the OpenJKDF2 project (engine file names and conventions). Full list in "
        + app_e_link
        + ".",
        "",
        "### Locating files" if mode != "site" else "## Locating files",
        "",
        "Paths are given as *game - archive - internal path*. Archive paths are relative to the game's install folder. Internal names in GOB/GOO archives are case-insensitive and are shown in lower case. Any GOB/GOO extractor will open them (see "
        + app_d_link
        + ").",
        "",
    ]
    return lines


def appendix_a(mode: str) -> list[str]:
    lines = [
        P(
            "The full lists are in jk_unreferenced_assets.csv and mots_unreferenced_assets.csv (game, name, type, status, archive, internal path, referenced_by, dev_source; the MotS list also flags files that are byte-identical to, or share a name with, a JK file). Status \"unreferenced\" means no file mentions the asset; \"ref_only_by_unused\" means only another unused file points to it. Counts by file type:",
            mode,
        ),
        "",
    ]
    lines += counts_tables(mode)
    app_g = "appendix-g-changelog.md" if mode == "site" else "Appendix G"
    if mode == "site":
        ai_csv = f"[kc_feedback_ai_difficulty_files.csv]({BLOB}/kc_feedback_ai_difficulty_files.csv) ([download]({RAW}/kc_feedback_ai_difficulty_files.csv))"
        more = (
            f"Other tables: [comments_all.csv]({BLOB}/comments_all.csv) ([download]({RAW}/comments_all.csv)) and "
            f"[comments_flagged.csv]({BLOB}/comments_flagged.csv) ([download]({RAW}/comments_flagged.csv)) (every extracted comment, and the flagged ones with cross-game checks), "
            f"[comment_findings.csv]({BLOB}/comment_findings.csv) ([download]({RAW}/comment_findings.csv)) (evidence for the \"Hints in comments\" section), "
            f"[missing_references.csv]({BLOB}/missing_references.csv) ([download]({RAW}/missing_references.csv)) (names that are referenced but not shipped), "
            f"[3do_dev_source_paths.csv]({BLOB}/3do_dev_source_paths.csv) ([download]({RAW}/3do_dev_source_paths.csv)) (the source path and exporter version of every 3DO), "
            f"[jkl_headers.csv]({BLOB}/jkl_headers.csv) ([download]({RAW}/jkl_headers.csv)) (dev path and save date of every level) and "
            f"[unused_voice_transcripts_auto.txt]({BLOB}/unused_voice_transcripts_auto.txt) ([download]({RAW}/unused_voice_transcripts_auto.txt))."
        )
        ai_note = (
            "The .ai0 and .ai2 files are difficulty variants of .ai files, and they are loaded: the engine first opens the .ai name plus the difficulty digit (0 = Easy, 2 = Hard; Medium has no .ai1 file and falls back to the .ai). An earlier version of this document missed this rule; the 179 difficulty variants of used .ai files are now counted as used and removed from these lists (see "
            f"[Appendix G]({app_g}) and {ai_csv}). Most MotS entries are textures, and 176 of them are byte-identical copies of JK files carried over into MotS."
        )
    else:
        ai_note = P(
            "The .ai0 and .ai2 files are difficulty variants of .ai files, and they are loaded: the engine first opens the .ai name plus the difficulty digit (0 = Easy, 2 = Hard; Medium has no .ai1 file and falls back to the .ai). An earlier version of this document missed this rule; the 179 difficulty variants of used .ai files are now counted as used and removed from these lists (see Appendix G and kc_feedback_ai_difficulty_files.csv). Most MotS entries are textures, and 176 of them are byte-identical copies of JK files carried over into MotS.",
            mode,
        )
        more = P(
            "Other tables: comments_all.csv and comments_flagged.csv (every extracted comment, and the flagged ones with cross-game checks), comment_findings.csv (evidence for the \"Hints in comments\" section), missing_references.csv (names that are referenced but not shipped), 3do_dev_source_paths.csv (the source path and exporter version of every 3DO), jkl_headers.csv (dev path and save date of every level) and unused_voice_transcripts_auto.txt.",
            mode,
        )
    lines += [ai_note, "", more, ""]
    if mode == "site":
        lines += [
            "The [Data Files](data-files.md) page lists each of these tables with a short description, a row count, and view or download links.",
            "",
        ]
    return lines


def appendix_b(mode: str) -> list[str]:
    cap = "Unused textures (MotS JKMRES.GOO and JK Res2.gob). Index: unused_textures_sheet_index.csv."
    lines = [
        "First cell of a selection of unused textures. Blue colormap labels are the colormap of a level that uses a sibling or same-prefix texture; red labels with \"?\" are best guesses. bloody.mat and 00ramp3.mat have no image cells and are not shown. Every texture on the sheet was checked against both games; three that turned out to be used (13wcanw7, kbface, 09sky01) were removed.",
        "",
    ]
    lines += render_figure(img_path("unused_textures_sheet", mode), cap, mode)
    return lines


def appendix_c(mode: str) -> list[str]:
    lines = []
    for x in CAVEATS:
        lines.append(f"- {P(x, mode)}")
    lines.append("")
    return lines


def appendix_d(mode: str) -> list[str]:
    return [
        'GOB (JK) and GOO (MotS) files are the same container format: a "GOB " header, a directory offset, then a list of entries (offset, length, 128-byte name). Any GOB/GOO extractor (for example ConMan, JKEdit/JED tools or a small script) will unpack them. The MotS cutscene levels and S6L1 are inside ordinary zip files in Resource\\VIDEO: unzip CUTSCENES.ZIP to get cutscenes.goo and UNSUPPORTED.ZIP to get the S6L1 level files.',
        "",
        "3DO, KEY, JKL, COG, AI and episode.jk files are plain text and open in any text editor. The header comments quoted in this document are the first lines of each file.",
        "",
        "MAT textures need a colormap (.cmp, in misc\\cmp) to view 8-bit images. Most MAT viewers let you pick the colormap; use the one named in this document.",
        "",
        "Work on copies. Do not modify the original archives in the game folder.",
        "",
    ]


def appendix_e(mode: str, credits: list[str]) -> list[str]:
    lines = []
    for x in credits:
        lines.append(f"- {P(x, mode)}")
    lines.append("")
    return lines


def appendix_f(mode: str) -> list[str]:
    lines = [
        "Items from the first version of this document that the check against both games reclassified. Everything else that is described as unused was confirmed unused in both games.",
        "",
        "| Asset | Ships in | Evidence | Change |",
        "|---|---|---|---|",
    ]
    for a, s, e, c in CROSS_GAME_CHANGES:
        lines.append(f"| {md_cell(a, mode)} | {md_cell(s, mode)} | {md_cell(e, mode)} | {md_cell(c, mode)} |")
    lines.append("")
    return lines


def appendix_g(mode: str) -> list[str]:
    h3 = "###" if mode == "github" else "##"
    h4 = "####" if mode == "github" else "###"
    lines = [
        f"{h3} v1.0",
        "",
        "First published version (57 pages): findings A-G, the cross-game check (Appendix F) and the comment pass.",
        "",
        f"{h3} v2.0: Rev after KnightCop feedback",
        "",
        "KnightCop reviewed the first published version and wrote that some models and textures looked like ones used in multiplayer maps, that a sound looked like one JK uses, and that the little tractor model and the many unused Morgan Katarn home textures were missing. Thank you, KnightCop. Every point was checked again against both games, including every multiplayer, CTF and Kill-the-Fool map.",
        "",
        f"{h4} What changed",
        "",
        "| Asset | Ships in | Evidence | Change |",
        "|---|---|---|---|",
    ]
    for a, s, e, c in V20_CHANGES:
        lines.append(f"| {md_cell(a, mode)} | {md_cell(s, mode)} | {md_cell(e, mode)} | {md_cell(c, mode)} |")
    lines += ["", f"{h4} What was checked and did not change", ""]
    for x in UNCHANGED:
        lines.append(f"- {P(x, mode)}")
    lines += [
        "",
        f"{h3} v2.1: community theories from Shimstock (s5 E-Web gunner, ligt prod projectile)",
        "",
        "Added to finding 34 (s5.3do) and to the ligt.3do part of the \"Internal project name and personal folders\" finding, both labelled Community theory (Shimstock) and Speculative, with the file evidence for and against. Also added: the s5.3do source path (MotS JkMiss folder) and an eweb.3do render. Thank you, Shimstock.",
        "",
        'The wording for community theories that are not yet confirmed by a file is "Community theory (Name) — Speculative, not yet linked by any file" (or "Speculative" where a shorter label is used).',
        "",
        f"{h3} v2.2: unused voices, an unfinished saber throw, Warning Sense, and other leftovers",
        "",
        "Thank you to Shimstock for a set of notes that led to most of the additions and corrections below, and to Cogking for confirming that the Jedi Knight developers were experimenting with a saber throw.",
        "",
        "What changed:",
        "",
        "- Finding 2: the leftover level-05 Crow and TIE bomber animations are a paired sky dogfight; the transport animation is a path through the level. The written frame rates do not match, so the files as shipped would not finish together. Credited to Shimstock.",
        "- Finding 7: dropped \"snowy\" as a fact about 16world. The pale colors came from a guessed MotS colormap; a complete JK colormap shows a dark valley and a tower, not snow. The colors are uncertain.",
        "- Finding 12: the voiceuu folder has 46 files, not 26. That includes 28 civilian, rebel and announcement clips (previously counted as 26), 15 Ka'Pa the Hutt lines in Huttese, and 3 Abron Mar lines from leftover in-engine cutscenes that the shipped episode never plays. Credited to Shimstock for the folder, and to a review of this catalogue for identifying Ka'Pa.",
        "- Finding 20: added rep0.3do, the repeater's earlier unused projectile. Credited to Shimstock.",
        "- Finding 23: added Shimstock's speculative notes on kystab (possibly the Tusken prod melee) and kyrepel0 (a dropped radial push; Boc uses +force_repel with his own animation). Corrected the earlier claim that sab0.3do is used in both games. Short notes on unused +force_lightning2/3/4 templates and leftover MotS +force_repel templates.",
        "- Finding 24: no evidence for a Kaerobani boss fight. His unused body (kb.3do) stands. The leftover S4L1 opening-cutscene script plays kb74107–kb74109, but those files do not ship in JKMRES, voiceuu or JKMsndLO.goo, so the lines were likely cut from the finished video (not yet compared line by line). Credited to Shimstock for raising the lines.",
        "- Finding 44 (new): an unfinished JK saber throw (sab0.3do with a solid green blade, sab0.key, and an un-fired +force_saber template). MotS later shipped a working version. Credited to Cogking, and to a review of this catalogue for the model. Appendix F's earlier \"used in both games\" row for sab0.3do is superseded by this correction.",
        "- Finding 45 (new): MotS force_warning.cog, an unused \"Warning Sense\" Force power written for bin 38, which shipped as Force Push. An in-game test in the original executable confirmed the flags are set, with no visible effect. No other cog reads those flags.",
        "- Intro: a short paragraph on how MotS cutscenes were filmed in the game engine and recorded to .san videos, and that CUTSCENES.ZIP holds earlier JKL setups. Credited to Shimstock.",
        "- Housekeeping: the flagged-comment count is 6,688 (the previous text said 6,680). The tractor render uses colormap 20val.cmp, a best guess, instead of the darker 03house.cmp used in the v2.1 PDF.",
        "",
    ]
    return lines


def walk_findings(sections):
    n = 0
    out = []
    for secx in sections:
        items = []
        for f in secx[1]:
            n += 1
            items.append((n, f))
        out.append((letter_of(secx[0]), secx[0], secx[2] if len(secx) > 2 else [], items))
    return out, n


def findings_toc(walked) -> list[str]:
    lines = ["## Contents", ""]
    lines.append("- [About this document](#about-this-document)")
    for letter, title, _intro, items in walked:
        lines.append(f"- [{title}](#section-{letter.lower()})")
        for n, f in items:
            t = P(f["t"], "github")
            lines.append(f"  - [{n}. {t}](#finding-{n})")
    for letter, title in [
        ("A", "Appendix A. Unreferenced asset lists"),
        ("B", "Appendix B. Unused texture contact sheet"),
        ("C", "Appendix C. Caveats"),
        ("D", "Appendix D. How to extract these files yourself"),
        ("E", "Appendix E. Sources and credits"),
        ("F", "Appendix F. What the cross-game check changed"),
        ("G", "Appendix G. Change log"),
    ]:
        lines.append(f"- [{title}](#appendix-{letter.lower()})")
    lines.append("")
    return lines


def write_findings_md(sections, credits, walked) -> Path:
    lines = [
        "# Jedi Knight & Mysteries of the Sith: Unused, orphaned and leftover content in the shipped game data",
        "",
        f"**Version {VERSION.lstrip('v')}** — {VERSION_MONTH}",
        "",
        ISSUE_NOTE,
        "",
        "Research notes with file locations, quoted evidence, renders and source ratings. Game data: *Star Wars Jedi Knight: Dark Forces II* and *Mysteries of the Sith*, Steam releases.",
        "",
        "![ks.3do, the unused Kyle-on-speeder-bike model from MotS JKMRES.GOO, posed with its own ksgo.key animation. Grey parts use textures that never shipped.](renders/ks.png)",
        "",
        "*ks.3do, the unused Kyle-on-speeder-bike model from MotS JKMRES.GOO, posed with its own ksgo.key animation. Grey parts use textures that never shipped.*",
        "",
        "A print-ready PDF and a zip of this version will be added on the [Releases](" + REPO + "/releases) page when v2.2 is published. The last published files are still [v2.1](" + REPO + "/releases/tag/v2.1).",
        "",
    ]
    lines += findings_toc(walked)
    lines += ["<a id=\"about-this-document\"></a>", "## About this document", ""]
    lines += intro_body("github")
    for letter, title, intro, items in walked:
        lines += [f'<a id="section-{letter.lower()}"></a>', f"## {title}", ""]
        for x in intro:
            lines += [P(x, "github"), ""]
        for n, f in items:
            lines += render_finding(n, f, "github")
    appendices = [
        ("A", "Appendix A. Unreferenced asset lists", appendix_a("github")),
        ("B", "Appendix B. Unused texture contact sheet", appendix_b("github")),
        ("C", "Appendix C. Caveats", appendix_c("github")),
        ("D", "Appendix D. How to extract these files yourself", appendix_d("github")),
        ("E", "Appendix E. Sources and credits", appendix_e("github", credits)),
        ("F", "Appendix F. What the cross-game check changed", appendix_f("github")),
        ("G", "Appendix G. Change log", appendix_g("github")),
    ]
    for letter, title, body in appendices:
        lines += [f'<a id="appendix-{letter.lower()}"></a>', f"## {title}", ""]
        lines += body
    lines += ["---", "", ISSUE_NOTE, ""]
    path = ROOT / "FINDINGS.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path



def _fmt_count(n: int) -> str:
    return f"{n:,}"


def _fmt_size(n: int) -> str:
    mb = n / (1024 * 1024)
    if mb >= 10:
        return f"{mb:.0f} MB"
    if mb >= 1:
        # 18.7 MB reads as "about 19 MB" in the notes; keep one decimal otherwise
        if 18.5 <= mb < 19.5:
            return "19 MB"
        return f"{mb:.1f} MB"
    return f"{n / 1024:.0f} KB"


def write_data_files_page() -> list[str]:
    """Build the Data Files page from the reference files on disk."""
    d = csv_dir()
    blob = BLOB
    raw = RAW

    def stats(name: str):
        path = d / name
        size = path.stat().st_size
        if name.endswith(".csv"):
            with path.open(encoding="utf-8", errors="replace", newline="") as f:
                r = csv.reader(f)
                header = next(r, [])
                rows = sum(1 for _ in r)
            return rows, "rows", size, header
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = [ln for ln in text.splitlines() if ln.strip()]
        return len(lines), "lines", size, []

    # Semantic "supports" links for the website. Keep these in PDF/finding order.
    catalog = [
        {
            "name": "jk_unreferenced_assets.csv",
            "desc": "Every Jedi Knight file the reference graph never reached, with the archive path, status (unreferenced or only pointed to by another unused file), and how it checked out against MotS.",
            "supports": "[Appendix A](appendix-a-unreferenced-lists.md); the unused JK lists behind the findings in sections A–F",
        },
        {
            "name": "mots_unreferenced_assets.csv",
            "desc": "The same kind of list for Mysteries of the Sith, plus columns that flag a file with the same name as, or identical bytes to, a JK file.",
            "supports": "[Appendix A](appendix-a-unreferenced-lists.md); [Section A](a-barons-hed.md) (JK-era leftovers that only MotS ships); [Section H](h-community-feedback.md) (the tractor and Katarn-home textures were on this list)",
        },
        {
            "name": "cross_game_verification.csv",
            "desc": "The per-asset check of items named in this catalogue against both games: where each file ships, what references it in JK and in MotS, and the verdict.",
            "supports": "[How to read this catalogue](index.md#cross-game-check); [Appendix F](appendix-f-cross-game-check.md); used throughout the findings",
        },
        {
            "name": "missing_references.csv",
            "desc": "Names that a shipped file points to, but that are not in any archive that was read (the file is missing, or, for many MotS sounds, the MotS sound archive was not available).",
            "supports": "[Finding 18](d-unused-scripts.md#finding-18); [Appendix A](appendix-a-unreferenced-lists.md)",
        },
        {
            "name": "3do_dev_source_paths.csv",
            "desc": "The source path and exporter version from the header of every 3DO in both games (used and unused), which is how cut-level folders such as 05stuff and 13pipes were grouped.",
            "supports": "[Finding 26](f-headers-dates.md#finding-26); [Section A](a-barons-hed.md); [Appendix A](appendix-a-unreferenced-lists.md)",
        },
        {
            "name": "jkl_headers.csv",
            "desc": "The development path and \"Created\" stamp from the header of every level, including multiplayer, cutscene and S6L1 maps.",
            "supports": "[Finding 25](f-headers-dates.md#finding-25); [Appendix A](appendix-a-unreferenced-lists.md)",
        },
        {
            "name": "katarn_home_mats.csv",
            "desc": "Every texture with a level 3 or 4 prefix (03* and 04*) in both games: where it ships, whether either game uses it, and what references it.",
            "supports": "[Finding 43](h-community-feedback.md#finding-43); [Appendix G](appendix-g-changelog.md)",
        },
        {
            "name": "kc_feedback_ai_difficulty_files.csv",
            "desc": "The Easy (.ai0) and Hard (.ai2) difficulty variants of used AI files that were first listed as unused, then moved to used after the engine load rule was applied.",
            "supports": "[Appendix A](appendix-a-unreferenced-lists.md); [Appendix G](appendix-g-changelog.md) (the v2.0 revision)",
        },
        {
            "name": "comments_all.csv",
            "desc": "Every comment line extracted from both games (cogs, levels, templates, headers and the other text data files), with flags and any names that were cross-checked.",
            "supports": "[Section G](g-hints-in-comments.md); [Appendix A](appendix-a-unreferenced-lists.md)",
            "note": "This file is about 19 MB and may be slow to open as a table in the browser. Downloading it is the better option.",
        },
        {
            "name": "comments_flagged.csv",
            "desc": "The subset of extracted comments that looked interesting (old names, dates, commented-out code, and similar), with the cross-game checks on any file names they mention.",
            "supports": "[Section G](g-hints-in-comments.md); [Appendix A](appendix-a-unreferenced-lists.md)",
        },
        {
            "name": "comment_findings.csv",
            "desc": "The quoted comment lines used as evidence in the \"Hints in comments\" findings, with the classification and reasoning for each one.",
            "supports": "[Section G](g-hints-in-comments.md) (findings 29–41); [Appendix A](appendix-a-unreferenced-lists.md)",
        },
        {
            "name": "unused_textures_sheet_index.csv",
            "desc": "An index of the unused-texture contact sheet: each texture, the colormap used to draw it, whether that colormap is a known match or a best guess, and its size.",
            "supports": "[Appendix B](appendix-b-texture-sheet.md); [Finding 3](a-barons-hed.md#finding-3)",
        },
        {
            "name": "unused_voice_transcripts_auto.txt",
            "desc": "Automatic transcripts of the unused voice clips (approximate wording; check the recordings by ear).",
            "supports": "[Section C](c-unused-dialogue.md) (findings 9–12); [Appendix A](appendix-a-unreferenced-lists.md)",
        },
    ]

    lines = [
        "# Data Files",
        "",
        "These are the raw data behind the findings, for anyone who wants to verify a claim or dig deeper. Most readers can skip this page and stay with the write-ups and renders.",
        "",
        "## Why these files are useful",
        "",
        "If you like to check the work yourself, or go hunting for things the write-ups have not covered yet, the CSVs are the place to do it. They open in Excel, Google Sheets or LibreOffice, and you can search, sort and filter them like any spreadsheet.",
        "",
        "- **Verify any claim yourself.** Every unused file named in the catalogue is in the unreferenced lists, with the archive path and how it was checked against both games. If a finding says a model never loads, you can look up that name and see the result.",
        "- **Search and filter.** You can, for example, list every unused file that ships in one archive, or every 3DO whose source path contains a cut-level folder. Try opening `jk_unreferenced_assets.csv` and filtering the `ext` column to `wav` to see the unused JK sounds in one list. Or open `3do_dev_source_paths.csv` and search for `05stuff` to see the models exported from the cut \"Road to Baron's Hed\" folder.",
        "- **Spot leads that are not written up yet.** The unreferenced lists are longer than the findings. An odd 3DO comment, or a model with a surprising development path, may be a new finding.",
        "- **Cross-check JK against MotS.** MotS reuses a lot of JK data. The cross-game tables show whether a file is unused in both games, or a leftover copy of something the other game actually uses.",
        "- **Build on it for mods and restorations.** If you are putting a cut weapon or texture back into a level, the lists give you the exact file names, which archive they live in, and which textures or keys belong with them.",
        "",
        "If you want everything in one go, a zip of the whole folder (PDF, these data files, and the renders) will be added on the Releases page when v2.2 is published. The last published zip is still in the [v2.1 release](" + REPO + "/releases/tag/v2.1).",
        "",
        "## The files",
        "",
        "| File | What's in it | Supports | Links |",
        "|---|---|---|---|",
    ]

    for item in catalog:
        name = item["name"]
        n, unit, size, _header = stats(name)
        size_s = _fmt_size(size)
        count_s = f"{_fmt_count(n)} {unit}"
        desc = item["desc"]
        extra = ""
        if item.get("note"):
            extra = f" {item['note']}"
        what = f"{count_s} ({size_s}). {desc}{extra}"
        view = f"[View on GitHub]({blob}/{name})"
        dl = f"[Download]({raw}/{name})"
        # escape pipes in cells
        what = what.replace("|", "\\|")
        supports = item["supports"].replace("|", "\\|")
        lines.append(f"| [`{name}`]({blob}/{name}) | {what} | {supports} | {view} · {dl} |")

    lines += [
        "",
        "`comments_all.csv` is about 19 MB. GitHub can show it as a table, but it may take a while to load; downloading it is recommended.",
        "",
    ]
    return lines


def write_docs(sections, credits, walked) -> None:
    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)
    renders = docs / "renders"
    if renders.is_symlink() or renders.exists():
        if renders.is_symlink():
            pass
        else:
            raise SystemExit(f"{renders} exists and is not a symlink")
    else:
        os.symlink("../renders", renders, target_is_directory=True)

    # Home
    home = [
        "---",
        "title: How to read this catalogue",
        "---",
        "",
        "# Unused content from Jedi Knight and Mysteries of the Sith",
        "",
        f"**Version {VERSION.lstrip('v')}** — {VERSION_MONTH}",
        "",
        f"Have a new finding, a correction, or a file this catalogue should look at again? Please [open an issue]({ISSUE}) and tell us about it. The last published PDF is still [v2.1]({REPO}/releases/download/v2.1/JK_MotS_Unused_Content_Findings_v2.1.pdf); the v2.2 PDF and zip will be added on the Releases page when this version is published.",
        "",
        "This site is the web edition of the catalogue of unused, orphaned and leftover files in the retail *Star Wars Jedi Knight: Dark Forces II* (JK) and *Mysteries of the Sith* (MotS) data. Use the sidebar to jump to a section, or the table of contents on each page to jump to a finding. Every finding has a stable link, for example [Finding 34](g-hints-in-comments.md#finding-34).",
        "",
    ]
    home += render_figure(
        "renders/ks.png",
        "ks.3do, the unused Kyle-on-speeder-bike model from MotS JKMRES.GOO, posed with its own ksgo.key animation. Grey parts use textures that never shipped.",
        "site",
        skip_lightbox=True,
    )
    home += [
        "## About this document",
        "",
    ]
    home += intro_body("site")
    home += [
        "## Browse the findings",
        "",
        'A small chip before each finding title shows which game it is about: an orange <span class="game-icon game-icon--jk" title="Jedi Knight">JK</span> for Jedi Knight, a lavender <span class="game-icon game-icon--mots" title="Mysteries of the Sith">MotS</span> for Mysteries of the Sith, and both when the finding covers both games. Hover a chip for the full name. The location table under each finding still has the exact archives.',
        "",
        'Each finding also has a rating: a small "Rating:" label and a colored pill with an icon. Some findings add a second pill for a further classification, such as Confirmed cut or Likely rename.',
        "",
        '<p class="legend-pills">'
        + rating_pill_html("Known", "known", "check")
        + rating_pill_html("Partly known", "partly", "half")
        + rating_pill_html("Likely new", "new", "star")
        + rating_pill_html("Speculative", "speculative", "help")
        + "</p>",
        "",
    ]
    file_by_letter = dict(SECTION_FILES)
    for letter, title, _intro, items in walked:
        fn = file_by_letter[letter]
        first, last = items[0][0], items[-1][0]
        home.append(f"- [{title}]({fn}) — findings {first}–{last}")
    home += [
        "",
        "A single-file copy of the same text is also on GitHub as [FINDINGS.md](" + REPO + "/blob/main/FINDINGS.md), and each numbered release includes a print-ready PDF.",
        "",
        "The [Data Files](data-files.md) page lists the CSVs and the voice-transcript file behind this catalogue, with a short description of each and links to view or download them.",
        "",
    ]
    (docs / "index.md").write_text("\n".join(home), encoding="utf-8")

    for letter, title, intro, items in walked:
        fn = file_by_letter[letter]
        page = [f"# {title}", ""]
        for x in intro:
            page += [P(x, "site"), ""]
        for n, f in items:
            page += render_finding(n, f, "site")
        (docs / fn).write_text("\n".join(page), encoding="utf-8")

    apps = [
        ("A", "Appendix A. Unreferenced asset lists", appendix_a("site")),
        ("B", "Appendix B. Unused texture contact sheet", appendix_b("site")),
        ("C", "Appendix C. Caveats", appendix_c("site")),
        ("D", "Appendix D. How to extract these files yourself", appendix_d("site")),
        ("E", "Appendix E. Sources and credits", appendix_e("site", credits)),
        ("F", "Appendix F. What the cross-game check changed", appendix_f("site")),
        ("G", "Appendix G. Change log", appendix_g("site")),
    ]
    for letter, title, body in apps:
        page = [f"# {title}", ""] + body
        (docs / APPENDIX_FILES[letter]).write_text("\n".join(page), encoding="utf-8")

    (docs / "data-files.md").write_text("\n".join(write_data_files_page()), encoding="utf-8")


def main() -> None:
    sections, credits = load_sources()
    walked, n = walk_findings(sections)
    findings_path = write_findings_md(sections, credits, walked)
    write_docs(sections, credits, walked)
    print(f"Wrote {findings_path.relative_to(ROOT)} and docs/ ({n} findings)")


if __name__ == "__main__":
    main()
