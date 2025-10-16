# Python for Web Developers - Course Exercises

**Student:** Sourav Das  
**Course:** Python for Web Developers  
**Python Version:** 3.14.0  
**Last Updated:** October 16, 2025

---

# Exercise 1.1 — Python Environment Setup (Windows)

**Date:** October 15, 2025

## 📋 Overview

This exercise demonstrates proper Python environment setup using modern tools (`uv`) and best practices for Windows development. All mentor requirements and recommendations have been implemented.

## ✅ Completed Requirements

### 1. Python Installation
- **Version:** Python 3.14.0 (newer than required 3.8.7, taking advantage of latest features)
- **Verification:** `python --version`

### 2. Virtual Environments with Pure `uv` Workflow
Created two isolated virtual environments using **pure `uv`** (10x faster than traditional pip):

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

## 📁 Project Structure

```
Exercise 1.1/
├── .venv/                   # Default uv virtual environment
├── cf-python-base/          # Named virtual environment
├── cf-python-copy/          # Copy environment
├── screenshots/             # Organized screenshots folder
│   ├── step1_python_version.png
│   ├── step2_uv_init.png
│   ├── step3_uv_add_ipython.png
│   ├── step4_ipython_shell.png
│   ├── step5_pyproject_toml.png
│   └── step6_copy_env.png
├── add.py                   # Main script
├── test_run.py              # Simplified tests
├── pyproject.toml           # Modern dependency file (replaces requirements.txt)
├── uv.lock                  # Lock file for reproducible builds
├── learning_journal.md      # Learning documentation
└── requirements.txt         # Legacy file (kept for reference)
```

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

### Legacy Approach (Old Way with uv pip)

```powershell
# Create environment
uv venv cf-python-base

# Activate it
.\cf-python-base\Scripts\Activate.ps1

# Install packages (old way)
uv pip install ipython bcrypt

# Generate requirements.txt
uv pip freeze > requirements.txt
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

### Step 2: Initialize Project with uv
Created pyproject.toml using pure uv:
```powershell
uv init --bare
```
**Screenshot:** `screenshots/step2_uv_init.png`

### Step 3: Create Environment and Add Packages
Created `cf-python-base` and installed ipython with `uv add`:
```powershell
uv venv cf-python-base
.\cf-python-base\Scripts\Activate.ps1
uv add ipython
uv add bcrypt
```
**Screenshot:** `screenshots/step3_uv_add_ipython.png`

### Step 4: Test IPython Shell
Launched and tested IPython:
```powershell
ipython
```
**Screenshot:** `screenshots/step4_ipython_shell.png`

### Step 5: View pyproject.toml
Verified dependency tracking in pyproject.toml:
```powershell
cat pyproject.toml
```
**Screenshot:** `screenshots/step5_pyproject_toml.png`

### Step 6: Create Copy Environment
Created second environment and installed from pyproject.toml:
```powershell
deactivate
uv venv cf-python-copy
.\cf-python-copy\Scripts\Activate.ps1
uv pip install -r pyproject.toml
```
**Screenshot:** `screenshots/step6_copy_env.png`

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

## 🔧 Command Reference

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

### Legacy uv pip Commands (Old Way)

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
2. **Pure `uv` workflow is superior to hybrid `uv pip`** — Why use pip commands if uv has better alternatives?
3. **`pyproject.toml` is the modern standard** — More informative than requirements.txt
4. **`uv add` auto-manages dependencies** — No manual pip freeze needed
5. **`uv` is significantly faster** — 10-100x speedup compared to traditional pip
6. **No activation needed with uv** — Commands run with `uv` auto-detect the environment
7. **`uv.lock` ensures reproducibility** — Exact same packages install on any machine

## 🔍 Verification

Both virtual environments have identical packages (proof that pyproject.toml works correctly):

```powershell
# In cf-python-base
.\cf-python-base\Scripts\Activate.ps1
ipython --version

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

---

# Exercise 1.2 — Data Types and Data Structures in Python

**Date:** October 15, 2025

## 📋 Overview

This exercise explores Python's core data structures (tuples, lists, dictionaries, strings) through hands-on practice tasks and a recipe management application.

## ✅ Completed Requirements

### Practice Tasks (5 Total)

1. **Compound Interest Calculator** — File I/O, type conversion, mathematical operations
2. **World Population Analysis** — Tuple operations, slicing, max() function
3. **Ford Vehicle Management** — List manipulation, append(), sort()
4. **String Slicing Practice** — Predictions and verification of slice operations
5. **Month Dictionary** — Numeric keys mapping to month names

### Main Task: Recipe Management

