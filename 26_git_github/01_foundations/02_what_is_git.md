# What Is Git?

**Git** is a free, open-source tool that tracks changes to your files over time. It is the most widely used **version control system**.

## Key Concepts

- **Version control:** Records every change so you can review history or undo mistakes.
- **Repository (repo):** A project folder that Git tracks. Its history lives in a hidden `.git/` folder.
- **Commit:** A saved checkpoint with a message describing what changed.
- **Snapshot:** Each commit stores the state of your files at that moment, so you can return to it later.

## Why Developers Use Git

- Undo mistakes and restore older versions
- See who changed what, and why
- Work on features without breaking working code
- Collaborate with teammates without overwriting each other's work

## Essential Commands

Start tracking a project:

```bash
git init
```

Check which files changed:

```bash
git status
```

Stage a file, then save a commit:

```bash
git add index.html
git commit -m "Add homepage layout"
```

View history:

```bash
git log --oneline
```

## Basic Workflow

1. Edit your files.
2. Run `git status` to review changes.
3. Run `git add <file>` to stage them.
4. Run `git commit -m "message"` to save a snapshot.

> **Tip:** Write short, clear commit messages like "Fix login bug" so history stays readable.