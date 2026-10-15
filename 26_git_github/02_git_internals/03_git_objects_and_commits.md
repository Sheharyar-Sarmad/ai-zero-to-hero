# Git Objects and Commits

Git is a content-addressed store: every object is named by a hash of its content.

## The Four Building Blocks

| Object | Simple meaning | Stores |
|--------|----------------|--------|
| **Blob** | A file's contents | Data only, no filename |
| **Tree** | A folder | Names pointing to blobs and other trees |
| **Commit** | A saved snapshot | Root tree, parent, author, message |
| **Reference** | A readable name | Pointer to a commit (branch, tag, `HEAD`) |

## Diagram

```
 HEAD --> main (ref)
            |
            v
         Commit C3 ---parent---> Commit C2 ---parent---> Commit C1
            |
            v
         Tree (root)
          /      \
     Blob          Tree (src/)
   README.md          |
                    Blob
                    app.py
```

## Commit Hashes

- A hash (e.g. `a1b2c3d`) is a unique ID computed from the commit's content.
- Change anything (file, message, parent) and the hash changes.
- This makes history tamper-evident.

## Parent Commits

- Each commit points to its parent, forming a chain.
- The first commit has no parent; a merge commit has two.
- A branch is just a ref to the newest commit in a chain.

```
 C1 <-- C2 <-- C3 <-- C4     (main)
                \
                 C5 <-- C6   (feature)
```

## Examples

```bash
git log --oneline                # short history
git log --graph --oneline --all  # draw branches
git cat-file -t HEAD             # type: commit
git cat-file -p HEAD             # show commit: tree, parent, author
git cat-file -p HEAD^{tree}      # show root tree entries
git cat-file -p <blob-hash>      # show file contents
git rev-parse HEAD               # full hash of HEAD
```

## Key Points

- Same content gives the same blob hash.
- Commits are immutable; "editing" creates a new commit.
- Branches and tags are cheap: just names for hashes.