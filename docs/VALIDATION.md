# Validation record

Recorded: 2026-10-13.

## Checks rerun for repository preparation

| Version | Check | Result |
|---|---|---|
| v0 | Design specification and provenance reviewed | Design only; no runtime test applies |
| v1.0.0 | `python -m unittest discover -s tests -v` | 14 passed |
| v1.0.0 | `python scripts/check_package.py --build` | Passed; 10 skill files in each archive |
| v1.0.0 | Public-content review | No real client workspace, credentials or local personal paths included |
| v1.0.1 | `python scripts/check_package.py --build` | Passed; 10 skill files in each archive |
| v1.0.1 | Compare current source package with repository | All 10 skill files match byte-for-byte |
| v1.0.1 | Repository Markdown references and whitespace | Passed |

The initializer and its tests are unchanged between v1.0.0 and v1.0.1; the 14-test result applies to that same helper implementation. Only the skill's version metadata and writing guidance change.

The package validator checks YAML, version alignment, internal references, helper syntax, entrypoint size and absence of client-state files in the distributable folder. Unit tests use fictional identities and temporary directories; no profile is fetched and nothing is published.

## Historical behavioral checks

Before repository publication, separate local forward tests exercised a fictional founder setup, switching clients, durable corrections, temporary overrides, state reload and continuation of a revision. The recorded results included eight founder checks, fifteen continuity assertions and fourteen revision assertions. These counts describe historical local runs, not the portable unit suite.

Raw client workspaces, machine-specific execution records and private account material are intentionally outside this repository. The scenarios and quality contract are described in [quality.md](../kleo-personal-brand/references/quality.md). A reader can rerun comparable model-driven scenarios in their own host; the unit command alone does not reproduce them.

## Known limits

- Automated checks cannot prove that an assistant followed every instruction.
- A saved URL/source entry is not sufficient evidence of actual browser inspection.
- A supported voice requires observed/authentic samples; a populated manifest alone is insufficient.
- Live profile access, publishing, asset generation, background automation and private analytics were not validated by this repository's tests.
- Editorial self-scores are separate from human preference, reach, sales or product-equivalence measurements.

## v1.0.1 public-demo reconstruction

A worked example from the official Kleo tutorial was linked to Jake Ward's published post. A fresh writer received a reconstructed brief and source packet while the original final copy was withheld. A revised output followed additional editorial direction and the v1.0.1 writing guide. Original and revised local drafts were kept separate.

The review found that the original had stronger narrative momentum; the skill draft made evidence limitations more explicit. Revision improved focus and readability. The evaluator supplied a curated packet and knew which system produced each output. Author memory, full history and model settings were unavailable. This was a one-case qualitative comparison, not a controlled parity benchmark or human preference study.

The public provenance, change and limits are documented in [specs/v1.0.1.md](../specs/v1.0.1.md). No third-party post is reproduced in full and no real client workspace is published.
