# Recipe Management System with MySQL
# Exercise 1.6 - Database Application

import mysql.connector

# ============================================
# PART 1: DATABASE CONNECTION
# ============================================

def connect_database():
    """Connect to MySQL database and return connection and cursor objects."""
    conn = mysql.connector.connect(
        host='localhost',
        user='cf-python',
        passwd='password'
    )
    cursor = conn.cursor()
    
    # Create database if not exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS task_database;")
    cursor.execute("USE task_database;")
    
    # Create Recipes table if not exists
    cursor.execute("""CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    );""")
    
    conn.commit()
    return conn, cursor


# ============================================
# HELPER FUNCTION: Calculate Difficulty
# ============================================

def calculate_difficulty(cooking_time, ingredients):
    """
    Calculate recipe difficulty based on cooking time and number of ingredients.
    
    Args:
        cooking_time (int): Cooking time in minutes
        ingredients (list): List of ingredients
    
    Returns:
        str: Difficulty level (Easy, Medium, Intermediate, Hard)
    """
    num_ingredients = len(ingredients)
    
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:  # cooking_time >= 10 and num_ingredients >= 4
        difficulty = "Hard"
    
    return difficulty


# ============================================
# PART 3: CREATE RECIPE
# ============================================

def create_recipe(conn, cursor):
    """Create a new recipe and add it to the database."""
    print("\n" + "="*60)
    print("CREATE NEW RECIPE")
    print("="*60)
    
    # Collect recipe details
    name = input("\nEnter recipe name: ")
    cooking_time = int(input("Enter cooking time (in minutes): "))
    
    # Collect ingredients
    ingredients = []
    num_ingredients = int(input("How many ingredients? "))
    
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)
    
    # Calculate difficulty
    difficulty = calculate_difficulty(cooking_time, ingredients)
    
    # Convert ingredients list to comma-separated string
    ingredients_str = ", ".join(ingredients)
    
    # Insert into database
    sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s);"
    val = (name, ingredients_str, cooking_time, difficulty)
    
    cursor.execute(sql, val)
    conn.commit()
    
    print(f"\n✓ Recipe '{name}' created successfully!")
    print(f"  Difficulty: {difficulty}")
    print(f"  Cooking Time: {cooking_time} minutes")
    print(f"  Ingredients: {ingredients_str}")


# ============================================
# PART 4: SEARCH RECIPE
# ============================================

def search_recipe(conn, cursor):
    """Search for recipes by ingredient."""
    print("\n" + "="*60)
    print("SEARCH RECIPES BY INGREDIENT")
    print("="*60)
    
    # Fetch all ingredients from database
    cursor.execute("SELECT ingredients FROM Recipes;")
    results = cursor.fetchall()
    
    if not results:
        print("\nNo recipes found in database.")
        return
    
    # Build list of all unique ingredients
    all_ingredients = []
    for row in results:
        ingredients_str = row[0]
        # Split the comma-separated string into list
        ingredients_list = [ing.strip() for ing in ingredients_str.split(',')]
        
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    # Display all ingredients
    print("\nAvailable ingredients:")
    print("-" * 60)
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")
    
    # Get user choice
    try:
        choice = int(input("\nEnter the number of ingredient to search for: "))
        search_ingredient = all_ingredients[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice!")
        return
    
    # Search for recipes containing the ingredient
    # Use LIKE with wildcards to find ingredient in the string
    search_pattern = f"%{search_ingredient}%"
    cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s;", (search_pattern,))
    results = cursor.fetchall()
    
    if not results:
        print(f"\nNo recipes found with '{search_ingredient}'.")
        return
    
    # Display results
    print(f"\nRecipes containing '{search_ingredient}':")
    print("="*60)
    for row in results:
        print(f"\nID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Ingredients: {row[2]}")
        print(f"Cooking Time: {row[3]} minutes")
        print(f"Difficulty: {row[4]}")
        print("-"*60)


# ============================================
# PART 5: UPDATE RECIPE
# ============================================

def update_recipe(conn, cursor):
    """Update an existing recipe in the database."""
    print("\n" + "="*60)
    print("UPDATE RECIPE")
    print("="*60)
    
    # Fetch and display all recipes
    cursor.execute("SELECT * FROM Recipes;")
    results = cursor.fetchall()
    
    if not results:
        print("\nNo recipes found in database.")
        return
    
    print("\nAll Recipes:")
    print("-" * 60)
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]} | Cooking Time: {row[3]} min | Difficulty: {row[4]}")
    
    # Get recipe ID to update
    try:
        recipe_id = int(input("\nEnter the ID of recipe to update: "))
    except ValueError:
        print("Invalid ID!")
        return
    
    # Check if recipe exists
    cursor.execute("SELECT * FROM Recipes WHERE id = %s;", (recipe_id,))
    recipe = cursor.fetchone()
    
    if not recipe:
        print(f"Recipe with ID {recipe_id} not found!")
        return
    
    # Display current recipe details
    print(f"\nCurrent recipe details:")
    print(f"Name: {recipe[1]}")
    print(f"Ingredients: {recipe[2]}")
    print(f"Cooking Time: {recipe[3]} minutes")
    print(f"Difficulty: {recipe[4]}")
    
    # Choose column to update
    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")
    
    try:
        choice = int(input("\nEnter your choice (1-3): "))
    except ValueError:
        print("Invalid choice!")
        return
    
    # Update based on choice
    if choice == 1:
        # Update name
        new_name = input("Enter new name: ")
        cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s;", (new_name, recipe_id))
        print(f"✓ Recipe name updated to '{new_name}'")
    
    elif choice == 2:
        # Update cooking time (need to recalculate difficulty)
        new_time = int(input("Enter new cooking time (minutes): "))
        
        # Get current ingredients to recalculate difficulty
        ingredients_list = [ing.strip() for ing in recipe[2].split(',')]
        new_difficulty = calculate_difficulty(new_time, ingredients_list)
        
        cursor.execute("UPDATE Recipes SET cooking_time = %s, difficulty = %s WHERE id = %s;", 
                      (new_time, new_difficulty, recipe_id))
        print(f"✓ Cooking time updated to {new_time} minutes")
        print(f"✓ Difficulty recalculated to '{new_difficulty}'")
    
    elif choice == 3:
        # Update ingredients (need to recalculate difficulty)
        num_ingredients = int(input("How many ingredients? "))
        ingredients = []
        for i in range(num_ingredients):
            ingredient = input(f"Enter ingredient {i+1}: ")
            ingredients.append(ingredient)
        
        ingredients_str = ", ".join(ingredients)
        
        # Recalculate difficulty
        new_difficulty = calculate_difficulty(recipe[3], ingredients)
        
        cursor.execute("UPDATE Recipes SET ingredients = %s, difficulty = %s WHERE id = %s;", 
                      (ingredients_str, new_difficulty, recipe_id))
        print(f"✓ Ingredients updated")
        print(f"✓ Difficulty recalculated to '{new_difficulty}'")
    
    else:
        print("Invalid choice!")
        return
    
    conn.commit()
    print("\n✓ Recipe updated successfully!")


