"""Practical helpers for small development workflows."""

import re


def changed_files(before: list[str], after: list[str]) -> dict[str, list[str]]:
    """Compare two file-name collections."""
    old, new = set(before), set(after)
    return {"added": sorted(new - old), "removed": sorted(old - new)}


def normalize_version(value: str) -> str:
    """Normalize a simple semantic version by removing a leading v."""
    value = value.strip()
    if value.startswith("v"):
        value = value[1:]
    if not re.fullmatch(r"\d+(?:\.\d+){0,2}", value):
        raise ValueError("invalid version")
    return value
