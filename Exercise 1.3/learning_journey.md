# Learning Journal - Exercise 1.3

**Date:** October 16, 2025  
**Exercise:** Core Python Operations - Scripts, Conditionals, Loops, Functions  
**Student:** Sourav Das

---

## 📚 What I Learned

### Python Scripts
- **Scripts vs Shell:** Scripts allow saving and running multiple lines of code
- **File Extension:** `.py` files are Python scripts
- **Execution:** Run with `python filename.py`
- **Variables:** Cleared after script execution (clean slate each run)
- **Advantages:** Easier debugging, can modify and re-run, no variable confusion

### Conditionals (if-elif-else)
- **Purpose:** Make decisions based on conditions
- **Syntax:** Uses `:` and indentation (no curly braces like JavaScript)
- **if:** Checks first condition
- **elif:** Checks alternative conditions
- **else:** Catches all other cases
- **Comparison Operators:** `<`, `>`, `<=`, `>=`, `==`, `!=`
- **Boolean Operators:** `and`, `or`, `not`

### For Loops
- **Purpose:** Iterate through sequences
- **Syntax:** `for element in sequence:`
- **range() Function:** `range(start, end, step)` creates number sequences
- **Usage:** When you know number of iterations
- **Example:** Printing first N elements, iterating through lists

### While Loops
- **Purpose:** Repeat while condition is True
- **Syntax:** `while condition:`
- **Manual Control:** Must update condition variable yourself
- **Risk:** Infinite loops if condition never becomes False
- **Break:** Exit loop early with `break`
- **Continue:** Skip to next iteration with `continue`

### Functions
- **Definition:** `def function_name(parameters):`
- **Parameters:** Values passed into functions
- **Return:** Send values back with `return`
- **Benefits:** Code reusability, organization, avoid repetition
- **Variable Scope:** Local vs global variables

### Data Structures Review
- **Lists:** Ordered, mutable collections `[]`
- **Dictionaries:** Key-value pairs `{}`
- **Nested Structures:** Lists of dictionaries
- **List Methods:** `append()`, `sort()`, `in` keyword

---

## 💡 Key Insights

### Recipe Management System
Created a complete application that:
- Collects user input for multiple recipes
- Stores data in structured format (dictionaries)
- Calculates difficulty dynamically
- Displays organized output

### Difficulty Calculation Logic
Implemented multi-condition logic:

| Cooking Time | Ingredients | Difficulty |
|--------------|-------------|------------|
| < 10 min | < 4 | Easy |
| < 10 min | >= 4 | Medium |
| >= 10 min | < 4 | Intermediate |
| >= 10 min | >= 4 | Hard |

**Code Implementation:**
```python
if cooking_time < 10 and num_ingredients < 4:
    difficulty = "Easy"
elif cooking_time < 10 and num_ingredients >= 4:
    difficulty = "Medium"
elif cooking_time >= 10 and num_ingredients < 4:
    difficulty = "Intermediate"
else:
    difficulty = "Hard"
```

### Function Design
The `take_recipe()` function demonstrates:
- **Encapsulation:** All input logic in one place
- **Return Values:** Returns dictionary with recipe data
- **Reusability:** Called multiple times without rewriting code

### Data Collection Pattern
```python
# Collect unique ingredients
for ingredient in recipe['ingredients']:
    if ingredient not in ingredients_list:
        ingredients_list.append(ingredient)
```

---

## 🎯 Challenges & Solutions

### Challenge 1: Understanding Script Execution
**Problem:** Initially confused about running Python code  
**Solution:** Learned distinction between:
- PowerShell commands (shell operations)
- Python code (must be in .py file)
- Running scripts: `python filename.py`

### Challenge 2: File Naming
**Problem:** File named "code Exercise_1.3.py" with spaces  
**Solution:** Used quotes when running: `python "code Exercise_1.3.py"`  
**Learning:** Avoid spaces in filenames for easier use

### Challenge 3: Nested Loops
**Problem:** Understanding loop within loop  
**Solution:** 
- Outer loop: iterates through recipes
- Inner loop: iterates through ingredients of each recipe
**Learning:** Each loop has its own iteration variable and scope

### Challenge 4: Conditional Logic
**Problem:** Four different difficulty conditions  
**Solution:** Used if-elif-else chain with `and` operators  
**Learning:** Conditions evaluated top-to-bottom, first match wins

---

## 🚀 Practice Tasks Completed

### Practice Task 1: If-Else Statements (Calculator)
**Objective:** Create calculator with + and - operators

