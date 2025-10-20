# Part 2: recipe_search.py Script
# This script searches for recipes by ingredient from a binary file

import pickle

# Function to display a recipe
def display_recipe(recipe):
    """
    Display all attributes of a recipe.
    
    Args:
        recipe (dict): Dictionary containing recipe details
    """
    print("\n" + "="*50)
    print(f"Recipe: {recipe['name']}")
    print("="*50)
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print(f"Difficulty: {recipe['difficulty']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"  - {ingredient}")
    print("="*50)


# Function to search for recipes containing a specific ingredient
def search_ingredient(data):
    """
    Search for recipes containing a specific ingredient.
    
    Args:
        data (dict): Dictionary containing recipes_list and all_ingredients
    """
    # Display all available ingredients
    all_ingredients = data['all_ingredients']
    
    print("\nAvailable ingredients:")
    print("-" * 50)
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index}. {ingredient}")
    print("-" * 50)
    
    # Try to get user input for ingredient selection
    try:
        ingredient_index = int(input("\nEnter the number of the ingredient you'd like to search for: "))
        ingredient_searched = all_ingredients[ingredient_index]
        
    except ValueError:
        print("Error: Please enter a valid number.")
        return
        
    except IndexError:
        print("Error: The number you entered is not in the list.")
        return
        
    except Exception:
        print("Error: An unexpected error occurred.")
        return
    
    else:
        # Search for recipes containing the selected ingredient
        recipes_list = data['recipes_list']
        found = False
        
        print(f"\nRecipes containing '{ingredient_searched}':")
        
        for recipe in recipes_list:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
                found = True
        
        if not found:
            print(f"\nNo recipes found containing '{ingredient_searched}'.")


# Main code
filename = input("Enter the filename where your recipes are stored (without extension): ")
# Add .bin extension automatically
filename = filename.strip() + '.bin'

# Try to open and load the recipe data
try:
    file = open(filename, 'rb')
    data = pickle.load(file)
    
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    print("Please make sure you've created recipes using recipe_input.py first.")
    
except Exception:
    print("Error: An unexpected error occurred while loading the file.")
    
else:
    file.close()
    # Call search_ingredient function
    search_ingredient(data)
