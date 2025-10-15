# Exercise 1.1 — Python Environment Setup (Windows)

**Student:** Sourav Das  
**Course:** Python for Web Developers  
**Date:** October 15, 2025  
**Python Version:** 3.14.0

## 📋 Overview

This exercise demonstrates proper Python environment setup using modern tools (`uv`) and best practices for Windows development. All mentor requirements and recommendations have been implemented.

## ✅ Completed Requirements

### 1. Python Installation
- **Version:** Python 3.14.0 (newer than required 3.8.7, taking advantage of latest features)
- **Verification:** `python --version`

### 2. Virtual Environments with `uv`
Created two isolated virtual environments using `uv` (10x faster than traditional pip):

- **cf-python-base** — Primary development environment
- **cf-python-copy** — Duplicate environment created from requirements.txt

**Why `uv`?**
- 10-100x faster package installation
- Better dependency resolution
- Modern Python tooling recommended by mentor

### 3. Package Installation
All packages installed within activated virtual environments:
- **ipython** 9.6.0 — Enhanced interactive Python shell
- **bcrypt** 5.0.0 — Password hashing library
- Plus 14 dependencies (see requirements.txt)

### 4. Requirements File
**Generated (NOT hardcoded)** using:
```powershell
uv pip freeze > requirements.txt
```

This ensures exact package versions are captured from the actual environment.

### 5. add.py Script
Clean, readable script that:
- Prompts user for two integers
- Stores values in variables `a` and `b`
- Adds them to variable `c`
- Prints the result

Follows mentor specifications exactly.

### 6. Testing
Simplified test file (as per mentor recommendation):
- Uses direct import instead of importlib
- Tests multiple scenarios
- Easy to understand and maintain

## 📁 Project Structure

```
Exercise 1.1/
├── screenshots/              # Organized screenshots folder
│   ├── step1_python_version.png
│   ├── step2_create_env.png
│   ├── step3_install_ipython.png
│   ├── step4_ipython_shell.png
│   ├── step5_export_requirements.png
│   └── step6_copy_env.png
├── add.py                   # Main script
├── test_run.py             # Simplified tests
├── requirements.txt        # Generated package list
├── learning_journal.md     # Learning documentation
└── README.md              # This file
```

## 🚀 How to Use

### Install `uv` (if not already installed)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Create Virtual Environment

```powershell
# Create environment
uv venv cf-python-base

# Activate it
.\cf-python-base\Scripts\Activate.ps1
```

### Install Packages

```powershell
# Install from requirements.txt
uv pip install -r requirements.txt

# Or install individually
uv pip install ipython bcrypt
```

### Run add.py

```powershell
python add.py
```

Enter two numbers when prompted, and it will display their sum.

### Run Tests

```powershell
python test_run.py
```

Should output: `All tests passed.`

### Launch IPython Shell

```powershell
ipython
```

Interactive Python shell with syntax highlighting and auto-completion.

## 📦 Installed Packages

From `requirements.txt` (generated with `uv pip freeze`):

```
asttokens==3.0.0
bcrypt==5.0.0
colorama==0.4.6
decorator==5.2.1
executing==2.2.1
ipython==9.6.0
ipython-pygments-lexers==1.1.1
jedi==0.19.2
matplotlib-inline==0.1.7
parso==0.8.5
prompt-toolkit==3.0.52
pure-eval==0.2.3
pygments==2.19.2
stack-data==0.6.3
traitlets==5.14.3
wcwidth==0.2.14
```

## 🎯 Steps Completed

### Step 1: Python Installation
Verified Python 3.14.0 installation:
```powershell
python --version
```
**Screenshot:** `screenshots/step1_python_version.png`

### Step 2: Create Virtual Environment
Created `cf-python-base` using uv:
```powershell
uv venv cf-python-base
.\cf-python-base\Scripts\Activate.ps1
```
**Screenshot:** `screenshots/step2_create_env.png`

### Step 3: Install IPython
Installed ipython within activated environment:
```powershell
uv pip install ipython
```
**Screenshot:** `screenshots/step3_install_ipython.png`

### Step 4: Test IPython Shell
Launched and tested IPython:
```powershell
ipython
```
**Screenshot:** `screenshots/step4_ipython_shell.png`

### Step 5: Export Requirements
Generated requirements.txt from activated environment:
```powershell
uv pip freeze > requirements.txt
```
**Screenshot:** `screenshots/step5_export_requirements.png`

### Step 6: Create Copy Environment
Created second environment from requirements:
```powershell
deactivate
uv venv cf-python-copy
.\cf-python-copy\Scripts\Activate.ps1
uv pip install -r requirements.txt
```
**Screenshot:** `screenshots/step6_copy_env.png`

## ✅ Mentor Requirements Addressed

### Required (All Completed)

- ✅ **Virtual environment set up correctly** using `uv` (10x faster than pip)
- ✅ **ipython installed within virtual environment** (cf-python-base was activated)
- ✅ **Requirements.txt generated, not hardcoded** (used `uv pip freeze`)

### Recommendations (All Implemented)

- ✅ **Screenshots organized** in separate `screenshots/` folder with clear naming
- ✅ **Test file simplified** — removed importlib, uses direct import
- ✅ **Structured submission** — clear folder organization and documentation

## 🔧 Command Reference

**Activate environment:**
```powershell
.\cf-python-base\Scripts\Activate.ps1
```

**Deactivate:**
```powershell
deactivate
```

**Install package:**
```powershell
uv pip install <package-name>
```

**List packages:**
```powershell
uv pip list
```

**Generate requirements:**
```powershell
uv pip freeze > requirements.txt
```

**Install from requirements:**
```powershell
uv pip install -r requirements.txt
```

## 📝 Key Learnings

1. **Virtual environments isolate dependencies** — Each project can have different package versions
2. **`uv` is significantly faster** — 10-100x speedup compared to traditional pip
3. **Generated requirements.txt ensures reproducibility** — Exact same packages install on any machine
4. **Always activate before installing** — Prevents polluting global Python installation
5. **Modern Python development uses tools like uv** — Faster and more reliable than older tools

## 🔍 Verification

Both virtual environments have identical packages (proof that requirements.txt works correctly):

```powershell
# In cf-python-base
.\cf-python-base\Scripts\Activate.ps1
uv pip list

# In cf-python-copy
deactivate
.\cf-python-copy\Scripts\Activate.ps1
uv pip list
```

Both show the same 16 packages with matching versions.

## 📚 Additional Resources

- [uv Documentation](https://github.com/astral-sh/uv)
- [IPython Documentation](https://ipython.readthedocs.io/)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [PowerShell Execution Policy](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies)

---

**Repository:** [python-web-development](https://github.com/souravdas090300/python-web-development)  
**Author:** Sourav Das  
**Exercise:** 1.1 - Python Environment Setup  
**Submission Date:** October 15, 2025
