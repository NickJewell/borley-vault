#!/usr/bin/env python3
"""NLM deep enrichment script for the Borley wiki.

Usage:
    python3 .nlm-enricher.py [BATCH_SIZE]

Processes BATCH_SIZE pages (default 20) from the progress queue,
querying NotebookLM and appending Research Notes to enriched pages.
Resume by re-running — it picks up from current_index.
"""

import json
import subprocess
import sys
import re
import time
from pathlib import Path
from datetime import datetime

VAULT = Path("/Users/nick/Library/Mobile Documents/com~apple~CloudDocs/borley-vault/borley")
NOTEBOOK_ID = "110b445d-a217-4a2b-829b-4d637e9d76c7"
PROGRESS_FILE = VAULT / "wiki/.nlm-enrichment-progress.json"
SLEEP_SECONDS = 5
BATCH_SIZE = int(sys.argv[1]) if len(sys.argv) > 1 else 20
TODAY = "2026-05-30"

# NLM source UUID prefix → vault slug prefix
SOURCE_MAP = {
    "335002f6": "15mhh",
    "f20bf3be": "brc",
    "a129f585": "bps",
    "d086f9b3": "spr",
    "728b0bb8": "ebr",
    "99520c38": "enbr",
    "cf7e9dfe": "brfa",
    "30fd1a01": "gtwnd",
    "4c30d97d": "gotb",
    "1da15024": "hast",
    "99df314d": "hbrs",
    "30adbfa2": "nhf",
    "76c99366": "mhh",
    "c99a1b4b": "slbr",
    "bd459ecd": "wob",
    "2861338c": "web",   # foxearth.org live page (not in vault sources)
}

QUERY_TEMPLATES = {
    "person": (
        "What specific facts, events, dates, quotes, contradictions, or lesser-known biographical "
        "details do the Borley sources record about {title}? Focus on details that a thorough "
        "reference article should include. Please draw on all available sources."
    ),
    "place": (
        "What specific details do the Borley sources record about {title} — physical description, "
        "key events that occurred there, who was associated with it, and any contradictions between "
        "accounts? Focus on concrete details a reference article should include."
    ),
    "phenomenon": (
        "What are all recorded instances, witness descriptions, and proposed explanations of "
        "{title} in the Borley sources? Include specific dates, witnesses, and source perspectives."
    ),
    "theme": (
        "What evidence, arguments, and perspectives do the Borley sources present regarding "
        "{title}? Include specific claims, who makes them, and any counter-arguments."
    ),
}


def read_page(path):
    """Return (title, type, full_text) from a wiki page."""
    text = Path(path).read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, None, text
    fm = text[3:end]
    title = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    type_ = re.search(r'^type:\s*(\w+)', fm, re.MULTILINE)
    return (
        title.group(1).strip('"\'') if title else None,
        type_.group(1) if type_ else None,
        text,
    )


def query_nlm(query):
    """Query NLM with --json, return (answer_text, citation_slug_map) or (None, None) on failure."""
    try:
        result = subprocess.run(
            ["notebooklm", "ask", query,
             "--notebook", NOTEBOOK_ID,
             "--json"],
            capture_output=True, text=True, timeout=120,
        )
        if result.returncode != 0 or not result.stdout.strip():
            return None, None
        data = json.loads(result.stdout)
        answer = data.get("answer", "").strip()
        references = data.get("references", [])

        # Build citation_number → slug_prefix map
        citation_map = {}
        for ref in references:
            cnum = ref.get("citation_number")
            src_id = ref.get("source_id", "")
            prefix = SOURCE_MAP.get(src_id[:8], "corpus")
            if cnum and cnum not in citation_map:
                citation_map[cnum] = prefix

        return answer, citation_map
    except (subprocess.TimeoutExpired, json.JSONDecodeError, Exception):
        return None, None


def should_enrich(answer):
    """Heuristic: is the response substantive enough to add to the page?"""
    if not answer or len(answer) < 200:
        return False
    no_info = [
        "don't have information",
        "no information",
        "not mentioned",
        "not specifically mentioned",
        "cannot find",
        "no specific details",
        "no details",
        "not directly",
        "no record",
    ]
    lower = answer.lower()
    if any(p in lower for p in no_info) and len(answer) < 500:
        return False
    return True