Created 5 recipe dictionaries stored in a list structure:
- Each recipe contains: name, cooking_time, ingredients (list)
- Demonstrated nested data structures
- Displayed all recipe details

### Data Structure Justifications

**Dictionary for Individual Recipes:**
> "I chose a dictionary for individual recipes because it provides labeled access to recipe components (name, cooking_time, ingredients) through meaningful keys rather than positional indices. Dictionaries are mutable, allowing recipe modifications, and self-documenting through key names. This structure makes the code more readable and maintainable, as accessing `recipe['name']` is clearer than `recipe[0]`. The flexibility to add new recipe attributes later without breaking existing code makes dictionaries ideal for this use case."

**List for All Recipes Collection:**
> "I selected a list for the outer all_recipes structure because recipes have a natural sequential ordering and we need to iterate through all recipes systematically. Lists are mutable, allowing us to easily add, remove, or modify recipes in our collection. The indexing capability enables accessing specific recipes by position when needed, and lists efficiently handle variable numbers of recipes through append() operations."

## 📁 Project Structure

```
Exercise 1.2/
├── 1.2-Practice Task 1/
│   └── codepractice1.txt
├── 1.2-Practice Task 2/
├── 1.2-Practice Task 3/
├── 1.2-Practice Task 4/
├── 1.2-Practice Task 5/
├── README.md
└── learning_journal.md
```

## 📝 Key Learnings

- **Tuples:** Immutable sequences, ideal for fixed data
- **Lists:** Mutable, ordered collections with append() and sort()
- **Dictionaries:** Key-value pairs for structured, labeled data
- **Strings:** Immutable character sequences with powerful slicing
- **Nested Structures:** Lists containing dictionaries for complex data models

---

# Exercise 1.3 — Core Python Operations

**Date:** October 16, 2025

## 📋 Overview

This exercise covers essential Python programming concepts: scripts vs interactive shell, conditionals (if-elif-else), loops (for/while), and functions with parameters and return values.

## ✅ Completed Requirements

### Practice Tasks (3 Total)

1. **Calculator with Conditionals** — if-elif-else statements for arithmetic operations (+, -)
2. **Top 3 Test Scores** — for loop with range() to find highest scores
3. **Loop Comparison** — Rewriting prints using both while and for loops

### Main Task: Recipe Management System

**Features Implemented:**
- User input collection for multiple recipes
- `take_recipe()` function returning dictionary
- Automatic difficulty calculation based on cooking time and ingredients
- Four difficulty levels: Easy, Medium, Intermediate, Hard
- Unique ingredient collection across all recipes
- Alphabetically sorted ingredient display

**Difficulty Logic:**
- **Easy:** < 10 min cooking + < 4 ingredients
- **Medium:** < 10 min cooking + ≥ 4 ingredients
- **Intermediate:** ≥ 10 min cooking + < 4 ingredients
- **Hard:** ≥ 10 min cooking + ≥ 4 ingredients

## 📁 Project Structure

```
Exercise 1.3/
├── 1.3-Practice Task 1/
│   └── code practice1_calculator.py
├── 1.3-Practice Task 2/
├── 1.3-Practice Task 3/
├── screenshots/
├── Exercise_1.3.py
└── learning_journal.md
```

## 🚀 How to Run

```powershell
cd "Exercise 1.3"
python Exercise_1.3.py
```

**Example Usage:**
```
How many recipes would you like to enter? 2

RECIPE 1
Enter the recipe name: Tea
Enter the cooking time (in minutes): 5
How many ingredients does this recipe have? 3
  Enter ingredient 1: Tea Leaves
  Enter ingredient 2: Water
  Enter ingredient 3: Sugar

RECIPE 2
Enter the recipe name: Coffee
Enter the cooking time (in minutes): 7
How many ingredients does this recipe have? 4
  Enter ingredient 1: Coffee Powder
  Enter ingredient 2: Water
  Enter ingredient 3: Milk
  Enter ingredient 4: Sugar

[Displays all recipes with difficulty levels and sorted ingredients]
```

## 📝 Key Learnings

- **Scripts vs Shell:** Scripts (.py files) allow reusable, shareable code vs one-time interactive commands
- **Conditionals:** Multi-condition logic with if-elif-else chains
- **For Loops:** Iterator-based loops with range() for counting
- **While Loops:** Condition-based loops requiring manual iteration management
- **Functions:** Reusable code blocks with parameters and return values
- **Nested Loops:** Inner loops for detailed processing within outer iteration

---

**Repository:** [python-web-development](https://github.com/souravdas090300/python-web-development)  
**Author:** Sourav Das  
**Last Updated:** October 16, 2025