**Implementation:**
- Used `input()` for user data
- `float()` for type conversion
- if-elif-else for operator selection
- else for error handling

**Key Learning:** Conditional flow control for decision making

### Practice Task 2: For Loops (Test Scores)
**Objective:** Print top 3 scores from a list

**Steps:**
1. Created list: `[45, 23, 89, 78, 98, 55, 74, 87, 95, 75]`
2. Sorted descending: `test_scores.sort(reverse=True)`
3. Used `range(3)` to print first 3

**Key Learning:** Combining list methods with loops

### Practice Task 3: While vs For Loops
**Objective:** Rewrite print statements using loops

**Original:**
```python
print(10)
print(20)
...
```

**For Loop:**
```python
for num in range(10, 60, 10):
    print(num)
```

**While Loop:**
```python
num = 10
while num <= 50:
    print(num)
    num += 10
```

**Key Learning:** Different loops for different scenarios

---

## 📈 Progress Assessment

**What I can do now:**
- ✅ Write and run Python scripts
- ✅ Create custom functions with parameters and return values
- ✅ Implement conditional logic (if-elif-else)
- ✅ Use for loops with range()
- ✅ Use while loops with proper exit conditions
- ✅ Work with nested data structures (list of dictionaries)
- ✅ Process user input and convert types
- ✅ Calculate values based on multiple conditions
- ✅ Organize code with functions
- ✅ Debug script errors

**What I want to improve:**
- Error handling with try-except blocks
- More complex function parameters (default values, keyword args)
- List comprehensions for concise code
- File I/O (reading/writing data to files)
- Working with external libraries

---

## 💭 Reflections

**Most Valuable Concept:**
Functions - They transform repetitive code into reusable, organized blocks. The `take_recipe()` function made the main code much cleaner and easier to understand.

**Most Challenging Concept:**
Nested loops and understanding variable scope. Keeping track of which loop iteration you're in and which variables are accessible required careful thinking.

**Real-World Application:**
This recipe management system is a practical example of CRUD operations (Create, Read). Could be extended to:
- Update recipes (modify existing)
- Delete recipes
- Save/load from files
- Search recipes by ingredient
- Filter by difficulty

**Coding Best Practices Learned:**
- Meaningful variable names (`recipe`, not `r`)
- Functions for repeated operations
- Comments to explain logic
- Consistent indentation (4 spaces)
- Clear user prompts

---

## 🎓 Concepts Connection

**How This Builds on Exercise 1.2:**
- Exercise 1.2: Data structures (lists, dictionaries)
- Exercise 1.3: Using those structures with logic and functions
- Building recipes uses dictionaries (from 1.2)
- Storing recipes uses lists (from 1.2)
- Added: Functions, conditionals, loops to process the data

**Preparing for Future Exercises:**
- File I/O will let us save recipes permanently
- Error handling will make programs more robust
- Classes/objects will organize recipe data better
- Database integration for real applications

---

## 📝 Code Examples to Remember

### Function with Return Value
```python
def take_recipe():
    # Collect data
    recipe = {'name': name, 'cooking_time': time, 'ingredients': list}
    return recipe
```

### Nested Loop
```python
for recipe in recipes_list:
    for ingredient in recipe['ingredients']:
        # Process each ingredient
```

### Multi-Condition Logic
```python
if condition1 and condition2:
    # Both must be true
elif condition3 or condition4:
    # At least one must be true
else:
    # None of the above
```

---

## 🚀 Next Steps

**For Exercise 1.4:**
- File operations (open, read, write, close)
- Exception handling (try-except)
- Persisting data between runs

**Personal Practice Goals:**
- Write more functions in daily tasks
- Practice nested loops with different data
- Experiment with list comprehensions
- Read Python documentation

---

**Hours Spent:** ~3-4 hours  
**Completion Date:** October 16, 2025  
**Status:** ✅ Complete - All practice tasks and main task finished

---

## ✨ Achievement Summary

**Completed:**
- ✅ Practice Task 1: Calculator with if-else
- ✅ Practice Task 2: Top 3 scores with for loop
- ✅ Practice Task 3: While loop practice
- ✅ Main Task: Recipe Management System
- ✅ Learning Journal Documentation
- ✅ Screenshots for all tasks

**Skills Demonstrated:**
- Python script creation and execution
- Function definition and usage
- Conditional logic implementation
- Loop iteration (for and while)
- Data structure manipulation
- User input processing
- Code organization and documentation
