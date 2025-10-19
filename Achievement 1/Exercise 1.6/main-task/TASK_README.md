# Exercise 1.6 - Databases in Python with MySQL

## 📋 Overview

This exercise introduces **database management** using MySQL and Python, focusing on creating, reading, updating, and deleting (CRUD) data through a command-line Recipe Management System.

**Student:** Sourav Das  
**Course:** Python for Web Developers  
**Date:** October 19, 2025  
**Status:** ✅ Completed

---

## 🎯 Learning Objectives

By completing this exercise, I have learned to:

- ✅ Understand relational database management systems (RDBMS)
- ✅ Install and configure MySQL server
- ✅ Create MySQL users and grant privileges
- ✅ Connect Python to MySQL using mysql-connector-python
- ✅ Execute SQL queries from Python scripts
- ✅ Perform CRUD operations (Create, Read, Update, Delete)
- ✅ Use SQL statements: CREATE, INSERT, SELECT, UPDATE, DELETE
- ✅ Implement parameterized queries to prevent SQL injection
- ✅ Manage database connections and transactions
- ✅ Convert between Python lists and SQL comma-separated strings
- ✅ Build a complete database-driven application

---

## 📂 Project Structure

```
Exercise 1.6/
│
├── 1.6-Practice Task 1/
│   └── screenshot/                # Practice screenshots
│       └── [various screenshots]
│
├── Exercise 1.6-Task/
│   ├── recipe_mysql.py            # Complete recipe management system
│   └── screenshots/               # Task execution screenshots
│       ├── 01-create-recipes.png
│       ├── 02-search-recipes.png
│       ├── 03-update-recipes.png
│       ├── 04-delete-recipe.png
│       └── 05-exit-program.png
│
├── recipe_mysql.py                # Main script file
├── learning_journal.md            # Detailed reflection and learnings
├── learning_journey.md            # Personal growth documentation
└── README.md                      # This file
```

---

## 🗄️ Database Schema

### Database: `task_database`

### Table: `Recipes`

| Column | Data Type | Constraints | Description |
|--------|-----------|-------------|-------------|
| `id` | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for each recipe |
| `name` | VARCHAR(50) | | Name of the recipe |
| `ingredients` | VARCHAR(255) | | Comma-separated list of ingredients |
| `cooking_time` | INT | | Cooking time in minutes |
| `difficulty` | VARCHAR(20) | | Easy, Medium, Intermediate, or Hard |

**Example Data:**
```
+----+-----------+--------------------------------+--------------+-------------+
| id | name      | ingredients                    | cooking_time | difficulty  |
+----+-----------+--------------------------------+--------------+-------------+
|  1 | Tea       | Tea Leaves, Sugar, Water       |            5 | Easy        |
|  2 | Sushi     | Rice, Fish, Avocado, Nori      |           40 | Hard        |
|  3 | Pancakes  | Flour, Eggs, Milk, Sugar       |           15 | Hard        |
|  4 | Smoothie  | Bananas, Milk, Honey, Ice      |            5 | Medium      |
+----+-----------+--------------------------------+--------------+-------------+
```

---

## 🚀 Features

### 1. Create Recipe
- Collects recipe name, cooking time, and ingredients from user
- Automatically calculates difficulty based on time and ingredient count
- Converts ingredient list to comma-separated string for MySQL storage
- Inserts new recipe into database

### 2. Search Recipe by Ingredient
- Displays all unique ingredients from all recipes
- Allows user to select ingredient to search for
- Uses SQL `LIKE` operator with wildcards for flexible searching
- Displays all recipes containing the selected ingredient

### 3. Update Recipe
- Lists all recipes with their IDs
- Allows user to select recipe to update
- Supports updating: name, cooking time, or ingredients
- Automatically recalculates difficulty when time or ingredients change
- Commits changes to database

### 4. Delete Recipe
- Displays all recipes with IDs
- Allows user to select recipe for deletion
- Confirms deletion before executing
- Removes recipe from database

