# Exercise 1.4: File Handling in Python

## 📁 Project Overview

This project implements a complete recipe management system using Python's file handling capabilities. The system consists of two scripts that work together to store recipes in binary format and search them by ingredient.

**Key Features:**
- 🗂️ Persistent storage using binary files and pickle
- 🔍 Search recipes by ingredient
- ⚠️ Robust error handling
- 📊 Automatic difficulty calculation
- 🎯 User-friendly interface

---

## 📋 Table of Contents

- [Learning Objectives](#learning-objectives)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage Instructions](#usage-instructions)
- [Features](#features)
- [Code Examples](#code-examples)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Screenshots](#screenshots)
- [Learning Outcomes](#learning-outcomes)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## 🎯 Learning Objectives

By completing this exercise, I learned to:

✅ **File Operations:**
- Read from and write to text files
- Work with binary files using pickle module
- Understand file modes ('r', 'w', 'rb', 'wb')

✅ **Data Persistence:**
- Store complex data structures (lists, dictionaries)
- Retrieve saved data across program sessions
- Append new data without losing existing information

✅ **Directory Navigation:**
- Use os.getcwd() to find current directory
- Navigate with os.chdir()
- List contents with os.listdir()
- Create directories with os.mkdir()

✅ **Error Handling:**
- Implement try-except-else-finally blocks
- Handle specific exceptions (FileNotFoundError, ValueError, IndexError)
- Create robust, crash-resistant programs
- Provide user-friendly error messages

✅ **Application Development:**
- Build multi-script applications
- Design user-friendly interfaces
- Validate user input
- Create reusable functions

---

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **pickle** - Binary serialization module
- **os** - Operating system interface (for directory operations)
- **IPython** - Interactive Python shell for testing

---

## 📂 Project Structure

```
Exercise 1.4/main-task/
│
├── recipe_input.py          # Script to input and store recipes
├── recipe_search.py         # Script to search recipes by ingredient
├── recipes.bin              # Binary file storing recipe data
│
├── learning_journal.md      # Detailed learning reflections
├── learning_journey.md      # Personal growth documentation
├── README.md                # This file
│
├── MAIN_TASK_GUIDE.txt      # Step-by-step task instructions
│
└── screenshot/              # Screenshots of program execution
    ├── step1_input_tea.png
    ├── step2_input_pasta.png
    ├── step3_input_cake.png
    ├── step4_search_water.png
    └── step5_search_sugar.png
```

---

## 🚀 Installation & Setup

### Prerequisites

1. **Python 3.x installed**
   ```bash
   python --version
   ```

2. **Virtual Environment (Recommended)**
   ```bash
   # Create virtual environment
   python -m venv cf-python-base
   
   # Activate virtual environment
   # On Windows:
   .\cf-python-base\Scripts\Activate.ps1
   
   # On macOS/Linux:
   source cf-python-base/bin/activate
   ```

3. **IPython (Optional but recommended)**
   ```bash
   pip install ipython
   ```

### Installation Steps

1. Clone or download this repository
2. Navigate to the Exercise 1.4/main-task directory
3. Activate your virtual environment
4. You're ready to run the scripts!

---

## 📖 Usage Instructions

### Part 1: Adding Recipes (recipe_input.py)

#### Option A: Using Python directly
```bash
python recipe_input.py
```

#### Option B: Using IPython
```bash
ipython
%run recipe_input.py
```

#### Steps:
1. **Enter filename** when prompted (e.g., `recipes.bin`)
2. **Enter number of recipes** you want to add
3. **For each recipe, provide:**
   - Recipe name
   - Cooking time (in minutes)
   - Number of ingredients
   - Each ingredient name

#### Example Session:
```
Enter the filename where you'd like to store your recipes: recipes.bin
File doesn't exist - creating a new one.

How many recipes would you like to enter? 2

--- Recipe 1 ---
Enter the recipe name: Tea
Enter the cooking time (in minutes): 5
Enter the number of ingredients: 3
Enter ingredient 1: Tea Leaves
Enter ingredient 2: Sugar
Enter ingredient 3: Water

--- Recipe 2 ---
Enter the recipe name: Pasta
Enter the cooking time (in minutes): 15
Enter the number of ingredients: 5
Enter ingredient 1: Pasta
Enter ingredient 2: Tomato Sauce
Enter ingredient 3: Garlic
Enter ingredient 4: Olive Oil
Enter ingredient 5: Basil

Recipes saved successfully to recipes.bin!
```

---

### Part 2: Searching Recipes (recipe_search.py)

#### Running the script:
```bash
python recipe_search.py
```

#### Steps:
1. **Enter filename** containing your recipes (e.g., `recipes.bin`)
2. **View list of available ingredients** with index numbers
3. **Select ingredient number** to search for
4. **View all recipes** containing that ingredient

#### Example Session:
```
Enter the filename where your recipes are stored: recipes.bin

Available ingredients:
--------------------------------------------------
0. Tea Leaves
1. Sugar
2. Water
3. Pasta
4. Tomato Sauce
5. Garlic
6. Olive Oil
7. Basil
--------------------------------------------------

Enter the number of the ingredient you'd like to search for: 2

Recipes containing 'Water':

==================================================
Recipe: Tea
==================================================
Cooking Time: 5 minutes
Difficulty: Easy
Ingredients:
  - Tea Leaves
  - Sugar
  - Water
==================================================
```

---

## ✨ Features

### 1. **Automatic Difficulty Calculation**

The system automatically calculates recipe difficulty based on:

| Cooking Time | Ingredients | Difficulty |
|--------------|-------------|------------|
| < 10 minutes | < 4 items   | Easy       |
| < 10 minutes | ≥ 4 items   | Medium     |
| ≥ 10 minutes | < 4 items   | Intermediate |
| ≥ 10 minutes | ≥ 4 items   | Hard       |

**Implementation:**
```python
def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"
```

---

### 2. **Persistent Data Storage**

Uses Python's pickle module to:
- Store complex nested data structures
- Preserve exact data types
- Enable fast serialization/deserialization
- Maintain data integrity across sessions

**Data Structure:**
```python
data = {
    'recipes_list': [
        {
            'name': 'Tea',
            'cooking_time': 5,
            'ingredients': ['Tea Leaves', 'Sugar', 'Water'],
            'difficulty': 'Easy'
        },
        # ... more recipes
    ],
    'all_ingredients': ['Tea Leaves', 'Sugar', 'Water', 'Pasta', ...]
}
```

---

### 3. **Comprehensive Error Handling**

Both scripts handle multiple error scenarios:

**recipe_input.py handles:**
- ✅ FileNotFoundError (creates new file)
- ✅ Unexpected errors (starts fresh)
- ✅ Always extracts data in finally block

**recipe_search.py handles:**
- ✅ FileNotFoundError (file doesn't exist)
- ✅ ValueError (invalid number input)
- ✅ IndexError (out-of-range selection)
- ✅ General exceptions (unexpected errors)

---

### 4. **Ingredient Tracking**

- Maintains a master list of all unique ingredients
- Automatically adds new ingredients
- Avoids duplicates
- Enables efficient searching

---

### 5. **User-Friendly Interface**

- Clear prompts for all inputs
- Formatted output for readability
- Helpful error messages
- Numbered ingredient selection
- Visual separators for recipes

---

## 💻 Code Examples

### Example 1: Using Pickle to Save Data

```python
import pickle

# Prepare data
data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
}

# Save to binary file
with open('recipes.bin', 'wb') as file:
    pickle.dump(data, file)
```

### Example 2: Loading Data with Error Handling

```python
try:
    file = open(filename, 'rb')
    data = pickle.load(file)
except FileNotFoundError:
    print("File doesn't exist - creating a new one.")
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']
```

### Example 3: Searching with Multiple Exception Handlers

```python
try:
    ingredient_index = int(input("Enter ingredient number: "))
    ingredient_searched = all_ingredients[ingredient_index]
except ValueError:
    print("Error: Please enter a valid number.")
except IndexError:
    print("Error: The number you entered is not in the list.")
else:
    # Search and display recipes
    for recipe in recipes_list:
        if ingredient_searched in recipe['ingredients']:
            display_recipe(recipe)
```

---

## ⚠️ Error Handling

### Common Errors & Solutions

#### Error 1: File Not Found
```
Error: File 'recipes.bin' not found.
Please make sure you've created recipes using recipe_input.py first.
```
**Solution:** Run recipe_input.py to create the file first.

#### Error 2: Invalid Input
```
Error: Please enter a valid number.
```
**Solution:** Enter a numeric value when selecting ingredients.

#### Error 3: Out of Range
```
Error: The number you entered is not in the list.
```
**Solution:** Select a number from the displayed list.

---

## 🧪 Testing

### Test Case 1: First Time Usage
1. Run recipe_input.py with new filename
2. Add 3 recipes (Easy, Medium, Hard difficulty)
3. Verify recipes.bin is created
4. Run recipe_search.py
5. Search for common ingredient
6. Verify correct recipes are displayed

**Result:** ✅ Passed

---

### Test Case 2: Appending Recipes
1. Run recipe_input.py with existing filename
2. Add 2 more recipes
3. Verify existing recipes are preserved
4. Verify new recipes are added
5. Search for new ingredients

**Result:** ✅ Passed

---

### Test Case 3: Error Handling
1. Try to search without creating file first
2. Enter invalid ingredient number (text)
3. Enter out-of-range ingredient number
4. Verify all errors are handled gracefully

**Result:** ✅ Passed

---

## 📸 Screenshots

Screenshots demonstrating the complete workflow are available in the `screenshot/` folder:

1. **step1_input_tea.png** - Adding first recipe (Easy difficulty)
2. **step2_input_pasta.png** - Adding second recipe (Medium difficulty)
3. **step3_input_cake.png** - Adding third recipe (Hard difficulty)
4. **step4_search_water.png** - Searching for recipes with "Water"
5. **step5_search_sugar.png** - Searching for recipes with "Sugar"
6. **step6_error_handling.png** - Demonstrating error handling

---

## 🎓 Learning Outcomes

### Technical Skills Acquired:

1. **File I/O Mastery**
   - Reading and writing files
   - Working with text and binary files
   - Understanding file modes
   - Proper file closing with else blocks

2. **Pickle Module Proficiency**
   - Serializing complex data structures
   - Deserializing saved data
   - Understanding pickle limitations
   - When to use pickle vs other formats

3. **Error Handling Expertise**
   - try-except-else-finally structure
   - Handling specific exception types
   - Creating user-friendly error messages
   - Preventing program crashes

4. **Directory Management**
   - Navigating with os module
   - Understanding working directories
   - Listing and creating directories

### Conceptual Understanding:

- **Data Persistence:** How programs save state
- **Error Recovery:** Building robust applications
- **User Experience:** Providing helpful feedback
- **Code Organization:** Separating concerns into functions
- **Data Structures:** Choosing appropriate structures for tasks

---

## 🚀 Future Improvements

### Planned Enhancements:

1. **Add Recipe Editing**
   - Modify existing recipes
   - Delete recipes
   - Update ingredients

2. **Advanced Search**
   - Search by multiple ingredients
   - Search by difficulty level
   - Search by cooking time range

3. **Export Functionality**
   - Export to JSON format
   - Export to CSV for spreadsheets
   - Generate recipe cards (PDF)

4. **GUI Implementation**
   - Build graphical interface with Tkinter
   - Add recipe images
   - Visual difficulty indicators

5. **Data Validation**
   - Validate ingredient names
   - Check for duplicate recipes
   - Verify cooking time ranges

6. **Recipe Categories**
   - Categorize by meal type
   - Add cuisine tags
   - Create recipe collections

---

## 📊 Project Statistics

- **Lines of Code:** ~250
- **Functions Created:** 4
- **Files Created:** 2 scripts + 1 data file
- **Error Types Handled:** 4
- **Test Cases Passed:** 3/3
- **Time to Complete:** 3 hours
- **Difficulty Level:** Intermediate

---

## 🔗 Related Exercises

- **Exercise 1.1:** Introduction to Python Basics
- **Exercise 1.2:** Data Structures (Lists, Tuples, Dictionaries)
- **Exercise 1.3:** Operators and Functions
- **Exercise 1.5:** Object-Oriented Programming *(Coming Next)*

---

## 📚 Resources Used

- [Python Official Documentation - File I/O](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python pickle Module](https://docs.python.org/3/library/pickle.html)
- [Python os Module](https://docs.python.org/3/library/os.html)
- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
- CareerFoundry Python Course Materials

---

## 👤 Author

**Sourav Das**  
*Full-Stack Web Development Student*  
*CareerFoundry - Python Specialization*

- GitHub: [@souravdas090300](https://github.com/souravdas090300)
- Repository: [python-web-development](https://github.com/souravdas090300/python-web-development)

---

## 📝 License

This project is part of my educational journey with CareerFoundry.  
Created for learning purposes.

---

## ✅ Submission Checklist

- [x] recipe_input.py implemented and tested
- [x] recipe_search.py implemented and tested
- [x] recipes.bin created with sample data
- [x] Error handling implemented in both scripts
- [x] Screenshots captured for all steps
- [x] learning_journal.md completed
- [x] learning_journey.md completed
- [x] README.md created
- [x] All files uploaded to GitHub
- [x] Repository link submitted

---

## 🎯 Key Takeaways

> **"Programs that can't save data are just toys. Programs that can't handle errors are fragile. This exercise taught me how to build real, professional applications that store data reliably and handle problems gracefully."**

This exercise was transformational because it taught me:
1. How to make programs remember data across sessions
2. How to handle errors without crashing
3. How to think about user experience
4. How real-world applications work behind the scenes

---

**Last Updated:** October 18, 2025  
**Status:** ✅ Complete  
**Ready for Review:** Yes
