# Exercise 1.5 - Object-Oriented Programming in Python

## 📋 Overview

This exercise introduces **Object-Oriented Programming (OOP)** concepts in Python, focusing on creating classes, working with objects, implementing special methods, and building a complete OOP-based application.

**Student:** Sourav Das  
**Course:** Python for Web Developers  
**Date:** October 19, 2025  
**Status:** ✅ Completed

---

## 🎯 Learning Objectives

By completing this exercise, I have learned to:

- ✅ Understand core OOP concepts (classes, objects, inheritance, encapsulation, polymorphism)
- ✅ Create classes with constructors (`__init__`)
- ✅ Implement instance and class variables
- ✅ Write getters and setters for data attributes
- ✅ Use variable-length arguments (`*args`)
- ✅ Implement special methods (`__str__`, `__sub__`, comparison operators)
- ✅ Design and build a complete OOP application
- ✅ Understand when and how to use OOP principles effectively

---

## 📂 Project Structure

```
Exercise 1.5/
│
├── 1.5-Practice Task 1/
│   ├── shopping_list.py          # Shopping list OOP implementation
│   └── screenshot/                # Screenshots of execution
│
├── 1.5-Practice Task 2/
│   ├── height_operations.py      # Height subtraction with operator overloading
│   └── screenshot/                # Screenshots of execution
│
├── 1.5-Practice Task 3/
│   ├── height_comparison.py      # Height comparison operators
│   └── screenshot/                # Screenshots of execution
│
├── main-task/
│   ├── recipe_oop.py             # Complete Recipe OOP application
│   └── screenshot/                # Screenshots of execution
│
├── learning_journal.md            # Detailed reflection and learnings
├── learning_journey.md            # Personal growth documentation
└── README.md                      # This file
```

---

## 🔧 Practice Tasks

### Practice Task 1: Shopping List Class

**Objective:** Create a basic class to understand OOP fundamentals.

**Implementation:**
- Created `ShoppingList` class with `list_name` and `shopping_list` attributes
- Implemented `add_item()` method with duplicate prevention
- Implemented `remove_item()` method with error handling
- Implemented `view_list()` method for formatted display

**Key Concepts:**
- Class structure and `__init__` constructor
- Instance variables
- Methods operating on object data

**File:** `1.5-Practice Task 1/shopping_list.py`

---

### Practice Task 2: Height Operations

**Objective:** Implement operator overloading for custom objects.

**Implementation:**
- Created `Height` class with `feet` and `inches` attributes
- Implemented `__sub__` method to overload the `-` operator
- Converted heights to inches for calculation
- Converted result back to feet and inches format

**Key Concepts:**
- Operator overloading
- Special methods (`__sub__`)
- Unit conversion logic
- Creating new objects from operations

**File:** `1.5-Practice Task 2/height_operations.py`

**Example:**
```python
height1 = Height(5, 10)  # 5 feet 10 inches
height2 = Height(3, 9)   # 3 feet 9 inches
result = height1 - height2  # 2 feet 1 inch
```

---

### Practice Task 3: Height Comparison

**Objective:** Implement comparison operators for custom objects.

**Implementation:**
- Extended `Height` class with comparison operators
- Implemented all six comparison methods:
  - `__gt__` (>)
  - `__ge__` (>=)
  - `__eq__` (==)
  - `__ne__` (!=)
  - `__lt__` (<)
  - `__le__` (<=)
- All comparisons convert heights to inches for accurate comparison

**Key Concepts:**
- Comparison operator overloading
- Consistent comparison logic
- Boolean return values

**File:** `1.5-Practice Task 3/height_comparison.py`

**Example:**
```python
height1 = Height(5, 10)
height2 = Height(3, 9)
print(height1 > height2)   # True
print(height1 == height2)  # False
print(height1 <= height2)  # False
```

---

## 🎓 Main Task: Recipe OOP Application

### Overview

Built a complete **Recipe Management System** using OOP principles to manage recipes, ingredients, and difficulty levels.

**File:** `main-task/recipe_oop.py` (219 lines)

### Features

#### 1. Recipe Class

**Data Attributes:**
- `name`: Recipe name (string)
- `ingredients`: List of ingredients
- `cooking_time`: Cooking time in minutes (integer)
- `difficulty`: Calculated difficulty level (string)

