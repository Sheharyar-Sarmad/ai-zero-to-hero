# Git Rebase Basics

`git rebase` replays your branch's commits on top of another branch's latest commit, giving a straight, linear history.

## How It Works

Before: `feature` branched from an older `main`.

```
A---B---C   main
     \
      D---E   feature
```

After `git rebase main` (run on `feature`):

```
A---B---C   main
         \
          D'---E'   feature
```

`D'` and `E'` contain the same changes but have new hashes, because their parent commit changed.

## Rebase a Feature Branch

```bash
git switch main
git pull
git switch feature
git rebase main
```

Then integrate with a fast-forward:

```bash
git switch main
git merge feature
```

## Resolving Conflicts

Git pauses on each commit that conflicts.

```bash
git status               # find conflicted files
# edit files, remove the <<<<<<< ======= >>>>>>> markers
git add <file>           # mark as resolved
git rebase --continue    # apply the next commit
```

Repeat until Git reports the rebase is finished.

## Cancelling

```bash
git rebase --abort
```

This restores the branch to its state before the rebase started.

## Merge vs Rebase

| | Merge | Rebase |
|---|---|---|
| History | Preserves branching, adds a merge commit | Linear, rewritten |
| Commits | Unchanged | Recreated with new hashes |

## ⚠️ Golden Rule

**Never rebase commits others have already pulled** (e.g. `main` or a shared branch). Rewriting shared history forces teammates into confusing conflicts. Rebase only your own local, unpublished work.