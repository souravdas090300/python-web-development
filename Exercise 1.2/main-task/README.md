# Exercise 1.2 — Data Types and Structures

**Student:** Sourav Das  
**Course:** Python for Web Developers  
**Achievement:** 1 - CLI Recipe App  
**Date:** October 15, 2025  
**Python Version:** 3.14.0  
**Time Investment:** 6 hours

---

## � Exercise Overview

This exercise focuses on **Python data types and structures**, teaching how to store and organize recipe information effectively. Students learn to choose appropriate data structures (strings, integers, lists, tuples, dictionaries) based on requirements and justify their decisions professionally.

**Key Topics:**
- Python data types: strings, integers, lists, dictionaries
- Data structure selection and justification
- Mutable vs immutable data structures
- Nested data structures (lists of dictionaries)
- Data access patterns and best practices
- Working in IPython interactive shell

**Main Task:** Create 5 recipes using dictionaries stored in a list, demonstrating proper data structure selection with written justifications (75 and 60 words).

---

## 🎯 Learning Objectives

1. Understand Python's core data types and their characteristics
2. Choose appropriate data structures for specific use cases
3. Justify data structure decisions with technical reasoning
4. Work with nested data structures (list of dictionaries)
5. Access and manipulate structured data effectively
6. Use IPython for interactive data exploration

------

## 🎯 Requirements

1. Create a recipe structure with: name (str), cooking_time (int), ingredients (list)
2. Choose appropriate data structure for individual recipes
3. Create an outer structure to hold all recipes
4. Generate 5 recipes total
5. Print ingredients of each recipe
6. Provide written justifications (75 and 60 words) for data structure choices

---

### Individual Recipe Structure: **Dictionary**

**Chosen Structure:** Dictionary (`dict`)

**Justification (75 words):**
I chose a dictionary for individual recipes because it provides clear, labeled access to recipe attributes through keys (name, cooking_time, ingredients). Unlike tuples, dictionaries are mutable, allowing future updates to recipes. Compared to lists, dictionaries offer better readability and self-documenting code—accessing `recipe['name']` is more intuitive than `recipe[0]`. The key-value structure naturally maps to recipe attributes, making the code maintainable and extensible for future features like difficulty levels or ratings.

### Outer Structure for All Recipes: **List**

**Chosen Structure:** List (`list`)

**Justification (60 words):**
I selected a list for the outer `all_recipes` structure because it provides a sequential, ordered collection that's easy to iterate through. Lists are mutable, allowing recipes to be added, removed, or reordered. They support indexing and slicing for accessing specific recipes, and can dynamically grow as more recipes are added. This flexibility is ideal for a recipe collection that will expand over time.

## 📝 Step-by-Step Implementation

### Step 1: Create recipe_1 (Tea)

```python
recipe_1 = {
    'name': 'Tea',
    'cooking_time': 5,
    'ingredients': ['Tea leaves', 'Sugar', 'Water']
}
```

**Data Structure:** Dictionary with:
- `name`: string
- `cooking_time`: integer (minutes)
- `ingredients`: list of strings

### Step 2: Create all_recipes and add recipe_1

```python
all_recipes = []
all_recipes.append(recipe_1)
```

or simply:

```python
all_recipes = [recipe_1]
```

### Step 3: Create recipe_2 (Coffee)

```python
recipe_2 = {
    'name': 'Coffee',
    'cooking_time': 7,
    'ingredients': ['Coffee powder', 'Sugar', 'Milk', 'Water']
}
all_recipes.append(recipe_2)
```

### Step 4: Create recipe_3 (Scrambled Eggs)

```python
recipe_3 = {
    'name': 'Scrambled Eggs',
    'cooking_time': 10,
    'ingredients': ['Eggs', 'Butter', 'Salt', 'Pepper']
}
all_recipes.append(recipe_3)
```

### Step 5: Create recipe_4 (Pasta)

```python
recipe_4 = {
    'name': 'Pasta',
    'cooking_time': 15,
    'ingredients': ['Pasta', 'Tomato sauce', 'Garlic', 'Olive oil', 'Parmesan']
}
all_recipes.append(recipe_4)
```

### Step 6: Create recipe_5 (Oatmeal)

```python
recipe_5 = {
    'name': 'Oatmeal',
    'cooking_time': 8,
    'ingredients': ['Oats', 'Milk', 'Honey', 'Banana', 'Cinnamon']
}
all_recipes.append(recipe_5)
```

### Step 7: Print Ingredients of Each Recipe