### 5. Exit Program
- Commits all pending changes
- Safely closes database connection
- Clean program termination

---

## 💻 Technical Implementation

### Database Connection

```python
import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)

# Create cursor for executing queries
cursor = conn.cursor()

# Select database
cursor.execute("USE task_database")
```

### Difficulty Calculation Logic

```python
def calculate_difficulty(cooking_time, ingredients):
    """
    Easy: < 10 min AND < 4 ingredients
    Medium: < 10 min AND >= 4 ingredients
    Intermediate: >= 10 min AND < 4 ingredients
    Hard: >= 10 min AND >= 4 ingredients
    """
    num_ingredients = len(ingredients)
    
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"
```

### CRUD Operations

#### Create (INSERT)
```python
def create_recipe(conn, cursor):
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (minutes): "))
    
    ingredients = []
    num_ingredients = int(input("How many ingredients? "))
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)
    
    # Calculate difficulty
    difficulty = calculate_difficulty(cooking_time, ingredients)
    
    # Convert list to comma-separated string
    ingredients_str = ", ".join(ingredients)
    
    # Insert into database using parameterized query
    sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (name, ingredients_str, cooking_time, difficulty)
    cursor.execute(sql, val)
    conn.commit()
```

#### Read (SELECT)
```python
def search_recipe(conn, cursor):
    # Get all ingredients from database
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    
    # Build unique ingredients list
    all_ingredients = []
    for row in results:
        ingredients_list = [ing.strip() for ing in row[0].split(',')]
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    # Display ingredients
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")
    
    # Search using LIKE with wildcards
    choice = int(input("Enter ingredient number: "))
    search_ingredient = all_ingredients[choice - 1]
    search_pattern = f"%{search_ingredient}%"
    
    cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", (search_pattern,))
    results = cursor.fetchall()
    
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Difficulty: {row[4]}")
```

#### Update (UPDATE)
```python
def update_recipe(conn, cursor):
    # Display all recipes
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]}")
    
    recipe_id = int(input("Enter recipe ID to update: "))
    
    # Choose what to update
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")
    choice = int(input("Enter choice: "))
    
    if choice == 2:  # Cooking time - need to recalculate difficulty
        new_time = int(input("Enter new cooking time: "))
        
        # Get current ingredients
        cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        ingredients_str = cursor.fetchone()[0]
        ingredients_list = ingredients_str.split(', ')
        
        # Recalculate difficulty
        new_difficulty = calculate_difficulty(new_time, ingredients_list)
        
        # Update both time and difficulty
        cursor.execute("UPDATE Recipes SET cooking_time = %s, difficulty = %s WHERE id = %s",
                      (new_time, new_difficulty, recipe_id))
    
    conn.commit()
```

#### Delete (DELETE)
```python
def delete_recipe(conn, cursor):
    # Display all recipes
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]}")
    
    recipe_id = int(input("Enter recipe ID to delete: "))
    
    # Confirm deletion
    cursor.execute("SELECT name FROM Recipes WHERE id = %s", (recipe_id,))
    recipe_name = cursor.fetchone()[0]
    confirm = input(f"Delete '{recipe_name}'? (yes/no): ")
    
    if confirm.lower() == 'yes':
        cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
        conn.commit()
        print("Recipe deleted successfully!")
```

---

## 🔐 Security Features

### 1. SQL Injection Prevention

**Always use parameterized queries:**
```python
# ❌ VULNERABLE
search = input("Enter ingredient: ")
cursor.execute(f"SELECT * FROM Recipes WHERE ingredients LIKE '%{search}%'")

# ✓ SAFE
search = input("Enter ingredient: ")
cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", (f"%{search}%",))
```

### 2. Input Validation

```python
try:
    cooking_time = int(input("Enter cooking time: "))
except ValueError:
    print("Invalid input! Please enter a number.")
```

### 3. Connection Management

