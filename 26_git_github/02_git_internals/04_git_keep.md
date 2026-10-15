# Tracking Empty Directories

Git tracks **files**, not directories. If a folder is empty, Git ignores it, so it won't appear in commits or on GitHub.

## The Problem

```bash
mkdir logs
git status
```

```
nothing to commit, working tree clean
```

The empty `logs/` folder is invisible to Git.

## The Fix: `.gitkeep`

Add a placeholder file inside the folder:

```bash
touch logs/.gitkeep
git add logs/.gitkeep
git commit -m "Add logs directory"
```

Now `logs/` is tracked because it contains a file.

## Notes

- `.gitkeep` is only a **convention**. Git gives it no special meaning; any file would work.
- The leading dot hides the file in most listings.
- Once real files are added to the folder, you can delete `.gitkeep`.
- If you want the folder but not its contents (e.g. log files), pair it with `.gitignore`:

```
logs/*
!logs/.gitkeep
```