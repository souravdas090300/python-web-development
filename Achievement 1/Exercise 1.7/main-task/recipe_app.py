# Recipe Management Application with SQLAlchemy ORM
# Exercise 1.7 - Object Relational Mapping

from sqlalchemy import create_engine, Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ============================================
# DATABASE SETUP
# ============================================

# Create engine - connects to MySQL database
# Format: mysql+pymysql://username:password@host/database
engine = create_engine("mysql+pymysql://cf-python:Das0987654@localhost/task_database")

# Create declarative base class
Base = declarative_base()

# Create Session class
Session = sessionmaker(bind=engine)
session = Session()


# ============================================
# RECIPE MODEL
# ============================================

class Recipe(Base):
    """Recipe model representing the recipes table in database."""
    
    __tablename__ = "final_recipes"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    
    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name}>"
    
    def __str__(self):
        """Return formatted string representation of recipe."""
        difficulty = self.calculate_difficulty()
        return f"""
{'='*50}
Recipe ID: {self.id}
Name: {self.name}
Ingredients: {self.ingredients}
Cooking Time: {self.cooking_time} minutes
Difficulty: {difficulty}
{'='*50}
"""
    
    def calculate_difficulty(self):
        """Calculate and return difficulty based on cooking time and ingredients."""
        # Count number of ingredients by splitting the string
        ingredients_list = self.ingredients.split(', ')
        num_ingredients = len(ingredients_list)
        
        # Determine difficulty
        if self.cooking_time < 10 and num_ingredients < 4:
            difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            difficulty = "Intermediate"
        else:
            difficulty = "Hard"
        
        return difficulty
    
    def return_ingredients_as_list(self):
        """Return ingredients as a list."""
        if self.ingredients:
            return self.ingredients.split(', ')
        return []


# Create all tables in the database
Base.metadata.create_all(engine)


# ============================================
# HELPER FUNCTIONS
# ============================================

def check_recipes_exist():
    """Check if any recipes exist in the database."""
    return session.query(Recipe).count() > 0


def validate_recipe_name(name):
    """
    Validate recipe name using Python built-in methods.
    Returns tuple (is_valid, error_message)
    """
    if not name or len(name) == 0:
        return False, "Recipe name cannot be empty!"
    
    if len(name) > 50:
        return False, "Recipe name too long! Maximum 50 characters."
    
    # Check if name contains only alphanumeric characters and spaces
    # Remove spaces for validation
    name_without_spaces = name.replace(' ', '')
    if not name_without_spaces.isalnum():
        return False, "Recipe name should contain only letters and numbers!"
    
    return True, ""


def validate_cooking_time(time_str):
    """
    Validate cooking time using Python built-in methods.
    Returns tuple (is_valid, cooking_time, error_message)
    """
    # Check if input is numeric
    if not time_str.isnumeric():
        return False, None, "Please enter a valid number!"
    
    cooking_time = int(time_str)
    if cooking_time < 1:
        return False, None, "Cooking time must be positive!"
    
    return True, cooking_time, ""


def validate_ingredient(ingredient):
    """
    Validate ingredient using Python built-in methods.
    Returns tuple (is_valid, error_message)
    """
    if not ingredient:
        return False, "Ingredient cannot be empty!"
    
    # Remove spaces for validation
    ingredient_without_spaces = ingredient.replace(' ', '')
    
    # Check if ingredient contains only alphabetic characters
    if not ingredient_without_spaces.isalpha():
        return False, "Ingredient should contain only letters!"
    
    return True, ""


def get_validated_name():
    """Get and validate recipe name from user."""
    while True:
        name = input("\nEnter recipe name (max 50 characters): ").strip()
        is_valid, error = validate_recipe_name(name)
        if is_valid:
            return name
        print(f"Error: {error}")


def get_validated_cooking_time():
    """Get and validate cooking time from user."""
    while True:
        time_str = input("Enter cooking time in minutes: ").strip()
        is_valid, cooking_time, error = validate_cooking_time(time_str)
        if is_valid:
            return cooking_time
        print(f"Error: {error}")


