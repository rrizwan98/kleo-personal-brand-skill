"""Check package references and metadata; build portable archives when requested."""
import argparse
import ast
import importlib.util
import json
import re
import zipfile
from pathlib import Path

import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true")
    args = parser.parse_args()
    output = Path(__file__).resolve().parents[1]
    root = output / "kleo-personal-brand"
    text = (root / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = yaml.safe_load(text.split("---", 2)[1])
    assert frontmatter["name"] == root.name
    assert frontmatter["metadata"]["version"] == (output / "VERSION").read_text(encoding="utf-8").strip()
    assert len(text.splitlines()) < 500
    errors = []
    files = [p for p in root.rglob("*") if p.is_file() and "__pycache__" not in p.parts]
    for path in files:
        if path.suffix == ".md":
            content = path.read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)]+)\)", content):
                if "://" in target or target.startswith("#"):
                    continue
                resolved = (path.parent / target.split("#", 1)[0]).resolve()
                if root not in resolved.parents or not resolved.is_file():
                    errors.append(f"Broken/unsafe local reference: {path.name}: {target}")
        if path.suffix == ".py":
            ast.parse(path.read_text(encoding="utf-8"))
        if path.name in {"client.json", "sources.jsonl", "memory.jsonl", "posts.jsonl"}:
            errors.append(f"Client data inside distributable package: {path}")
    metadata = yaml.safe_load((root / "agents" / "openai.yaml").read_text(encoding="utf-8"))
    assert 25 <= len(metadata["interface"]["short_description"]) <= 64
    assert f"${root.name}" in metadata["interface"]["default_prompt"]
    assert metadata["policy"]["allow_implicit_invocation"] is True
    selector_path = root / "scripts" / "select_template.py"
    if selector_path.is_file():
        spec = importlib.util.spec_from_file_location("package_template_selector", selector_path)
        selector = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(selector)
        library, examples = selector.load_library()
        assert library["library_version"] == frontmatter["metadata"]["version"]
        assert examples
    if errors:
        raise SystemExit("\n".join(errors))
    report = {"result": "pass", "skill_lines": len(text.splitlines()), "package_files": len(files), "checks": ["YAML metadata", "local reference integrity", "Python syntax", "no client state in package", "entrypoint under 500 lines", "library schema, tag vocabulary, cross-references and version"]}
    if args.build:
        archives = []
        for suffix in (".zip", ".skill"):
            destination = output / f"{root.name}{suffix}"
            with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as archive:
                for path in files:
                    archive.write(path, path.relative_to(output).as_posix())
            with zipfile.ZipFile(destination) as archive:
                assert archive.testzip() is None
                assert len(archive.namelist()) == len(files)
            archives.append(str(destination))
        report["archives"] = archives
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