```python
# Print ingredients for recipe_1
print(recipe_1['ingredients'])

# Print ingredients for recipe_2
print(recipe_2['ingredients'])

# Print ingredients for recipe_3
print(recipe_3['ingredients'])

# Print ingredients for recipe_4
print(recipe_4['ingredients'])

# Print ingredients for recipe_5
print(recipe_5['ingredients'])
```

**Alternative (using loop):**

```python
for recipe in all_recipes:
    print(recipe['ingredients'])
```

---

## � Project Structure

```
Exercise 1.2/
├── main-task/
│   ├── Exercise_1.2.py          # Main script (IPython commands)
│   ├── learning_journal.md      # Technical learning documentation
│   ├── learning_journey.md      # Personal growth narrative
│   └── README.md                # This file
├── screenshots/                 # Task step screenshots
│   ├── step1_recipe1.png
│   ├── step2_all_recipes.png
│   ├── step3_recipe2.png
│   ├── step4_recipe3.png
│   ├── step5_recipe4.png
│   ├── step6_recipe5.png
│   └── step7_print_ingredients.png
└── practice-tasks/              # 5 practice task solutions
    ├── practice1_compound_interest.py
    ├── practice2_tuples.py
    ├── practice3_lists.py
    ├── practice4_strings.py
    └── practice5_dictionaries.py
```

---

## 🚀 How to Use

### Run in IPython (Recommended)

This exercise is designed to be completed in the IPython interactive shell:

```powershell
# Activate your virtual environment
.\cf-python-base\Scripts\Activate.ps1

# Launch IPython
ipython

# Then run the code step by step (see Quick Commands section below)
```

### Quick Commands for IPython

Complete sequence to create all 5 recipes and print their ingredients:

```python
# Step 1: Create recipe_1
recipe_1 = {
    'name': 'Tea',
    'cooking_time': 5,
    'ingredients': ['Tea leaves', 'Sugar', 'Water']
}

# Step 2: Create all_recipes
all_recipes = [recipe_1]

# Step 3: Create and add recipe_2
recipe_2 = {
    'name': 'Coffee',
    'cooking_time': 7,
    'ingredients': ['Coffee powder', 'Sugar', 'Milk', 'Water']
}
all_recipes.append(recipe_2)

# Step 4: Create and add recipe_3
recipe_3 = {
    'name': 'Scrambled Eggs',
    'cooking_time': 10,
    'ingredients': ['Eggs', 'Butter', 'Salt', 'Pepper']
}
all_recipes.append(recipe_3)

# Step 5: Create and add recipe_4
recipe_4 = {
    'name': 'Pasta',
    'cooking_time': 15,
    'ingredients': ['Pasta', 'Tomato sauce', 'Garlic', 'Olive oil', 'Parmesan']
}
all_recipes.append(recipe_4)

# Step 6: Create and add recipe_5
recipe_5 = {
    'name': 'Oatmeal',
    'cooking_time': 8,
    'ingredients': ['Oats', 'Milk', 'Honey', 'Banana', 'Cinnamon']
}
all_recipes.append(recipe_5)

# Step 7: Print all ingredients
print(recipe_1['ingredients'])
print(recipe_2['ingredients'])
print(recipe_3['ingredients'])
print(recipe_4['ingredients'])
print(recipe_5['ingredients'])
```

---

## 📸 Screenshots Checklist

### Required Screenshots (7 Steps)

- [x] **Step 1:** Creating recipe_1 (Tea) dictionary
- [x] **Step 2:** Creating all_recipes list and adding recipe_1
- [x] **Step 3:** Creating and adding recipe_2 (Coffee)
- [x] **Step 4:** Creating and adding recipe_3 (Scrambled Eggs)
- [x] **Step 5:** Creating and adding recipe_4 (Pasta)
- [x] **Step 6:** Creating and adding recipe_5 (Oatmeal)
- [x] **Step 7:** Printing ingredients of all 5 recipes

### Verification Screenshots

- [x] Running `len(all_recipes)` showing 5
- [x] Running `print(all_recipes)` showing complete structure
- [x] Accessing individual recipe elements (e.g., `all_recipes[0]['name']`)

---

## ✅ Verification

To verify your all_recipes structure:

```python
# Check length
len(all_recipes)  # Should return 5

# Check structure
print(all_recipes)

# Access individual recipes
print(all_recipes[0]['name'])  # Should print: Tea
print(all_recipes[4]['cooking_time'])  # Should print: 8
```

## 📊 Final Structure

