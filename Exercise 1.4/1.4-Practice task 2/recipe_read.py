# Code Practice 2: Binary Files - Reading Recipe Data
# Step 4: Load data back using pickle.load() and display with readable formatting
import pickle

# Open the binary file in read mode and load the recipe
with open('recipe_binary.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)

# Display the recipe with readable formatting
print("=" * 50)
print("RECIPE DETAILS")
print("=" * 50)
print(f"Ingredient Name: {recipe['ingredient_name']}")
print(f"Ingredients: {', '.join(recipe['ingredients'])}")
print(f"Cooking Time: {recipe['cooking_time']} minutes")
print(f"Difficulty: {recipe['difficulty']}")
print("=" * 50)
