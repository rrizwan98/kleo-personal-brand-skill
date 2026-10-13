# Versioning and provenance

`VERSION` and `kleo-personal-brand/SKILL.md` identify the executable package version. Annotated Git tags identify reviewable checkpoints.

| Tag | Meaning |
|---|---|
| `v0` | Retrospectively written initial design specification; no executable skill |
| `v1.0.0` | Reconstructed initial implementation, with the exact reconstruction method documented in its spec |

These commits were created while preparing this repository. Dates were not backdated. A reconstruction is not presented as a preserved original commit.

## Reading history

```sh
git tag --list
git show v0:specs/v0.md
git show v1.0.0:specs/v1.0.0.md
git switch --detach v1.0.0
```

## Future changes

1. Describe the behavior change and acceptance evidence in a specification or patch note.
2. Update the skill, `VERSION`, frontmatter version and changelog together.
3. Run the portable tests and package validator; run a realistic writing scenario when behavior changes.
4. Review tracked content for client state, credentials and local-only paths.
5. Commit the change and create a new annotated tag. Published version tags are immutable; corrections receive a new version.

Use patch versions for compatible corrections/refinements, minor versions for added compatible capabilities, and major versions for incompatible workflow or state-contract changes. A client-state schema change must describe migration requirements explicitly.

Generated `.zip` and `.skill` archives are ignored by Git. Build them from the checked-out tag so the contents correspond to that version.
