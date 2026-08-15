

# Interfaces in Operating Systems

An **interface** is the way a user interacts with an operating system or computer.

The two major types of interfaces are:

1. **CLI — Command Line Interface**
2. **GUI — Graphical User Interface**

---

# 1. CLI — Command Line Interface

**CLI (Command Line Interface)** is an interface where the user interacts with the computer by typing commands.

Instead of clicking buttons and icons, the user types commands into a terminal.

### Example

```bash
ls

This command lists files and directories.

Other examples:

cd Desktop
mkdir projects
rm file.txt
Common CLI Environments
Bash
Zsh
PowerShell
Command Prompt
Linux Terminal
Advantages of CLI
Fast for experienced users
Powerful
Easy to automate
Useful for scripting
Excellent for server administration
Uses fewer graphical resources
Commonly used in Linux servers and cloud environments
2. GUI — Graphical User Interface

GUI (Graphical User Interface) allows users to interact with a computer using graphical elements.

These include:

Windows
Icons
Buttons
Menus
Mouse
Touch
File managers

Example

Instead of typing:

mkdir projects

you can create a folder by:

Right Click
    ↓
New Folder
    ↓
Enter Name
GUI Examples

Common GUI-based operating systems include:

Windows
macOS
Ubuntu Desktop
Linux Mint
Windows Interface

Windows generally prefers a GUI-based user experience.

As a Windows user, you will mainly work with the GUI-based interface for normal daily tasks.

For example:

Opening applications
Managing files
Browsing folders
Changing settings
Installing applications
Using web browsers
Managing the desktop

Windows also provides CLI tools such as:

PowerShell
Command Prompt
Windows Terminal

So Windows supports both GUI and CLI, but the GUI is the primary interface for most regular users.

Linux / Ubuntu Interface

Linux provides both GUI and CLI interfaces.

When using Ubuntu Desktop, a user can work with the graphical desktop for normal tasks and use the terminal when needed.

Ubuntu
  |
  ├── GUI
  │    ├── Applications
  │    ├── File Manager
  │    ├── Settings
  │    └── Desktop
  │
  └── CLI
       ├── Terminal
       ├── Bash
       ├── Commands
       └── Shell Scripts

Therefore, when I am using Ubuntu, I can use both GUI and CLI.

GUI vs CLI
Feature	GUI	CLI
Full Name	Graphical User Interface	Command Line Interface
Interaction	Graphics	Commands
Input	Mouse/keyboard/touch	Keyboard
Beginner Friendly	Usually easier	Requires learning commands
Automation	Limited	Excellent
Speed for repetitive tasks	Can be slower	Often faster
Resource Usage	Higher	Lower
File Management	Graphical file manager	Commands
Server Administration	Less common	Very common
Linux Usage	Common on desktop	Extremely important
Simple Example

Suppose we want to create a folder called projects.

GUI
Right Click
     ↓
New Folder
     ↓
projects
CLI
mkdir projects

Both methods perform the same basic task, but they use different interfaces.

Windows vs Ubuntu
Windows
Windows
   |
   ├── GUI ⭐ Main interface for most users
   |
   └── CLI
        ├── PowerShell
        ├── Command Prompt
        └── Windows Terminal

Windows users will mainly work with the GUI-based interface for everyday computer usage.

Ubuntu
Ubuntu
   |
   ├── GUI
   |    ├── Desktop
   |    ├── Applications
   |    └── File Manager
   |
   └── CLI ⭐ Very important
        ├── Terminal
        ├── Bash
        ├── Commands
        └── Scripts

Ubuntu users can work with both GUI and CLI.

For Linux development, learning the CLI/terminal is especially important.

Why CLI Is Important for Linux

Many Linux servers do not have a graphical desktop environment.

For example:

Cloud Server
     |
     └── Linux
          |
          └── Terminal / SSH

A developer can connect to the server through SSH and manage it using commands.

Example:

ssh user@server

After connecting, the developer can use commands such as:

ls
cd
mkdir
rm
cp
mv
sudo
apt
systemctl

My Learning Setup

I am using Windows as my main operating system and Ubuntu through WSL to learn Linux.

My workflow can therefore use both interfaces:

Windows
   |
   ├── GUI
   |    └── Normal Windows usage
   |
   └── WSL
        |
        └── Ubuntu
             |
             ├── CLI ⭐
             |    └── Linux Terminal / Bash
             |
             └── GUI
                  └── Available with appropriate Ubuntu desktop setup

For my Linux learning, I will mainly practice the CLI/terminal, because understanding the command line is an important part of working with Linux.

Quick Summary
GUI
↓
Interact using graphics, windows, icons, menus, and mouse.


CLI
↓
Interact by typing commands.


Windows
↓
Supports both GUI and CLI.
GUI is the primary interface for most everyday users.


Ubuntu/Linux
↓
Supports both GUI and CLI.
CLI is especially important for developers, servers, and system administration.

Key Point: Windows generally provides a GUI-first user experience, while Linux/Ubuntu gives users strong access to both GUI and CLI, with the CLI being especially important in development and server environments.