# Basic Git Workflow

## Theory: The Three Areas

```
Working Directory  --git add-->  Staging Area  --git commit-->  Repository
 (your files)                    (next snapshot)                 (history)
```

Git saves **snapshots** (commits) of only what you stage. Staging lets you choose exactly which changes go into each commit.

## Core Commands

| Command | Purpose |
|---|---|
| `git init` | Create a repository (hidden `.git/` folder) |
| `git status` | Show untracked, modified, and staged files |
| `git add <file>` / `git add .` | Stage changes |
| `git commit -m "message"` | Save the staged snapshot |
| `git log --oneline` | View commit history |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |

## .gitignore

Lists files Git should not track, one pattern per line:

```
node_modules/
.env
*.log
```

Commit `.gitignore` itself so the whole team shares it.

## Empty Directories

Git tracks file *content*, not folders. An empty folder has no content, so Git never saves it. Add a placeholder file, by convention named `.gitkeep`:

```bash
mkdir logs
touch logs/.gitkeep
```

## Hands-On Workflow

```bash
mkdir my-project && cd my-project
git init                          # start repository
echo "# My Project" > README.md
echo "*.log" > .gitignore
git status                        # both files untracked
git add .                         # stage
git commit -m "Initial commit"    # save snapshot

echo "First change" >> README.md
git diff                          # see what changed
git add README.md
git commit -m "Update README"
git log --oneline                 # two commits listed
```

**Cycle to repeat:** edit → `git status` → `git diff` → `git add` → `git commit`