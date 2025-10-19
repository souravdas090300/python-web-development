# Exercise 1.3 — Core Python Operations

**Student:** Sourav Das  
**Course:** Python for Web Developers  
**Achievement:** 1 - CLI Recipe App  
**Date:** October 16, 2025  
**Python Version:** 3.14.0  
**Time Investment:** 10 hours

---

## � Exercise Overview

This exercise covers **essential Python programming concepts** for building dynamic applications: **scripts vs interactive shell**, **conditionals (if-elif-else)**, **loops (for/while)**, and **functions** with parameters and return values.

**Key Topics:**
- Scripts (.py files) vs IPython interactive shell - when to use each
- Conditional statements with compound conditions (and/or operators)
- For loops with range() and iterating over collections
- While loops for condition-based iteration
- Functions with parameters, return values, and docstrings
- Multi-condition logic for complex decision making
- Data structure operations (lists, dictionaries)

**Main Task:** Build a complete **Recipe Management System** that:
- Collects multiple recipes from user input
- Uses `take_recipe()` function to encapsulate input logic
- Calculates difficulty automatically (4 levels: Easy, Medium, Intermediate, Hard)
- Collects unique ingredients across all recipes
- Displays results with alphabetically sorted ingredients

All mentor recommendations have been implemented, including improved `range()` usage and non-destructive sorting with `sorted()`.

---

## 🎯 Learning Objectives

