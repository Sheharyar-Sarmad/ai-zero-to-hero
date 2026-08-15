

## Linux Users, Root, Sudo & Services

## Users

A user is an account that interacts with the Linux system.

whoami

Shows the current user.

id

Shows UID, GID, and groups.

groups

Shows groups the current user belongs to.

## Root User

root is the superuser with almost unrestricted system permissions.

UID = 0

## Root can:

Modify system files
Install software
Manage users
Manage services
Change permissions

Check root:

sudo whoami

## Output:

root

## Normal User vs Root

Normal User	Root
Limited permissions	Almost full permissions
UID usually 1000+	UID 0
Prompt usually $	Prompt usually #
Uses sudo when needed	Already has privileges

## sudo

sudo runs a command with elevated privileges.

sudo command

## Example:

sudo apt update

## Check:

sudo whoami

Output:

root

su

su means switch user.

su username

Switch to root:

su -

## sudo su

sudo su

Opens a root shell.

Better alternative:

sudo -i

Exit root:

exit

## Creating Users

sudo adduser username

Example:

sudo adduser ali

## Delete:

sudo deluser ali

## Groups

Groups allow multiple users to share permissions.

groups

## Add user to a group:

sudo usermod -aG group username

## Example:

sudo usermod -aG sudo ali

## Services

A service is a background program that provides a system function.

## Examples:

SSH
Docker
Web servers
Databases

Ubuntu commonly uses systemd to manage services.

## Check:

systemctl status SERVICE

## Start:

sudo systemctl start SERVICE

## Stop:

sudo systemctl stop SERVICE

## Restart:

sudo systemctl restart SERVICE

## Enable at boot:

sudo systemctl enable SERVICE

## Disable at boot:

sudo systemctl disable SERVICE

##  Important Commands

whoami
id
groups
sudo command
su -
sudo -i
exit
adduser
deluser
usermod
systemctl

## Key Concept

Normal User
     ↓
   sudo
     ↓
Root Privileges
     ↓
System Management
     ↓
Users + Permissions + Services

## Remember:

$ → normal user
# → root
/ → root directory
root → superuser
sudo → temporarily elevated command
systemctl → service management