**Class Variable:**
- `all_ingredients`: Tracks all unique ingredients across all recipes

**Methods:**

| Method | Purpose |
|--------|---------|
| `__init__(name)` | Initialize recipe with name |
| `get_name()` | Return recipe name |
| `set_name(name)` | Set recipe name |
| `get_cooking_time()` | Return cooking time |
| `set_cooking_time(time)` | Set cooking time |
| `add_ingredients(*ingredients)` | Add ingredients using variable-length arguments |
| `get_ingredients()` | Return ingredients list |
| `calculate_difficulty()` | Calculate difficulty based on time and ingredient count |
| `get_difficulty()` | Return difficulty (calculates if needed) |
| `search_ingredient(ingredient)` | Check if ingredient exists in recipe |
| `update_all_ingredients()` | Update class variable with new ingredients |
| `__str__()` | Return formatted string representation |

#### 2. Difficulty Calculation Logic

```
IF cooking_time < 10 AND ingredients < 4:
    difficulty = "Easy"
ELIF cooking_time < 10 AND ingredients >= 4:
    difficulty = "Medium"
ELIF cooking_time >= 10 AND ingredients < 4:
    difficulty = "Intermediate"
ELIF cooking_time >= 10 AND ingredients >= 4:
    difficulty = "Hard"
```

#### 3. recipe_search() Function

- Takes a list of Recipe objects and a search term
- Searches for recipes containing the specified ingredient
- Prints all matching recipes with full details

### Implementation

#### Sample Recipes Created

1. **Tea** (Easy)
   - Ingredients: Tea Leaves, Sugar, Water
   - Cooking Time: 5 minutes

2. **Coffee** (Easy)
   - Ingredients: Coffee Powder, Sugar, Water
   - Cooking Time: 5 minutes

3. **Cake** (Hard)
   - Ingredients: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk
   - Cooking Time: 50 minutes

4. **Banana Smoothie** (Medium)
   - Ingredients: Bananas, Milk, Peanut Butter, Sugar, Ice Cubes
   - Cooking Time: 5 minutes

#### Search Tests Performed

- ✅ Search for recipes containing "Water" → Found Tea, Coffee
- ✅ Search for recipes containing "Sugar" → Found Tea, Coffee, Cake, Banana Smoothie
- ✅ Search for recipes containing "Bananas" → Found Banana Smoothie

### Code Quality

- ✅ Comprehensive docstrings for all methods
- ✅ Clear comments and section dividers
- ✅ Professional output formatting with visual separators
- ✅ Modular design with single-responsibility methods
- ✅ Proper use of class and instance variables
- ✅ Error-free execution

---

## 🚀 How to Run

### Prerequisites

- Python 3.x installed
- Virtual environment (cf-python-base) set up
- IPython installed in virtual environment

### Execution Steps

#### Method 1: Using IPython (Recommended)

```powershell
# Navigate to Exercise 1.4 directory (where virtual environment is located)
cd "c:\Users\dasau\python-web-development\Exercise 1.4"

# Activate virtual environment
.\cf-python-base\Scripts\Activate.ps1

# Navigate to task directory
cd "..\Exercise 1.5\main-task"

# Start IPython
ipython

# In IPython, run the script
%run recipe_oop.py
```

#### Method 2: Direct Python Execution

```powershell
# Navigate to task directory
cd "c:\Users\dasau\python-web-development\Exercise 1.5\main-task"

# Run with Python
python recipe_oop.py
```

### Running Practice Tasks

```powershell
# Practice Task 1
cd "Exercise 1.5\1.5-Practice Task 1"
python shopping_list.py

# Practice Task 2
cd "..\1.5-Practice Task 2"
python height_operations.py

# Practice Task 3
cd "..\1.5-Practice Task 3"
python height_comparison.py
```

---

## 📊 Expected Output

### Main Task Output