```python
try:
    conn = mysql.connector.connect(...)
    # ... operations ...
    conn.commit()
except mysql.connector.Error as err:
    print(f"Database Error: {err}")
    conn.rollback()
finally:
    conn.close()
```

---

## 🏃‍♂️ How to Run

### Prerequisites

1. **MySQL Server** installed and running
2. **Python 3.x** installed
3. **mysql-connector-python** package installed
4. **MySQL user** configured:
   - Username: `cf-python`
   - Password: `password`
   - Privileges: ALL on all databases

### Installation Steps

#### 1. Install MySQL Server
- Windows: Download from mysql.com
- Mac: `brew install mysql`
- Linux: `sudo apt-get install mysql-server`

#### 2. Create MySQL User
```sql
-- In MySQL Command Line Client
CREATE USER 'cf-python'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'cf-python'@'localhost';
FLUSH PRIVILEGES;
```

#### 3. Install Python Package
```bash
pip install mysql-connector-python
```

### Running the Application

```bash
# Navigate to Exercise 1.6 directory
cd "c:\Users\dasau\python-web-development\Exercise 1.6"

# Activate virtual environment (optional)
..\Exercise 1.4\cf-python-base\Scripts\Activate.ps1

# Run the script
python recipe_mysql.py
```

---

## 📸 Screenshots

All screenshots documenting the execution are located in:
- **Practice Task:** `1.6-Practice Task 1/screenshot/`
- **Main Task:** `Exercise 1.6-Task/screenshots/`

### Screenshot Requirements Met:

1. ✅ **Create Recipes**: 3-4 recipes created successfully
2. ✅ **Search Recipes**: Search by ingredient functionality demonstrated
3. ✅ **Update Recipes**: 2-3 recipe updates performed
4. ✅ **Delete Recipe**: One recipe deleted
5. ✅ **Exit Program**: Clean program termination

---

## 📚 Key Learning Points

### Database Advantages Over Files

| Aspect | Files | Database |
|--------|-------|----------|
| **Structure** | Unstructured | Structured tables |
| **Speed** | Slow searches | Optimized queries |
| **Concurrent Access** | Difficult | Native support |
| **Data Integrity** | Manual validation | Built-in constraints |
| **Relationships** | Manual linking | Foreign keys |
| **Security** | File permissions | User authentication |

### SQL Commands Used

```sql
-- Database Management
CREATE DATABASE IF NOT EXISTS task_database;
USE task_database;

-- Table Management
CREATE TABLE IF NOT EXISTS Recipes (...);
DROP TABLE IF EXISTS Recipes;
ALTER TABLE Recipes ADD COLUMN ...;

-- Data Operations
INSERT INTO Recipes (name, ...) VALUES (%s, ...);
SELECT * FROM Recipes;
SELECT * FROM Recipes WHERE ingredients LIKE %s;
UPDATE Recipes SET name = %s WHERE id = %s;
DELETE FROM Recipes WHERE id = %s;
```

### Python-MySQL Integration

```python
# Connection
import mysql.connector
conn = mysql.connector.connect(host, user, passwd)
cursor = conn.cursor()

# Execution
cursor.execute("SQL QUERY", (parameters,))

# Fetching Results
single_row = cursor.fetchone()
all_rows = cursor.fetchall()

# Transaction Management
conn.commit()  # Save changes
conn.rollback()  # Undo changes

# Cleanup
cursor.close()
conn.close()
```

---

## 🎓 Skills Developed

1. **Database Design**: Creating normalized schemas with appropriate data types
2. **SQL Proficiency**: Writing complex queries with joins, wildcards, and conditions
3. **Python Integration**: Using mysql-connector-python library effectively
4. **CRUD Operations**: Implementing all four basic database operations
5. **Error Handling**: Managing database exceptions gracefully
6. **Security**: Preventing SQL injection with parameterized queries
7. **Data Transformation**: Converting between Python and SQL data types
8. **User Interface**: Building intuitive menu-driven applications
9. **Transaction Management**: Using commit/rollback appropriately
10. **Code Organization**: Structuring code with modular functions