def get_validated_ingredients():
    """Get and validate ingredients list from user."""
    print("\nEnter ingredients (one per line).")
    print("Type 'done' when finished:")
    ingredients_list = []
    
    while True:
        ingredient = input("> ").strip()
        if ingredient.lower() == 'done':
            if len(ingredients_list) == 0:
                print("Error: Please enter at least one ingredient!")
                continue
            break
        
        if ingredient:
            is_valid, error = validate_ingredient(ingredient)
            if is_valid:
                ingredients_list.append(ingredient)
            else:
                print(f"Error: {error}")
                print("Please enter the ingredient again.")
    
    return ingredients_list


def create_recipe():
    """Create a new recipe and add it to the database."""
    print("\n" + "="*50)
    print("CREATE NEW RECIPE")
    print("="*50)
    
    # Get validated inputs using helper functions
    name = get_validated_name()
    cooking_time = get_validated_cooking_time()
    ingredients_list = get_validated_ingredients()
    
    # Join ingredients into comma-separated string
    ingredients_str = ', '.join(ingredients_list)
    
    # Validate total length
    if len(ingredients_str) > 255:
        print("\nError: Ingredient list too long! Maximum 255 characters.")
        print("Recipe not created.")
        return
    
    # Create recipe object (without difficulty - it's calculated)
    recipe = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=cooking_time
    )
    
    # Add to database
    session.add(recipe)
    session.commit()
    
    print(f"\n✓ Recipe '{name}' created successfully!")
    print(f"  Difficulty: {recipe.calculate_difficulty()}")


def view_all_recipes():
    """Display all recipes in the database."""
    print("\n" + "="*50)
    print("ALL RECIPES")
    print("="*50)
    
    # Check if recipes exist using helper function
    if not check_recipes_exist():
        print("\nNo recipes found in the database.")
        return
    
    # Retrieve all recipes
    recipes = session.query(Recipe).all()
    
    print(f"\nTotal recipes: {len(recipes)}\n")
    
    for recipe in recipes:
        print(recipe)


def search_by_ingredient():
    """Search for recipes containing specific ingredients."""
    print("\n" + "="*50)
    print("SEARCH BY INGREDIENT")
    print("="*50)
    
    # Check if any recipes exist using helper function
    if not check_recipes_exist():
        print("\nNo recipes available to search.")
        return
    
    # Get all unique ingredients from all recipes
    all_recipes = session.query(Recipe).all()
    all_ingredients = set()
    
    for recipe in all_recipes:
        ingredients_list = recipe.return_ingredients_as_list()
        all_ingredients.update(ingredients_list)
    
    # Convert to sorted list for display
    all_ingredients = sorted(list(all_ingredients))
    
    # Display available ingredients
    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")
    
    # Get user choices (multiple selections allowed)
    print(f"\nSelect ingredient numbers (1-{len(all_ingredients)}) separated by spaces.")
    print("Example: 1 3 5")
    
    while True:
        try:
            user_input = input("\nYour selection: ").strip()
            
            # Split input by spaces and convert to integers
            choices = [int(choice) for choice in user_input.split()]
            
            # Validate all choices are in range
            if all(1 <= choice <= len(all_ingredients) for choice in choices):
                selected_ingredients = [all_ingredients[choice - 1] for choice in choices]
                break
            else:
                print(f"Error: All numbers must be between 1 and {len(all_ingredients)}!")
        except ValueError:
            print("Error: Please enter valid numbers separated by spaces!")
    
    # Search for recipes containing ALL selected ingredients
    print(f"\nSearching for recipes containing: {', '.join(selected_ingredients)}")
    
    matching_recipes = []
    for recipe in all_recipes:
        recipe_ingredients = recipe.return_ingredients_as_list()
        # Check if all selected ingredients are in this recipe
        if all(ingredient in recipe_ingredients for ingredient in selected_ingredients):
            matching_recipes.append(recipe)
    
    if not matching_recipes:
        print(f"\nNo recipes found containing all selected ingredients.")
        return
    
    print(f"\n{'='*50}")
    print(f"Recipes found: {len(matching_recipes)}")
    print('='*50)
    
    for recipe in matching_recipes:
        print(recipe)


