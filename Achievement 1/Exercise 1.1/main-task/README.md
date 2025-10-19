# Exercise 1.1 — Python Environment Setup (Windows)

**Student:** Sourav Das  
**Course:** Python for Web Developers  
**Achievement:** 1 - CLI Recipe App  
**Date:** October 14-16, 2025  
**Python Version:** 3.14.0  
**Time Investment:** 8 hours

---

## � Exercise Overview

This exercise introduces **Python for backend web development**, focusing on proper environment setup, virtual environments, package management, and the IPython REPL. The exercise demonstrates the modern **pure `uv` workflow** (10-100x faster than pip) and establishes foundational skills for managing Python projects professionally.

**Key Topics:**
- Python installation and verification
- Virtual environments for dependency isolation
- Package management with `uv` (modern alternative to pip)
- Interactive Python with IPython REPL
- Dependency tracking with `pyproject.toml` (modern alternative to requirements.txt)
- Creating and testing simple Python scripts

All mentor requirements and recommendations have been implemented.

---

## ✅ Completed Requirements

### 1. Python Installation
- **Version:** Python 3.14.0 (newer than required 3.8.7)
- **Verification:** `python --version`
- **Platform:** Windows with PowerShell

### 2. Virtual Environments with Pure `uv` Workflow
Created isolated virtual environments using **pure `uv`** (10x faster than traditional pip):

- **cf-python-base** — Primary development environment
- **cf-python-copy** — Duplicate environment created from pyproject.toml
- **.venv** — Default uv environment (auto-created by `uv add`)

**Why Pure `uv`?**
- 10-100x faster package installation
- Better dependency resolution
- **No need to activate environments** - uv auto-detects
- Modern Python tooling recommended by mentor
- Uses `pyproject.toml` instead of `requirements.txt`

### 3. Package Installation with `uv add`
All packages installed using **`uv add`** (not `uv pip install`):
- **ipython** 9.6.0 — Enhanced interactive Python shell
- **bcrypt** 5.0.0 — Password hashing library
- Plus 14 dependencies (auto-resolved)

**Key Difference:**
- ❌ Old way: `uv pip install ipython` (hybrid approach)
- ✅ New way: `uv add ipython` (pure uv workflow)

### 4. Dependency Management with `pyproject.toml`
**Modern dependency tracking** using `pyproject.toml`:
```toml
[project]
name = "exercise-1-1"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [
    "bcrypt>=5.0.0",
    "ipython>=9.6.0",
]
```

**Benefits over `requirements.txt`:**
- More informative (project metadata included)
- Industry standard for Python projects
- Auto-updated by `uv add` commands
- No need to manually `pip freeze`

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

---

## 📁 Project Structure

```
Exercise 1.1/
├── main-task/
│   ├── .venv/                   # Default uv virtual environment
│   ├── cf-python-base/          # Named virtual environment
│   ├── cf-python-copy/          # Copy environment
│   ├── add.py                   # Main script (addition calculator)
│   ├── test_run.py              # Simplified tests
│   ├── pyproject.toml           # Modern dependency file
│   ├── uv.lock                  # Lock file for reproducible builds
│   ├── learning_journal.md      # Technical learning documentation
│   ├── learning_journey.md      # Personal growth narrative
│   ├── requirements.txt         # Legacy file (kept for reference)
│   └── README.md                # This file
├── screenshots/                 # Organized screenshots folder
│   ├── step1_python_version.png
│   ├── step2_uv_init.png
│   ├── step3_uv_add_ipython.png
│   ├── step4_ipython_shell.png
│   ├── step5_pyproject_toml.png
│   └── step6_copy_env.png
└── practice-tasks/              # Practice task solutions
    ├── practice1_*.py
    ├── practice2_*.py
    └── practice3_*.py
```

---

## 🚀 How to Use

### Install `uv` (if not already installed)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Pure `uv` Workflow (Recommended)

