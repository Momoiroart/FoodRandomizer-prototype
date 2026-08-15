# 🍔 Food Randomizer & 🎓 Git Learning Lab

Welcome to the **Food Randomizer** project! This repository is designed as both a **fully functional Python food recommendation application** and an **interactive, highly visual teaching resource** for mastering Git in real-world software projects.

---

## 🗺️ The Git Journey: From Sandbox to Repository

Before diving into the code, let's visualize how Git manages your files. Understanding Git's internal areas is the secret to never losing code.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        GIT THREE-STAGE ARCHITECTURE                    │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  📁 Working Directory      📝 Staging Area          🗄️ Local Repository │
│   [Unstaged Changes]       [Prepared Changes]       [Committed History]│
│                                                                        │
│     ┌───────────┐            ┌───────────┐             ┌───────────┐   │
│     │  main.py  │ ─────────> │  main.py  │ ──────────> │  main.py  │   │
│     └───────────┘            └───────────┘             └───────────┘   │
│           │                        ▲                         │         │
│           │     git add <file>     │         git commit      │         │
│           └────────────────────────┘                         │         │
│                                                              │         │
│           ▲                                                  │         │
│           └──────────────────────────────────────────────────┘         │
│                                 git checkout                           │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Interactive Git Cheat Sheet & Tutorial

Here is the exact progression of Git commands you will use in this project, complete with visual explanations and code snippets.

### 1️⃣ Initializing the Sandbox
Before Git can track anything, you must initialize a repository. This creates a hidden `.git` folder that tracks every change.

```bash
git init
```
*💡 **Visual Analogy:** This is like turning on the security cameras in your office building. From this moment on, every entry and exit is logged.*

---

### 2️⃣ Checking the Project Pulse
To see what files Git is aware of, which ones have changed, and what is ready to be committed, use `status`.

```bash
git status
```
*💡 **Pro-Tip:** Run `git status` constantly. It is your ultimate compass and safety net.*

---

### 3️⃣ Preparing Files for Commit (Staging)
When you modify a file, it sits in your **Working Directory**. To tell Git "I want to include this file in my next snapshot," you must add it to the **Staging Area**.

```bash
# Stage a specific file
git add logic.py

# Stage all files in the current folder
git add .
```

---

### 4️⃣ Creating a Permanent Snapshot (Committing)
A commit is a permanent, cryptographic snapshot of your project at a specific moment in time. 

```bash
# Open an editor to write a detailed, multi-line commit message
git commit

# Quick commit with a short inline message (Best practice for small changes)
git commit -m "Add core randomizing logic to logic.py"
```

---

### 5️⃣ The Fast-Track: Bypassing the Staging Area
If you are modifying files that Git **already tracks**, you can stage and commit them in a single command using the `-a` (all) and `-m` (message) flags combined.

```bash
git commit -a -m "Fix logic bug in main recommendation loop"
```
> ⚠️ **Warning:** This will **not** stage new, untracked files. It only works for files that have been committed at least once before.

---

### 6️⃣ Reading the Project's History
To view the timeline of your project, read the commit messages, and trace back who did what and when.

```bash
# View full details (hashes, authors, dates, and full messages)
git log

# View a clean, single-line representation of history
git log --oneline
```

---

## 🍲 About the Food Randomizer Application

The application itself is a smart CLI tool to solve the age-old question: **"What should I eat today?"**

### 📦 Project Structure
- ⚙️ `logic.py` — The core logic module containing the `FoodRecommender` class.
- 🗃️ `food_database.json` — A structured JSON file holding categorized menu items (Japanese, Thai, Western).
- 🎮 `main.py` — The user-facing application entry point (designed for interactive CLI choices).
- 🛡️ `.gitignore` — Instructs Git to ignore sensitive and temporary files (e.g., `.env` files).

### 🛠️ Quick Start & Usage
1. Make sure you have **Python 3.x** installed.
2. Clone or download this repository.
3. Run the interactive CLI:
   ```bash
   python main.py
   ```

---

## 🎓 Next Steps in Your Learning
To see a live reconstruction of how this actual project was built step-by-step using these Git commands, open the **[Git Teaching Guide](./git_teaching_guide.md)** inside this directory!
