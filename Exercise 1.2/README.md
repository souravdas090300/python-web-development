# Exercise 1.2 — Data Types and Structures

**Student:** Sourav Das  
**Course:** Python for Web Developers  
**Date:** October 15, 2025  

## 📋 Task Overview

Create data structures to store recipe information for the Recipe app, demonstrating understanding of Python data types and structures.

## 🎯 Requirements

1. Create a recipe structure with: name (str), cooking_time (int), ingredients (list)
2. Choose appropriate data structure for individual recipes
3. Create an outer structure to hold all recipes
4. Generate 5 recipes total
5. Print ingredients of each recipe

## 💡 Data Structure Decisions

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

## 📸 Screenshots Checklist

- [ ] Step 1: Creating recipe_1 (Tea)
- [ ] Step 2: Creating all_recipes and adding recipe_1
- [ ] Step 3: Creating and adding recipe_2 (Coffee)
- [ ] Step 4: Creating and adding recipe_3 (Scrambled Eggs)
- [ ] Step 5: Creating and adding recipe_4 (Pasta)
- [ ] Step 6: Creating and adding recipe_5 (Oatmeal)
- [ ] Step 7: Printing ingredients of all 5 recipes

## 🚀 Quick Commands for IPython

**Complete sequence to run in IPython:**

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

1. **Screenshots** - All 7 steps documented
2. **README.md** - This file with justifications
3. **Learning Journal** - Updated with learnings from Exercise 1.2

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
