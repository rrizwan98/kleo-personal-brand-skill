"""Create or reuse a client-isolated workspace without overwriting existing data.

Python 3.10+; standard library only. No network calls or credentials.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


RESERVED = {"con", "prn", "aux", "nul"} | {
    f"{prefix}{n}" for prefix in ("com", "lpt") for n in range(1, 10)
}


def canonical_url(value):
    if not value:
        return None
    parts = urlsplit(value.strip())
    if parts.scheme not in {"https", "http"} or not parts.hostname or parts.username or parts.password:
        raise ValueError("Profile URL must be an absolute HTTP(S) URL without credentials.")
    host = parts.hostname.lower().removeprefix("www.")
    if parts.port:
        host += f":{parts.port}"
    return urlunsplit((parts.scheme.lower(), host, parts.path.rstrip("/"), "", ""))


def ensure_client(root, client_id, display_name, profile_url=None):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", client_id) or len(client_id) > 64:
        raise ValueError("Client ID must be 1-64 lowercase letters/digits separated by hyphens.")
    if client_id in RESERVED:
        raise ValueError("Client ID is a reserved Windows device name.")
    display_name = display_name.strip()
    if not display_name:
        raise ValueError("Display name must not be empty.")
    profile_url = canonical_url(profile_url)
    root = Path(root).expanduser().resolve()
    skill_dir = Path(__file__).resolve().parent.parent
    if root == skill_dir or skill_dir in root.parents:
        raise ValueError("Client data must be stored outside the distributable skill directory.")
    target = root / client_id
    if target.resolve().parent != root:
        raise ValueError("Client path resolves outside the requested root.")
    manifest = target / "client.json"
    if target.exists():
        if not manifest.is_file():
            raise ValueError("Existing directory has no client.json; review it before reusing this ID.")
        current = json.loads(manifest.read_text(encoding="utf-8"))
        if current.get("client_id") != client_id:
            raise ValueError("Existing client ID does not match; no files changed.")
        if current.get("display_name", "").strip().casefold() != display_name.casefold():
            raise ValueError("Existing client name differs; resolve identity before reusing this ID.")
        old_url = canonical_url(current.get("profile_url"))
        if profile_url and old_url != profile_url:
            raise ValueError("Existing profile differs or was unknown; review and explicitly update it first.")
        return {"status": "existing", "client_id": client_id, "path": str(target)}
    now = datetime.now(timezone.utc).isoformat()
    data = {
        "schema_version": 1,
        "client_id": client_id,
        "display_name": display_name,
        "profile_url": profile_url,
        "created_at": now,
        "updated_at": now,
        "identity": {},
        "offers": [],
        "audience": {},
        "voice": {"version": 1, "confidence": "provisional", "sample_refs": [], "patterns": []},
        "goals": [],
        "preferences": {"publication_language": None, "timezone": None, "cadence": None},
        "capabilities": {},
        "authorization": [],
    }
    root.mkdir(parents=True, exist_ok=True)
    # Exclusive mkdir prevents two initializers from writing the same client.
    target.mkdir(exist_ok=False)
    with manifest.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    for name in ("sources", "knowledge", "memory", "ideas", "posts", "runs"):
        (target / f"{name}.jsonl").touch(exist_ok=False)
    for name in ("drafts", "analytics"):
        (target / name).mkdir()
    return {"status": "created", "client_id": client_id, "path": str(target)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, help="Client storage root outside this skill")
    parser.add_argument("--client-id", required=True, help="Stable client slug, e.g. maya-flowdesk")
    parser.add_argument("--display-name", required=True)
    parser.add_argument("--profile-url", default=None)
    args = parser.parse_args()
    try:
        result = ensure_client(args.root, args.client_id, args.display_name, args.profile_url)
    except (ValueError, OSError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
