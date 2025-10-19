# Exercise 1.3 - Recipe Management System with Difficulty Calculation

# Step 1: Initialize empty lists
recipes_list = []
ingredients_list = []

# Step 2: Define take_recipe() function
def take_recipe():
    """
    Takes user input for a recipe and returns a dictionary
    containing name, cooking_time, and ingredients.
    """
    # Get recipe name
    name = input("\nEnter the recipe name: ")
    
    # Get cooking time
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    
    # Get ingredients
    ingredients = []
    n_ingredients = int(input("How many ingredients does this recipe have? "))
    
    for i in range(1, n_ingredients + 1):
        ingredient = input(f"  Enter ingredient {i}: ")
        ingredients.append(ingredient)
    
    # Create and return recipe dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    
    return recipe

# Step 3: Main code starts here
print("=" * 60)
print("RECIPE MANAGEMENT SYSTEM")
print("=" * 60)

# Ask user how many recipes they want to enter
n = int(input("\nHow many recipes would you like to enter? "))

# Step 4: Loop to collect all recipes
for i in range(n):
    print(f"\n{'='*60}")
    print(f"RECIPE {i+1}")
    print("=" * 60)
    
    # Get recipe from user
    recipe = take_recipe()
    
    # Add unique ingredients to ingredients_list
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    
    # Add recipe to recipes_list
    recipes_list.append(recipe)
    print(f"\n✓ Recipe '{recipe['name']}' added successfully!")

# Step 5: Display all recipes with difficulty
print("\n" + "=" * 60)
print("ALL RECIPES WITH DIFFICULTY LEVELS")
print("=" * 60)

for recipe in recipes_list:
    # Calculate difficulty
    cooking_time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])
    
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:  # cooking_time >= 10 and num_ingredients >= 4
        difficulty = "Hard"
    
    # Display recipe
    print(f"\nRecipe: {recipe['name']}")
    print(f"Cooking Time (min): {cooking_time}")
    print(f"Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"  - {ingredient}")
    print(f"Difficulty: {difficulty}")

# Step 6: Display all ingredients in alphabetical order
print("\n" + "=" * 60)
print("ALL INGREDIENTS (Alphabetical Order)")
print("=" * 60)

# Create sorted copy to preserve original ingredients_list
sorted_ingredients_list = sorted(ingredients_list)

print()
for ingredient in sorted_ingredients_list:
    print(f"- {ingredient}")

print("\n" + "=" * 60)
print("Thank you for using the Recipe Management System!")
print("=" * 60)