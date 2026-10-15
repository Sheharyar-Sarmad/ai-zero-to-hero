# Centralized vs Distributed Version Control Systems

## 1. What Is Version Control?

**Version control** is a system that records changes to files over time so you can recall specific versions, compare changes, and collaborate without overwriting each other's work.

A **repository** (repo) stores the files plus their complete change history. The main difference between VCS types is **where the repository lives** and **who has a copy of it**.

---

## 2. Centralized VCS (CVCS)

### Definition
A Centralized VCS keeps **one single repository on a central server**. Developers check out files from it and commit changes back to it. Clients hold only a working copy, not the history.

### Theory
- The server is the **single source of truth**.
- Every history operation (log, diff, blame, commit) needs a network connection to the server.
- Access control is simple: the admin controls who can read or write.
- If the server fails and there is no backup, the history can be lost.

### Examples
Subversion (SVN), Perforce, CVS

```bash
svn checkout https://example.com/repo
svn update                    # get latest changes
svn commit -m "Fix login bug" # goes directly to server
```

---

## 3. Distributed VCS (DVCS)

### Definition
A Distributed VCS gives **every developer a full copy of the repository**, including the complete history. A server (such as GitHub) is only a convenient place to share work.

### Theory
- Each clone is a **complete backup** of the project.
- Committing, branching, merging, and viewing history are **local operations**: fast and available offline.
- Sharing is a separate step: you **push** your commits and **pull** others'.
- No single point of failure; any clone can restore the project.

### Examples
Git, Mercurial

```bash
git clone https://example.com/repo.git
git add .
git commit -m "Fix login bug"  # saved locally only
git push origin main           # shared with the remote
```

---

## 4. Key Concepts Compared

### Server Dependency
- **CVCS:** Needed for almost every action. Server down means work stops.
- **DVCS:** Needed only to share (push/pull). Server down means you keep working.

### Local History
- **CVCS:** Not stored locally. Only the latest snapshot is on your machine.
- **DVCS:** The entire history is stored locally.

### Collaboration
- **CVCS:** Everyone commits to the same central line. Simple, but conflicts appear at commit time.
- **DVCS:** Everyone works independently, then merges. Supports many workflows (feature branches, pull requests, forks).

---

## 5. Comparison Table

| Feature         | Centralized (SVN)        | Distributed (Git)         |
|-----------------|--------------------------|---------------------------|
| Repository      | One on the server        | Full copy on every clone  |
| History access  | Needs network            | Local and instant         |
| Offline work    | Very limited             | Almost everything         |
| Commit          | Goes straight to server  | Local, then push          |
| Speed           | Network-bound            | Mostly local, fast        |
| Backup          | Single point of failure  | Every clone is a backup   |
| Branching       | Heavier, more rigid      | Lightweight and cheap     |
| Learning curve  | Easier                   | Steeper                   |
| Examples        | SVN, Perforce, CVS       | Git, Mercurial            |

---

## 6. Practical Workflows

**CVCS daily flow**
```bash
svn update
# edit files
svn commit -m "Add feature"
```

**DVCS daily flow**
```bash
git pull origin main
git switch -c feature/login
# edit files
git add .
git commit -m "Add login form"
git push -u origin feature/login
```

---

## 7. Summary

| Choose      | When                                                         |
|-------------|--------------------------------------------------------------|
| **CVCS**    | You need strict central control or work with very large binary assets (e.g., Perforce in game studios). |
| **DVCS**    | You want speed, offline work, flexible branching, and resilience. Git is the industry standard. |