
## Linux Filesystem

Linux uses a hierarchical/tree-based filesystem that starts at /.

/
├── bin
├── boot
├── dev
├── etc
├── home
│   └── user
├── mnt
├── opt
├── root
├── tmp
├── usr
└── var

/ → root of the entire filesystem

/home/user → user's home directory

~ → current user's home directory

## Important Path Symbols

Symbol	Meaning
/	Root directory
.	Current directory
..	Parent directory
~	Home directory

## Examples:

cd /
cd ..
cd .
cd ~
3. Navigation
pwd — Current Directory
pwd

Shows the current working directory.

ls — List Files
ls
ls -l      # detailed information
ls -a      # hidden files
ls -la     # detailed + hidden
cd — Change Directory
cd Documents
cd ..
cd /
cd ~

## Create Directories and Files

mkdir — Create Directory
mkdir projects
mkdir projects documents images
touch — Create Empty File
touch file.txt
touch 1.txt 2.txt 3.txt
5. Remove Files and Directories
rm — Remove File
rm file.txt

rm normally does not send files to a recycle bin.

rmdir — Remove Empty Directory
rmdir projects

Only works when the directory is empty.

## Move and Rename

mv — Move or Rename

Rename:

mv file.txt 1.txt

Move:

mv file.txt documents/

Move + rename:

mv file.txt documents/important.txt
7. Copy
cp — Copy Files
cp 2.txt documents/

The original remains unchanged.

Copy and rename:

cp 2.txt documents/copy.txt
8. View File Contents
cat
cat file.txt

Displays the entire file.

less
less file.txt

Read large files page by page.

Press q to exit.

head
head file.txt
head -n 5 file.txt

Shows the beginning of a file.

tail
tail file.txt
tail -n 5 file.txt

Shows the end of a file.

## Search and Identify

find

Find files/directories:

find . -name "file.txt"
find . -name "*.txt"

. means current directory.

file

Identifies the file type:

file file.txt
tree

Shows the directory structure:

tree

Install on Ubuntu:

sudo apt install tree

## Absolute vs Relative Paths

Absolute Path

Starts from /:

/home/sheharyar/Documents/file.txt
Relative Path

Starts from the current directory:

Documents/file.txt

If you're currently in:

/home/sheharyar

then:

Documents/file.txt

means:

/home/sheharyar/Documents/file.txt

## Quick Practice

mkdir linux-practice
cd linux-practice


touch 1.txt 2.txt 3.txt
mkdir backup


mv 1.txt backup/
cp 2.txt backup/
mv 3.txt notes.txt


tree
rm notes.txt

Final structure before removing notes.txt:

linux-practice/
├── 2.txt
├── backup/
│   ├── 1.txt
│   └── 2.txt
└── notes.txt

## Command Cheat Sheet

## Command	Purpose
   pwd	    Show current directory
   ls	    List files
   cd	    Change directory
   cd ..	Go to parent
   cd /	    Go to root
   cd ~	    Go home
   mkdir	Create directory
   rmdir	Remove empty directory
   touch	Create file
   mv	    Move/rename
   cp	    Copy
   rm	    Remove file
   cat	    Display file
   less	    Read file
   head	    Show beginning
   tail	    Show end
   find	    Search files
   file	    Identify file type
   tree	    Show directory tree

## ⭐ Learn These First

pwd
ls
cd
cd ..
mkdir
rmdir
touch
mv
cp
rm

These are the core Linux file-management commands.