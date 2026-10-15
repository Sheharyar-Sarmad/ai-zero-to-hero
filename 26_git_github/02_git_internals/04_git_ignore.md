# .gitignore

## What Is .gitignore?

`.gitignore` is a plain text file that tells Git which files and folders to **ignore**. Ignored files don't appear in `git status` and can't be staged by accident with `git add .`.

```
All project files
      |
      v
 .gitignore filter --> ignored files (never tracked)
      |
      v
 Tracked / trackable files --> git add --> git commit
```

## Why Do We Need It?

| Problem | Example | Why ignore it |
|---|---|---|
| **Secrets** | `.env`, API keys | Pushing them to GitHub exposes passwords |
| **Generated files** | `node_modules/`, `dist/`, `__pycache__/` | Rebuilt from code, so they only bloat the repo |
| **Personal files** | `.vscode/`, `.DS_Store` | Specific to your machine, not the project |
| **Noise** | `*.log`, `*.tmp` | Change constantly and clutter `git status` |

## Creating One

Create `.gitignore` in the project root, then commit it so the whole team shares the same rules:

```bash
touch .gitignore
git add .gitignore
git commit -m "Add .gitignore"
```

## Pattern Syntax

```
# This is a comment
*.log            # all files ending in .log
.env             # a specific file
node_modules/    # a whole folder
/build           # only the build folder in the project root
!important.log   # exception: do NOT ignore this file
```

## Hands-On Example

```bash
git init
echo "SECRET=123" > .env
echo "debug" > app.log
echo "# App" > README.md

git status                  # .env, app.log, README.md all untracked

printf ".env\n*.log\n" > .gitignore
git status                  # only README.md and .gitignore appear

git add .
git commit -m "Add README and .gitignore"
```

## Common Gotchas

- **Already-tracked files stay tracked.** `.gitignore` only affects untracked files. To stop tracking a file but keep it on disk:

```bash
git rm --cached .env
git commit -m "Stop tracking .env"
```

- **Check why a file is ignored:**

```bash
git check-ignore -v app.log
```

- **Empty folders:** Git can't track an empty folder (see `.gitkeep`). If you ignore a folder's contents but want the folder kept, add a `.gitkeep` and un-ignore it with `!.gitkeep`.

## Rule of Thumb

Ignore anything that is **secret**, **generated**, or **personal**. Commit only the source files others need.