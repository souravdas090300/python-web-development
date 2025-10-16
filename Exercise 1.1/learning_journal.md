# Learning Journal — Exercise 1.1: Getting Started with Python

**Date:** October 14-15, 2025  
**Student:** Sourav Das  
**Exercise:** 1.1 - Python Environment Setup

---

## 📝 What I Did

### 1. Python Installation
- **Installed Python 3.14.0** (newer than the required 3.8.7)
- Verified installation using `python --version`
- Added Python to Windows PATH during installation
- Chose the latest stable version to take advantage of new features and improvements

### 2. Virtual Environment Setup with `uv`
- **Discovered and installed `uv`** - A modern, fast Python package installer (10-100x faster than pip)
- **Created first virtual environment:** `cf-python-base`
  - Command: `uv venv cf-python-base`
  - Activated with: `.\cf-python-base\Scripts\Activate.ps1`
- **Created second virtual environment:** `cf-python-copy`
  - Duplicated from requirements.txt to practice environment replication
  - Command: `uv venv cf-python-copy`

### 3. Package Installation
- **Installed IPython 9.6.0** within activated `cf-python-base` environment
  - Command: `uv pip install ipython`
  - Verified by launching IPython shell
- **Installed bcrypt 5.0.0** for password hashing practice
  - Command: `uv pip install bcrypt`
- Total of **16 packages** installed (including dependencies)

### 4. Requirements Management
- **Generated requirements.txt** from actual environment (not hardcoded)
  - Command: `uv pip freeze > requirements.txt`
  - Captured exact versions: ipython==9.6.0, bcrypt==5.0.0, etc.
- **Installed packages in second environment** from requirements.txt
  - Command: `uv pip install -r requirements.txt`
  - Verified both environments have identical packages

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

---

## 💡 What I Learned

### Technical Concepts

#### 1. Virtual Environments Are Essential
- **Isolation:** Each project can have different package versions without conflicts
- **Reproducibility:** requirements.txt ensures anyone can recreate the exact environment
- **Cleanliness:** Global Python installation stays clean and minimal
- **Best Practice:** Always activate environment before installing packages

#### 2. Modern Python Tooling - `uv` vs Traditional `pip`
- **Speed Advantage:** `uv` is 10-100x faster than pip for package installation
- **Better Dependency Resolution:** More intelligent handling of package conflicts
- **Modern Standard:** Industry is moving toward faster, more reliable tools
- **Backward Compatible:** Still uses pip commands (`uv pip install`, `uv pip freeze`)

#### 3. Windows PowerShell Challenges
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

### Challenge 3: Choosing Between `uv` and Traditional `pip`
**Problem:** Tutorial used pip, but mentor recommended uv. Unsure which to use.

**Solution:** 
- Researched both tools
- Decided to use `uv` for speed and modern best practices
- Used `uv pip` commands for compatibility with course instructions
- Plan to explore full uv workflow (`uv init`, `uv add`) in future projects

**Learning:** New tools can be intimidating but offer significant advantages. Starting with familiar commands (`uv pip`) while learning new tool is a good transition strategy.

---

### Challenge 4: Understanding `requirements.txt` Generation
**Problem:** Didn't understand why we "freeze" requirements instead of manually listing packages.

**Solution:** Realized that:
- Manual lists miss dependency versions
- `pip freeze` captures EXACT state of environment
- Anyone can recreate identical environment from frozen requirements
- Prevents "works on my machine" problems

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

2. **Tool Evolution** - Python ecosystem constantly improves. New tools like `uv` offer significant advantages over older approaches.

3. **Documentation Matters** - Well-organized screenshots and README files make projects professional and easy to review.

4. **Reproducibility is Critical** - Generated `requirements.txt` ensures anyone can recreate your exact environment anywhere.

5. **Platform Awareness** - Windows development has unique challenges (execution policies, path separators) that Unix-based tutorials may not cover.

6. **Mentor Feedback is Valuable** - Recommendations about simplified tests and better organization immediately improved my work quality.

---

## 🎯 What I Want to Learn Next

### Immediate Next Steps (Exercise 1.2)
- **Data Types and Data Structures** in Python
- Working with tuples, lists, dictionaries, and strings
- Understanding when to use each data structure
- Nested data structures for complex data modeling

### Advanced `uv` Workflow
Based on mentor's recommendations, I want to explore:
- **`uv init --bare`** - Initialize projects with `pyproject.toml`
- **`uv add <package>`** - Direct package installation without pip
- **`pyproject.toml` vs `requirements.txt`** - Modern dependency management
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
- Two virtual environments created and tested
- IPython and bcrypt installed correctly
- requirements.txt generated and used successfully
- add.py script working correctly
- Test file created and simplified
- Screenshots organized professionally
- Comprehensive documentation written

### Areas for Improvement 📈
- Transition to full `uv` workflow (`uv init`, `uv add`) instead of `uv pip`
- Learn `pyproject.toml` as modern alternative to `requirements.txt`
- Practice with more complex scripts beyond simple addition
- Explore IPython features more deeply (magic commands, debugging)

### Confidence Level 🎓
- **Virtual Environments:** 9/10 - Solid understanding, practiced twice
- **Package Management:** 8/10 - Comfortable with uv pip, want to learn pure uv
- **Python Basics:** 7/10 - Can write simple scripts, need more practice
- **Windows Development:** 8/10 - Solved execution policy issues, understand platform differences
- **Documentation:** 9/10 - Organized, clear, professional presentation

---

## 🔄 Reflection on Mentor Feedback

**What Went Well:**
- Screenshots organization praised as "clean and easy to review"
- Using `uv` recognized as good choice
- README.md documentation appreciated
- Test file implementation noted positively

**Required Action Completed:**
- ✅ Learning journal for Exercise 1.1 now complete

**Recommendations to Implement:**
- Consider transitioning to full `uv` workflow in future exercises
- Use `uv init --bare` to create `pyproject.toml`
- Practice `uv add` instead of `uv pip install`
- Understand automatic environment detection with uv

**My Plan:**
- Complete current course exercises with `uv pip` (familiar, working well)
- After gaining more Python fundamentals, revisit uv advanced features
- Create a practice project using pure uv workflow
- Compare `pyproject.toml` vs `requirements.txt` in real scenario

---

## 📚 Resources I Found Helpful

1. **uv Documentation** - https://github.com/astral-sh/uv
2. **Python Virtual Environments Guide** - Official Python docs
3. **IPython Documentation** - Interactive shell features
4. **PowerShell Execution Policies** - Microsoft docs
5. **Mentor Feedback** - Specific, actionable recommendations

---

**Status:** Exercise 1.1 Complete - Ready for Resubmission  
**Next Exercise:** 1.2 - Data Types and Data Structures  
**Date Completed:** October 15, 2025