---

## 🔮 Real-World Applications

This exercise prepared me for:

- **Web Development**: Backend systems with Django/Flask
- **E-commerce**: Product catalogs, inventory, orders
- **Content Management**: Blogs, articles, media libraries
- **User Systems**: Authentication, profiles, permissions
- **Analytics**: Data collection and reporting systems
- **APIs**: RESTful services with database backends

---

## 🎯 Completion Checklist

### Part 1: Database Setup
- ✅ MySQL server installed and running
- ✅ User 'cf-python' created with proper privileges
- ✅ Database `task_database` created
- ✅ Table `Recipes` created with correct schema

### Part 2: Main Menu
- ✅ Menu loop implemented
- ✅ Four options functional
- ✅ Exit option closes connection properly

### Part 3: Create Recipe
- ✅ Collect recipe details from user
- ✅ Calculate difficulty automatically
- ✅ Convert ingredients list to string
- ✅ Insert into database

### Part 4: Search Recipe
- ✅ Fetch all ingredients from database
- ✅ Build unique ingredients list
- ✅ Use LIKE operator with wildcards
- ✅ Display matching recipes

### Part 5: Update Recipe
- ✅ Display all recipes
- ✅ Allow column selection
- ✅ Recalculate difficulty when needed
- ✅ Commit changes

### Part 6: Delete Recipe
- ✅ Display all recipes
- ✅ Confirm deletion
- ✅ Execute DELETE query
- ✅ Commit changes

### Part 7: Testing & Documentation
- ✅ 3-4 recipes created
- ✅ Search functionality tested
- ✅ 2-3 recipes updated
- ✅ 1 recipe deleted
- ✅ Program exited cleanly
- ✅ Screenshots captured
- ✅ Learning journal written
- ✅ README documentation created

---

## 🐛 Troubleshooting

### Common Issues and Solutions

**Issue 1: Module not found error**
```
ModuleNotFoundError: No module named 'mysql'
```
**Solution:**
```bash
pip install mysql-connector-python
```

**Issue 2: Connection refused**
```
mysql.connector.errors.DatabaseError: 2003: Can't connect to MySQL server
```
**Solution:** Ensure MySQL server is running

**Issue 3: Access denied**
```
mysql.connector.errors.ProgrammingError: 1045: Access denied for user 'cf-python'
```
**Solution:** Check username and password, grant privileges

**Issue 4: Database doesn't exist**
```
mysql.connector.errors.ProgrammingError: 1049: Unknown database 'task_database'
```
**Solution:** Script creates database automatically, ensure user has CREATE privileges

---

## 📖 Additional Resources

- [MySQL Official Documentation](https://dev.mysql.com/doc/)
- [mysql-connector-python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)
- [Python Database API Specification](https://peps.python.org/pep-0249/)

---

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | October 19, 2025 | Initial completion of all tasks |

---

## 👨‍💻 Author

**Sourav Das**  
Python for Web Developers Course  
October 2025

---

## 📝 Notes

This exercise represents a crucial transition from file-based data storage to professional database-driven applications. The concepts learned here—SQL queries, database connections, CRUD operations, and data integrity—are fundamental to modern web development and will be extensively used in Django framework.

**Key Achievement:** Successfully built a complete database-driven command-line application with all four CRUD operations, demonstrating proficiency in both Python and SQL.

**Next Steps:** Apply these database concepts in Exercise 1.7 and prepare for Django's Object-Relational Mapper (ORM) which abstracts database operations into Python objects.

---

**Exercise Status:** ✅ **COMPLETED**  
**Date Completed:** October 19, 2025  
**Total Time Invested:** ~6 hours  
**Lines of Code:** ~350 lines  
**SQL Queries Written:** ~25 queries