def build_sources_legend(citation_map):
    """Build a compact sources legend showing unique slug prefixes drawn on."""
    if not citation_map:
        return ""
    unique = sorted(set(citation_map.values()))
    return "**Sources:** " + " · ".join(unique)


def append_research_notes(page_path, answer, citation_map):
    """Append ## Research Notes to the page if not already present."""
    text = Path(page_path).read_text(encoding="utf-8")
    if "## Research Notes" in text:
        return False
    legend = build_sources_legend(citation_map)
    section = (
        f"\n\n## Research Notes\n\n"
        f"*Sourced via NotebookLM corpus research, {TODAY}.*\n\n"
        f"{answer}\n"
    )
    if legend:
        section += f"\n{legend}\n"
    Path(page_path).write_text(text.rstrip() + section, encoding="utf-8")
    return True


def load_progress():
    return json.loads(PROGRESS_FILE.read_text())


def save_progress(data):
    data["last_updated"] = datetime.now().isoformat()
    PROGRESS_FILE.write_text(json.dumps(data, indent=2))


def main():
    progress = load_progress()
    queued = progress["queued"]
    start_idx = progress["current_index"]
    end_idx = min(start_idx + BATCH_SIZE, len(queued))

    if start_idx >= len(queued):
        print("All pages processed.")
        return

    print(f"NLM enrichment — pages {start_idx + 1}–{end_idx} of {len(queued)}")
    print(f"Enriched so far: {len(progress['enriched'])} | No-change: {len(progress['no_change'])} | Failed: {len(progress['failed'])}\n")

    enriched_run = no_change_run = failed_run = 0
    consecutive_failures = 0

    for i in range(start_idx, end_idx):
        page_rel = queued[i]
        page_path = VAULT / page_rel

        title, type_, _ = read_page(page_path)
        if not title or not type_:
            print(f"  [{i+1:>3}] SKIP (no frontmatter): {page_rel}")
            progress["no_change"].append(page_rel)
            progress["current_index"] = i + 1
            save_progress(progress)
            continue

        template = QUERY_TEMPLATES.get(type_, QUERY_TEMPLATES["person"])
        query = template.format(title=title)

        print(f"  [{i+1:>3}/{len(queued)}] {title[:50]:<50} ", end="", flush=True)

        answer, citation_map = query_nlm(query)
        time.sleep(SLEEP_SECONDS)

        if answer is None:
            print("FAILED — retrying in 30s")
            time.sleep(30)
            answer, citation_map = query_nlm(query)
            time.sleep(SLEEP_SECONDS)

        if answer is None:
            print("FAILED (2nd attempt)")
            progress["failed"].append(page_rel)
            failed_run += 1
            consecutive_failures += 1
            if consecutive_failures >= 3:
                print("\n⚠  3 consecutive failures — pausing. Check rate limits.")
                progress["current_index"] = i + 1
                save_progress(progress)
                return
        else:
            consecutive_failures = 0
            if should_enrich(answer):
                append_research_notes(page_path, answer, citation_map)
                progress["enriched"].append(page_rel)
                enriched_run += 1
                slugs = sorted(set(citation_map.values())) if citation_map else []
                print(f"ENRICHED  [{', '.join(slugs[:4])}{'…' if len(slugs)>4 else ''}]")
            else:
                progress["no_change"].append(page_rel)
                no_change_run += 1
                print("no change")

        progress["current_index"] = i + 1
        save_progress(progress)

    print(f"\n--- Batch complete ---")
    print(f"  This run:  enriched={enriched_run}  no-change={no_change_run}  failed={failed_run}")
    print(f"  All-time:  enriched={len(progress['enriched'])}  no-change={len(progress['no_change'])}  failed={len(progress['failed'])}")
    print(f"  Progress:  {progress['current_index']}/{len(queued)} pages done")
    remaining = len(queued) - progress["current_index"]
    if remaining > 0:
        print(f"  Remaining: {remaining} pages (~{remaining * 15 // 60} min at 15s/page)")
        print(f"\nResume with:  python3 borley/.nlm-enricher.py [BATCH_SIZE]")
    else:
        print("  All pages processed!")


if __name__ == "__main__":
    main()
