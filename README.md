# Python for Web Developers - Course Exercises

**Student:** Sourav Das  
**Course:** Python for Web Developers  
**Python Version:** 3.14.0  
**Last Updated:** October 19, 2025

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

# Exercise 1.4 — File Handling in Python

**Date:** October 18, 2025

## 📋 Overview

This exercise focuses on file operations in Python using binary files with the `pickle` module for data persistence. Built a complete recipe management system with file-based storage.

## ✅ Completed Requirements

### Practice Tasks (2 Total)

1. **Text File Operations** — Reading and writing text files with various modes
2. **Pickle Binary Files** — Using pickle.dump() and pickle.load() for data serialization

### Main Task: Recipe Management with File Storage

**Features Implemented:**
- **recipe_input.py** — Create and save recipes to binary file
  - Collects recipe details from user
  - Calculates difficulty automatically
  - Saves using pickle
  - Appends to existing data

- **recipe_search.py** — Search recipes from file
  - Loads recipes from binary file
  - Search by ingredient
  - Displays all matching recipes
  - Handles file not found errors

**Data Persistence:**
- Uses `pickle` module for binary serialization
- Stores list of recipe dictionaries
- Maintains data between program runs

## 📁 Project Structure

```
Exercise 1.4/
├── 1.4-Practice task 1/
│   ├── hello.txt
│   ├── number_list.txt
│   └── desserts.txt
├── 1.4-Practice task 2/
│   ├── codepractice2_pickle.py
│   ├── recipe_read.py
│   └── recipe_write.py
├── main-task/
│   ├── recipe_input.py
│   ├── recipe_search.py
│   ├── recipes.bin
│   ├── screenshots/
│   └── README.md
├── veggies.txt
└── learning_journal.md
```

## 🚀 How to Run

```powershell
cd "Exercise 1.4\main-task"

# Create recipes
python recipe_input.py

# Search recipes
python recipe_search.py
```

## 📝 Key Learnings

- **File Modes:** 'r', 'w', 'a', 'rb', 'wb', 'ab'
- **Pickle Module:** Serializing Python objects to binary
- **Error Handling:** try/except for file operations
- **Data Persistence:** Saving and loading between program runs

---

# Exercise 1.5 — Object-Oriented Programming in Python

**Date:** October 18, 2025

## 📋 Overview

This exercise introduces Object-Oriented Programming (OOP) concepts through building a Recipe class with methods, attributes, and proper encapsulation.

## ✅ Completed Requirements

### Practice Tasks

1. **Shopping List Class** — Basic class with initialization and methods
2. **Height Tracker** — Class with attributes and calculations
3. **Class Attributes Practice** — Understanding class vs instance variables

### Main Task: Recipe Class System

**Features Implemented:**
- **Recipe Class** with proper OOP design
  - `__init__()` constructor with name and cooking_time
  - `add_ingredients()` method for adding ingredients
  - `calculate_difficulty()` method (4-tier logic)
  - `search_ingredient()` method to check if ingredient exists
  - `update_all_ingredients()` class method
  - `__str__()` method for string representation

- **Recipe Search Function**
  - Searches multiple recipes for specific ingredient
  - Returns all matching recipes
  - Uses instance method for searching

**OOP Concepts Demonstrated:**
- Encapsulation: Data and methods bundled together
- Class vs Instance attributes
- Instance methods vs Class methods
- Special methods (__init__, __str__)
- Data validation and type checking

## 📁 Project Structure

```
Exercise 1.5/
├── 1.5-Practice Task 1/
├── 1.5-Practice Task 2/
├── 1.5-Practice Task 3/
├── main-task/
│   ├── recipe_oop.py
│   ├── screenshots/
│   └── README.md
└── learning_journal.md
```

## 🚀 How to Run

```powershell
cd "Exercise 1.5\main-task"
python recipe_oop.py
```

## 📝 Key Learnings

- **Classes and Objects:** Blueprint vs instances
- **Constructor:** __init__() for object initialization
- **Instance Methods:** self parameter for object-specific operations
- **Class Methods:** @classmethod decorator for class-level operations
- **String Representation:** __str__() for readable output
- **Encapsulation:** Bundling data and methods together

---

# Exercise 1.6 — Databases in Python with MySQL

**Date:** October 18, 2025

## 📋 Overview

This exercise introduces database programming with MySQL and Python, building a complete Recipe Management System with CREATE, READ, UPDATE, DELETE (CRUD) operations.

## ✅ Completed Requirements

### Technology Stack
- **MySQL 9.0** — Database server
- **mysql-connector-python** — Python MySQL driver
- **Python 3.14** — Programming language

### Main Task: Recipe Database Application

**Features Implemented:**
- **Database Connection** — Connects to MySQL server
- **Table Creation** — Creates Recipes table with proper schema
- **Create Recipe** — Add new recipes with validation
- **Search Recipe** — Search by ingredient using LIKE operator
- **Update Recipe** — Edit name, cooking time, or ingredients
- **Delete Recipe** — Remove recipes with confirmation
- **Main Menu** — Interactive CLI with 5 options

