# Branching

## What Is a Branch?

A branch is a **movable label (pointer) that points to a commit**. It is not a copy of your project. Creating a branch only creates a tiny 41-byte reference, so it is instant and cheap.

```
A --- B --- C
            ^
          main
```

`HEAD` is a special pointer that shows **which branch you are currently on**. New commits are added to that branch.

```
A --- B --- C
            ^
          main  <-- HEAD
```

## Why Do We Need Branches?

| Problem without branches | How branches solve it |
|---|---|
| Half-finished work breaks the working code | Work in isolation; `main` stays stable |
| Several people edit the same code at once | Each person works on their own branch |
| Trying an experiment is risky | Delete the branch if it fails |
| Hard to review changes | Review one branch (feature) at a time |

**Purpose:** keep `main` always working, while new work happens safely on the side.

## How Branches Work

**1. Create a branch.** Both labels point to the same commit.

```
A --- B --- C
            ^
          main
          feature
```

**2. Commit on the branch.** Only the current branch's label moves forward.

```
A --- B --- C --- D --- E
            ^             ^
          main         feature  <-- HEAD
```

**3. Switch back to main.** Your files return to the state of commit C. Work on `feature` is safe and not lost.

```
A --- B --- C --- D --- E
            ^             ^
          main  <-- HEAD  feature
```

## Core Commands

| Command | What it does |
|---|---|
| `git branch` | List local branches (`*` = current) |
| `git branch -v` | List branches with their last commit |
| `git branch -a` | List local and remote branches |
| `git branch <name>` | Create a branch (stay on current one) |
| `git switch <name>` | Move to an existing branch |
| `git switch -c <name>` | Create a branch and switch to it |
| `git switch -` | Jump back to the previous branch |
| `git merge <name>` | Merge `<name>` into the current branch |
| `git branch -d <name>` | Delete a merged branch (safe) |
| `git branch -D <name>` | Force delete, even if unmerged |
| `git branch -m <new-name>` | Rename the current branch |
| `git log --oneline --graph --all` | Draw all branches as a graph |

> Older tutorials use `git checkout <name>` and `git checkout -b <name>`. They do the same as `git switch`.

## Merging

`git merge` combines another branch's work into the branch you are on. **Always switch to the receiving branch first.**

### Fast-forward merge
`main` has no new commits, so Git just moves the `main` label forward.

```
Before:                      After:
A --- B --- C                A --- B --- C --- D --- E
            \                                         ^
             D --- E                         main, feature
             ^
          feature
```

### Three-way merge
Both branches have new commits, so Git creates a **merge commit (M)** with two parents.

```
Before:                      After:
        D --- E  (feature)           D --- E
       /                            /       \
A --- B --- C --- F  (main)   A --- B --- C --- F --- M  (main)
```

## Merge Conflicts

A conflict happens when both branches change **the same lines**. Git pauses and marks the file:

```
<<<<<<< HEAD
Title from main
=======
Title from feature
>>>>>>> feature
```

Fix it:

1. Edit the file, keep the correct text, delete the markers.
2. `git add <file>`
3. `git commit` (completes the merge)

To cancel instead: `git merge --abort`

## Hands-On Workflow

```bash
git branch                          # * main
git switch -c feature-login         # create + switch

echo "Login page" > login.txt
git add login.txt
git commit -m "Add login page"

git log --oneline --graph --all     # see both branches

git switch main                     # return to main
git merge feature-login             # bring changes in
git branch -d feature-login         # delete merged branch
git log --oneline                   # feature commit is on main
```

## Pushing a Branch to GitHub

```bash
git push -u origin feature-login    # first push, sets upstream
git push                            # later pushes
```

## Key Points

- A branch is a pointer, not a copy of files.
- `HEAD` shows where you are; commits go to the current branch.
- Merge **into** the branch you are on.
- `-d` is safe; `-D` can lose unmerged work.
- Commit or stash changes before switching branches.
- Good habit: one branch per feature or bug fix, with short, clear names like `feature-login` or `fix-navbar`.