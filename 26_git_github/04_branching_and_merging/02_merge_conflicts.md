# Merge Conflicts

## What Is a Merge Conflict?

A conflict happens when two branches change **the same lines** of the same file. Git cannot decide which version is correct, so it **pauses the merge** and asks you to choose.

```
        D  (feature: title = "Login Page")
       /
A --- B --- C  (main: title = "Welcome Page")
```

Both D and C edited the same line, so Git cannot combine them automatically.

## Why Do Conflicts Happen?

| Situation | Result |
|---|---|
| Different files changed | Auto-merged, no conflict |
| Same file, different lines | Auto-merged, no conflict |
| Same file, **same lines** | **Conflict** |

Conflicts are normal in team work. They are not errors.

## Conflict Markers

Git writes both versions into the file:

```
<<<<<<< HEAD
Welcome Page
=======
Login Page
>>>>>>> feature-login
```

| Marker | Meaning |
|---|---|
| `<<<<<<< HEAD` | Start: your current branch (main) |
| `=======` | Divider between the two versions |
| `>>>>>>> feature-login` | End: the incoming branch |

## Hands-On: Create and Resolve a Conflict

```bash
echo "Home" > title.txt
git add . && git commit -m "Add title"

git switch -c feature-login
echo "Login Page" > title.txt
git commit -am "Change title on feature"

git switch main
echo "Welcome Page" > title.txt
git commit -am "Change title on main"

git merge feature-login      # CONFLICT in title.txt
git status
```

Status shows:

```
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
	both modified:   title.txt
```

## Resolve in 4 Steps

1. Open `title.txt`.
2. Keep the correct text and **delete all three markers**:
```
   Login Page
```
3. Mark it resolved:
```bash
   git add title.txt
```
4. Finish the merge:
```bash
   git commit -m "Merge feature-login"
```

```
        D ----------.
       /             \
A --- B --- C ------- M  (main, merge commit)
```

## Cancel the Merge

Changed your mind? Return to the state before merging:

```bash
git merge --abort
```

## Key Points

- Conflicts only block the merge, so no work is lost.
- Run `git status` often to see which files need fixing.
- Never commit with markers (`<<<<<<<`) left in the file.
- Small, frequent merges mean fewer conflicts.