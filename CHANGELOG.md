# Changelog

Versions describe the reusable skill, not individual client workspaces. Repository history was created on 2026-10-13; the provenance notes below distinguish retrospective records from preserved source.

## 1.1.0 — 2026-10-14

- Add 40 original template cards with audience, goal, pillar, evidence, development and misuse guidance.
- Add 24 dated public-post reference cards across eight authors, containing direct links and original structural notes rather than copied post bodies or verified-performance claims.
- Add a local read-only selector with evidence filtering, explicit tag-fit reasons, bounded results and recent-use penalties; document a manual fallback.
- Connect selection to the client's actual product, audience, voice and brief. Preserve user-provided structures, minimal edits and supported custom structures.
- Add optional selection metadata without changing existing client-state requirements.
- Retain three same-brief baseline/updated draft pairs and a limited qualitative self-review; no independent or live-Kleo comparison is claimed.
- No third-party template vault was imported. Publishing, analytics and extension capabilities remain host-dependent.

See [v1.1.0 specification](specs/v1.1.0.md) and [comparison](evals/v1.1.0/comparison.md).

## 1.0.1 — 2026-10-13

**Preserved earlier implementation imported from the tested local skill.**

- Focus news-led posts on one reader-relevant implication and connected narrative beats.
- Keep required attribution/uncertainty while moving research-process details into editorial notes.
- Evaluate readability separately from factual completeness.
- Place supporting source links outside public copy when appropriate for the destination.
- Preserve all discovery, client-state, authorization and helper behavior from v1.0.0.

A public-demo reconstruction exposed the readability gap. Its 209-word revised output used an explicit local length request; no universal post-length rule or measured parity claim was introduced.

See [v1.0.1 specification](specs/v1.0.1.md).

## 1.0.0 — 2026-10-13

**Reconstructed implementation baseline.** Recovered from v1.0.1 by reversing its two recorded writing-guide changes and version metadata. No original v1.0.0 Git commit was available.

- Executable discovery, positioning, strategy, voice, drafting and review workflow.
- Separate client memory, evidence, ideas, draft versions and run state.
- Durable preferences and same-post temporary overrides.
- Optional host-tool routes for visuals, authorized publishing and analytics.
- Evidence and action gates, bounded editing and an explicitly internal editorial rubric.
- Python workspace initializer with 14 portable unit tests.
- Public repository metadata, specifications and packaging validator.

See [v1.0.0 specification](specs/v1.0.0.md).

## v0 — documented 2026-10-13

**Retrospective design-only baseline.** Captures the original personal-brand/ghostwriting objective, intended users, scope, constraints and acceptance plan. No executable v0 package or historical code snapshot is claimed.

See [v0 specification](specs/v0.md).
