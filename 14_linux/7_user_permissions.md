

# Linux User Permissions

---

## 1. Permission Types

Linux has 3 basic permissions:

- `r` → Read
- `w` → Write
- `x` → Execute

---

## Permission Groups

Permissions apply to:

- `u` → User/Owner
- `g` → Group
- `o` → Others

Example:

-rwxr-xr--

Breakdown:

Owner  → rwx
Group  → r-x
Others → r--
3. File Permissions
Permission	Meaning
r	Read file
w	Modify file
x	Execute file
4. Directory Permissions
Permission	Meaning
r	List contents
w	Create/delete files
x	Enter/access directory
5. Check Permissions
ls -l

Example:

-rwxr-xr-- 1 sheharyar developers 1200 app.sh

## chmod

chmod changes file or directory permissions.

Numeric Method
chmod 755 script.sh

Permission values:

r = 4
w = 2
x = 1

Therefore:

7 = rwx
6 = rw-
5 = r-x
4 = r--
0 = ---

Example:

chmod 755 script.sh

Means:

Owner  → rwx
Group  → r-x
Others → r-x
Common Permissions
755 → rwxr-xr-x
644 → rw-r--r--
600 → rw-------
7. Symbolic chmod
chmod +x script.sh
chmod -x script.sh
chmod u+w file.txt
chmod g-w file.txt
chmod o+r file.txt
u → User
g → Group
o → Others
a → All
8. chown

Change file owner:

sudo chown user file.txt

Change owner and group:

sudo chown user:group file.txt

Recursive:

sudo chown -R user:group project/

## chgrp

Change group ownership:

sudo chgrp developers file.txt

## sudo

Run a command with elevated/root privileges:

sudo command

Example:

sudo chown root file.txt
## Check User and Groups

whoami - Shows current user.

id - Shows UID, GID, and groups.

groups - Shows groups of the current user.

## Important Commands

ls -l                  # Check permissions
chmod 755 file         # Change permissions
chmod +x script.sh     # Add execute permission
chown user file        # Change owner
chown user:group file  # Change owner and group
chgrp group file       # Change group
id                     # Show user/group information
groups                 # Show user's groups
sudo command           # Run with elevated privileges
Key Concept
                Permissions
                     |
          +----------+----------+
          |          |          |
        User       Group      Others
          |          |          |
         rwx        rwx        rwx

Rule: Give users only the permissions they need. Avoid unnecessary 777 permissions.