```powershell
# Step 1: Initialize project
uv init --bare

# Step 2: Create first virtual environment
uv venv cf-python-base

# Step 3: Activate and add packages
.\cf-python-base\Scripts\Activate.ps1
uv add ipython
uv add bcrypt

# Step 4: Create second environment
deactivate
uv venv cf-python-copy

# Step 5: Activate and install from pyproject.toml
.\cf-python-copy\Scripts\Activate.ps1
uv pip install -r pyproject.toml

# No need to pip freeze - pyproject.toml auto-updates!
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

---

## 📦 Installed Packages

From `pyproject.toml` (auto-updated with `uv add`):

**Direct Dependencies:**
```toml
dependencies = [
    "bcrypt>=5.0.0",
    "ipython>=9.6.0",
]
```

**All Packages (including transitive dependencies):**
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

---

## 🎯 Steps Completed

### Step 1: Python Installation
Verified Python 3.14.0 installation:
```powershell
python --version
```

### Step 2: Initialize Project with uv
Created pyproject.toml using pure uv:
```powershell
uv init --bare
```

### Step 3: Create Environment and Add Packages
Created `cf-python-base` and installed ipython with `uv add`:
```powershell
uv venv cf-python-base
.\cf-python-base\Scripts\Activate.ps1
uv add ipython
uv add bcrypt
```

### Step 4: Test IPython Shell
Launched and tested IPython:
```powershell
ipython
```

### Step 5: View pyproject.toml
Verified dependency tracking in pyproject.toml:
```powershell
cat pyproject.toml
```

### Step 6: Create Copy Environment
Created second environment and installed from pyproject.toml:
```powershell
deactivate
uv venv cf-python-copy
.\cf-python-copy\Scripts\Activate.ps1
uv pip install -r pyproject.toml
```

---

## ✅ Mentor Requirements Addressed

### Required (All Completed)

- ✅ **Virtual environment set up correctly** using pure `uv` workflow
- ✅ **ipython installed using `uv add`** (modern approach, not `uv pip install`)
- ✅ **Learning journal completed** with comprehensive reflections
- ✅ **pyproject.toml created** (replaces requirements.txt)

### Recommendations (All Implemented)

- ✅ **Pure `uv` workflow** — Using `uv init`, `uv add` instead of `uv pip`
- ✅ **pyproject.toml for dependency management** — More informative than requirements.txt
- ✅ **No manual pip freeze needed** — Dependencies auto-tracked
- ✅ **Screenshots organized** in separate `screenshots/` folder with clear naming
- ✅ **Test file simplified** — removed importlib, uses direct import
- ✅ **Structured submission** — clear folder organization and documentation

---

## � Screenshots Checklist

### Required Screenshots (6 Steps)

- [x] **Step 1:** Python version verification (`python --version` showing 3.14.0)
- [x] **Step 2:** Project initialization with `uv init --bare` and pyproject.toml creation
- [x] **Step 3:** Installing ipython with `uv add ipython` (showing auto-dependency tracking)
- [x] **Step 4:** IPython shell running with syntax highlighting
- [x] **Step 5:** Contents of pyproject.toml showing dependencies
- [x] **Step 6:** Second environment created and packages verified

### Additional Documentation Screenshots

- [x] `uv.lock` file showing locked dependencies
- [x] `add.py` script code
- [x] Running `python add.py` with example input/output
- [x] Running `python test_run.py` showing tests passing
- [x] Directory structure showing both virtual environments

---

## �🔧 Command Reference

### Pure uv Commands (Recommended)

**Initialize project:**
```powershell
uv init --bare
```

**Create virtual environment:**
```powershell
uv venv <env-name>
```

**Add package (auto-updates pyproject.toml):**
```powershell
uv add <package-name>
```

**Install from pyproject.toml:**
```powershell
uv pip install -r pyproject.toml
```

**Activate environment:**
```powershell
.\<env-name>\Scripts\Activate.ps1
```

**Deactivate:**
```powershell
deactivate
```

---

## 📝 Key Learnings

1. **Virtual environments isolate dependencies** — Each project can have different package versions
2. **Pure `uv` workflow is superior to hybrid `uv pip`** — Why use pip commands if uv has better alternatives?
3. **`pyproject.toml` is the modern standard** — More informative than requirements.txt
4. **`uv add` auto-manages dependencies** — No manual pip freeze needed
5. **`uv` is significantly faster** — 10-100x speedup compared to traditional pip
6. **No activation needed with uv** — Commands run with `uv` auto-detect the environment
7. **`uv.lock` ensures reproducibility** — Exact same packages install on any machine

---

## � Deliverables

### Files to Submit

1. **Screenshots** (minimum 6, organized in `screenshots/` folder)
   - All required steps documented with clear filenames
   
2. **add.py** - Simple addition script that:
   - Prompts for two integers
   - Stores in variables `a` and `b`
   - Calculates sum in variable `c`
   - Prints the result

3. **test_run.py** - Simplified test file (per mentor recommendation)
   - Tests add.py functionality
   - Uses direct import instead of importlib

4. **pyproject.toml** - Modern dependency file
   - Auto-generated and maintained by `uv add` commands
   - Lists ipython and bcrypt dependencies

5. **learning_journal.md** - Comprehensive learning documentation
   - Reflection questions answered
   - Challenges and solutions documented
   - Practice task reflections

6. **learning_journey.md** - Personal growth narrative
   - Transformation story
   - Time investment tracking
   - Growth mindset reflections

7. **README.md** - This documentation file
   - Project overview and requirements
   - Complete setup instructions
   - All mentor recommendations addressed

### Virtual Environments (Not Submitted)

- `cf-python-base/` - First environment with packages installed
- `cf-python-copy/` - Second environment created from pyproject.toml
- `.venv/` - Default uv environment

*Virtual environments are not submitted as they can be recreated from pyproject.toml*

---

## �🔍 Verification

Both virtual environments have identical packages (proof that pyproject.toml works correctly):

```powershell
# In cf-python-base
.\cf-python-base\Scripts\Activate.ps1
ipython --version

# In cf-python-copy
deactivate
.\cf-python-copy\Scripts\Activate.ps1
ipython --version
```

Both show the same version: `9.6.0`

---

## 📚 Additional Resources

- [uv Documentation](https://github.com/astral-sh/uv)
- [uv Guide on pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [IPython Documentation](https://ipython.readthedocs.io/)
- [PowerShell Execution Policy](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies)

---

**Repository:** [python-web-development](https://github.com/souravdas090300/python-web-development)  
**Author:** Sourav Das  
**Exercise:** 1.1 - Python Environment Setup  
**Status:** ✅ Complete - Ready for Submission

---

## 🎯 Next Steps

**Immediate:** Move to Exercise 1.2 (Data Types and Structures)  
**Upcoming:** Exercise 1.3 (Control Flow - Functions, Loops, Conditionals)  
**Achievement 1 Goal:** Build complete CLI Recipe Application

### Skills Gained in This Exercise

✅ Python installation and verification  
✅ Virtual environment creation and management  
✅ Modern package management with `uv`  
✅ Dependency tracking with pyproject.toml  
✅ IPython REPL usage  
✅ Simple script creation and testing  
✅ Professional project organization  

### Ready for Next Exercise

With virtual environments and package management mastered, you're now prepared to:
- Work with Python data types and structures (Exercise 1.2)
- Build more complex scripts with proper dependency management
- Use IPython for interactive development and testing
- Maintain professional project documentation
