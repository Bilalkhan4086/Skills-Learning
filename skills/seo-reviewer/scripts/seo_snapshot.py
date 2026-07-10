#!/usr/bin/env python3
"""Create a small SEO evidence snapshot from a URL or HTML file.

This helper intentionally uses only Python standard-library modules so the
seo-reviewer skill remains portable. It is not a crawler or full SEO auditor;
it extracts common document-level signals that can support a human-readable
audit report.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


class SeoHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title_parts: list[str] = []
        self.in_title = False
        self.current_heading: str | None = None
        self.heading_parts: list[str] = []
        self.headings: list[dict[str, str]] = []
        self.meta: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.images: list[dict[str, str]] = []
        self.anchors: list[dict[str, str]] = []
        self.json_ld_count = 0
        self.lang = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {key.lower(): value or "" for key, value in attrs}

        if tag == "html":
            self.lang = attr.get("lang", "")
        elif tag == "title":
            self.in_title = True
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.current_heading = tag
            self.heading_parts = []
        elif tag == "meta":
            self.meta.append(attr)
        elif tag == "link":
            self.links.append(attr)
        elif tag == "img":
            self.images.append(
                {
                    "src": attr.get("src", ""),
                    "alt": attr.get("alt", ""),
                    "loading": attr.get("loading", ""),
                    "width": attr.get("width", ""),
                    "height": attr.get("height", ""),
                }
            )
        elif tag == "a":
            self.anchors.append({"href": attr.get("href", ""), "text": ""})
        elif tag == "script" and attr.get("type", "").lower() == "application/ld+json":
            self.json_ld_count += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        elif self.current_heading == tag:
            text = " ".join("".join(self.heading_parts).split())
            self.headings.append({"level": tag, "text": text})
            self.current_heading = None
            self.heading_parts = []

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self.current_heading:
            self.heading_parts.append(data)
        if self.anchors:
            current = self.anchors[-1]
            current["text"] = " ".join((current["text"] + " " + data).split())

    def snapshot(self) -> dict[str, Any]:
        metas_by_name = {
            item.get("name", "").lower(): item.get("content", "")
            for item in self.meta
            if item.get("name")
        }
        metas_by_property = {
            item.get("property", "").lower(): item.get("content", "")
            for item in self.meta
            if item.get("property")
        }
        links_by_rel: dict[str, list[str]] = {}
        for item in self.links:
            rel = item.get("rel", "").lower()
            href = item.get("href", "")
            if rel and href:
                links_by_rel.setdefault(rel, []).append(href)

        return {
            "html_lang": self.lang,
            "title": " ".join("".join(self.title_parts).split()),
            "meta_description": metas_by_name.get("description", ""),
            "robots_meta": metas_by_name.get("robots", ""),
            "viewport": metas_by_name.get("viewport", ""),
            "canonical": links_by_rel.get("canonical", []),
            "open_graph": {
                key: value
                for key, value in metas_by_property.items()
                if key.startswith("og:")
            },
            "twitter_cards": {
                key: value
                for key, value in metas_by_name.items()
                if key.startswith("twitter:")
            },
            "json_ld_count": self.json_ld_count,
            "headings": self.headings,
            "h1_count": sum(1 for item in self.headings if item["level"] == "h1"),
            "images_total": len(self.images),
            "images_missing_alt": sum(1 for item in self.images if not item["alt"]),
            "images_missing_dimensions": sum(
                1 for item in self.images if not item["width"] or not item["height"]
            ),
            "links_total": len(self.anchors),
            "links_without_href": sum(1 for item in self.anchors if not item["href"]),
            "links_without_text": sum(1 for item in self.anchors if not item["text"]),
        }


def read_target(target: str) -> tuple[str, dict[str, Any]]:
    if target.startswith(("http://", "https://")):
        request = urllib.request.Request(
            target,
            headers={"User-Agent": "seo-reviewer-snapshot/1.0"},
        )
        with urllib.request.urlopen(request, timeout=20) as response:
            raw = response.read()
            charset = response.headers.get_content_charset() or "utf-8"
            metadata = {
                "source": target,
                "status": response.status,
                "final_url": response.geturl(),
                "content_type": response.headers.get("content-type", ""),
            }
            return raw.decode(charset, errors="replace"), metadata

    path = Path(target)
    metadata = {"source": str(path), "status": None, "final_url": None, "content_type": "file"}
    return path.read_text(encoding="utf-8", errors="replace"), metadata


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract a basic SEO snapshot from a URL or HTML file.")
    parser.add_argument("target", help="URL or local HTML file path")
    args = parser.parse_args()

    try:
        html, metadata = read_target(args.target)
    except (OSError, urllib.error.URLError, TimeoutError) as exc:
        print(json.dumps({"error": str(exc), "source": args.target}, indent=2), file=sys.stderr)
        return 1

    html_parser = SeoHTMLParser()
    html_parser.feed(html)
    result = {"metadata": metadata, "snapshot": html_parser.snapshot()}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
