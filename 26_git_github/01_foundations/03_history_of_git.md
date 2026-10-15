# History of Git

## Why Git Was Created

In 2005, the Linux kernel team lost free access to **BitKeeper**, the proprietary version control tool they relied on. Linus Torvalds started Git in April 2005 as a replacement, and the first version came together in just a few weeks.

## The Problem

Existing tools (CVS, Subversion) were centralized and slow for a project as large as the kernel. Developers needed fast, offline-friendly, distributed work.

## Design Goals

- **Speed**: most operations run locally
- **Distributed**: every clone holds full history
- **Data integrity**: content is checksummed (SHA-1, later SHA-256 support)
- **Non-linear development**: cheap branching and merging
- **Scales** to thousands of contributors

## Practical Workflow

Every clone is a complete repository:

```bash
git clone https://github.com/torvalds/linux.git
cd linux
git log --oneline -5
```

Branching is fast and local:

```bash
git switch -c fix-typo
git add .
git commit -m "Fix typo"
git switch main
git merge fix-typo
```

## Key Takeaway

Git was built for speed, safety, and distributed collaboration.