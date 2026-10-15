# Git Tags

## What Is a Tag?

A tag is a **permanent, human-readable label attached to a specific commit**. It is most often used to mark release versions like `v1.0.0`.

A branch label moves forward with every new commit. A tag **never moves**.

```
A --- B --- C --- D --- E   <- main (moves)
      ^           ^
    v1.0        v1.1        (tags stay fixed)
```

## Why Do We Need Tags?

Commit hashes like `9fceb02` are hard to remember. Tags give important points in history a clear name.

| Problem | How tags help |
|---|---|
| Hard to find the release commit | `v1.0.0` names it exactly |
| Need to roll back to a stable version | Check out the tag |
| Users want to download a release | GitHub builds releases from tags |
| Team needs to know what shipped | Tags show release history |

## Tags vs Branches

| | Branch | Tag |
|---|---|---|
| Moves with new commits | Yes | **No** |
| Purpose | Ongoing work | Mark a fixed point |
| Typical name | `feature-login` | `v1.0.0` |

## Two Types of Tags

| Type | Stores | Use for |
|---|---|---|
| **Lightweight** | Just a pointer to a commit | Quick, private markers |
| **Annotated** | Tagger, date, message (full Git object) | **Releases (recommended)** |

```
Lightweight:  v1.0 ---> commit C

Annotated:    v1.0 ---> [tag object: author, date, message] ---> commit C
```

## Core Commands

| Command | What it does |
|---|---|
| `git tag` | List all tags |
| `git tag v1.0.0` | Create a lightweight tag on the current commit |
| `git tag -a v1.0.0 -m "Release 1.0.0"` | Create an annotated tag |
| `git tag -a v0.9.0 <commit-hash>` | Tag an older commit |
| `git show v1.0.0` | Show tag details and its commit |
| `git push origin v1.0.0` | Push one tag to GitHub |
| `git push origin --tags` | Push all tags |
| `git tag -d v1.0.0` | Delete a local tag |
| `git push origin --delete v1.0.0` | Delete a remote tag |
| `git switch --detach v1.0.0` | View code at that tag |

> `git push` does **not** send tags automatically. You must push them.

## Hands-On Workflow

```bash
echo "v1 code" > app.txt
git add app.txt
git commit -m "Finish version 1"

git tag -a v1.0.0 -m "First release"     # create annotated tag
git tag                                  # v1.0.0
git show v1.0.0                          # tag info + commit

echo "more features" >> app.txt
git commit -am "Add new features"

git tag -a v1.1.0 -m "Second release"
git push origin --tags                   # publish tags to GitHub
```

## Going Back to a Tag

```bash
git switch --detach v1.0.0     # look at old release (read-only exploration)
git switch main                # come back
```

Tags point to a commit, not a branch. This puts you in **detached HEAD** state, which is fine for viewing. To make changes from it, create a branch:

```bash
git switch -c fix-v1 v1.0.0
```

## Versioning Convention (SemVer)

Format: `vMAJOR.MINOR.PATCH`

| Part | Increase when | Example |
|---|---|---|
| MAJOR | Breaking changes | `v1.0.0` → `v2.0.0` |
| MINOR | New features, backward compatible | `v1.0.0` → `v1.1.0` |
| PATCH | Bug fixes only | `v1.0.0` → `v1.0.1` |

## Tags on GitHub

After pushing, tags appear under **Releases / Tags** on the repository page. You can turn a tag into a **GitHub Release** with notes and downloadable files.

## Key Points

- A tag is a fixed label on one commit; it never moves.
- Use **annotated** tags (`-a -m`) for releases.
- Tags are not pushed by default: use `git push origin <tag>` or `--tags`.
- Use `git show <tag>` to inspect a release.
- Follow `vMAJOR.MINOR.PATCH` naming.
- Deleting a tag locally does not delete it on GitHub, so delete both.