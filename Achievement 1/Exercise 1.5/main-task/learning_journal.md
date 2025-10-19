# Learning Journal - Exercise 1.5
## Object-Oriented Programming in Python

**Student:** Sourav Das  
**Date:** October 19, 2025  
**Course:** Python for Web Developers  
**Exercise:** 1.5 - Introduction to Object-Oriented Programming

---

## Learning Objectives Achieved

This exercise focused on understanding and implementing Object-Oriented Programming (OOP) concepts in Python, including:
- Creating and using classes and objects
- Implementing instance and class variables
- Writing getters, setters, and methods
- Understanding operator overloading
- Implementing special methods (`__init__`, `__str__`, `__sub__`, comparison operators)
- Working with variable-length arguments (`*args`)
- Building a complete OOP application

---

## Reflection Questions

### 1. In your own words, what is object-oriented programming? What are the benefits of OOP?

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code around "objects" - self-contained units that combine data (attributes) and behavior (methods). Instead of writing procedural code with separate functions and data structures, OOP allows us to model real-world entities as objects that interact with each other.

**Key OOP Concepts:**
- **Classes**: Blueprints that define the structure and behavior of objects
- **Objects**: Instances of classes with their own unique data
- **Encapsulation**: Bundling data and methods together, controlling access through getters/setters
- **Inheritance**: Creating new classes based on existing ones to reuse code
- **Polymorphism**: Different classes can be used interchangeably through shared interfaces

**Benefits of OOP:**

1. **Code Reusability**: Classes can be reused across projects, and inheritance allows extending functionality without rewriting code.

2. **Modularity**: Each class is self-contained, making code easier to understand, debug, and maintain.

3. **Data Protection**: Encapsulation allows controlling access to data, preventing unintended modifications.

4. **Real-World Modeling**: OOP naturally maps to real-world concepts, making code more intuitive (e.g., a Recipe class for recipes).

5. **Scalability**: OOP makes it easier to add new features without breaking existing code.

6. **Collaboration**: Different team members can work on different classes simultaneously.

**Example from Exercise:**
```python
# Without OOP (Procedural)
recipe1_name = "Tea"
recipe1_ingredients = ["Tea Leaves", "Sugar", "Water"]
recipe1_time = 5

# With OOP
class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0

tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
```

The OOP approach is cleaner, more maintainable, and easier to extend with new functionality.

---

### 2. What are objects and classes in Python? Come up with a real-world example to illustrate how objects and classes work.

**Classes** are blueprints or templates that define the structure and behavior of objects. They specify what attributes (data) and methods (functions) an object will have.

**Objects** are specific instances of a class. Each object has its own unique data but shares the same structure and methods defined by its class.

**Real-World Example: A Car Dealership**

```python
class Car:
    """Blueprint for creating car objects."""
    
    # Class variable (shared by all cars)
    total_cars_produced = 0
    
    def __init__(self, make, model, year, color):
        """Initialize a new car."""
        self.make = make          # Instance variable
        self.model = model        # Instance variable
        self.year = year          # Instance variable
        self.color = color        # Instance variable
        self.mileage = 0          # Instance variable
        self.is_running = False   # Instance variable
        Car.total_cars_produced += 1
    
    def start_engine(self):
        """Start the car engine."""
        if not self.is_running:
            self.is_running = True
            return f"{self.color} {self.make} {self.model} engine started!"
        return "Engine is already running."
    
    def drive(self, miles):
        """Drive the car for a given distance."""
        if self.is_running:
            self.mileage += miles
            return f"Drove {miles} miles. Total mileage: {self.mileage}"
        return "Start the engine first!"
    
    def __str__(self):
        """String representation of the car."""
        return f"{self.year} {self.color} {self.make} {self.model} ({self.mileage} miles)"

# Creating objects (instances of Car class)
car1 = Car("Toyota", "Camry", 2023, "Blue")
car2 = Car("Honda", "Civic", 2024, "Red")
car3 = Car("Ford", "Mustang", 2023, "Black")

# Each object has its own data
print(car1)  # 2023 Blue Toyota Camry (0 miles)
print(car2)  # 2024 Red Honda Civic (0 miles)

# Objects behave independently
car1.start_engine()
car1.drive(100)
print(car1)  # 2023 Blue Toyota Camry (100 miles)
print(car2)  # 2024 Red Honda Civic (0 miles) - unchanged

# Class variable is shared
print(f"Total cars produced: {Car.total_cars_produced}")  # 3
```

