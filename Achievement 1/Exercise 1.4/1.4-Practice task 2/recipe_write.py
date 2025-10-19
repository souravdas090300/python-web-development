# Code Practice 2: Binary Files - Writing Recipe Data
# Step 1: Import the pickle module
import pickle

# Step 2: Create a recipe dictionary for tea
recipe = {
    'ingredient_name': 'Tea',
    'ingredients': ['Tea leaves', 'Water', 'Sugar'],
    'cooking_time': 5,
    'difficulty': 'Easy'
}

# Step 3: Store the dictionary in a binary file using pickle.dump()
my_file = open('recipe_binary.bin', 'wb')
pickle.dump(recipe, my_file)
my_file.close()

print("Recipe has been successfully written to recipe_binary.bin")