1. Understand when to use scripts vs interactive shell for different tasks
2. Implement multi-condition logic with if-elif-else statements
3. Master both for loops (count-based) and while loops (condition-based)
4. Create reusable functions with parameters and return values
5. Design clean, modular code following DRY (Don't Repeat Yourself) principle
6. Work with compound conditions (and/or operators)
7. Perform non-destructive data operations
8. Collect and display unique values from nested structures

---

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
- Alphabetically sorted ingredient display (preserving original list)

**Difficulty Logic:**
- **Easy:** < 10 min cooking + < 4 ingredients
- **Medium:** < 10 min cooking + ≥ 4 ingredients
- **Intermediate:** ≥ 10 min cooking + < 4 ingredients
- **Hard:** ≥ 10 min cooking + ≥ 4 ingredients

---

## 📁 Project Structure

```
Exercise 1.3/
├── main-task/
│   ├── Exercise_1.3.py          # Main Recipe Management System
│   ├── learning_journal.md      # Technical learning documentation
│   ├── learning_journey.md      # Personal growth narrative
│   └── README.md                # This file
├── screenshots/                 # Program execution screenshots
│   ├── recipe_input_example.png
│   ├── difficulty_calculation.png
│   ├── unique_ingredients.png
│   └── complete_output.png
└── practice-tasks/              # 3 practice task solutions
    ├── 1.3-Practice Task 1/
    │   └── practice1_calculator.py
    ├── 1.3-Practice Task 2/
    │   └── practice2_top_scores.py
    └── 1.3-Practice Task 3/
        └── practice3_loop_comparison.py
```

---

## � Screenshots Checklist

### Main Task Screenshots

- [x] **User Input:** Collecting recipe information (name, cooking time, ingredients)
- [x] **take_recipe() Function:** Code showing function definition and implementation
- [x] **Recipe Display:** Output showing all recipes with calculated difficulty levels
- [x] **Difficulty Calculation:** Examples of Easy, Medium, Intermediate, and Hard recipes
- [x] **Unique Ingredients:** Alphabetically sorted ingredient list (using `sorted()`)
- [x] **Complete Execution:** Full program run from start to finish

### Practice Task Screenshots

- [x] **Practice 1:** Calculator with if-elif-else (arithmetic operations)
- [x] **Practice 2:** Top 3 test scores using for loop
- [x] **Practice 3:** While loop vs for loop comparison

### Code Quality Screenshots

- [x] Mentor feedback implemented: `range(1, n+1)` instead of `range(n)` with `i+1`
- [x] Mentor feedback implemented: `sorted()` instead of `.sort()` for non-destructive sorting

---

## �🚀 How to Run

### Prerequisites
- Python 3.14.0 installed
- Virtual environment activated (optional but recommended)

### Run the Main Script

```powershell
cd "Exercise 1.3"
python Exercise_1.3.py
```

### Example Usage

```
============================================================
RECIPE MANAGEMENT SYSTEM
============================================================

How many recipes would you like to enter? 2

============================================================
RECIPE 1
============================================================

Enter the recipe name: Tea
Enter the cooking time (in minutes): 5
How many ingredients does this recipe have? 3
  Enter ingredient 1: Tea Leaves
  Enter ingredient 2: Water
  Enter ingredient 3: Sugar

✓ Recipe 'Tea' added successfully!

============================================================
RECIPE 2
============================================================

Enter the recipe name: Coffee
Enter the cooking time (in minutes): 7
How many ingredients does this recipe have? 4
  Enter ingredient 1: Coffee Powder
  Enter ingredient 2: Water
  Enter ingredient 3: Milk
  Enter ingredient 4: Sugar

✓ Recipe 'Coffee' added successfully!

============================================================
ALL RECIPES WITH DIFFICULTY LEVELS
============================================================

Recipe: Tea
Cooking Time (min): 5
Ingredients:
  - Tea Leaves
  - Water
  - Sugar
Difficulty: Easy

Recipe: Coffee
Cooking Time (min): 7
Ingredients:
  - Coffee Powder
  - Water
  - Milk
  - Sugar
Difficulty: Medium

============================================================
ALL INGREDIENTS (Alphabetical Order)
============================================================

- Coffee Powder
- Milk
- Sugar
- Tea Leaves
- Water

============================================================
Thank you for using the Recipe Management System!
============================================================
```

---

## 💡 Key Features

### 1. take_recipe() Function
Encapsulates all recipe input logic:
```python
def take_recipe():
    """
    Takes user input for a recipe and returns a dictionary
    containing name, cooking_time, and ingredients.
    """
    name = input("\nEnter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    
    ingredients = []
    n_ingredients = int(input("How many ingredients does this recipe have? "))
    
    for i in range(1, n_ingredients + 1):
        ingredient = input(f"  Enter ingredient {i}: ")
        ingredients.append(ingredient)
    
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    
    return recipe
```

### 2. Difficulty Calculation
Multi-condition logic for accurate difficulty assessment:
```python
if cooking_time < 10 and num_ingredients < 4:
    difficulty = "Easy"
elif cooking_time < 10 and num_ingredients >= 4:
    difficulty = "Medium"
elif cooking_time >= 10 and num_ingredients < 4:
    difficulty = "Intermediate"
else:  # cooking_time >= 10 and num_ingredients >= 4
    difficulty = "Hard"
```

### 3. Unique Ingredient Collection
Prevents duplicates using conditional membership check:
```python
for ingredient in recipe['ingredients']:
    if ingredient not in ingredients_list:
        ingredients_list.append(ingredient)
```

### 4. Non-Destructive Sorting
Preserves original data using `sorted()` function:
```python
# Create sorted copy to preserve original ingredients_list
sorted_ingredients_list = sorted(ingredients_list)
```

---

## ✅ Mentor Recommendations Implemented

### Recommendation 1: Improved for loop range
**Before:**
```python
for i in range(n_ingredients):
    ingredient = input(f"  Enter ingredient {i+1}: ")
```

**After:**
```python
for i in range(1, n_ingredients + 1):
    ingredient = input(f"  Enter ingredient {i}: ")
```
**Benefit:** Cleaner code - no need for `i+1` arithmetic inside the loop

---

### Recommendation 2: Use sorted() instead of .sort()
**Before:**
```python
ingredients_list.sort()
for ingredient in ingredients_list:
    print(f"- {ingredient}")
```

**After:**
```python
sorted_ingredients_list = sorted(ingredients_list)
for ingredient in sorted_ingredients_list:
    print(f"- {ingredient}")
```
**Benefit:** Preserves original `ingredients_list` unchanged - follows best practice of not modifying original data

---

## 📝 Key Learnings

### 1. Scripts vs Interactive Shell
- **Scripts (.py files):** Reusable, shareable code that can be run repeatedly
- **Interactive Shell (IPython):** One-time commands, testing, exploration
- **When to use scripts:** Multi-step programs, data that needs to persist, code to share

### 2. Conditionals (if-elif-else)
- Multi-condition logic with compound conditions (`and`, `or`)
- Exhaustive condition chains to handle all cases
- Proper indentation for code blocks

### 3. For Loops
- Iterator-based loops with `range(start, stop)`
- Accessing list/dictionary items during iteration
- Nested loops for multi-level processing

### 4. While Loops
- Condition-based loops
- Manual iteration management (incrementing counters)
- Use when number of iterations unknown upfront

### 5. Functions
- Reusable code blocks with `def`
- Parameters for input, `return` for output
- Docstrings for documentation
- Variable scope (local vs global)

---

## 🎯 Practice Task Solutions

### Practice Task 1: Calculator
Simple calculator using if-elif-else:
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+ or -): ")

if operator == "+":
    result = a + b
    print(f"Result: {result}")
elif operator == "-":
    result = a - b
    print(f"Result: {result}")
else:
    print("Error: Unknown operator")
```

### Practice Task 2: Top 3 Scores
Using for loop to find highest scores:
```python
scores = [78, 92, 88, 95, 67, 89, 91]
top_scores = []

for i in range(3):
    max_score = max(scores)
    top_scores.append(max_score)
    scores.remove(max_score)

print(f"Top 3 scores: {top_scores}")
```

### Practice Task 3: Loop Comparison
Demonstrating while vs for loops:
```python
# Using while loop
i = 0
while i < 5:
    print(f"Number: {i}")
    i += 1

# Using for loop
for i in range(5):
    print(f"Number: {i}")
