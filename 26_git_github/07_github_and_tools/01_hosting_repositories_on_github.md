# Hosting Repositories on GitHub

## Git vs GitHub

- **Git**: a tool on your computer that tracks changes in your code.
- **GitHub**: a website that stores Git repositories online so you can back them up and share them.

```text
Your computer (Git)  <-- push / pull -->  GitHub (remote)
```

## 1. Create a GitHub Account

1. Go to [github.com](https://github.com) and click **Sign up**.
2. Enter your email, password, and username, then verify your email.
3. Tell Git who you are (once, in Git Bash or any terminal):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 2. Create a Repository on GitHub

1. Click **+** (top right) → **New repository**.
2. Enter a name, e.g. `my-project`.
3. Choose **Public** or **Private**.
4. For an existing local project, leave "Add a README" **unchecked**.
5. Click **Create repository** and copy the URL, e.g. `https://github.com/your-username/my-project.git`.

## 3. Connect Local to GitHub (Git Bash)

Open Git Bash in your project folder:

```bash
git init                      # skip if already a Git repo
git add .
git commit -m "Initial commit"

git remote add origin https://github.com/your-username/my-project.git
git remote -v                 # verify the link
git branch -M main            # rename current branch to main
git push -u origin main       # first upload; -u remembers origin/main
```

- `origin` is the nickname for your GitHub URL.
- `-u` lets you use plain `git push` and `git pull` afterward.

## 4. Connect Using VS Code

1. Open your project folder in VS Code.
2. Open the **Source Control** tab (`Ctrl+Shift+G`) → **Initialize Repository**.
3. Type a message, click **Commit**.
4. Click **Publish Branch** (or **Publish to GitHub**) and sign in to GitHub when prompted.
5. Or open the terminal (`` Ctrl+` ``) and run the Git Bash commands above.

## 5. Daily Workflow

```text
Working folder --add--> Staging --commit--> Local repo --push--> GitHub
Working folder <--------------------------- pull --------------- GitHub
                         Local repo <------ fetch ------------- GitHub
```

| Command | What it does |
|---|---|
| `git push` | Uploads your local commits to GitHub |
| `git fetch` | Downloads new commits but does **not** change your files |
| `git pull` | Fetch + merge: downloads and updates your files |

Example:

```bash
git pull                      # get the latest first
# ...edit files...
git add .
git commit -m "Add login page"
git push
```

Use `git fetch` when you want to look before merging; use `git pull` to update right away.

## Common Problems

- **Login/authentication fails**: use the browser sign-in popup or a Personal Access Token as your password (GitHub no longer accepts account passwords for Git).
- **`remote origin already exists`**: run `git remote set-url origin <URL>`.