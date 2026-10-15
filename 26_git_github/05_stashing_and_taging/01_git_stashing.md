# Git Stash

## What Is Stash?

`git stash` temporarily **shelves your uncommitted changes** and gives you a clean working directory. You can bring the changes back later. Think of it as a drawer where you put half-finished work.

```
Working Directory          Stash (drawer)
 (messy changes)  --stash-->  stash@{0}
 (clean again)    <--pop----  (changes restored)
```

> Stash is a **Git** feature that lives only in your **local** repository. It is never pushed to GitHub.

## Why Do We Need It?

Git won't let you switch branches if your uncommitted changes would be overwritten. You also may not want to commit unfinished work.

| Situation | How stash helps |
|---|---|
| Urgent bug fix while mid-feature | Stash work, fix the bug, come back |
| Need to switch branches, work isn't ready | Stash, switch, return, restore |
| Pulled changes conflict with local edits | Stash, pull, then pop |
| Want a clean state to test something | Stash, test, restore |

## How It Works

**1. You have uncommitted changes.**

```
A --- B --- C   <- main (HEAD)
Modified: app.txt   (not committed)
```

**2. `git stash` saves them and resets files to commit C.**

```
A --- B --- C   <- main (HEAD)      Stash: [ stash@{0}: changes to app.txt ]
Working directory: clean
```

**3. `git stash pop` restores them and removes the stash entry.**

```
A --- B --- C   <- main (HEAD)      Stash: [ empty ]
Modified: app.txt   (back again)
```

Stashes form a **stack**: newest first (`stash@{0}`), then `stash@{1}`, and so on.

## What Gets Stashed?

| File type | Stashed by default? |
|---|---|
| Modified tracked files | Yes |
| Staged changes | Yes |
| New untracked files | **No** (use `-u`) |
| Ignored files | **No** (use `-a`) |

## Core Commands

| Command | What it does |
|---|---|
| `git stash` | Stash tracked changes |
| `git stash push -m "message"` | Stash with a descriptive name |
| `git stash -u` | Also stash untracked files |
| `git stash -a` | Also stash ignored files |
| `git stash list` | Show all stashes |
| `git stash show` | Summary of the latest stash |
| `git stash show -p` | Full diff of the latest stash |
| `git stash pop` | Restore latest stash **and delete it** |
| `git stash apply` | Restore latest stash **and keep it** |
| `git stash pop stash@{1}` | Restore a specific stash |
| `git stash drop stash@{0}` | Delete one stash |
| `git stash clear` | Delete **all** stashes |
| `git stash branch <name>` | New branch from a stash, then pop it |
| `git stash push -- <file>` | Stash only one file |

## pop vs apply

| | `pop` | `apply` |
|---|---|---|
| Restores changes | Yes | Yes |
| Removes stash entry | Yes | No |
| Best for | Normal use | Applying the same changes to several branches |

## Hands-On Workflow

```bash
# Working on a feature
git switch -c feature-search
echo "search code" > search.txt
git add search.txt
git commit -m "Start search"
echo "half-done work" >> search.txt     # uncommitted change

# Urgent bug! Stash the work
git stash push -m "search work in progress"
git status                              # working tree clean
git stash list                          # stash@{0}: On feature-search: search work in progress

# Fix the bug on main
git switch main
git switch -c hotfix-typo
echo "fix" > fix.txt
git add fix.txt
git commit -m "Fix typo"
git switch main
git merge hotfix-typo
git branch -d hotfix-typo

# Return and restore
git switch feature-search
git stash pop                           # changes are back
git status                              # search.txt modified
```

## Stashing Untracked Files

```bash
echo "new" > notes.txt                  # untracked
git stash                               # notes.txt is NOT stashed
git stash -u                            # notes.txt IS stashed
```

## Stash Conflicts

If restored changes clash with the current files, Git reports a conflict.

- The stash is **kept** (not deleted), so nothing is lost.
- Resolve it like a merge conflict: edit the file, then `git add <file>`.
- Delete the old stash manually with `git stash drop`.

## Key Points

- Stash saves **uncommitted** work only; it is not a replacement for commits.
- Always add a message with `push -m` so you can identify stashes later.
- Use `-u` if you have new untracked files.
- `pop` deletes the stash, `apply` keeps it.
- `git stash clear` is permanent, so check `git stash list` first.
- Stash is local; it will not appear on GitHub.
- Don't let stashes pile up. Restore or drop them regularly.