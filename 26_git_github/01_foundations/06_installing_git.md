# Installing Git

Git is a **distributed version control system**. It saves project history as snapshots (commits), so you can review changes, undo mistakes, and collaborate. Every clone contains the full history, so most work happens offline. Each commit records an author, so Git needs your name and email.

## Install

**Windows**
```powershell
winget install --id Git.Git -e
```
Or download the installer from git-scm.com. It includes Git Bash.

**macOS**
```bash
brew install git
# or: xcode-select --install
```

**Linux**
```bash
sudo apt install git   # Debian/Ubuntu
sudo dnf install git   # Fedora
```

## Verify
```bash
git --version
```

## Initial Configuration (once per machine)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --list
```
- `--global` saves to `~/.gitconfig` (all repos).
- Levels: system → global → local. Local (per repo) overrides global.
- Use the email linked to your GitHub account.

## Workflow Example
```bash
mkdir demo && cd demo
git init
git config user.email "work@company.com"   # local override
git config --list --show-origin            # see where each value comes from
```