**Security Features:**
- Parameterized queries (prevents SQL injection)
- Input validation (length, type checking)
- Error handling for database operations
- Transaction management (commit/rollback)

**Database Schema:**
```sql
CREATE TABLE Recipes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
);
```

## 📁 Project Structure

```
Exercise 1.6/
├── 1.6-Practice Task 1/
│   └── screenshots/
├── main-task/
│   ├── recipe_mysql.py
│   ├── TASK_README.md
│   ├── screenshots/ (12 images)
│   └── learning_journal.md
├── learning_journey.md
└── README.md
```

## 🚀 How to Run

```powershell
# Activate virtual environment
cd "Exercise 1.4"
.\cf-python-base\Scripts\Activate.ps1

# Run application
cd "..\Exercise 1.6\main-task"
python recipe_mysql.py
```

## 📝 Key Learnings

- **SQL Basics:** CREATE, INSERT, SELECT, UPDATE, DELETE
- **Database Design:** Tables, columns, primary keys
- **mysql.connector:** Python database connectivity
- **Parameterized Queries:** SQL injection prevention
- **CRUD Operations:** Complete data management
- **Transaction Management:** commit() and rollback()
- **Cursor Usage:** Executing queries and fetching results

---

# Exercise 1.7 — Object Relational Mapping with SQLAlchemy

**Date:** October 19, 2025

## 📋 Overview

This exercise demonstrates **Object Relational Mapping (ORM)** using SQLAlchemy, allowing database operations through Python objects instead of raw SQL queries.

## ✅ Completed Requirements

### Technology Stack
- **SQLAlchemy 2.0.44** — ORM framework
- **PyMySQL 1.1.2** — MySQL connector for SQLAlchemy
- **MySQL 9.0** — Database server
- **Python 3.14** — Programming language

### Practice Tasks (3 Total)

1. **Adding Entries with ORM** — Created Tea, Coffee, Cake, Banana Smoothie using session.add()
2. **Searching with filter()** — Used filter() and like() to search recipes containing Sugar
3. **Updating Entries** — Modified Cake recipe, added Chocolate Powder

### Main Task: Recipe Management with ORM

**Features Implemented:**
- **Recipe Model** — Class definition with SQLAlchemy
  - Columns: id, name, ingredients, cooking_time, difficulty
  - Methods: calculate_difficulty(), return_ingredients_as_list()
  - Special methods: __repr__(), __str__()
  
- **CRUD Operations (Object-Based)**
  - Create: session.add(object) + session.commit()
  - Read: session.query(Recipe).all()
  - Update: Modify object attributes + session.commit()
  - Delete: session.delete(object) + session.commit()

- **Advanced Queries**
  - filter() with conditions
  - like() for pattern matching
  - get() for primary key lookup
  - with_entities() for specific columns
  - count() for existence checking

- **Complete CLI Application**
  - Interactive main menu
  - Input validation and error handling
  - Search by ingredient (from unique ingredient list)
  - Edit recipes with difficulty recalculation
  - Delete with confirmation prompts

**ORM Advantages Demonstrated:**
- Work with Python objects, not SQL strings
- Automatic type conversion
- Built-in SQL injection protection
- Database-agnostic code
- Cleaner, more maintainable code

## 📁 Project Structure

```
Exercise 1.7/
├── 1.7-Practice Task 1/
│   └── screenshots/ (9 images)
├── 1.7-Practice Task 2/
│   └── screenshots/ (5 images)
├── 1.7-Practice Task 3/
│   └── screenshots/ (6 images)
├── main-task/
│   ├── recipe_app.py (436 lines)
│   ├── README.md
│   ├── requirements.txt
│   └── screenshots/
├── learning_journey.md
└── VERIFICATION_CHECKLIST.md
```

## 🚀 How to Run

```powershell
# Activate virtual environment
cd "Exercise 1.4"
.\cf-python-base\Scripts\Activate.ps1

# Navigate to Exercise 1.7
cd "..\Exercise 1.7\main-task"

# Run the application
python recipe_app.py
```

**Menu Options:**
1. Create a new recipe
2. View all recipes
3. Search for recipes by ingredient
4. Edit a recipe
5. Delete a recipe
6. Exit

## 📝 Key Learnings

### SQLAlchemy Core Concepts
- **Engine:** Database connection factory
- **Session:** Transaction workspace
- **Base:** Declarative base class
- **Model:** Class mapped to database table
- **Column:** Table column definition
- **Query:** Lazy-loaded query builder

### ORM vs SQL Comparison

| Operation | Exercise 1.6 (SQL) | Exercise 1.7 (ORM) |
|-----------|-------------------|-------------------|
| **Connection** | mysql.connector.connect() | create_engine() + sessionmaker() |
| **Create Table** | cursor.execute("CREATE TABLE...") | Base.metadata.create_all() |
| **Insert** | cursor.execute("INSERT...") | session.add(object) |
| **Select** | cursor.execute("SELECT...") | session.query(Model).all() |
| **Update** | cursor.execute("UPDATE...") | object.attribute = new_value |
| **Delete** | cursor.execute("DELETE...") | session.delete(object) |
| **Search** | WHERE ... LIKE | .filter(Model.column.like(...)) |

