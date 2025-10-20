# Main Task: Recipe OOP
# Exercise 1.5 - Object-Oriented Programming

class Recipe:
    """
    A class to represent recipes with ingredients and cooking time.
    Automatically calculates difficulty based on time and ingredient count.
    """
    
    # Class variable to track all ingredients across all recipes
    all_ingredients = []
    
    def __init__(self, name):
        """
        Initialize a Recipe object.
        
        Args:
            name (str): Name of the recipe
        """
        self._name = name
        self._ingredients = []
        self._cooking_time = 0
        self._difficulty = None
    
    # Property for name (Pythonic way using @property decorator)
    @property
    def name(self):
        """Return the recipe name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Set the recipe name."""
        self._name = value
    
    # Property for cooking_time (Pythonic way using @property decorator)
    @property
    def cooking_time(self):
        """Return the cooking time."""
        return self._cooking_time
    
    @cooking_time.setter
    def cooking_time(self, value):
        """Set the cooking time in minutes."""
        self._cooking_time = value
    
    # Property for ingredients (read-only, use add_ingredients to modify)
    @property
    def ingredients(self):
        """Return the list of ingredients."""
        return self._ingredients
    
    # Property for difficulty (read-only, calculated automatically)
    @property
    def difficulty(self):
        """
        Return the difficulty level.
        Calculates difficulty if not already calculated.
        """
        if self._difficulty is None:
            self.calculate_difficulty()
        return self._difficulty
    
    def add_ingredients(self, *ingredients):
        """
        Add ingredients to the recipe.
        Takes variable-length arguments.
        
        Args:
            *ingredients: Variable number of ingredient names
        """
        for ingredient in ingredients:
            self._ingredients.append(ingredient)
        # Update the class variable with all ingredients
        self.update_all_ingredients()
    
    def calculate_difficulty(self):
        """
        Calculate recipe difficulty based on cooking time and ingredient count.
        
        Logic:
        - Easy: < 10 min AND < 4 ingredients
        - Medium: < 10 min AND >= 4 ingredients
        - Intermediate: >= 10 min AND < 4 ingredients
        - Hard: >= 10 min AND >= 4 ingredients
        """
        num_ingredients = len(self._ingredients)
        
        if self._cooking_time < 10 and num_ingredients < 4:
            self._difficulty = "Easy"
        elif self._cooking_time < 10 and num_ingredients >= 4:
            self._difficulty = "Medium"
        elif self._cooking_time >= 10 and num_ingredients < 4:
            self._difficulty = "Intermediate"
        elif self._cooking_time >= 10 and num_ingredients >= 4:
            self._difficulty = "Hard"
    
    def search_ingredient(self, ingredient):
        """
        Search for an ingredient in the recipe.
        
        Args:
            ingredient (str): Ingredient to search for
            
        Returns:
            bool: True if ingredient found, False otherwise
        """
        return ingredient in self._ingredients
    
    def update_all_ingredients(self):
        """
        Update the class variable all_ingredients with ingredients
        from this recipe that aren't already present.
        """
        for ingredient in self._ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)
    
    def __str__(self):
        """
        Return a formatted string representation of the recipe.
        """
        output = "\n" + "="*60
        output += f"\nRecipe: {self.name}"
        output += "\n" + "="*60
        output += f"\nCooking Time: {self.cooking_time} minutes"
        output += f"\nDifficulty: {self.difficulty}"
        output += "\nIngredients:"
        for ingredient in self._ingredients:
            output += f"\n  - {ingredient}"
        output += "\n" + "="*60
        return output


def recipe_search(data, search_term):
    """
    Search for recipes containing a specific ingredient.
    
    Args:
        data (list): List of Recipe objects to search through
        search_term (str): Ingredient to search for
    """
    print(f"\n{'='*60}")
    print(f"Recipes containing '{search_term}':")
    print('='*60)
    
    found_count = 0
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)
            found_count += 1
    
    if found_count == 0:
        print(f"\nNo recipes found containing '{search_term}'.")
        print('='*60)


# ============================================
# MAIN CODE
# ============================================

print("="*60)
print("RECIPE OOP APPLICATION - EXERCISE 1.5 MAIN TASK")
print("="*60)

# Recipe 1: Tea
print("\n>>> Creating Recipe 1: Tea")
tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.cooking_time = 5
print(tea)

# Recipe 2: Coffee
print("\n>>> Creating Recipe 2: Coffee")
coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.cooking_time = 5
print(coffee)

# Recipe 3: Cake
print("\n>>> Creating Recipe 3: Cake")
cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.cooking_time = 50
print(cake)

# Recipe 4: Banana Smoothie
print("\n>>> Creating Recipe 4: Banana Smoothie")
banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.cooking_time = 5
print(banana_smoothie)

# Wrap recipes into a list
recipes_list = [tea, coffee, cake, banana_smoothie]

print("\n" + "="*60)
print("ALL RECIPES CREATED SUCCESSFULLY!")
print(f"Total Recipes: {len(recipes_list)}")
print("="*60)

# Display all unique ingredients
print("\n" + "="*60)
print("ALL INGREDIENTS ACROSS ALL RECIPES:")
print("="*60)
for i, ingredient in enumerate(Recipe.all_ingredients, 1):
    print(f"{i}. {ingredient}")
print("="*60)

# Search for recipes containing specific ingredients
print("\n" + "="*60)
print("SEARCHING FOR RECIPES BY INGREDIENT")
print("="*60)

# Search for Water
recipe_search(recipes_list, "Water")

# Search for Sugar
recipe_search(recipes_list, "Sugar")

# Search for Bananas
recipe_search(recipes_list, "Bananas")

print("\n" + "="*60)
print("RECIPE OOP APPLICATION COMPLETED!")
print("="*60)