```
============================================================
RECIPE OOP APPLICATION - EXERCISE 1.5 MAIN TASK
============================================================

>>> Creating Recipe 1: Tea

============================================================
Recipe: Tea
============================================================
Cooking Time: 5 minutes
Difficulty: Easy
Ingredients:
  - Tea Leaves
  - Sugar
  - Water
============================================================

[... similar output for Coffee, Cake, Banana Smoothie ...]

============================================================
ALL INGREDIENTS ACROSS ALL RECIPES:
============================================================
1. Tea Leaves
2. Sugar
3. Water
4. Coffee Powder
5. Butter
6. Eggs
7. Vanilla Essence
8. Flour
9. Baking Powder
10. Milk
11. Bananas
12. Peanut Butter
13. Ice Cubes
============================================================

============================================================
Recipes containing 'Water':
============================================================
[Tea and Coffee recipes displayed]

============================================================
Recipes containing 'Sugar':
============================================================
[All 4 recipes displayed]

============================================================
Recipes containing 'Bananas':
============================================================
[Banana Smoothie recipe displayed]
```

---

## 💡 Key Learnings

### OOP Concepts Mastered

1. **Classes and Objects**
   - Classes as blueprints
   - Objects as instances with unique data

2. **Encapsulation**
   - Bundling data and methods
   - Controlled access through getters/setters

3. **Polymorphism**
   - Operator overloading (`__sub__`, `__gt__`, etc.)
   - Method overriding
   - Duck typing

4. **Special Methods**
   - `__init__`: Constructor
   - `__str__`: String representation
   - `__sub__`: Subtraction operator
   - Comparison operators (`__gt__`, `__eq__`, etc.)

5. **Variable-Length Arguments**
   - Using `*args` for flexible method parameters
   - Iterating through variable arguments

6. **Class Variables**
   - Shared data across all instances
   - Accessed via `ClassName.variable`

### Design Principles Applied

- **Single Responsibility**: Each method has one clear purpose
- **DRY (Don't Repeat Yourself)**: Reusable methods and class structure
- **Encapsulation**: Data protection through methods
- **Clear Interfaces**: Well-defined public methods

---

## 🔍 Code Examples

### Creating and Using Objects

```python
# Create a recipe
tea = Recipe("Tea")

# Set properties
tea.set_cooking_time(5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")

# Get information
print(tea.get_name())        # Tea
print(tea.get_difficulty())  # Easy
print(tea)                   # Formatted recipe display
```

### Operator Overloading

```python
# Height subtraction
height1 = Height(5, 10)
height2 = Height(3, 9)
result = height1 - height2   # Uses __sub__ method
print(result)                # 2' 1"

# Height comparison
print(height1 > height2)     # Uses __gt__ method: True
print(height1 == height2)    # Uses __eq__ method: False
```

### Class Variables

```python
# Access class variable
print(Recipe.all_ingredients)  # List of all unique ingredients

# Class variable updated automatically when adding ingredients
tea.add_ingredients("Tea Leaves", "Sugar")
coffee.add_ingredients("Coffee Powder", "Sugar")  # Sugar not duplicated
print(Recipe.all_ingredients)  # ['Tea Leaves', 'Sugar', 'Coffee Powder']
```

---

## 📸 Screenshots

Screenshots documenting the execution and output of all tasks are located in:
- `1.5-Practice Task 1/screenshot/`
- `1.5-Practice Task 2/screenshot/`
- `1.5-Practice Task 3/screenshot/`
- `main-task/screenshot/`

---

## 🎯 Completion Checklist

- ✅ Practice Task 1: Shopping List class implemented
- ✅ Practice Task 2: Height subtraction operator overloaded
- ✅ Practice Task 3: Height comparison operators implemented
- ✅ Main Task: Recipe OOP application completed
- ✅ All code tested and verified
- ✅ Learning journal written
- ✅ Learning journey documented
- ✅ README documentation created
- ✅ Screenshots captured
- ✅ Code follows PEP 8 style guidelines
- ✅ All files organized properly

---

## 📚 Additional Resources

- [Python Official Documentation - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/)
- [Python Special Methods Guide](https://docs.python.org/3/reference/datamodel.html#special-method-names)

---

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | October 19, 2025 | Initial completion of all tasks |

---

## 👨‍💻 Author

**Sourav Das**  
Python for Web Developers Course  
October 2025

---

## 📝 Notes

This exercise marks a significant transition from procedural to object-oriented programming. The concepts learned here form the foundation for building complex applications, particularly web applications with frameworks like Django that heavily rely on OOP principles.

**Next Steps:** Apply these OOP concepts in Exercise 1.6 and beyond, building increasingly complex applications with proper object-oriented design.

---

**Exercise Status:** ✅ **COMPLETED**  
**Date Completed:** October 19, 2025
