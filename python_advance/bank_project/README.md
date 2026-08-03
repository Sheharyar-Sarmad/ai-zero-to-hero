# 🏦 Secure Banking Logic System

A robust, console-based banking application built with Python. It features end-to-end encrypted PIN storage, complete transaction management, and persistent data storage using JSON.

## ✨ Key Features

- **🔐 Secure Authentication:** PINs are **hashed using SHA-256 with salt** before storage (never stored in plain text).
- **💳 Full Account Management:** Create, update, view, and permanently delete accounts.
- **💰 Core Banking Operations:** Deposit, withdraw, and transfer funds between accounts.
- **📊 Transaction History:** Automatically logs every deposit, withdrawal, and transfer with timestamps and IDs.
- **🔍 Account Searching:** Find other users by name or account number.
- **📁 Data Persistence:** All data is saved automatically to a `data.json` file for seamless restarts.
- **🛡️ Input Validation:** Robust validation for names, ages, emails, PINs, and monetary amounts.
- **⏱️ Session Management:** Auto-logout after 5 minutes of inactivity for enhanced security.
- **⚔️ Rate Limiting:** Prevents brute-force attacks with a limit on failed login attempts.

## 🛠️ Installation & Usage

1. **Make sure you have Python 3.6+ installed.**

2. **Clone the repository** (or download the files):
   ```bash
   git clone https://github.com/Sheharyar-Sarmad/Banking-Logic.git
