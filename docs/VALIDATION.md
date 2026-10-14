# Validation record

Updated: 2026-10-14. Earlier records retain their original scope.

## v1.1.0 library update

| Check | Result |
|---|---|
| Portable unit suite | 28 passed: 14 existing initializer tests and 14 selector/provenance tests |
| Evidence-filter regressions | Unsupported client results and missing stories excluded; an empty evidence set produces an honest empty shortlist |
| Retrieval behavior | Reader/pillar fit, recent template/opening penalties, deterministic ties, 1–5 result bound and explicit invalid-input errors checked |
| CLI portability | Runs from a different working directory and creates no files there |
| Library integrity | 40 original template cards; 24 unique public-post links; eight authors; valid categories, unique IDs and example cross-references |
| Package validator | Metadata, references, Python syntax, no client state, entrypoint length, library schema and version alignment pass; 15 skill files |
| Writing exercise | Three identical fictional briefs, six retained drafts, selector traces and qualitative comparison |
| Format checks | All six drafts meet 120–170 words, omit hashtags and do not include the unsupported efficiency figure |
| Creator maintenance | Persona, concrete decision questions and constraint/reason/application principles reviewed against the scenario outputs |
| Distribution | ZIP and `.skill` archives built and integrity-checked; all 15 packaged files match both the installed skill and desktop source copy byte-for-byte |
| Version preservation | Previous local v1.0.1 files and archives backed up before installation; existing published version tags retained |
| Repository document review | All local Markdown targets resolve, whitespace check passes and the public-content scan found no private client paths/records or credential-pattern matches |

See [comparison, all six drafts and limitations](../evals/v1.1.0/comparison.md), [briefs](../evals/v1.1.0/briefs.json), [selection traces](../evals/v1.1.0/selection-traces.json) and [source index](../kleo-personal-brand/library/INDEX.md).

Source verification means public post text and displayed author were observed with the web tool. It does not verify every source claim, metric, current availability, true authorship or use of Kleo. Some web responses are cached. Video examples are caption/public-transcript analyses; the videos were not watched. Dates are review dates, and exact post publication dates remain unknown. No third-party full posts, screenshots or template vault were packaged.

This writing comparison was conducted by the same assistant with known conditions and a small fictional sample. It supports inspectable structure selection, not a measured improvement percentage, human preference or Kleo equivalence. The baseline was also strong; the leadership example had no clear winner. The first validation caught an omitted evidence tag, which was corrected before the passing run.

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