### Key Methods Learned
- `create_engine()` — Create database connection
- `declarative_base()` — Generate base class
- `sessionmaker()` — Create session factory
- `session.add()` — Stage object for insertion
- `session.commit()` — Save changes to database
- `session.query()` — Start a query
- `.filter()` — Add WHERE conditions
- `.like()` — Pattern matching
- `.all()` — Get all results
- `.one()` — Get single result
- `.first()` — Get first result
- `.get(id)` — Get by primary key
- `.count()` — Count records
- `session.delete()` — Remove object

### Design Patterns Applied
- **Repository Pattern:** Session acts as repository
- **Active Record:** Objects know how to save themselves
- **Unit of Work:** Session tracks changes
- **Identity Map:** One object per database row

## 🔍 Exercise Comparison Summary

### Exercises 1.4 vs 1.6 vs 1.7

| Feature | 1.4 (Files) | 1.6 (MySQL) | 1.7 (ORM) |
|---------|------------|-------------|-----------|
| **Storage** | Binary files (pickle) | MySQL database | MySQL via SQLAlchemy |
| **Data Access** | pickle.load() | SQL queries | Python objects |
| **Query Language** | Python code | SQL | Python methods |
| **Scalability** | Limited | High | High |
| **Concurrent Access** | Difficult | Supported | Supported |
| **Code Style** | Procedural | Procedural + SQL | Object-Oriented |
| **Learning Curve** | Easy | Medium | Medium-High |
| **Real-World Use** | Small apps | Enterprise apps | Web applications |

### Evolution of Recipe Management
1. **1.4:** Pickle files — Simple persistence
2. **1.6:** Raw SQL — Professional database operations
3. **1.7:** ORM — Modern application development

---

## 🎓 Achievement 1 Summary

### Progress Overview

| Exercise | Topic | Status | Key Skill |
|----------|-------|--------|-----------|
| 1.1 | Python Setup | ✅ Complete | Virtual environments, uv |
| 1.2 | Data Structures | ✅ Complete | Lists, dicts, tuples |
| 1.3 | Control Flow | ✅ Complete | Loops, conditionals, functions |
| 1.4 | File Handling | ✅ Complete | pickle, binary files |
| 1.5 | OOP | ✅ Complete | Classes, objects, methods |
| 1.6 | Databases | ✅ Complete | MySQL, SQL queries |
| 1.7 | ORM | ✅ Complete | SQLAlchemy, models |

### Skills Acquired

**Python Fundamentals:**
- ✅ Variables, data types, operators
- ✅ Control structures (if/else, loops)
- ✅ Functions and scope
- ✅ Data structures (lists, dicts, tuples)
- ✅ File I/O operations
- ✅ Error handling (try/except)

**Object-Oriented Programming:**
- ✅ Classes and objects
- ✅ Instance vs class methods
- ✅ Constructors and special methods
- ✅ Encapsulation principles
- ✅ Code organization and reusability

**Database Programming:**
- ✅ SQL fundamentals (CRUD operations)
- ✅ Database design and schema
- ✅ MySQL connectivity (mysql.connector)
- ✅ Parameterized queries
- ✅ Transaction management
- ✅ ORM concepts (SQLAlchemy)
- ✅ Model-based database access

**Software Engineering:**
- ✅ Virtual environment management
- ✅ Dependency tracking
- ✅ Input validation
- ✅ Error handling and debugging
- ✅ Code documentation
- ✅ Git version control
- ✅ README documentation

### Recipe Application Evolution

**Exercise 1.2:** Dictionary-based storage (in-memory)
```python
recipe = {'name': 'Tea', 'cooking_time': 5, 'ingredients': ['Tea Leaves', 'Water']}
```

**Exercise 1.3:** Function-based with calculations
```python
def take_recipe():
    recipe = {}
    # ... collect data
    return recipe
```

**Exercise 1.4:** File persistence with pickle
```python
pickle.dump(recipes_list, file)
recipes_list = pickle.load(file)
```

**Exercise 1.5:** Object-oriented design
```python
class Recipe:
    def __init__(self, name):
        self.name = name
    
    def calculate_difficulty(self):
        # ...
```

**Exercise 1.6:** Database with SQL
```python
cursor.execute("INSERT INTO recipes VALUES (?, ?, ?)", (name, ingredients, time))
conn.commit()
```

**Exercise 1.7:** ORM with SQLAlchemy
```python
recipe = Recipe(name=name, ingredients=ingredients, cooking_time=time)
session.add(recipe)
session.commit()
```

### Next Steps: Achievement 2

**Upcoming Topics:**
- Django web framework
- Web development fundamentals
- HTTP requests and responses
- Templates and views
- URL routing
- Forms and user input
- Authentication and authorization
- Deployment to production

---

**Repository:** [python-web-development](https://github.com/souravdas090300/python-web-development)  
**Author:** Sourav Das  
**Last Updated:** October 19, 2025
