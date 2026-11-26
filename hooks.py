"""MkDocs hook: clean TOC chip prefixes and wrap content tables."""
from __future__ import annotations

import re

_CHIP_PREFIX = re.compile(r"^(?:JK(?:\s+MotS)?|MotS)\s+")
_BARE_TABLE = re.compile(r"<table(?![^>]*\bclass=)[^>]*>.*?</table>", re.S)


def _clean_toc(items) -> None:
    for item in items or []:
        if getattr(item, "title", None):
            item.title = _CHIP_PREFIX.sub("", item.title)
        if getattr(item, "children", None):
            _clean_toc(item.children)


def _wrap_tables(html: str) -> str:
    def repl(match: re.Match) -> str:
        block = match.group(0)
        if 'class="md-typeset__table"' in match.string[max(0, match.start()-80):match.start()]:
            return block
        return f'<div class="md-typeset__table">{block}</div>'

    return _BARE_TABLE.sub(repl, html)


def on_page_content(html, page, config, files):
    toc = getattr(page, "toc", None)
    if toc:
        _clean_toc(toc)
    return _wrap_tables(html)