**Key Points:**
- **Class (Car)**: Defines what every car has (make, model, year, color, mileage) and can do (start, drive)
- **Objects (car1, car2, car3)**: Specific cars with their own unique values
- **Instance Variables**: Each car has its own make, model, mileage
- **Class Variables**: `total_cars_produced` is shared across all cars
- **Methods**: Functions that operate on the object's data

This is exactly like the Recipe class in our exercise - the Recipe class defines the blueprint, while `tea`, `coffee`, `cake`, etc., are specific recipe objects.

---

### 3. In your own words, write brief explanations of the following OOP concepts: inheritance, encapsulation, and polymorphism.

#### **1. Inheritance**

**Definition:** Inheritance allows a class to inherit attributes and methods from another class, creating a parent-child relationship. The child class (subclass) gets all the functionality of the parent class (superclass) and can add or override features.

**Purpose:** Promotes code reuse and establishes natural hierarchies.

**Example:**
```python
class Vehicle:
    """Parent class for all vehicles."""
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def start(self):
        return f"{self.brand} vehicle started."

class Car(Vehicle):
    """Child class inheriting from Vehicle."""
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)  # Call parent constructor
        self.doors = doors
    
    def honk(self):
        return "Beep beep!"

class Motorcycle(Vehicle):
    """Another child class inheriting from Vehicle."""
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar
    
    def wheelie(self):
        return "Doing a wheelie!"

# Both inherit start() from Vehicle
my_car = Car("Toyota", 2023, 4)
my_bike = Motorcycle("Harley", 2022, False)

print(my_car.start())    # Toyota vehicle started.
print(my_bike.start())   # Harley vehicle started.
print(my_car.honk())     # Beep beep!
print(my_bike.wheelie()) # Doing a wheelie!
```

**Benefits:**
- Avoid code duplication
- Create logical hierarchies
- Easy to extend functionality

---

#### **2. Encapsulation**

**Definition:** Encapsulation is the practice of bundling data (attributes) and methods that operate on that data within a single unit (class), and controlling access to that data through public interfaces (getters/setters).

**Purpose:** Protects data from unintended modification and hides internal implementation details.

**Example:**
```python
class BankAccount:
    """Demonstrates encapsulation."""
    
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute (convention)
    
    # Getter method (controlled read access)
    def get_balance(self):
        """Return the account balance."""
        return self.__balance
    
    # Setter method (controlled write access with validation)
    def deposit(self, amount):
        """Add money to account with validation."""
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid deposit amount."
    
    def withdraw(self, amount):
        """Remove money from account with validation."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Invalid withdrawal amount or insufficient funds."

# Using encapsulation
account = BankAccount("John Doe", 1000)

# Can't directly access __balance (it's encapsulated)
# account.__balance = 999999  # This won't work as expected

# Must use public methods
print(account.get_balance())  # 1000
print(account.deposit(500))   # Deposited $500. New balance: $1500
print(account.withdraw(200))  # Withdrew $200. New balance: $1300
print(account.withdraw(2000)) # Invalid withdrawal amount or insufficient funds.
```

**Benefits:**
- Data protection and validation
- Internal changes don't break external code
- Clear interface for interacting with objects

**In Exercise 1.5:**
```python
class Recipe:
    def __init__(self, name):
        self.name = name
        self.cooking_time = 0  # Protected data
    
    def get_cooking_time(self):
        return self.cooking_time
    
    def set_cooking_time(self, cooking_time):
        # Could add validation here
        self.cooking_time = cooking_time
```

