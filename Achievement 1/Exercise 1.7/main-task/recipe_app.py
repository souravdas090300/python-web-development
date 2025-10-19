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
    difficulty = Column(String(20))
    
    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name}>"
    
    def __str__(self):
        """Return formatted string representation of recipe."""
        return f"""
{'='*50}
Recipe ID: {self.id}
Name: {self.name}
Ingredients: {self.ingredients}
Cooking Time: {self.cooking_time} minutes
Difficulty: {self.difficulty}
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

def create_recipe():
    """Create a new recipe and add it to the database."""
    print("\n" + "="*50)
    print("CREATE NEW RECIPE")
    print("="*50)
    
    # Get recipe name with validation
    while True:
        name = input("\nEnter recipe name (max 50 characters): ").strip()
        if len(name) == 0:
            print("Error: Recipe name cannot be empty!")
            continue
        if len(name) > 50:
            print("Error: Recipe name too long! Maximum 50 characters.")
            continue
        break
    
    # Get cooking time with validation
    while True:
        try:
            cooking_time = int(input("Enter cooking time in minutes: "))
            if cooking_time < 1:
                print("Error: Cooking time must be positive!")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number!")
    
    # Get ingredients
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
            ingredients_list.append(ingredient)
    
    # Join ingredients into comma-separated string
    ingredients_str = ', '.join(ingredients_list)
    
    # Validate total length
    if len(ingredients_str) > 255:
        print("\nError: Ingredient list too long! Maximum 255 characters.")
        print("Recipe not created.")
        return
    
    # Create recipe object
    recipe = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=cooking_time
    )
    
    # Calculate and set difficulty
    recipe.difficulty = recipe.calculate_difficulty()
    
    # Add to database
    session.add(recipe)
    session.commit()
    
    print(f"\n✓ Recipe '{name}' created successfully!")
    print(f"  Difficulty: {recipe.difficulty}")


def view_all_recipes():
    """Display all recipes in the database."""
    print("\n" + "="*50)
    print("ALL RECIPES")
    print("="*50)
    
    # Retrieve all recipes
    recipes = session.query(Recipe).all()
    
    if not recipes:
        print("\nNo recipes found in the database.")
        return
    
    print(f"\nTotal recipes: {len(recipes)}\n")
    
    for recipe in recipes:
        print(recipe)


def search_by_ingredient():
    """Search for recipes containing a specific ingredient."""
    print("\n" + "="*50)
    print("SEARCH BY INGREDIENT")
    print("="*50)
    
    # Check if any recipes exist
    if session.query(Recipe).count() == 0:
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
    
    # Get user choice
    while True:
        try:
            choice = int(input(f"\nSelect ingredient number (1-{len(all_ingredients)}): "))
            if 1 <= choice <= len(all_ingredients):
                search_ingredient = all_ingredients[choice - 1]
                break
            else:
                print(f"Error: Please enter a number between 1 and {len(all_ingredients)}!")
        except ValueError:
            print("Error: Please enter a valid number!")
    
    # Search for recipes containing this ingredient
    search_pattern = f"%{search_ingredient}%"
    matching_recipes = session.query(Recipe).filter(Recipe.ingredients.like(search_pattern)).all()
    
    if not matching_recipes:
        print(f"\nNo recipes found containing '{search_ingredient}'.")
        return
    
    print(f"\n{'='*50}")
    print(f"Recipes containing '{search_ingredient}': {len(matching_recipes)}")
    print('='*50)
    
    for recipe in matching_recipes:
        print(recipe)


def edit_recipe():
    """Update an existing recipe's details."""
    print("\n" + "="*50)
    print("EDIT RECIPE")
    print("="*50)
    
    # Check if any recipes exist
    if session.query(Recipe).count() == 0:
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
            recipe = session.query(Recipe).get(recipe_id)
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
        # Edit name
        while True:
            new_name = input("Enter new recipe name (max 50 characters): ").strip()
            if len(new_name) == 0:
                print("Error: Recipe name cannot be empty!")
                continue
            if len(new_name) > 50:
                print("Error: Recipe name too long! Maximum 50 characters.")
                continue
            recipe.name = new_name
            break
    
    elif choice == 2:
        # Edit cooking time
        while True:
            try:
                new_time = int(input("Enter new cooking time in minutes: "))
                if new_time < 1:
                    print("Error: Cooking time must be positive!")
                    continue
                recipe.cooking_time = new_time
                # Recalculate difficulty
                recipe.difficulty = recipe.calculate_difficulty()
                break
            except ValueError:
                print("Error: Please enter a valid number!")
    
    elif choice == 3:
        # Edit ingredients
        print("\nEnter new ingredients (one per line).")
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
                ingredients_list.append(ingredient)
        
        ingredients_str = ', '.join(ingredients_list)
        
        if len(ingredients_str) > 255:
            print("\nError: Ingredient list too long! Maximum 255 characters.")
            print("Ingredients not updated.")
            return
        
        recipe.ingredients = ingredients_str
        # Recalculate difficulty
        recipe.difficulty = recipe.calculate_difficulty()
    
    # Commit changes
    session.commit()
    print(f"\n✓ Recipe updated successfully!")
    print(f"  New difficulty: {recipe.difficulty}")


def delete_recipe():
    """Delete a recipe from the database."""
    print("\n" + "="*50)
    print("DELETE RECIPE")
    print("="*50)
    
    # Check if any recipes exist
    if session.query(Recipe).count() == 0:
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
            recipe = session.query(Recipe).get(recipe_id)
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
