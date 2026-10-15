# Working Directory vs. Staging Area vs. Repository

Git keeps your changes in three places. Each command moves changes between them. Understanding which area a change lives in explains almost every Git command.

## Theory

### Working directory
- The normal files and folders you see and edit.
- Git does not save anything here; it only compares these files against the other two areas.
- Files can be **untracked** (new to Git) or **tracked** (already known).

### Staging area (index)
- A draft of your next commit, stored in `.git/index`.
- Lets you choose exactly which changes to save, so one commit can contain one logical change even if you edited many files.
- It holds a full snapshot of every tracked file as it will appear in the next commit.

### Repository
- The permanent history, stored in `.git/objects/`.
- Every commit is an immutable snapshot with a message, author, and parent.
- `HEAD` points to the latest commit on your current branch.

## Differences

| Area | What it is | Location | Holds | Changed by |
|------|------------|----------|-------|------------|
| **Working directory** | Files you edit | Project folder | Current file contents | Your editor |
| **Staging area (index)** | Draft of next commit | `.git/index` | Selected changes | `git add` |
| **Repository** | Saved history | `.git/objects/` | Commits | `git commit` |

## Diagram

```
 Working Directory      Staging Area (Index)      Repository (HEAD)
 -----------------      --------------------      -----------------
        |                        |                       |
        |------- git add ------->|                       |
        |                        |---- git commit ------>|
        |                        |                       |
        |<--- git restore <file> |                       |
        |    (from index)        |                       |
        |                        |<-- git restore -------|
        |                        |    --staged <file>    |
        |                        |    (from HEAD)        |
        |<------ git restore --source=HEAD <file> -------|
```

## File States

| State | Meaning | Seen in `git status` as |
|-------|---------|-------------------------|
| Untracked | New file, unknown to Git | "Untracked files" |
| Modified | Changed in working directory only | "Changes not staged for commit" |
| Staged | Added to index | "Changes to be committed" |
| Committed | Stored in repository | Not listed (clean) |

## Examples

**Check state**
```bash
git status            # shows modified, staged, untracked files
```

**Working directory → staging**
```bash
git add app.txt       # stage one file
git add .             # stage everything
git add -p            # stage selected parts interactively
```

**Staging → repository**
```bash
git commit -m "Update app.txt"
```

**Discard working directory changes** (restores from the index)
```bash
git restore app.txt
```

**Unstage (keep edits in working directory)**
```bash
git restore --staged app.txt
git reset app.txt     # older equivalent
```

**Move HEAD back**
```bash
git reset --soft HEAD~1    # undo commit; changes stay staged
git reset --mixed HEAD~1   # undo commit; changes stay unstaged (default)
git reset --hard HEAD~1    # undo commit; delete changes (destructive)
```

## What `git reset` Changes

| Mode | Moves HEAD | Resets index | Resets working directory |
|------|:----------:|:------------:|:------------------------:|
| `--soft` | Yes | No | No |
| `--mixed` (default) | Yes | Yes | No |
| `--hard` | Yes | Yes | Yes |

## What `git diff` Compares

| Command | Compares |
|---------|----------|
| `git diff` | Working directory vs. index |
| `git diff --staged` | Index vs. last commit |
| `git diff HEAD` | Working directory vs. last commit |

## Example Session

```bash
echo "v1" > app.txt
git add app.txt              # app.txt is staged
echo "v2" >> app.txt         # edit again after staging
git status                   # app.txt is both staged AND modified
git diff                     # shows only v2 (working vs. index)
git diff --staged            # shows only v1 (index vs. HEAD)
git commit -m "Add app.txt"  # commits v1 only
```

The commit saves what was in the **index**, not what is currently in the working directory.

## Key Points

- `git restore <file>` overwrites your edits permanently.
- `git reset --hard` discards uncommitted work; use with care.
- Staging lets you split a messy working directory into clean, focused commits.
- A commit contains the index contents, not the working directory contents.