---

#### **3. Polymorphism**

**Definition:** Polymorphism means "many forms." It allows different classes to be treated uniformly through a common interface, even though they may implement that interface differently.

**Purpose:** Write flexible, reusable code that works with different object types.

**Types:**
1. **Method Overriding**: Subclasses provide specific implementations of parent methods
2. **Operator Overloading**: Define how operators work with custom classes
3. **Duck Typing**: "If it walks like a duck and quacks like a duck, it's a duck"

**Example 1: Method Overriding**
```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Polymorphism in action - same method name, different behavior
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())  # Each calls its own version of speak()

# Output:
# Woof!
# Meow!
# Moo!
```

**Example 2: Operator Overloading (from Practice Tasks)**
```python
class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    
    def __sub__(self, other):
        """Overload the - operator for Height objects."""
        total_inches_self = self.feet * 12 + self.inches
        total_inches_other = other.feet * 12 + other.inches
        result_inches = total_inches_self - total_inches_other
        
        result_feet = result_inches // 12
        result_inches = result_inches % 12
        return Height(result_feet, result_inches)
    
    def __str__(self):
        return f"{self.feet}' {self.inches}\""

# Using the overloaded - operator
height1 = Height(5, 10)
height2 = Height(3, 9)
difference = height1 - height2  # Calls __sub__
print(difference)  # 2' 1"
```

**Example 3: Duck Typing**
```python
# Different classes with same method names
class PDFReport:
    def generate(self):
        return "Generating PDF report..."

class ExcelReport:
    def generate(self):
        return "Generating Excel report..."

class HTMLReport:
    def generate(self):
        return "Generating HTML report..."

def create_report(report_type):
    """Works with any object that has a generate() method."""
    return report_type.generate()

# Polymorphism - same function works with different types
print(create_report(PDFReport()))    # Generating PDF report...
print(create_report(ExcelReport()))  # Generating Excel report...
print(create_report(HTMLReport()))   # Generating HTML report...
```

**Benefits:**
- Write code that works with multiple types
- Easy to add new types without changing existing code
- More flexible and maintainable programs

**In Exercise 1.5:**
```python
class Recipe:
    def __str__(self):
        """Polymorphic method - Python knows how to print Recipe objects."""
        return f"Recipe: {self.name}"

# Python's print() function works with any object that has __str__()
print(tea)    # Calls tea.__str__()
print(coffee) # Calls coffee.__str__()
```

---

## Key Concepts Learned

### 1. Classes and Objects
- **Class**: Blueprint defining structure and behavior
- **Object**: Instance of a class with unique data
- **`__init__`**: Constructor method called when creating objects

### 2. Instance vs. Class Variables
```python
class Recipe:
    all_ingredients = []  # Class variable (shared by all instances)
    
    def __init__(self, name):
        self.name = name  # Instance variable (unique to each object)
```

### 3. Special Methods (Magic Methods)
- `__init__(self)`: Constructor
- `__str__(self)`: String representation
- `__sub__(self, other)`: Subtraction operator
- `__eq__(self, other)`: Equality operator (==)
- `__lt__(self, other)`: Less than operator (<)
- `__gt__(self, other)`: Greater than operator (>)

### 4. Getters and Setters
```python
def get_name(self):
    return self.name

def set_name(self, name):
    self.name = name
```

### 5. Variable-Length Arguments
```python
def add_ingredients(self, *ingredients):
    """Accepts any number of arguments."""
    for ingredient in ingredients:
        self.ingredients.append(ingredient)

# Usage
recipe.add_ingredients("Sugar", "Flour", "Eggs")
```

### 6. Operator Overloading
```python
def __sub__(self, other):
    # Define how - operator works with custom objects
    pass
```

---

## Code Examples from Exercise

