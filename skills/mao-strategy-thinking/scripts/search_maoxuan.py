#!/usr/bin/env python3
"""Search local Mao Zedong Selected Works EPUB XHTML files.

Provide the source path with --epub or the MAOXUAN_EPUB_PATH environment
variable. The script expects an unpacked EPUB directory containing OEBPS/Text.
It uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


DEFAULT_EPUB_ENV = "MAOXUAN_EPUB_PATH"


def strip_tags(raw: str) -> str:
    raw = re.sub(r"<br\s*/?>", "\n", raw, flags=re.I)
    raw = re.sub(r"<[^>]+>", "", raw)
    raw = html.unescape(raw)
    raw = raw.replace("\u3000", " ")
    raw = re.sub(r"[ \t]+", " ", raw)
    return raw


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def build_title_map(epub_dir: Path) -> dict[str, str]:
    toc = epub_dir / "OEBPS" / "toc.ncx"
    title_map: dict[str, str] = {}
    if not toc.exists():
        return title_map

    root = ET.parse(toc).getroot()
    for nav_point in root.iter():
        if local_name(nav_point.tag) != "navPoint":
            continue
        label = None
        src = None
        for child in nav_point.iter():
            name = local_name(child.tag)
            if name == "text" and child.text and label is None:
                label = child.text.strip()
            elif name == "content":
                src = child.attrib.get("src")
        if label and src:
            title_map[Path(src).name] = label
    return title_map


def iter_text_files(epub_dir: Path) -> list[Path]:
    text_dir = epub_dir / "OEBPS" / "Text"
    if not text_dir.exists():
        raise FileNotFoundError(f"Text directory not found: {text_dir}")
    return sorted(text_dir.glob("*.xhtml"))


def title_from_file(path: Path, title_map: dict[str, str]) -> str:
    if path.name in title_map:
        return title_map[path.name]
    text = path.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"<title>(.*?)</title>", text, flags=re.S | re.I)
    if match:
        return strip_tags(match.group(1)).strip()
    return path.stem


def paragraphs(path: Path) -> list[tuple[int, str]]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    items: list[tuple[int, str]] = []
    buffer: list[str] = []
    start = 1
    in_para = False
    for idx, line in enumerate(lines, start=1):
        if re.search(r"<(p|h[1-6])\b", line):
            in_para = True
            start = idx
            buffer = [line]
            if re.search(r"</(p|h[1-6])>", line):
                text = strip_tags(" ".join(buffer)).strip()
                if text:
                    items.append((start, text))
                in_para = False
        elif in_para:
            buffer.append(line)
            if re.search(r"</(p|h[1-6])>", line):
                text = strip_tags(" ".join(buffer)).strip()
                if text:
                    items.append((start, text))
                in_para = False
    return items


def normalize(text: str) -> str:
    return text.lower()


def snippet(text: str, terms: list[str], width: int = 110) -> str:
    lowered = normalize(text)
    positions = [lowered.find(normalize(term)) for term in terms if normalize(term) in lowered]
    pos = min(positions) if positions else 0
    start = max(0, pos - width // 3)
    end = min(len(text), start + width)
    out = text[start:end]
    if start > 0:
        out = "..." + out
    if end < len(text):
        out += "..."
    return out


def list_articles(epub_dir: Path) -> int:
    title_map = build_title_map(epub_dir)
    for path in iter_text_files(epub_dir):
        title = title_from_file(path, title_map)
        if title:
            print(f"{path.name}\t{title}")
    return 0


def search(epub_dir: Path, terms: list[str], article: str | None, max_results: int) -> int:
    title_map = build_title_map(epub_dir)
    files = iter_text_files(epub_dir)
    found = 0
    article_norm = normalize(article) if article else None
    term_norms = [normalize(term) for term in terms]

    for path in files:
        title = title_from_file(path, title_map)
        if article_norm and article_norm not in normalize(title) and article_norm not in normalize(path.name):
            continue
        for line_no, para in paragraphs(path):
            haystack = normalize(para)
            if all(term in haystack for term in term_norms):
                print(f"[{found + 1}] {title} ({path.name}:{line_no})")
                print(snippet(para, terms))
                print()
                found += 1
                if found >= max_results:
                    return 0
    if found == 0:
        print("No matches found.", file=sys.stderr)
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", nargs="*", help="Search terms. All terms must match.")
    parser.add_argument(
        "--epub",
        default=os.environ.get(DEFAULT_EPUB_ENV),
        help=f"Path to unpacked EPUB directory. Defaults to ${DEFAULT_EPUB_ENV}.",
    )
    parser.add_argument("--article", help="Restrict search to an article title or file name.")
    parser.add_argument("--max", type=int, default=10, help="Maximum result count.")
    parser.add_argument("--list", action="store_true", help="List article files and titles.")
    args = parser.parse_args()

    if not args.epub:
        print(
            f"Provide --epub or set ${DEFAULT_EPUB_ENV} to your local unpacked EPUB directory.",
            file=sys.stderr,
        )
        return 2
    epub_dir = Path(args.epub).expanduser()
    if not epub_dir.exists():
        print(f"EPUB path not found: {epub_dir}", file=sys.stderr)
        return 2
    if args.list:
        return list_articles(epub_dir)
    if not args.terms:
        parser.error("provide at least one search term or use --list")
    return search(epub_dir, args.terms, args.article, args.max)


if __name__ == "__main__":
    raise SystemExit(main())
