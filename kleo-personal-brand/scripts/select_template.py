"""Shortlist local writing structures from explicit brief/evidence tags. No network or writes."""

import argparse
import json
import sys
from pathlib import Path


LIBRARY = Path(__file__).resolve().parents[1] / "library"


def load_library(root=LIBRARY):
    templates = json.loads((root / "templates.json").read_text(encoding="utf-8"))
    examples = json.loads((root / "examples.json").read_text(encoding="utf-8"))
    if templates.get("schema_version") != 1 or examples.get("schema_version") != 1:
        raise ValueError("Unsupported library schema")
    if templates.get("library_version") != examples.get("library_version"):
        raise ValueError("Library versions do not match")
    cards = templates["templates"]
    refs = examples["examples"]
    for records, name in ((cards, "template"), (refs, "example")):
        ids = [record["id"] for record in records]
        if not ids or len(set(ids)) != len(ids):
            raise ValueError(f"Empty or duplicate {name} IDs")
    known_refs = {record["id"] for record in refs}
    taxonomy = templates["taxonomy"]
    for card in cards:
        for field, vocab in (("goals", "goals"), ("audiences", "audiences"),
                             ("pillars", "pillars"), ("required_evidence", "evidence")):
            if not card[field] or set(card[field]) - set(taxonomy[vocab]):
                raise ValueError(f"Invalid {field} in {card['id']}")
        if set(card["example_ids"]) - known_refs:
            raise ValueError(f"Unknown example in {card['id']}")
        if len(card["beats"]) < 3 or not card["avoid"] or not card["voice_adaptation"]:
            raise ValueError(f"Incomplete writing card: {card['id']}")
    return templates, {record["id"]: record for record in refs}


def shortlist(library, examples, *, goal, audience, pillar, evidence,
              recent=(), recent_openings=(), limit=3):
    """Evidence tags must already be checked for ownership, scope and publication use."""
    taxonomy = library["taxonomy"]
    for label, value, vocab in (("goal", goal, "goals"), ("audience", audience, "audiences"),
                                ("pillar", pillar, "pillars")):
        if value not in taxonomy[vocab]:
            raise ValueError(f"Unknown {label}: {value}; inspect --list-tags")
    available = set(evidence)
    if available - set(taxonomy["evidence"]):
        raise ValueError("Unknown evidence tag; inspect --list-tags")
    if not 1 <= limit <= 5:
        raise ValueError("limit must be between 1 and 5")
    recent = set(recent)
    recent_openings = set(recent_openings)
    known_ids = {card["id"] for card in library["templates"]}
    known_openings = {card["opening_type"] for card in library["templates"]}
    if recent - known_ids or recent_openings - known_openings:
        raise ValueError("Unknown recent template ID or opening type")
    candidates = []
    blocked = []
    for card in library["templates"]:
        if goal not in card["goals"]:
            continue
        missing = sorted(set(card["required_evidence"]) - available)
        if missing:
            blocked.append({"id": card["id"], "missing_evidence": missing})
            continue
        score = 4
        reasons = [f"goal={goal}", "required evidence tags present; claims still need editorial verification"]
        for requested, tags, weight, label in ((audience, card["audiences"], 3, "audience"),
                                               (pillar, card["pillars"], 2, "pillar")):
            if requested != "any" and requested in tags:
                score += weight
                reasons.append(f"{label}={requested}")
            elif requested == "any" or "any" in tags:
                score += 1
                reasons.append(f"{label}: general-purpose match")
            else:
                reasons.append(f"{label}: adaptation required")
        if card["id"] in recent:
            score -= 4
            reasons.append("recently used template: -4")
        if card["opening_type"] in recent_openings:
            score -= 2
            reasons.append("recently used opening: -2")
        candidates.append({"id": card["id"], "tag_fit_score": score, "reasons": reasons,
                           "template": card,
                           "examples": [examples[key] for key in card["example_ids"]]})
    candidates.sort(key=lambda item: (-item["tag_fit_score"], item["id"]))
    return {
        "library_version": library["library_version"],
        "status": "shortlist" if candidates else "no_eligible_template",
        "selection_basis": "Deterministic tag fit, not writing quality, semantic matching or predicted performance. Voice, product fit and claims require the assistant's review.",
        "eligible_count": len(candidates),
        "candidates": candidates[:limit],
        "blocked_for_evidence": blocked,
        "fallback": "Use a supported original structure or request only the missing material; never invent evidence to unlock a template." if not candidates else None,
    }


def csv_values(value):
    return [item.strip() for item in value.split(",") if item.strip()]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list-tags", action="store_true")
    parser.add_argument("--goal")
    parser.add_argument("--audience", default="any")
    parser.add_argument("--pillar", default="any")
    parser.add_argument("--evidence", default="", help="Comma-separated, verified publishable evidence categories")
    parser.add_argument("--recent", default="", help="Comma-separated recent template IDs")
    parser.add_argument("--recent-openings", default="", help="Comma-separated recent opening types")
    parser.add_argument("--limit", type=int, default=3)
    args = parser.parse_args(argv)
    try:
        library, examples = load_library()
        if args.list_tags:
            result = {**library["taxonomy"], "opening_types": sorted({c["opening_type"] for c in library["templates"]})}
        else:
            if not args.goal:
                parser.error("--goal is required unless --list-tags is used")
            result = shortlist(library, examples, goal=args.goal, audience=args.audience,
                               pillar=args.pillar, evidence=csv_values(args.evidence),
                               recent=csv_values(args.recent), recent_openings=csv_values(args.recent_openings),
                               limit=args.limit)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Library selection failed: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