### Practice Task 1: Shopping List
```python
class ShoppingList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []
    
    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(f"'{item}' added to {self.list_name}.")
    
    def view_list(self):
        print(f"\n{self.list_name}:")
        for item in self.shopping_list:
            print(f"  - {item}")

# Usage
pet_store_list = ShoppingList("Pet Store Shopping List")
pet_store_list.add_item("dog food")
pet_store_list.view_list()
```

### Practice Task 2: Height Subtraction
```python
class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    
    def __sub__(self, other):
        total_inches_self = self.feet * 12 + self.inches
        total_inches_other = other.feet * 12 + other.inches
        result_inches = total_inches_self - total_inches_other
        result_feet = result_inches // 12
        result_inches = result_inches % 12
        return Height(result_feet, result_inches)

# Usage
height1 = Height(5, 10)
height2 = Height(3, 9)
result = height1 - height2  # 2' 1"
```

### Practice Task 3: Height Comparison
```python
class Height:
    def __gt__(self, other):
        return (self.feet * 12 + self.inches) > (other.feet * 12 + other.inches)
    
    def __eq__(self, other):
        return (self.feet * 12 + self.inches) == (other.feet * 12 + other.inches)

# Usage
height1 = Height(5, 10)
height2 = Height(3, 9)
print(height1 > height2)  # True
```

### Main Task: Recipe OOP Application
```python
class Recipe:
    all_ingredients = []
    
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None
    
    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients)
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

# Usage
tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
print(tea.get_difficulty())  # Easy
```

---

## Challenges and Solutions

### Challenge 1: Understanding Class vs. Instance Variables
**Problem:** Initially confused about when to use class variables vs. instance variables.

**Solution:** 
- **Instance variables** (`self.name`, `self.ingredients`): Unique to each object
- **Class variables** (`Recipe.all_ingredients`): Shared across all objects
- Used class variable for tracking all ingredients across all recipes

### Challenge 2: Implementing Operator Overloading
**Problem:** Understanding how to make subtraction work with custom Height objects.

**Solution:**
```python
def __sub__(self, other):
    # Convert to common unit (inches)
    total_inches_self = self.feet * 12 + self.inches
    total_inches_other = other.feet * 12 + other.inches
    # Perform operation
    result_inches = total_inches_self - total_inches_other
    # Convert back to feet and inches
    result_feet = result_inches // 12
    result_inches = result_inches % 12
    return Height(result_feet, result_inches)
```

### Challenge 3: Variable-Length Arguments
**Problem:** How to accept any number of ingredients in `add_ingredients()`.

**Solution:** Use `*args` syntax:
```python
def add_ingredients(self, *ingredients):
    for ingredient in ingredients:
        self.ingredients.append(ingredient)
```

---

## Skills Developed

1. **OOP Design**: Creating classes that model real-world entities
2. **Encapsulation**: Using getters/setters to control data access
3. **Code Organization**: Structuring code in a modular, reusable way
4. **Special Methods**: Implementing magic methods for custom behavior
5. **Data Management**: Using class variables to track shared data
6. **Problem Solving**: Breaking down complex problems into methods
7. **Code Documentation**: Writing clear docstrings and comments

---

## Conclusion

Exercise 1.5 provided a solid foundation in Object-Oriented Programming, transforming my approach from procedural to object-oriented thinking. The progression from simple shopping lists to complex recipe management demonstrated how OOP principles scale from basic to real-world applications.

Key takeaways:
- OOP makes code more organized, reusable, and maintainable
- Classes provide blueprints for creating multiple similar objects
- Encapsulation protects data and provides controlled access
- Inheritance enables code reuse through parent-child relationships
- Polymorphism allows flexible, extensible code
- Special methods enable natural Python syntax with custom objects

These OOP concepts will be fundamental for building larger, more complex applications in future exercises, particularly web applications with Django.

---

**Date Completed:** October 19, 2025  
**Status:** ✅ All tasks completed successfully  
**Next Steps:** Exercise 1.6 - Continue building on OOP concepts
