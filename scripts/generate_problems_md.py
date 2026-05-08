#!/usr/bin/env python3
from __future__ import annotations

import argparse
import dataclasses
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Iterable


LEETCODE_GRAPHQL = "https://leetcode.com/graphql"

try:
    import requests  # type: ignore
except Exception:  # pragma: no cover
    requests = None


@dataclasses.dataclass(frozen=True)
class Problem:
    number: int
    title: str
    slug: str
    solution_path: Path
    difficulty: str | None = None
    tags: list[str] = dataclasses.field(default_factory=list)
    time_complexity: str | None = None
    space_complexity: str | None = None


def _slugify_title(title: str) -> str:
    """
    Best-effort slugification for LeetCode titleSlug.
    Works for most problems (e.g. 'Add Two Numbers' -> 'add-two-numbers', '3Sum' -> '3sum').
    """
    t = title.strip().lower()
    t = t.replace("&", " and ")
    t = re.sub(r"[’'`]", "", t)  # remove apostrophes
    t = re.sub(r"[^a-z0-9]+", "-", t)
    t = re.sub(r"-{2,}", "-", t).strip("-")
    return t


def _parse_problem_dir_name(name: str) -> tuple[int, str] | None:
    # Accept: "1. Two Sum", "2.Add Two Numbers", "15. 3Sum", etc.
    m = re.match(r"^\s*(\d+)\s*[\.\-]?\s*(.+?)\s*$", name)
    if not m:
        return None
    num = int(m.group(1))
    title = m.group(2).strip()
    if not title:
        return None
    return num, title


def _find_single_py_file(folder: Path) -> Path | None:
    py_files = sorted([p for p in folder.iterdir() if p.is_file() and p.suffix == ".py"])
    if not py_files:
        return None
    if len(py_files) == 1:
        return py_files[0]
    # Prefer files that include the number in the filename (your current style: Leetcode_1.py)
    preferred = [p for p in py_files if re.search(r"\d+", p.stem)]
    return preferred[0] if preferred else py_files[0]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _load_cache(cache_path: Path) -> dict[str, Any]:
    if not cache_path.exists():
        return {}
    try:
        return json.loads(cache_path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_cache(cache_path: Path, cache: dict[str, Any]) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _http_post_json(url: str, payload: dict[str, Any], timeout_s: int = 25) -> dict[str, Any]:
    # Prefer requests (bundles certifi; avoids SSL issues on some systems).
    if requests is not None:
        resp = requests.post(
            url,
            json=payload,
            timeout=timeout_s,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "mkdocs-leetcode-generator/1.0",
                "Referer": "https://leetcode.com/",
            },
        )
        resp.raise_for_status()
        return resp.json()

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "mkdocs-leetcode-generator/1.0",
            "Referer": "https://leetcode.com/",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        body = resp.read().decode("utf-8")
        return json.loads(body)


