# Git Internals

Git helps you save versions of your project. This guide uses plain words and one simple idea: **sending a package**.

---

## 1. The Big Idea (Analogy)

| Git Area | Real-life Example | Plain Meaning |
|----------|-------------------|---------------|
| **Working tree** | Your desk | Where you work on your files |
| **Staging area** | The box on your desk | Where you put the changes you want to save |
| **Local repository** | Your filing cabinet | Where saved versions are kept on your computer |
| **Remote repository** | The post office / cloud | A copy online (GitHub) that others can see |

---

## 2. The Four Areas

### Working tree
The files you see and edit in your folder.

### Staging area (index)
A waiting room. You choose which changes go into the next save.

### Local repository
The hidden `.git/` folder. Every save (commit) lives here.

### Remote repository
A copy on a server like GitHub. Usually named `origin`.

---

## 3. Picture of the Flow

```
 Working Tree  --->  Staging Area  --->  Local Repo  --->  Remote Repo
  (your desk)        (the box)          (your cabinet)      (GitHub)

        git add            git commit            git push
```

Coming back:

```
 Remote Repo  --->  Local Repo  --->  Working Tree
              git fetch        git pull (fetch + merge)
```

---

## 4. The 4-Step Workflow

| Step | Action | Command | What happens |
|------|--------|---------|--------------|
| 1 | **Edit** | (use any editor) | You change a file |
| 2 | **Add** | `git add app.txt` | Change goes into the box |
| 3 | **Commit** | `git commit -m "message"` | Box is saved in your cabinet |
| 4 | **Push** | `git push origin main` | Cabinet is copied online |

Example:

```bash
echo "hello" >> app.txt          # 1. edit
git add app.txt                  # 2. add
git commit -m "Add greeting"     # 3. commit
git push origin main             # 4. push
```

---

## 5. Life of a File

```
 New file --add--> Staged --commit--> Saved
                                        |
                                      edit
                                        v
                                    Modified --add--> Staged
```

| State | Easy meaning |
|-------|--------------|
| **Untracked** | Git doesn't know this file yet |
| **Modified** | You changed it, not in the box yet |
| **Staged** | In the box, ready to save |
| **Committed** | Saved safely |

---

## 6. Common Commands

| I want to... | Command |
|--------------|---------|
| See what changed | `git status` |
| Put a file in the box | `git add <file>` |
| Take a file out of the box | `git restore --staged <file>` |
| Undo my edits | `git restore <file>` |
| Save the box | `git commit -m "msg"` |
| Upload my saves | `git push` |
| Download new saves (no merge) | `git fetch` |
| Download and merge | `git pull` |
| See history | `git log --oneline` |

---

## 7. What's Inside `.git/` (Simple)

| Item | What it is |
|------|------------|
| `objects/` | All your saved data |
| `index` | The staging area |
| `HEAD` | Says which branch you're on |
| `refs/` | Names (branches, tags) that point to commits |

---

## 8. Key Words

| Word | Simple definition |
|------|-------------------|
| **Commit** | A saved snapshot with a message |
| **Branch** | A named line of work |
| **HEAD** | "You are here" marker |
| **origin** | Default name of your online copy |
| **Hash** | A unique ID for each commit (like `a1b2c3d`) |

---

## Remember

- **Add** = choose what to save.
- **Commit** = save it on your computer.
- **Push** = share it online.
- Nothing is online until you **push**.