# Practice Task 1: Shopping List Class
# Exercise 1.5 - Object-Oriented Programming in Python

# Step 1: Define the ShoppingList class
class ShoppingList(object):
    """
    A class to manage a shopping list with items to purchase.
    """
    
    # Step 2: Initialize the class with __init__ method
    def __init__(self, list_name):
        """
        Initialize the shopping list with a name and empty item list.
        
        Args:
            list_name (str): Name of the shopping list
        """
        self.list_name = list_name
        self.shopping_list = []  # Empty list to store items
    
    # Step 3: Define add_item method
    def add_item(self, item):
        """
        Add an item to the shopping list if it's not already there.
        
        Args:
            item (str): Item to add to the list
        """
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(f"'{item}' has been added to the list.")
        else:
            print(f"'{item}' is already in the list.")
    
    # Step 4: Define remove_item method
    def remove_item(self, item):
        """
        Remove an item from the shopping list.
        
        Args:
            item (str): Item to remove from the list
        """
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f"'{item}' has been removed from the list.")
        else:
            print(f"'{item}' is not in the list.")
    
    # Step 5: Define view_list method
    def view_list(self):
        """
        Display all items in the shopping list.
        """
        print("\n" + "="*50)
        print(f"{self.list_name}")
        print("="*50)
        
        if len(self.shopping_list) == 0:
            print("The list is empty.")
        else:
            print(f"Total items: {len(self.shopping_list)}\n")
            for index, item in enumerate(self.shopping_list, 1):
                print(f"{index}. {item}")
        
        print("="*50 + "\n")


# Main code starts here
print("🛒 Shopping List Manager - Practice Task 1")
print("="*50)

# Step 6: Create an object called pet_store_list
pet_store_list = ShoppingList("Pet Store Shopping List")
print(f"\nCreated: {pet_store_list.list_name}\n")

# Step 7: Add items to the list
print("Adding items to the list...")
print("-" * 50)
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

# Step 8: Remove 'flea collars' from the list
print("\n" + "-" * 50)
print("Removing an item...")
print("-" * 50)
pet_store_list.remove_item("flea collars")

# Step 9: Try adding 'frisbee' again (should show it's already in the list)
print("\n" + "-" * 50)
print("Attempting to add 'frisbee' again...")
print("-" * 50)
pet_store_list.add_item("frisbee")

# Step 10: Display the entire shopping list
print("\n" + "-" * 50)
print("Final Shopping List:")
print("-" * 50)
pet_store_list.view_list()

print("✅ Practice Task 1 Complete!")