```python
all_recipes = [
    {
        'name': 'Tea',
        'cooking_time': 5,
        'ingredients': ['Tea leaves', 'Sugar', 'Water']
    },
    {
        'name': 'Coffee',
        'cooking_time': 7,
        'ingredients': ['Coffee powder', 'Sugar', 'Milk', 'Water']
    },
    {
        'name': 'Scrambled Eggs',
        'cooking_time': 10,
        'ingredients': ['Eggs', 'Butter', 'Salt', 'Pepper']
    },
    {
        'name': 'Pasta',
        'cooking_time': 15,
        'ingredients': ['Pasta', 'Tomato sauce', 'Garlic', 'Olive oil', 'Parmesan']
    },
    {
        'name': 'Oatmeal',
        'cooking_time': 8,
        'ingredients': ['Oats', 'Milk', 'Honey', 'Banana', 'Cinnamon']
    }
]
```

## 📦 Deliverables

### Files to Submit

1. **Screenshots** (7 required steps + verification screenshots)
   - All steps clearly documented
   - Organized in `screenshots/` folder

2. **Exercise_1.2.py** (optional) - Script version of IPython commands
   - Contains all recipe creation code
   - Can be run as standalone script

3. **Data Structure Justifications** - Written explanations (included in this README)
   - Dictionary justification (75 words minimum)
   - List justification (60 words minimum)

4. **learning_journal.md** - Technical learning documentation
   - Reflection questions on iPython benefits
   - Data types analysis (immutable vs mutable)
   - Lists vs tuples comparison
   - Flashcard structure justification

5. **learning_journey.md** - Personal growth narrative
   - Learning story and insights
   - Time investment tracking

6. **README.md** - This comprehensive documentation
   - Data structure decisions explained
   - Complete implementation guide
   - Quick commands reference

### Practice Tasks (5 Total)

- Practice 1: Compound Interest calculation (File I/O, Type Conversion)
- Practice 2: Tuple operations and slicing
- Practice 3: List manipulation and sorting
- Practice 4: String slicing and indexing
- Practice 5: Dictionary creation and access

---

## 🔍 Key Learnings

- **Dictionaries** provide labeled, self-documenting access to data
- **Lists** are ideal for sequential, ordered collections
- **Data structure choice** impacts code readability and maintainability
- **Mutability** allows for flexible data management
- **Nested structures** (list of dictionaries) enable complex data organization

---

## 🎯 Practice Tasks Summary

This exercise includes 5 code practice tasks to master Python data structures:

### Practice Task 1: Types & Calculations
- **Topic:** File I/O, Type Conversion, Mathematical Operations
- **Task:** Calculate compound interest from values in a text file
- **Key Learning:** Reading files, converting strings to floats, exponentiation operator

### Practice Task 2: Tuples
- **Topic:** Tuple Creation, Slicing, Built-in Functions
- **Task:** Store world population data and slice every 3rd element
- **Key Learning:** Tuple slicing with step parameter, `max()` function

### Practice Task 3: Lists
- **Topic:** List Manipulation, Sorting
- **Task:** Create Ford vehicle lineup, add Mustang, sort alphabetically
- **Key Learning:** `append()` method, `sort()` method, list mutability

### Practice Task 4: Strings
- **Topic:** String Slicing, Indexing
- **Task:** Predict results of various string slicing operations
- **Key Learning:** Negative indices, step parameter, reverse slicing

### Practice Task 5: Dictionaries
- **Topic:** Dictionary Creation, Key-Value Pairs
- **Task:** Create month number to month name dictionary
- **Key Learning:** Dictionary keys, values, accessing by key

---

**Repository:** [python-web-development](https://github.com/souravdas090300/python-web-development)  
**Exercise:** 1.2 - Data Types and Structures  
**Completion Date:** October 16, 2025  
**Status:** ✅ Complete

---

## 🎯 Next Steps

**Immediate:** Move to Exercise 1.3 (Core Python Operations - Scripts, Conditionals, Loops, Functions)  
**Achievement 1 Progress:** 2/7 exercises complete

### Skills Gained in This Exercise

✅ Understanding Python data types (strings, integers, lists, dictionaries)  
✅ Choosing appropriate data structures for specific use cases  
✅ Justifying technical decisions professionally  
✅ Working with nested data structures (list of dictionaries)  
✅ Manipulating structured data effectively  
✅ Using IPython for interactive development  

### Ready for Next Exercise

With data structures mastered, you're now prepared to:
- Write Python scripts (.py files) for persistent code
- Implement conditional logic (if-elif-else statements)
- Use loops (for/while) for iteration
- Create reusable functions with parameters and return values
- Build the Recipe Management System with difficulty calculation
