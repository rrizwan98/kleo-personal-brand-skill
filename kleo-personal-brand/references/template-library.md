# Choose a structure from the curated writing library

Use this guide for a fresh post or a substantial rewrite. Preserve an effective structure for a minimal edit. An explicit user structure takes priority. The library contains 40 original template cards and 24 real public-post reference cards across eight authors. It is a pilot with English business/technology emphasis, not a comprehensive niche library, a Kleo template export or a collection of performance-proven formulas.

## Evidence first, then retrieval

1. Load the active client's audience, offer/product, voice, current brief, source facts and recent posts. Establish the one thing this post should help a reader understand or do.
2. Map the goal, reader role and pillar to the tags below. Identify only evidence that is available, attributable and usable in public. A fact that is private or belongs to another author cannot unlock a client-story template.
3. Retrieve at most three candidates. Read their development beats, exclusions and at most two relevant reference cards. Do not load every external post or the whole library into the writing context.
4. Choose the structure that fits the actual idea, offer and voice; the top tag score is only a retrieval aid. State a short internal rationale and reject any beat that would add an unsupported claim. A custom structure is valid when none fits.
5. Draft from the client's evidence in their supported voice. The card is a reasoning scaffold, not a fill-in-the-blanks post. Vary openings, development and endings across a batch. Do not automatically add a CTA.
6. Apply the existing three editorial passes. Check factual ownership, distinctive borrowed phrasing, client voice, hook/body fit and repeated angles. Save the optional selection trace beside the post metadata, never in public copy.

## Tags and mapping

Goals: `education` teaches a usable idea; `authority` develops a supported position or proof; `trust` explains genuine experience or working principles; `demand` helps a buyer evaluate an actual offer; `conversation` invites a specific useful response. These are retrieval tags, not mandatory content ratios. Existing strategy purposes map by intent: discovery can be education/authority; proof usually authority; connection often trust; action often demand.

Audience tags describe the **reader**, not necessarily the author: `founder`, `operator`, `consultant`, `marketer`, `engineer`, `leader`, `agency_owner`, `designer`, `analyst`, `creator`, or `any`. Map a niche role to the closest supported role and retain the actual reader description in the brief. Use `any` when none fits; do not change the client's audience to fit the index.

Pillars: `operations`, `technology`, `positioning`, `strategy`, `research`, `leadership`, `product`, `customer_experience`, `career`, or `any`. These are broad retrieval categories; preserve the client's more specific pillar name in their strategy.

| Evidence tag | What must actually be available |
|---|---|
| `reasoning` | A defensible explanation or explicitly hypothetical example; no implied personal incident |
| `observation` | A specific publishable client observation with its actual source and scope, not a guessed market pattern |
| `process` | A sourced procedure or a clearly framed recommendation; distinguish proposed steps from existing behavior |
| `product` | Verified relevant current capabilities, with scope and limitations |
| `offer` | Actual service/product scope, deliverable and any stated conversion route |
| `personal_story` | This client's authentic, publishable experience; no borrowed incidents |
| `decision` | This client's confirmed choice, intention or proposed experiment; not an inferred belief |
| `results` | This client's publishable measured result with baseline, scope and timeframe |
| `research` | Relevant attributable primary material; verify changing claims before using them |
| `artifact` | A real artifact that can be described or shared under its actual permission |
| `question` | A real audience/customer question; remove private identifiers as appropriate |
| `resource` | An existing, accessible resource with a verified access route |
| `opinion` | A supported client stance, or a clearly proposed position awaiting calibration |

Never label a source author's results `results` for a client. A public-source case can be discussed with attribution as `research`. Keep supplied but unsupported numbers out of the available-evidence set.

## Optional local selector

Run from the skill directory (or use the script's absolute path):

```sh
python scripts/select_template.py --list-tags
python scripts/select_template.py --goal education --audience operator --pillar operations --evidence process,product --limit 3
python scripts/select_template.py --goal trust --audience leader --pillar leadership --evidence personal_story,decision --recent T19 --recent-openings specific_moment --limit 3
```

The standard-library helper reads only its local library and performs no network request, model call or file write. It first requires a matching goal and all required evidence tags, then ranks by audience/pillar fit with a penalty for recently used structures/openings. Recent-use penalties never relax evidence checks. It does not verify the supplied evidence or understand the client's voice. Inspect the returned reasons and make the editorial choice yourself.

An empty shortlist is valid. Choose a supported custom structure, reframe the goal with an explanation, or ask for the one essential missing fact. Never add fake proof to qualify. Invalid tags fail explicitly instead of silently widening the search. If Python is unavailable, use the same evidence rules and the compact [index](../library/INDEX.md), then read only selected cards in [templates.json](../library/templates.json) and [examples.json](../library/examples.json).

## Use real examples as structural references

Each example has a direct URL, observed author, observation date, access scope, original structural analysis and limits. Exact dates, metrics and Kleo authorship are unknown. The collection is not ranked by likes, sales or virality. It verifies observable post text, not all facts asserted by the author.

Use at most two examples when they materially help the draft. An example can illuminate an opening, development or ending without establishing the ideal format for a different client. Notes describe only observed public text; video entries do not claim watched-video analysis. Re-open a source if using its factual claims, quotation, current offer or a detail beyond the stored analysis. Access failure does not permit fabricated reconstruction; retain the dated limitation or choose another source.

Do not copy full posts, distinctive expressions, named frameworks, anecdotes, testimonials or source metrics into client copy. Do not claim these creators used Kleo. Do not import third-party collections solely because they are public on GitHub; verify the reuse basis before incorporating licensed material. This release uses no such collection. Broaden future curation according to actual client niches rather than padding the count.

## Trace and learning

Optional post fields: `library_version`, `template_id` (or `custom`), `opening_type`, `example_ids`, `selection_reason`, `adaptations`, and `evidence_checks` mapping required categories to active-client source/claim IDs. Older post records lacking these fields remain valid. Keep the trace brief; it must not contain another client's material.

On the next draft, inspect recent template IDs, openings, ideas and CTAs. Reusing a useful structure is allowed, but avoid adjacent near-duplicates. Client edits can change voice preferences under the existing memory rules. Published metrics can inform experiments only when genuinely observed; never turn a favored template into a claimed high-performing formula from one self-evaluation.

## Decision checks and principles

- Context: Is the request a minimal edit with a working structure? If yes, preserve it. Otherwise retrieve a bounded shortlist.
- Context: Does the evidence belong to this client and have public-use permission? If no, exclude that evidence category or keep source attribution explicit.
- Convergence: Does the draft deliver the requested idea, voice and format without filling unsupported slots? If no, adapt or abandon the card.
- Convergence: Are three editorial passes exhausted? If yes, deliver the supported work with the precise remaining gap under the existing quality contract.
- Boundary: Is a source a reference rather than a client fact? Keep it out of first-person claims; a reference never grants publishing authority.

**Evidence eligibility.** Constraint: remove candidates whose necessary evidence is absent. Reason: a persuasive structure can otherwise induce invented proof. Application: check required tags and map the chosen card to actual evidence IDs before drafting.

**Small-context retrieval.** Constraint: at most three initial candidates and two useful example cards per draft. Reason: unrelated styles and stories contaminate voice. Application: record selected IDs and use a custom structure if the shortlist does not fit.

**Original expression.** Constraint: source examples never supply the client's biography or ready-made wording. Reason: structure can transfer while ownership of experiences cannot. Application: inspect the final draft for borrowed incidents, unsupported claims and distinctive phrasing before marking it ready for review.
