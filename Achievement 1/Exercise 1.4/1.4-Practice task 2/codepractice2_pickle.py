# Code Practice 2: Binary Files - Complete Script
# This script demonstrates all steps for working with pickles

# ============================================================
# PART 1: Writing Recipe Data to Binary File
# ============================================================

# Step 1: Import the pickle module
import pickle

# Step 2: Create a recipe dictionary for tea
recipe = {
    'ingredient_name': 'Tea',
    'ingredients': ['Tea leaves', 'Water', 'Sugar'],
    'cooking_time': 5,
    'difficulty': 'Easy'
}

print("Step 2: Recipe dictionary created:")
print(recipe)
print()

# Step 3: Store the dictionary in a binary file using pickle.dump()
my_file = open('recipe_binary.bin', 'wb')
pickle.dump(recipe, my_file)
my_file.close()

print("Step 3: Recipe has been written to recipe_binary.bin")
print()

# ============================================================
# PART 2: Reading Recipe Data from Binary File
# ============================================================

# Step 4: Load data back using pickle.load() and display
with open('recipe_binary.bin', 'rb') as my_file:
    loaded_recipe = pickle.load(my_file)

print("Step 4: Recipe loaded from binary file and displayed:")
print("=" * 50)
print("RECIPE DETAILS")
print("=" * 50)
print(f"Ingredient Name: {loaded_recipe['ingredient_name']}")
print(f"Ingredients: {', '.join(loaded_recipe['ingredients'])}")
print(f"Cooking Time: {loaded_recipe['cooking_time']} minutes")
print(f"Difficulty: {loaded_recipe['difficulty']}")
print("=" * 50)
