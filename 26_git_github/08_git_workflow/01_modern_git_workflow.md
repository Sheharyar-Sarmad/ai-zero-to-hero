# Modern Git Workflow

Never commit directly to `main`. Do your work on a short-lived **feature branch**, then merge it through a **pull request (PR)** on GitHub. This keeps `main` stable and gives teammates a chance to review.

```text
main      o---------------------o------o  (merge)
           \                   /
feature     o---o---o---o-----+         (small commits, then PR)
```

## The Steps

1. **Update main** so you start from the latest code.
2. **Create a branch** named for the task.
3. **Commit small and often**, one logical change per commit.
4. **Push** the branch to GitHub.
5. **Open a PR** (GitHub shows a **Compare & pull request** button).
6. **Review**: teammates comment; you push fixes to the same branch.
7. **Merge** the PR (**Merge pull request**).
8. **Clean up**: delete the branch and update local `main`.

## Compact Command Sequence

```bash
git switch main
git pull
git switch -c feature-login

git add .
git commit -m "Add login form"
git add .
git commit -m "Validate email input"

git push -u origin feature-login
# Open the PR on GitHub, get review, click Merge

git switch main
git pull
git branch -d feature-login            # delete local branch
git push origin --delete feature-login # delete remote branch
```

GitHub also offers a **Delete branch** button after merging, which handles the remote branch for you.

## Good Commit Messages

- Short and specific: `Fix navbar overflow`
- Present tense: `Add`, `Fix`, `Update`

## Checklist

- [ ] `main` is up to date
- [ ] Working on a feature branch
- [ ] Commits are small with clear messages
- [ ] Branch pushed to GitHub
- [ ] PR has a clear title and description
- [ ] Review feedback addressed
- [ ] PR merged
- [ ] Branch deleted locally and on GitHub
- [ ] Local `main` pulled