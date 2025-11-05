#!/usr/bin/env python3
"""
Clean JD transcript .txt files by removing duplicate lines.

Defaults:
- Removes consecutive duplicate lines (after normalizing timestamps like [mm:ss] or [hh:mm:ss]).
- Keeps original file order.
- Writes changes back in place.
- Optional: make .bak backups and do global de-duplication.

Usage:
  python clean_transcripts.py --root transcripts --backup
  python clean_transcripts.py --root transcripts --backup --global-dedup
"""

import argparse
import re
from pathlib import Path

# Matches a leading timestamp like:
#   [00:12], 00:12, [01:02:03], 01:02:03.456
# and optional separators right after (e.g., " - " or ": " or " | ")
TIMESTAMP_RE = re.compile(
    r"""
    ^\s*                      # leading spaces
    \[?                       # optional '['
    (?:\d{1,2}:){1,2}\d{2}    # mm:ss OR hh:mm:ss
    (?:\.\d+)?                # optional .ms
    \]?                       # optional ']'
    \s*(?:[-:\|]\s*)*         # optional separators after timestamp
    """,
    re.VERBOSE,
)

def normalize_for_compare(
    line: str,
    ignore_case: bool = True,
    strip_timestamps: bool = True,
    collapse_ws: bool = True,
) -> str:
    """
    Build a comparison key for de-duplication without changing the original output line.
    """
    key = line
    if strip_timestamps:
        # Only strip a *leading* timestamp; keep other numbers alone
        key = TIMESTAMP_RE.sub("", key, count=1)
    if collapse_ws:
        key = " ".join(key.split())
    if ignore_case:
        key = key.lower()
    return key.strip()

def dedup_lines(lines, global_dedup: bool = False):
    """
    Remove duplicate lines, preserving order.
    - Always removes *consecutive* duplicates based on normalized comparison.
    - If global_dedup=True, also removes any line that appeared earlier anywhere.
    """
    cleaned = []
    seen = set()  # used only when global_dedup is True
    prev_key = None

    for raw in lines:
        # Keep original line content, but compare with normalized key
        key = normalize_for_compare(raw)

        # Treat fully blank (after normalization) as blank
        if not key:
            # Collapse runs of blank lines to a single blank
            if cleaned and cleaned[-1].strip() == "":
                continue
            cleaned.append("")
            prev_key = None
            continue

        # Drop consecutive duplicates
        if key == prev_key:
            continue

        # Optionally drop global duplicates
        if global_dedup:
            if key in seen:
                prev_key = key
                continue
            seen.add(key)

        cleaned.append(raw.rstrip())
        prev_key = key

    # Final pass: collapse multiple blank lines again (belt-and-suspenders)
    final = []
    prev_blank = False
    for ln in cleaned:
        is_blank = (ln.strip() == "")
        if is_blank and prev_blank:
            continue
        final.append(ln)
        prev_blank = is_blank

    return final

def process_file(path: Path, make_backup: bool, global_dedup: bool, dry_run: bool = False):
    # Read with a forgiving fallback
    try:
        original_text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        original_text = path.read_text(encoding="latin-1", errors="ignore")

    original_lines = original_text.splitlines()
    cleaned_lines = dedup_lines(original_lines, global_dedup=global_dedup)

    changed = cleaned_lines != original_lines
    removed = len(original_lines) - len(cleaned_lines)

    if changed and not dry_run:
        if make_backup:
            bak = path.with_suffix(path.suffix + ".bak")
            bak.write_text(original_text, encoding="utf-8", errors="ignore")
        # Write cleaned content with a single trailing newline
        path.write_text("\n".join(cleaned_lines).rstrip() + "\n", encoding="utf-8")

    return {
        "file": str(path),
        "lines_before": len(original_lines),
        "lines_after": len(cleaned_lines),
        "removed": removed,
        "changed": changed,
        "backup": make_backup and changed,
    }

def main():
    ap = argparse.ArgumentParser(description="Remove duplicate lines from transcript .txt files.")
    ap.add_argument("--root", required=True, help="Root directory containing transcript .txt files.")
    ap.add_argument("--glob", default="*.txt", help="Glob to match files (default: *.txt).")
    ap.add_argument("--backup", action="store_true", help="Write a .bak file before overwriting.")
    ap.add_argument("--global-dedup", action="store_true",
                    help="Remove duplicates that appear anywhere in the file (not just consecutive).")
    ap.add_argument("--dry-run", action="store_true", help="Analyze only, do not write changes.")
    args = ap.parse_args()

    root = Path(args.root)
    files = sorted(root.rglob(args.glob))
    if not files:
        print(f"No files matched under {root} with pattern {args.glob}")
        return

    total_removed = 0
    changed_files = 0

    for f in files:
        if not f.is_file():
            continue
        result = process_file(f, make_backup=args.backup, global_dedup=args.global_dedup, dry_run=args.dry_run)
        total_removed += result["removed"]
        changed_files += int(result["changed"])
        print(
            f"- {Path(f).name}: {result['lines_before']} → {result['lines_after']} "
            f"(removed {result['removed']})"
            + (" [backup]" if result["backup"] else "")
            + (" [changed]" if result["changed"] else " [unchanged]")
        )

    print(f"\nDone. Files changed: {changed_files}/{len(files)} | Total lines removed: {total_removed}")

if __name__ == "__main__":
    main()