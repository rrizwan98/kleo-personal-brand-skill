# Kleo Personal Brand Skill

A reusable agent skill for LinkedIn personal branding and ghostwriting: understand an author and their offer, retain separate client context, develop strategy and write grounded content.

Current version at this tag: **1.0.0 — reconstructed baseline**.

This is an independent implementation informed by Kleo's public workflow. It is not affiliated with Kleo, does not include proprietary Kleo prompts, and does not claim measured 85% equivalence.

## What it does

- Understands profile, offer, audience and available proof through supplied material or authorized research.
- Builds a provisional voice guide, positioning, content pillars, idea queue and calendar.
- Writes, edits and repurposes complete posts with factual checks and scoped client preferences.
- Maintains separate client workspaces across sessions.
- Routes optional visuals, publishing and analytics through tools actually available in the host.

Browser access, persistence and external actions depend on host capabilities. Saving a profile URL does not prove that the profile was visited. A calendar does not create a background scheduler. Voice matching requires authentic samples and client feedback.

## Install and use

Copy the complete [`kleo-personal-brand`](kleo-personal-brand/) directory into your host's skill directory. For Codex's usual local setup, that is `~/.codex/skills/kleo-personal-brand/`. Load a session that discovers the skill, then invoke it by name.

Example request:

> Use $kleo-personal-brand. Here is my profile, product page and three writing samples. Understand my audience, suggest positioning and write two English LinkedIn posts. Explain your choices in Roman Urdu. Keep everything as drafts.

Returning client:

> Use $kleo-personal-brand with my saved client workspace. Write one post from this new source, following my existing voice and preferences.

For a different author, use a separate client ID and workspace. The agent should use known context before asking repeated questions and label missing evidence rather than inventing it.

Optional workspace initialization, from the repository root:

```sh
python kleo-personal-brand/scripts/init_client.py --root ../Personal-Brand-Clients --client-id example-founder --display-name "Example Founder"
```

The initializer creates an empty local workspace; it does not scrape a profile or fill in facts. Client records belong outside this repository and the distributable skill.

## Specifications and history

- [v0: initial design](specs/v0.md) — retrospective, design only.
- [v1.0.0: executable baseline](specs/v1.0.0.md) — reconstructed from recorded changes.
- [Changelog](CHANGELOG.md) and [versioning/provenance](VERSIONING.md).

Read the specification for the selected tag before comparing behavior. The repository records what was tested and what remains unmeasured.

## Validate and package

Python 3.10+ is required for the helper. The helper itself has no third-party dependencies; the package validator needs PyYAML.

```sh
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python scripts/check_package.py
python scripts/check_package.py --build
```

The build produces `kleo-personal-brand.zip` and `kleo-personal-brand.skill` containing only the skill folder. Tests use fictional identities and temporary directories. They validate the initializer; they do not measure writing quality or live LinkedIn integrations.

Never commit real client workspaces, private drafts, credentials or account exports. Existing helper defaults keep voice provisional and authorization empty until actual evidence and user instructions are available.