def edit_recipe():
    """Update an existing recipe's details."""
    print("\n" + "="*50)
    print("EDIT RECIPE")
    print("="*50)
    
    # Check if any recipes exist using helper function
    if not check_recipes_exist():
        print("\nNo recipes available to edit.")
        return
    
    # Display all recipes with IDs
    recipes = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
    print("\nAvailable recipes:")
    for recipe_id, recipe_name in recipes:
        print(f"  {recipe_id}. {recipe_name}")
    
    # Get recipe to edit
    while True:
        try:
            recipe_id = int(input("\nEnter recipe ID to edit: "))
            # Use new non-deprecated method
            recipe = session.get(Recipe, recipe_id)
            if recipe:
                break
            else:
                print("Error: Recipe not found! Please enter a valid ID.")
        except ValueError:
            print("Error: Please enter a valid number!")
    
    # Display current recipe
    print(f"\nCurrent recipe details:{recipe}")
    
    # Show edit options
    print("\nWhat would you like to edit?")
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            if choice in [1, 2, 3]:
                break
            else:
                print("Error: Please enter 1, 2, or 3!")
        except ValueError:
            print("Error: Please enter a valid number!")
    
    # Update based on choice
    if choice == 1:
        # Edit name using validation helper
        recipe.name = get_validated_name()
    
    elif choice == 2:
        # Edit cooking time using validation helper
        recipe.cooking_time = get_validated_cooking_time()
    
    elif choice == 3:
        # Edit ingredients using validation helper
        ingredients_list = get_validated_ingredients()
        ingredients_str = ', '.join(ingredients_list)
        
        if len(ingredients_str) > 255:
            print("\nError: Ingredient list too long! Maximum 255 characters.")
            print("Ingredients not updated.")
            return
        
        recipe.ingredients = ingredients_str
    
    # Commit changes
    session.commit()
    print(f"\n✓ Recipe updated successfully!")
    print(f"  New difficulty: {recipe.calculate_difficulty()}")


def delete_recipe():
    """Delete a recipe from the database."""
    print("\n" + "="*50)
    print("DELETE RECIPE")
    print("="*50)
    
    # Check if any recipes exist using helper function
    if not check_recipes_exist():
        print("\nNo recipes available to delete.")
        return
    
    # Display all recipes with IDs
    recipes = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
    print("\nAvailable recipes:")
    for recipe_id, recipe_name in recipes:
        print(f"  {recipe_id}. {recipe_name}")
    
    # Get recipe to delete
    while True:
        try:
            recipe_id = int(input("\nEnter recipe ID to delete: "))
            # Use new non-deprecated method
            recipe = session.get(Recipe, recipe_id)
            if recipe:
                break
            else:
                print("Error: Recipe not found! Please enter a valid ID.")
        except ValueError:
            print("Error: Please enter a valid number!")
    
    # Display recipe details
    print(f"\nRecipe to be deleted:{recipe}")
    
    # Confirm deletion
    while True:
        confirm = input("Are you sure you want to delete this recipe? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y']:
            session.delete(recipe)
            session.commit()
            print(f"\n✓ Recipe '{recipe.name}' deleted successfully!")
            break
        elif confirm in ['no', 'n']:
            print("\nDeletion cancelled.")
            break
        else:
            print("Error: Please enter 'yes' or 'no'.")


# ============================================
# MAIN MENU
# ============================================

def main_menu():
    """Display main menu and handle user choices."""
    while True:
        print("\n" + "="*50)
        print("RECIPE MANAGEMENT APPLICATION")
        print("="*50)
        print("\nMain Menu:")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredient")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredient()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == '6':
            print("\n" + "="*50)
            print("Thank you for using Recipe Management App!")
            print("Goodbye!")
            print("="*50)
            session.close()
            break
        else:
            print("\nError: Invalid choice! Please enter a number between 1 and 6.")


# ============================================
# RUN APPLICATION
# ============================================

if __name__ == "__main__":
    main_menu()