def _fetch_leetcode_metadata(slug: str) -> tuple[str | None, list[str]]:
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        difficulty
        topicTags { name }
      }
    }
    """
    payload = {"query": query, "variables": {"titleSlug": slug}}
    try:
        out = _http_post_json(LEETCODE_GRAPHQL, payload)
    except Exception:
        return None, []
    question = (out.get("data") or {}).get("question") or None
    if not question:
        return None, []
    difficulty = question.get("difficulty")
    tags = [t.get("name") for t in (question.get("topicTags") or []) if isinstance(t, dict) and t.get("name")]
    tags = sorted(set(tags))
    return difficulty, tags


def _difficulty_badge(difficulty: str | None) -> str:
    if not difficulty:
        return '<span class="badge-medium">Unknown</span>'
    d = difficulty.strip().lower()
    if d == "easy":
        return '<span class="badge-easy">Easy</span>'
    if d == "medium":
        return '<span class="badge-medium">Medium</span>'
    if d == "hard":
        return '<span class="badge-hard">Hard</span>'
    return f'<span class="badge-medium">{difficulty}</span>'


def _render_problem_md(p: Problem, prev_slug: str | None, next_slug: str | None) -> str:
    code = _read_text(p.solution_path).rstrip()
    tags_line = ", ".join(p.tags) if p.tags else "—"

    nav_parts: list[str] = []
    if prev_slug:
        nav_parts.append(f'<a class="prev" href="../{prev_slug}/">Anterior</a>')
    else:
        nav_parts.append('<span></span>')
    if next_slug:
        nav_parts.append(f'<a class="next" href="../{next_slug}/">Siguiente</a>')
    else:
        nav_parts.append('<span></span>')

    return (
        f'---\n'
        f'title: "{p.number}. {p.title}"\n'
        f'---\n\n'
        f'<div class="problem-header">\n'
        f'  <div class="problem-number">{p.number}</div>\n'
        f'  <div>\n'
        f'    <div><strong>{p.title}</strong> {_difficulty_badge(p.difficulty)}</div>\n'
        f'    <div><strong>Tags:</strong> {tags_line}</div>\n'
        f'  </div>\n'
        f'</div>\n\n'
        f'## Solución (Python)\n\n'
        f'```python\n{code}\n```\n\n'
        f'<div class="navigation">\n'
        f'  {nav_parts[0]}\n'
        f'  {nav_parts[1]}\n'
        f'</div>\n'
    )


def _render_index_md(problems: list[Problem]) -> str:
    # Simple table (Material styling already in extra.css)
    lines: list[str] = []
    lines.append("# Problemas")
    lines.append("")
    lines.append("Listado generado automáticamente a partir de tus soluciones.")
    lines.append("")
    lines.append("| # | Problema | Dificultad | Tags | |")
    lines.append("| -: | - | - | - | - |")
    for p in problems:
        link = f"[{p.title}](./{p.slug}/)"
        diff = p.difficulty or "—"
        tags = ", ".join(p.tags) if p.tags else "—"
        lines.append(f"| {p.number} | {link} | {diff} | {tags} | |")
    lines.append("")
    return "\n".join(lines)


def _iter_problem_folders(solutions_root: Path) -> Iterable[Path]:
    for child in sorted(solutions_root.iterdir(), key=lambda p: p.name):
        if child.is_dir():
            yield child


def _build_problem_list(solutions_root: Path) -> list[Problem]:
    problems: list[Problem] = []
    for folder in _iter_problem_folders(solutions_root):
        parsed = _parse_problem_dir_name(folder.name)
        if not parsed:
            continue
        num, title = parsed
        py = _find_single_py_file(folder)
        if not py:
            continue
        slug = _slugify_title(title)
        problems.append(Problem(number=num, title=title, slug=slug, solution_path=py))
    problems.sort(key=lambda p: p.number)
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Genera docs/problemas/*.md a partir de soluciones locales.")
    parser.add_argument(
        "--solutions-dir",
        default=os.environ.get("LEETCODE_SOLUTIONS_DIR", ""),
        help="Ruta a la carpeta que contiene subcarpetas por problema (ej. '1. Two Sum').",
    )
    parser.add_argument(
        "--docs-dir",
        default="docs",
        help="Ruta a la carpeta docs de MkDocs (por defecto: ./docs).",
    )
    parser.add_argument(
        "--no-network",
        action="store_true",
        help="No consultar LeetCode (dificultad/tags quedarán vacíos).",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.15,
        help="Pausa entre requests a LeetCode (segundos).",
    )
    args = parser.parse_args()

    if not args.solutions_dir:
        print("Error: faltó --solutions-dir (o la variable LEETCODE_SOLUTIONS_DIR).", file=sys.stderr)
        return 2

    solutions_root = Path(args.solutions_dir).expanduser().resolve()
    if not solutions_root.exists():
        print(f"Error: no existe la ruta: {solutions_root}", file=sys.stderr)
        return 2

    docs_root = Path(args.docs_dir).resolve()
    problemas_root = docs_root / "problemas"
    problemas_root.mkdir(parents=True, exist_ok=True)

    cache_path = Path(".cache/leetcode-metadata.json")
    cache = _load_cache(cache_path)

    problems = _build_problem_list(solutions_root)
    if not problems:
        print("No encontré problemas en la carpeta de soluciones (¿formato de carpetas distinto?).", file=sys.stderr)
        return 1

    # Enrich metadata
    if not args.no_network:
        for i, p in enumerate(problems):
            cached = cache.get(p.slug)
            if isinstance(cached, dict) and cached.get("difficulty") and isinstance(cached.get("tags"), list):
                problems[i] = dataclasses.replace(
                    p,
                    difficulty=str(cached.get("difficulty")),
                    tags=[str(x) for x in cached.get("tags")],
                )
                continue

            difficulty, tags = _fetch_leetcode_metadata(p.slug)
            if difficulty or tags:
                cache[p.slug] = {"difficulty": difficulty, "tags": tags, "ts": int(time.time())}
                problems[i] = dataclasses.replace(p, difficulty=difficulty, tags=tags)
                _save_cache(cache_path, cache)
            time.sleep(max(0.0, float(args.sleep)))

    # Write index first
    (problemas_root / "index.md").write_text(_render_index_md(problems), encoding="utf-8")

    # Write individual pages
    for idx, p in enumerate(problems):
        prev_slug = problems[idx - 1].slug if idx > 0 else None
        next_slug = problems[idx + 1].slug if idx < len(problems) - 1 else None
        out_dir = problemas_root / p.slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.md").write_text(_render_problem_md(p, prev_slug, next_slug), encoding="utf-8")

    print(f"Generado: {len(problems)} problemas en {problemas_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

