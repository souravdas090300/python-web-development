# Learning Journal — Exercise 1.1: Getting Started with Python

**Date:** October 14-16, 2025  
**Student:** Sourav Das  
**Exercise:** 1.1 - Python Environment Setup  
**Updated:** October 16, 2025 - Implemented pure `uv` workflow per mentor recommendation

---

## 📝 What I Did

### 1. Python Installation
- **Installed Python 3.14.0** (newer than the required 3.8.7)
- Verified installation using `python --version`
- Added Python to Windows PATH during installation
- Chose the latest stable version to take advantage of new features and improvements

### 2. Virtual Environment Setup with Pure `uv` Workflow
- **Discovered and installed `uv`** - A modern, fast Python package installer (10-100x faster than pip)
- **Initialized project with `uv init --bare`**
  - Created `pyproject.toml` file automatically
  - Modern dependency management (replaces requirements.txt)
- **Created first virtual environment:** `cf-python-base`
  - Command: `uv venv cf-python-base`
  - Activated with: `.\cf-python-base\Scripts\Activate.ps1`
- **Created second virtual environment:** `cf-python-copy`
  - Duplicated from pyproject.toml to practice environment replication
  - Command: `uv venv cf-python-copy`

### 3. Package Installation with `uv add`
- **Installed IPython 9.6.0** using pure uv workflow
  - Command: `uv add ipython` (NOT `uv pip install ipython`)
  - Auto-created `.venv` folder
  - Auto-updated `pyproject.toml` with dependency
  - Verified by launching IPython shell
- **Installed bcrypt 5.0.0** with same approach
  - Command: `uv add bcrypt`
  - Automatically added to `pyproject.toml`
- Total of **16 packages** installed (including dependencies)

### 4. Modern Dependency Management with `pyproject.toml`
- **pyproject.toml auto-created** by `uv init --bare`
  - No manual editing needed
  - Auto-updated by `uv add` commands
  - More informative than requirements.txt
- **Installed packages in second environment** from pyproject.toml
  - Command: `uv pip install -r pyproject.toml`
  - Verified both environments have identical packages
- **No pip freeze needed!** — Dependencies tracked automatically

### 5. Python Script Development
- **Created `add.py`** - Simple addition script following mentor specifications:
  - Prompts user for two integers
  - Stores in variables `a` and `b`
  - Calculates sum in variable `c`
  - Prints result to console
- **Created `test_run.py`** - Simplified test file (per mentor recommendation)
  - Uses direct import instead of importlib
  - Tests multiple input scenarios
  - Clean, maintainable code

### 6. Documentation
- **Organized screenshots** in separate `screenshots/` folder with descriptive names
- **Created comprehensive README.md** documenting all steps and commands
- **Structured project folder** for easy review and replication
- **Completed learning journal** with reflections and lessons learned

---

## 💡 What I Learned

### Technical Concepts

#### 1. Virtual Environments Are Essential
- **Isolation:** Each project can have different package versions without conflicts
- **Reproducibility:** pyproject.toml ensures anyone can recreate the exact environment
- **Cleanliness:** Global Python installation stays clean and minimal
- **Best Practice:** Always activate environment before installing packages

#### 2. Pure `uv` Workflow vs Hybrid `uv pip` Approach
- **Pure uv (Recommended):**
  - `uv init --bare` — Creates pyproject.toml
  - `uv add <package>` — Installs and auto-updates dependencies
  - No manual pip freeze needed
  - Industry standard approach
- **Hybrid uv pip (Old way):**
  - `uv pip install <package>` — Just a faster pip
  - `uv pip freeze > requirements.txt` — Manual tracking
  - Missing out on uv's full potential
- **Key Insight:** "If you're using uv pip, why install uv at all?" - Mentor feedback

#### 3. `pyproject.toml` vs `requirements.txt`
- **pyproject.toml advantages:**
  - Includes project metadata (name, version, Python version)
  - Industry standard for Python projects
  - Auto-updated by `uv add`
  - More informative and structured
- **requirements.txt:**
  - Legacy approach
  - Just a flat list of packages
  - Requires manual pip freeze
  - Still works, but outdated

#### 4. Modern Python Tooling - `uv` Capabilities
- **Speed Advantage:** `uv` is 10-100x faster than pip for package installation
- **Better Dependency Resolution:** More intelligent handling of package conflicts
- **Auto-detection:** No need to activate when using uv commands
- **Modern Standard:** Industry is moving toward faster, more reliable tools

#### 5. Windows PowerShell Challenges
- **Execution Policy:** PowerShell blocks script execution by default for security
  - Solution: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
  - Alternative: `powershell -ExecutionPolicy Bypass -File script.ps1`
