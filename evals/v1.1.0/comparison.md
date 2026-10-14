# Same-brief writing comparison: v1.0.1 and v1.1.0

Recorded 2026-10-14. Three fictional briefs, six complete English drafts. This is a development smoke test and qualitative self-review, not an independent, blind or live-Kleo benchmark.

## Method

The same assistant authored both conditions. Baseline drafts were saved before the library files and selection workflow were implemented, using v1.0.1's writing guide and the same [briefs](briefs.json). The assistant already knew the approved library plan and had researched public examples; baseline contamination and order effects are possible. No isolated model sessions or outside reviewers were used, and the baseline was not deliberately weakened.

The updated condition ran the actual local selector, inspected the relevant cards and produced a new draft from the same brief. Inputs, returned shortlists, selected structures, adaptations and evidence mappings are retained in [selection-traces.json](selection-traces.json). All identities, experiences, products and voice samples are fictional test fixtures. No user's private client workspace was used.

Each brief requires 120–170 words, English, no hashtags or invented proof, and a distinct voice. Review dimensions were factual accuracy, voice, specificity, readability and goal fit. Word counts are mechanical; all writing judgments below are subjective. No score ratio, measured uplift, human preference or performance claim is made.

## Drafts and observations

| Brief | Baseline | Updated | Selected structure | Assessment |
|---|---|---|---|---|
| Workflow founder | [v1.0.1](baseline-founder.md) | [v1.1.0](updated-founder.md) | T01; E13 structural reference | Updated copy makes pre-send review and post-reply ownership easier to distinguish. Baseline also provides useful responsibilities; neither invents the requested unsupported efficiency number. Updated copy is a little longer. |
| Engineering lead | [v1.0.1](baseline-leader.md) | [v1.1.0](updated-leader.md) | T19; E10 structural reference | Both preserve the actual mistake and untested next step. Updated copy opens on the consequence; baseline is equally usable and its ending may feel more natural. No clear quality winner. |
| Onboarding consultant | [v1.0.1](baseline-consultant.md) | [v1.1.0](updated-consultant.md) | T27; E14 structural reference | Updated copy gives an earlier fit condition and a clearer case for choosing a different service. Baseline is accurate but spends more of its limited space stating lack of guarantees. Both retain a modest invitation. |

## Factual and voice review

| Check | Observed result |
|---|---|
| Unsupported 40% efficiency claim | Absent in both founder drafts; neither implies measured customer results |
| Product capability fidelity | Both founder drafts claim only prepared emails and an approval/review step; additional checks are framed as team decisions |
| Incident ownership | Both leader drafts use only L1–L4; no source-author company, biography or conversation appears |
| Future versus achieved result | Both leader drafts explicitly keep next week's experiment unmeasured |
| Offer scope | Both consultant drafts preserve duration, documents, map deliverable and exclusion of software implementation |
| Style constraints | Calm founder voice, reflective first-person leader with no bullets/CTA, and one low-pressure consultant invitation are retained |
| Full copied source passages | None present; no source-post bodies are included in the library |
| Client/publishing actions | No real client state modified, profile visited on behalf of a client, or post published |

The six drafts passed a manual check against their fixture claims and format constraints. This verifies only these artifacts under the stated review method. It does not prove that future runs will always follow the evidence gates or improve writing.

Whitespace-delimited word counts: founder 148 → 151; leader 140 → 137; consultant 142 → 138. All six are within 120–170 words, contain no hashtags, and omit the unsupported 40% claim. These are format checks, not quality scores. Interpretive first-person phrasing would still need the real author's review outside this fictional test.

## What the test supports

The update adds inspectable choices: which structures were eligible, why one was selected, which sources influenced structure and which facts supported the draft. In this small review, the founder and offer-fit drafts showed useful differences in emphasis; the leadership case did not show a decisive quality improvement. The strongest measured software evidence is the selector's regression suite, including missing proof, no eligible match, invalid inputs and recent-use penalties.

For a stronger writing-quality claim, use unseen briefs, isolated baseline/updated sessions, several genuine client voice sets and independent reviewers who do not know the condition. Preserve raw outputs and hard factual gates. Real matched Kleo outputs would be needed for any Kleo-equivalence claim.

## Skill Creator Max maintenance review

- **Persona:** The numbered workflow now resolves the client and evidence, chooses an eligible structure, drafts, reviews and records the actual state. All three updated cases produced complete drafts and trace records.
- **Questions:** Evidence availability, minimal-edit scope, voice conflict and absent source access each have a defined action; no question requires unnecessary repeat intake when the fixture already answers it.
- **Principles:** Evidence eligibility is exercised by tests excluding unsupported proof; small-context retrieval bounds candidate counts; original expression is reviewed against source ownership. These checks supplement rather than replace the existing client isolation and authorization contract.

The first selector validation exposed an omitted `observation` tag used by T13. The vocabulary and guide were corrected, and the package validator was extended to load the library so this class of mismatch fails packaging as well as unit tests. The full suite then passed.