```

---

## 📦 Deliverables

### Main Task Files

1. **Exercise_1.3.py** - Complete Recipe Management System
   - `take_recipe()` function with docstring
   - Difficulty calculation logic (4 levels)
   - Unique ingredient collection
   - Alphabetically sorted display
   - All mentor recommendations implemented

2. **Screenshots** - Complete program documentation
   - User input examples
   - Difficulty calculation demonstrations
   - Sorted ingredient output
   - Practice task solutions

3. **learning_journal.md** - Comprehensive technical documentation
   - 3 detailed reflection questions answered:
     - Scripts vs Interactive Shell
     - For Loops vs While Loops
     - Functions Importance
   - Practice task reflections
   - Challenges and solutions documented

4. **learning_journey.md** - Personal coding journey
   - Building the Recipe System story
   - Learning progression narrative
   - Time investment (10 hours)

5. **README.md** - This complete documentation
   - Feature explanations
   - Code examples
   - Testing instructions
   - Mentor feedback implementation

### Practice Task Files (3 Total)

1. **Practice Task 1** - Calculator with if-elif-else
   - Arithmetic operations (+, -)
   - Input validation concepts

2. **Practice Task 2** - Top 3 test scores
   - For loop with range()
   - Finding maximum values

3. **Practice Task 3** - Loop comparison
   - While loop implementation
   - For loop implementation
   - Comparison of both approaches

---

## 🧪 Testing

### Quick Test (Automated)
```powershell
echo "1`nTea`n5`n3`nTea Leaves`nWater`nSugar" | python Exercise_1.3.py
```

### Manual Test Cases

**Test 1: Easy Recipe**
- Cooking time: 5 minutes
- Ingredients: 3
- Expected difficulty: Easy

**Test 2: Medium Recipe**
- Cooking time: 8 minutes
- Ingredients: 5
- Expected difficulty: Medium

**Test 3: Intermediate Recipe**
- Cooking time: 15 minutes
- Ingredients: 2
- Expected difficulty: Intermediate

**Test 4: Hard Recipe**
- Cooking time: 30 minutes
- Ingredients: 8
- Expected difficulty: Hard

---

## 🔍 Code Quality

### Best Practices Followed:
- ✅ Clear, descriptive variable names
- ✅ Function docstrings
- ✅ Consistent formatting and indentation
- ✅ Comments explaining complex logic
- ✅ Non-destructive data operations
- ✅ Proper code organization

### Mentor Feedback Addressed:
- ✅ Simplified for loop range
- ✅ Preserved original data with `sorted()`
- ✅ Clean, maintainable code structure

---

## 🚧 Future Improvements

### Input Validation (Coming in Future Exercises)
```python
# Future: Handle non-numeric input
try:
    cooking_time = int(input("Enter cooking time (in minutes): "))
except ValueError:
    print("Error: Please enter a valid number")
```

### Alternative Approaches Mentioned by Mentor

**Using `set` for unique ingredients:**
```python
# Alternative: Using set to automatically handle uniqueness
ingredients_set = set()
for recipe in recipes_list:
    ingredients_set.update(recipe['ingredients'])
sorted_ingredients = sorted(ingredients_set)
```

**Using `dict.fromkeys()` for uniqueness:**
```python
# Alternative: Dictionary keys are unique
ingredients_dict = {}
for recipe in recipes_list:
    for ingredient in recipe['ingredients']:
        ingredients_dict[ingredient] = True
sorted_ingredients = sorted(ingredients_dict.keys())
```

---

## 📚 Additional Resources

- [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Conditionals](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python Loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python sorted() vs list.sort()](https://docs.python.org/3/howto/sorting.html)

---

**Repository:** [python-web-development](https://github.com/souravdas090300/python-web-development)  
**Author:** Sourav Das  
**Exercise:** 1.3 - Core Python Operations  
**Status:** ✅ Complete - All Mentor Recommendations Implemented

---

## 🎯 Next Steps

**Immediate:** Move to Exercise 1.4 (File Operations - Reading/Writing Data)  
**Achievement 1 Progress:** 3/7 exercises complete

### Skills Gained in This Exercise

✅ Understanding scripts vs interactive shell workflows  
✅ Implementing multi-condition logic with if-elif-else  
✅ Mastering for loops with `range()` for count-based iteration  
✅ Using while loops for condition-based iteration  
✅ Creating reusable functions with parameters and return values  
✅ Designing modular code following DRY principle  
✅ Working with compound conditions (and/or operators)  
✅ Performing non-destructive data operations (`sorted()` vs `.sort()`)  
✅ Collecting unique values from nested structures  

### Ready for Next Exercise

With control flow and functions mastered, you're now prepared to:
- Work with file I/O (reading from and writing to files)
- Persist recipe data between program runs
- Handle errors with try-except blocks
- Use pickle for data serialization
- Build more robust, production-ready applications

### Mentor Feedback Successfully Implemented

✅ **Improved range() usage:** `range(1, n+1)` instead of `range(n)` with `i+1`  
✅ **Non-destructive sorting:** `sorted()` function instead of `.sort()` method  
✅ **Clean code structure:** Function encapsulation following best practices  
✅ **Professional documentation:** Comprehensive README and learning journals