- **Path Separators:** Windows uses backslashes `\` vs Unix forward slashes `/`
- **Activation Scripts:** Different from Unix (`.ps1` vs `.sh`)

#### 4. Python Package Ecosystem
- **Dependencies:** Installing one package often installs many dependencies
  - Example: ipython requires 15 additional packages (colorama, jedi, pygments, etc.)
- **Version Pinning:** `requirements.txt` locks exact versions (e.g., `ipython==9.6.0`)
- **Transitive Dependencies:** Understanding the full dependency tree is important

#### 5. Testing and Verification
- **Import Testing:** Verify packages are accessible before using in projects
- **Simple Tests:** Direct imports are clearer than complex importlib usage
- **Multiple Scenarios:** Test edge cases (zero, negative numbers, large values)

---

## 🚧 Challenges I Faced

### Challenge 1: PowerShell Execution Policy Error
**Problem:** When trying to activate virtual environment, got error:
```
cannot be loaded because running scripts is disabled on this system
```

**Solution:** Changed execution policy to allow local scripts:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Learning:** Windows security settings can block legitimate development tasks. Understanding execution policies is crucial for Windows Python development.

---

### Challenge 2: Understanding Virtual Environment Activation
**Problem:** Initially confused about when to activate environment and why it matters.

**Solution:** Learned that:
- Activation modifies PATH to use environment's Python and packages
- Without activation, packages install to global Python (bad practice)
- Each terminal session needs activation
- Prompt shows `(cf-python-base)` when active

**Learning:** Visual confirmation (prompt change) helps verify environment is active before installing packages.

---

### Challenge 3: Understanding Pure `uv` Workflow vs Hybrid Approach
**Problem:** Initially used `uv pip install` (hybrid approach). Mentor asked: "If you're using uv pip, why install uv at all?"

**Solution:** 
- Researched pure uv workflow
- Learned `uv init --bare` creates pyproject.toml
- Discovered `uv add` installs packages AND updates dependencies automatically
- Reimplemented Exercise 1.1 using pure uv commands
- Understood the difference:
  - ❌ `uv pip install` = Just faster pip (missing uv benefits)
  - ✅ `uv add` = Full uv power (auto dependency management)

**Learning:** Using a tool's subset features defeats the purpose. Pure `uv` workflow eliminates manual `pip freeze` and uses industry-standard `pyproject.toml`. Starting with hybrid approach was helpful for transition, but pure uv is the goal.

---

### Challenge 4: Understanding `pyproject.toml` vs `requirements.txt`
**Problem:** Didn't understand why pyproject.toml is better than requirements.txt.

**Solution:** Realized that:
- requirements.txt is just a flat list of packages
- pyproject.toml includes project metadata (name, version, Python version)
- `uv add` auto-updates pyproject.toml (no manual freeze needed)
- pyproject.toml is the modern Python standard
- requirements.txt is legacy but still widely used

**Learning:** Automation (freeze) is more reliable than manual documentation. Exact version tracking prevents subtle bugs from version mismatches.

---

### Challenge 5: Testing the `add.py` Script
**Problem:** First version didn't handle invalid input (non-numeric strings).

**Solution:** 
- Added input validation in test file
- Kept main script simple per mentor instructions
- Learned that production code needs error handling, but learning exercises can focus on core concepts

**Learning:** Balance between robust production code and clear learning examples. Sometimes simplicity aids understanding.

---

## 🔍 Key Takeaways

1. **Virtual Environments Are Not Optional** - They're a fundamental best practice in Python development, not an advanced feature.

2. **Pure `uv` workflow is superior to hybrid approach** - Using `uv pip` defeats the purpose of installing uv. Use `uv add` for full benefits.

3. **`pyproject.toml` is the modern standard** - requirements.txt is legacy. Industry has moved to more informative, auto-managed dependency files.

4. **Tool Evolution** - Python ecosystem constantly improves. New tools like `uv` offer significant advantages over older approaches.

5. **Documentation Matters** - Well-organized screenshots and README files make projects professional and easy to review.

6. **Reproducibility is Critical** - pyproject.toml and uv.lock ensure anyone can recreate your exact environment anywhere.

7. **Platform Awareness** - Windows development has unique challenges (execution policies, path separators) that Unix-based tutorials may not cover.

8. **Mentor Feedback is Invaluable** - Recommendations about pure uv workflow, simplified tests, and better organization immediately improved my work quality and understanding.

---

## 🎯 What I Want to Learn Next

### Immediate Next Steps (Exercise 1.2)
- **Data Types and Data Structures** in Python
- Working with tuples, lists, dictionaries, and strings
- Understanding when to use each data structure
- Nested data structures for complex data modeling

### Advanced `uv` Features (Now Implemented! ✅)
Mentor's recommendations that I've now implemented:
- ✅ **`uv init --bare`** - Initialize projects with `pyproject.toml`
- ✅ **`uv add <package>`** - Direct package installation without pip
- ✅ **`pyproject.toml` vs `requirements.txt`** - Modern dependency management
- **Automatic environment detection** - No manual activation needed

### Python Fundamentals
- Control flow (if/else, loops)
- Functions and code reusability
- File I/O operations
- Error handling and exceptions
- Object-oriented programming basics

### Development Best Practices
- Writing comprehensive tests
- Code organization and project structure
- Git workflow and version control
- Documentation standards
- Debugging techniques

### Windows Python Development
- Understanding Windows-specific Python challenges
- PowerShell scripting for automation
- Cross-platform compatibility considerations
- WSL (Windows Subsystem for Linux) as alternative environment

---

## 📊 Progress Assessment

### Completed Successfully ✅
- Python 3.14.0 installation and PATH configuration
- Pure `uv` workflow implemented (uv init, uv add)
- pyproject.toml created and auto-managed
- Two virtual environments created and tested (.venv, cf-python-base, cf-python-copy)
- IPython and bcrypt installed using `uv add`
- add.py script working correctly
- Test file created and simplified
- Screenshots organized professionally
- Comprehensive documentation written
- Learning journal completed with full reflections

### Successfully Implemented Mentor Recommendations ✅
- ✅ Transitioned to full `uv` workflow (`uv init`, `uv add`) from `uv pip`
- ✅ Using `pyproject.toml` as modern alternative to `requirements.txt`
- ✅ No manual pip freeze needed - dependencies auto-tracked
- ✅ Understanding pure uv benefits vs hybrid approach

### Areas for Future Exploration 📈
- Practice with more complex scripts beyond simple addition
- Explore IPython features more deeply (magic commands, debugging)
- Learn `uv sync` for environment synchronization
- Understand `uv.lock` file for reproducible builds

### Confidence Level 🎓
- **Virtual Environments:** 10/10 - Complete understanding, practiced with pure uv
- **Package Management:** 10/10 - Implemented pure uv workflow successfully
- **Modern Python Tooling:** 9/10 - Understand pyproject.toml, uv benefits
- **Python Basics:** 7/10 - Can write simple scripts, need more practice
- **Windows Development:** 8/10 - Solved execution policy issues, understand platform differences
- **Documentation:** 10/10 - Organized, clear, professional presentation with updates

---

## 🔄 Reflection on Mentor Feedback

**What Went Well:**
- Screenshots organization praised as "clean and easy to review"
- Using `uv` recognized as good choice
- README.md documentation appreciated
- Test file implementation noted positively

**Required Action Completed:**
- ✅ Learning journal for Exercise 1.1 now complete (October 16, 2025)

**Recommendations - ALL IMPLEMENTED! ✅**
- ✅ Transitioned to full `uv` workflow (done October 16, 2025)
- ✅ Used `uv init --bare` to create `pyproject.toml`
- ✅ Practiced `uv add` instead of `uv pip install`
- ✅ Understood automatic environment detection with uv
- ✅ Compared `pyproject.toml` vs `requirements.txt` in real scenario

**What I Did After Feedback:**
1. Reimplemented Exercise 1.1 using pure uv workflow
2. Created pyproject.toml with `uv init --bare`
3. Installed packages with `uv add ipython` and `uv add bcrypt`
4. Created second environment and installed from pyproject.toml
5. Updated README.md to document pure uv commands
6. Updated learning journal to reflect new understanding
7. Kept requirements.txt as reference but noted it's legacy

**Key Insight from Mentor:**
> "Though uv has pip, you'll be missing a lot if you use pip inside of uv. If that's the case, then no need installing uv in the first place."

This feedback was transformative - it made me realize I was using only 20% of uv's capabilities. Now I understand and use the full power of modern Python tooling!

---

## 📚 Resources I Found Helpful

1. **uv Documentation** - https://github.com/astral-sh/uv
2. **uv Guide on pyproject.toml** - Understanding modern dependency management
3. **Python Virtual Environments Guide** - Official Python docs
4. **IPython Documentation** - Interactive shell features
4. **PowerShell Execution Policies** - Microsoft docs
5. **Mentor Feedback** - Specific, actionable recommendations

---

**Status:** Exercise 1.1 Complete - Ready for Resubmission  
**Next Exercise:** 1.2 - Data Types and Data Structures  
**Date Completed:** October 15, 2025
