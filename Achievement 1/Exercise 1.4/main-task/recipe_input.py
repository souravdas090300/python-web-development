# Part 1: recipe_input.py Script
# This script takes recipes from the user and stores them in a binary file

import pickle

# Function to calculate difficulty based on cooking time and number of ingredients
def calc_difficulty(cooking_time, num_ingredients):
    """
    Calculate recipe difficulty based on cooking time and number of ingredients.
    
    Args:
        cooking_time (int): Cooking time in minutes
        num_ingredients (int): Number of ingredients
    
    Returns:
        str: Difficulty level (Easy, Medium, Intermediate, or Hard)
    """
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and num_ingredients >= 4:
        difficulty = "Hard"
    
    return difficulty


# Function to take recipe input from the user
def take_recipe():
    """
    Take recipe details from user input.
    
    Returns:
        dict: Dictionary containing recipe name, cooking_time, ingredients, and difficulty
    """
    # Get recipe name
    name = input("Enter the recipe name: ")
    
    # Get cooking time
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    
    # Get ingredients
    ingredients = []
    num_ingredients = int(input("Enter the number of ingredients: "))
    
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i + 1}: ")
        ingredients.append(ingredient)
    
    # Calculate difficulty
    difficulty = calc_difficulty(cooking_time, num_ingredients)
    
    # Create recipe dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }
    
    return recipe


# Main code
filename = input("Enter the filename where you'd like to store your recipes: ")

# Try to open and load existing recipe data
try:
    file = open(filename, 'rb')
    data = pickle.load(file)
    
except FileNotFoundError:
    print("File doesn't exist - creating a new one.")
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }
    
except:
    print("An unexpected error occurred - creating a new data structure.")
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }
    
else:
    file.close()
    
finally:
    # Extract the values from the dictionary
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']


# Ask user how many recipes they want to enter
num_recipes = int(input("\nHow many recipes would you like to enter? "))

# Loop to take recipes from user
for i in range(num_recipes):
    print(f"\n--- Recipe {i + 1} ---")
    recipe = take_recipe()
    
    # Add recipe to recipes_list
    recipes_list.append(recipe)
    
    # Add new ingredients to all_ingredients
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

# Update the data dictionary
data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
}

# Write the updated data to the binary file
with open(filename, 'wb') as file:
    pickle.dump(data, file)

print(f"\nRecipes saved successfully to {filename}!")
