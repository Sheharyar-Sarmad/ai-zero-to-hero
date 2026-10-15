# Git vs GitHub

- **Git**: a version control tool that runs on your computer and tracks file changes.
- **GitHub**: a website that hosts Git repositories online for backup and collaboration.
- **Local repository**: lives on your machine. You `commit` here.
- **Remote repository**: lives on a server (e.g. GitHub). You `push` here.

Flow: edit files → stage → commit locally → push to remote.

## Tables

| | Git | GitHub |
|---|---|---|
| Type | Software tool | Online service |
| Runs | Locally | In the cloud |
| Purpose | Track history | Share and collaborate |

| | Local repo | Remote repo |
|---|---|---|
| Location | Your computer | GitHub server |
| Updated by | `git commit` | `git push` |

## Minimal Workflow

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/user/repo.git
git push -u origin main
```

## Line by Line

- `git init`: creates a local repository. `init` = initialize.
- `git add .`: stages changes. `add` = stage files; `.` = everything in the current folder.
- `git commit -m "Initial commit"`: saves a snapshot. `commit` = snapshot; `-m` = message follows.
- `git remote add origin <URL>`: links a remote. `remote` = manage remotes; `add` = register one; `origin` = default nickname; `<URL>` = repo address.
- `git push -u origin main`: uploads commits. `push` = upload; `-u` = remember this target; `origin` = the remote; `main` = the branch.