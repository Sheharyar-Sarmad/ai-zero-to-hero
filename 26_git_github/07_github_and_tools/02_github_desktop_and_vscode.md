# GitHub Desktop and VS Code

Both tools give you a visual interface for Git. Install [GitHub Desktop](https://desktop.github.com) and [VS Code](https://code.visualstudio.com), then sign in to GitHub in each.

```text
Edit files -> Review changes -> Stage -> Commit -> Push
     ^                                              |
     +---------------- Pull <-----------------------+
```

## Operations Compared

| Task | GitHub Desktop | VS Code (Source Control, `Ctrl+Shift+G`) | Terminal |
|---|---|---|---|
| Clone | File → Clone repository | Command Palette → **Git: Clone** | `git clone <URL>` |
| Review changes | **Changes** tab | Click a file under Changes (diff view) | `git status` / `git diff` |
| Stage | Tick the checkbox | Click **+** on a file | `git add <file>` |
| Commit | Message → **Commit to main** | Message → **Commit** | `git commit -m "msg"` |
| Switch branch | **Current Branch** menu | Click branch name (bottom-left) | `git switch <branch>` |
| New branch | Current Branch → **New Branch** | Branch name → **Create new branch** | `git switch -c <branch>` |
| Pull | **Fetch/Pull origin** | **Sync Changes** or `...` → Pull | `git pull` |
| Push | **Push origin** | **Sync Changes** or `...` → Push | `git push` |

## Resolving Conflicts

A conflict happens when two people edit the same lines. Git marks the file:

```text
<<<<<<< HEAD
your version
=======
their version
>>>>>>> branch-name
```

1. Open the conflicted file (GitHub Desktop: **Open in Visual Studio Code**).
2. In VS Code, click **Accept Current**, **Accept Incoming**, or **Accept Both**, or edit the text manually.
3. Make sure all `<<<`, `===`, `>>>` markers are gone.
4. Stage the file and commit.

```bash
git add <file>
git commit -m "Resolve merge conflict"
```

## Practical Workflow

```bash
git clone https://github.com/user/repo.git
git switch -c feature-login
# edit files, review in the GUI
git add .
git commit -m "Add login form"
git push -u origin feature-login
```

**Tip:** Pull before you start working to reduce conflicts.