# ============================================
# PART 6: DELETE RECIPE
# ============================================

def delete_recipe(conn, cursor):
    """Delete a recipe from the database."""
    print("\n" + "="*60)
    print("DELETE RECIPE")
    print("="*60)
    
    # Fetch and display all recipes
    cursor.execute("SELECT * FROM Recipes;")
    results = cursor.fetchall()
    
    if not results:
        print("\nNo recipes found in database.")
        return
    
    print("\nAll Recipes:")
    print("-" * 60)
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]} | Cooking Time: {row[3]} min | Difficulty: {row[4]}")
    
    # Get recipe ID to delete
    try:
        recipe_id = int(input("\nEnter the ID of recipe to delete: "))
    except ValueError:
        print("Invalid ID!")
        return
    
    # Confirm deletion
    cursor.execute("SELECT name FROM Recipes WHERE id = %s;", (recipe_id,))
    recipe = cursor.fetchone()
    
    if not recipe:
        print(f"Recipe with ID {recipe_id} not found!")
        return
    
    confirm = input(f"\nAre you sure you want to delete '{recipe[0]}'? (yes/no): ")
    
    if confirm.lower() == 'yes':
        cursor.execute("DELETE FROM Recipes WHERE id = %s;", (recipe_id,))
        conn.commit()
        print(f"\n✓ Recipe '{recipe[0]}' deleted successfully!")
    else:
        print("\nDeletion cancelled.")


# ============================================
# PART 2: MAIN MENU
# ============================================

def main_menu(conn, cursor):
    """Display main menu and handle user choices."""
    
    while True:
        print("\n" + "="*60)
        print("RECIPE MANAGEMENT SYSTEM - MAIN MENU")
        print("="*60)
        print("\nWhat would you like to do?")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            print("\n" + "="*60)
            print("Saving changes and exiting...")
            conn.commit()
            conn.close()
            print("✓ Database connection closed.")
            print("Thank you for using Recipe Management System!")
            print("="*60)
            break
        else:
            print("\n✗ Invalid choice! Please enter a number between 1 and 5.")


# ============================================
# MAIN PROGRAM
# ============================================

if __name__ == "__main__":
    print("="*60)
    print("WELCOME TO RECIPE MANAGEMENT SYSTEM")
    print("="*60)
    print("\nConnecting to database...")
    
    try:
        conn, cursor = connect_database()
        print("✓ Connected to database successfully!")
        
        # Run main menu
        main_menu(conn, cursor)
        
    except mysql.connector.Error as err:
        print(f"\n✗ Database Error: {err}")
    except Exception as e:
        print(f"\n✗ Error: {e}")
