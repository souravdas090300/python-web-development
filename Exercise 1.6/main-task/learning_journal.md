# Learning Journal - Exercise 1.6
## Databases in Python - MySQL Integration

**Student:** Sourav Das  
**Date:** October 19, 2025  
**Course:** Python for Web Developers  
**Exercise:** 1.6 - Introduction to Databases and MySQL

---

## Learning Objectives Achieved

This exercise focused on understanding and implementing database operations in Python, including:
- Understanding relational database management systems (RDBMS)
- Installing and configuring MySQL server
- Connecting Python to MySQL using mysql-connector-python
- Creating databases and tables with SQL queries
- Performing CRUD operations (Create, Read, Update, Delete)
- Using SQL statements: CREATE, INSERT, SELECT, UPDATE, DELETE
- Managing database connections and transactions
- Converting between Python data types and SQL data types
- Working with comma-separated strings to simulate arrays

---

## Reflection Questions

### 1. What are databases and what are their advantages over using files to store data?

**What is a Database?**

A **database** is an organized collection of structured data stored electronically in a computer system. It's managed by a Database Management System (DBMS), which provides tools to create, read, update, and delete data efficiently and securely.

**Types of Databases:**
- **Relational Databases (RDBMS)**: Store data in tables with rows and columns (e.g., MySQL, PostgreSQL, SQLite)
- **NoSQL Databases**: Store data in various formats like documents, key-value pairs, graphs (e.g., MongoDB, Redis)
- **In-Memory Databases**: Store data in RAM for ultra-fast access (e.g., Redis, Memcached)

---

**Comparison: Databases vs. File Storage**

| Aspect | File Storage | Database |
|--------|-------------|----------|
| **Data Organization** | Unstructured or semi-structured files | Structured tables with defined schemas |
| **Data Integrity** | Manual validation required | Built-in constraints and validation |
| **Concurrent Access** | Difficult, can cause corruption | Multiple users simultaneously, with locking |
| **Search/Query** | Manual parsing, slow | Optimized SQL queries, very fast |
| **Scalability** | Poor, files become unwieldy | Excellent, handles millions of records |
| **Security** | Basic file permissions | User authentication, role-based access |
| **Data Relationships** | Manual linking required | Built-in foreign keys and relationships |
| **Backup/Recovery** | Manual file copying | Automated backups and transaction logs |
| **Data Redundancy** | High, duplicate data common | Normalized, minimal redundancy |

---

**Advantages of Databases Over Files:**

**1. Data Integrity and Validation**
```python
# File Storage - No validation
with open('recipes.txt', 'a') as file:
    file.write("Tea,,5,")  # Can write incomplete data!

# Database - Enforces constraints
cursor.execute("INSERT INTO Recipes (name, cooking_time) VALUES (%s, %s)", 
               ("Tea", 5))
# If 'name' is required, database prevents NULL values
```

**2. Efficient Searching and Querying**
```python
# File Storage - Must read entire file
with open('recipes.txt', 'r') as file:
    for line in file:
        if 'Sugar' in line:  # Slow linear search
            print(line)

# Database - Optimized indexed search
cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", ("%Sugar%",))
# Instant results even with millions of records!
```

**3. Concurrent Access**
```python
# File Storage - Can cause corruption
# User A opens file → reads data → modifies
# User B opens file → reads same data → modifies
# One user's changes overwrite the other!

# Database - Handles concurrency automatically
# Multiple users can read/write simultaneously
# Database uses locking mechanisms to prevent conflicts
```

**4. Data Relationships**
```python
# File Storage - Manual linking
# recipes.txt: "1,Tea,5"
# ingredients.txt: "1,Sugar", "1,Water", "1,Tea Leaves"
# Must manually maintain relationships!

# Database - Built-in relationships
"""
Recipes table:       Ingredients table:
id | name           recipe_id | ingredient
1  | Tea            1         | Sugar
                    1         | Water
                    1         | Tea Leaves
                    
Can use JOIN to connect them automatically!
"""
```

**5. Transaction Management**
```python
# File Storage - No rollback
file.write("Recipe 1")  # Written
file.write("Recipe 2")  # Written
# If error occurs, Recipe 1 is already saved (inconsistent state)

# Database - ACID properties
cursor.execute("INSERT INTO Recipes ...")  # Not saved yet
cursor.execute("INSERT INTO Ingredients ...")  # Not saved yet
conn.commit()  # Both saved together
# If error occurs before commit(), both are rolled back (consistent state)
```

**6. Security and Access Control**
```python
# File Storage - Basic file permissions (read/write/execute)

# Database - Granular permissions
"""
GRANT SELECT ON Recipes TO 'viewer';  # Can only read
GRANT INSERT, UPDATE ON Recipes TO 'editor';  # Can add/modify
GRANT ALL PRIVILEGES ON Recipes TO 'admin';  # Full access
"""
```

**Real-World Example:**

Imagine a library system:
- **File Storage**: Each book is a text file. To find all books by "J.K. Rowling", you'd need to open every single file and search. If 10 people try to borrow the same book simultaneously, chaos ensues!
- **Database**: One query finds all books instantly. Multiple people can search simultaneously. When someone borrows a book, the system automatically updates availability. You can easily see borrowing history, popular books, overdue items, etc.

---

### 2. What is the difference between a Primary Key and a Foreign Key in a database?

**Primary Key and Foreign Key** are fundamental concepts in relational databases that establish relationships between tables and ensure data integrity.

---

#### **Primary Key**

**Definition:** A Primary Key is a unique identifier for each row in a table. It ensures that no two rows have the same identifier and that every row can be uniquely identified.

**Characteristics:**
- **Unique**: No duplicate values allowed
- **Not NULL**: Cannot be empty or NULL
- **Immutable**: Should not change once set
- **One per table**: Only one primary key per table
- **Indexed**: Automatically creates an index for fast lookups

**Example:**
```sql
CREATE TABLE Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Primary Key
    name VARCHAR(50),
    cooking_time INT
);
```

**In Our Exercise:**
```python
# Creating recipes with auto-incrementing ID (Primary Key)
cursor.execute("""CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each recipe
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)""")

# Each recipe gets a unique ID automatically
cursor.execute("INSERT INTO Recipes (name, cooking_time) VALUES ('Tea', 5)")
# ID = 1 (automatically assigned)

cursor.execute("INSERT INTO Recipes (name, cooking_time) VALUES ('Coffee', 5)")
# ID = 2 (automatically assigned)
```

---

#### **Foreign Key**

**Definition:** A Foreign Key is a column (or set of columns) in one table that references the Primary Key in another table. It creates a link between two tables and enforces referential integrity.

**Characteristics:**
- **References another table**: Points to a Primary Key in another table
- **Can be NULL**: Unless specified otherwise
- **Can have duplicates**: Multiple rows can reference the same foreign key
- **Enforces relationships**: Maintains data integrity between tables
- **Cascading actions**: Can automatically update/delete related rows

**Example:**
```sql
-- Parent table (has Primary Key)
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
);

-- Child table (has Foreign Key)
CREATE TABLE Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    user_id INT,  -- Foreign Key
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
```

---

#### **Real-World Example: Recipe and User Relationship**

Imagine we want to track which user created each recipe:

```sql
-- Users table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Primary Key
    username VARCHAR(50),
    email VARCHAR(100)
);

-- Recipes table
CREATE TABLE Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Primary Key
    name VARCHAR(50),
    cooking_time INT,
    created_by INT,  -- Foreign Key referencing Users table
    FOREIGN KEY (created_by) REFERENCES Users(user_id)
);

-- Sample Data
INSERT INTO Users (username, email) VALUES 
    ('john_doe', 'john@example.com'),    -- user_id = 1
    ('jane_smith', 'jane@example.com');  -- user_id = 2

INSERT INTO Recipes (name, cooking_time, created_by) VALUES 
    ('Tea', 5, 1),          -- Created by john_doe
    ('Coffee', 5, 1),       -- Created by john_doe
    ('Pancakes', 15, 2);    -- Created by jane_smith

-- Try to insert invalid data
INSERT INTO Recipes (name, cooking_time, created_by) VALUES 
    ('Pizza', 30, 999);  -- ERROR! user_id 999 doesn't exist
    -- Foreign key constraint prevents this!
```

---

#### **Visual Comparison**

```
┌─────────────────────────────────┐
│         Users Table             │
├──────────┬──────────┬───────────┤
│ user_id  │ username │  email    │  ← Primary Key (unique identifier)
│ (PK)     │          │           │
├──────────┼──────────┼───────────┤
│    1     │ john_doe │ john@...  │
│    2     │ jane_s...│ jane@...  │
└──────────┴──────────┴───────────┘
           ↑
           │
           │ References
           │
┌──────────┴────────────────────────┐
│         Recipes Table             │
├─────┬───────────┬──────┬──────────┤
│ id  │   name    │ time │created_by│  ← Foreign Key (references Users)
│(PK) │           │      │  (FK)    │
├─────┼───────────┼──────┼──────────┤
│  1  │ Tea       │  5   │    1     │  (created by john_doe)
│  2  │ Coffee    │  5   │    1     │  (created by john_doe)
│  3  │ Pancakes  │ 15   │    2     │  (created by jane_smith)
└─────┴───────────┴──────┴──────────┘
```

---

#### **Key Differences Summary**

| Aspect | Primary Key | Foreign Key |
|--------|------------|-------------|
| **Purpose** | Uniquely identify rows in THIS table | Link to rows in ANOTHER table |
| **Uniqueness** | Must be unique | Can have duplicates |
| **NULL values** | Cannot be NULL | Can be NULL (unless specified) |
| **Number per table** | Only ONE per table | Can have MULTIPLE per table |
| **References** | Doesn't reference anything | References Primary Key in another table |
| **Auto-increment** | Often used with AUTO_INCREMENT | Never auto-increments |

---

#### **Benefits of Primary and Foreign Keys**

**1. Data Integrity**
```sql
-- Without Foreign Key
INSERT INTO Recipes (name, created_by) VALUES ('Tea', 999);
-- Creates orphan record (user 999 doesn't exist)

-- With Foreign Key
INSERT INTO Recipes (name, created_by) VALUES ('Tea', 999);
-- ERROR: Cannot add - user 999 doesn't exist
-- Database prevents invalid data!
```

**2. Cascading Actions**
```sql
CREATE TABLE Recipes (
    id INT PRIMARY KEY,
    created_by INT,
    FOREIGN KEY (created_by) REFERENCES Users(user_id)
        ON DELETE CASCADE  -- If user deleted, delete their recipes
        ON UPDATE CASCADE  -- If user_id changes, update recipes
);

-- If we delete user with id=1
DELETE FROM Users WHERE user_id = 1;
-- All recipes with created_by=1 are automatically deleted!
```

**3. Query Joins**
```sql
-- Find all recipes with their creator's username
SELECT Recipes.name, Recipes.cooking_time, Users.username
FROM Recipes
JOIN Users ON Recipes.created_by = Users.user_id;

-- Result:
-- name     | cooking_time | username
-- Tea      | 5           | john_doe
-- Coffee   | 5           | john_doe
-- Pancakes | 15          | jane_smith
```

---

### 3. When would you use Python to interact with a database, and what would be the limitations of that interaction?

#### **When to Use Python for Database Interaction**

Python is an excellent choice for database interaction in many scenarios:

---

**1. Web Applications (Most Common Use Case)**

```python
# Flask/Django web application example
from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/recipes')
def get_recipes():
    """API endpoint to fetch recipes from database."""
    conn = mysql.connector.connect(host='localhost', user='cf-python', passwd='password')
    cursor = conn.cursor()
    cursor.execute("USE task_database")
    cursor.execute("SELECT * FROM Recipes")
    recipes = cursor.fetchall()
    conn.close()
    return {'recipes': recipes}

# Users access recipes through a web browser
# Python handles database queries behind the scenes
```

**Use Cases:**
- E-commerce sites (product catalogs, orders, users)
- Social media platforms (posts, comments, likes)
- Content management systems (articles, pages, media)
- SaaS applications (customer data, analytics, subscriptions)

---

**2. Data Analysis and Business Intelligence**

```python
# Analyzing recipe data
import mysql.connector
import pandas as pd

# Fetch data from database
conn = mysql.connector.connect(host='localhost', user='cf-python', passwd='password')
query = "SELECT * FROM Recipes"
df = pd.read_sql(query, conn)

# Perform analysis
average_cooking_time = df['cooking_time'].mean()
most_common_difficulty = df['difficulty'].mode()[0]
recipes_per_difficulty = df['difficulty'].value_counts()

# Generate reports, visualizations, insights
```

**Use Cases:**
- Sales reports and analytics
- Customer behavior analysis
- Performance metrics dashboards
- Data mining and pattern recognition

---

**3. Data Migration and ETL (Extract, Transform, Load)**

```python
# Migrating data from old system to new database
import mysql.connector
import csv

# Extract from CSV file
with open('old_recipes.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Transform and Load into MySQL
    conn = mysql.connector.connect(host='localhost', user='cf-python', passwd='password')
    cursor = conn.cursor()
    cursor.execute("USE task_database")
    
    for row in reader:
        # Transform: Clean and format data
        name = row['recipe_name'].strip()
        time = int(row['time_minutes'])
        ingredients = row['ingredients'].replace(';', ', ')
        
        # Load: Insert into database
        cursor.execute(
            "INSERT INTO Recipes (name, cooking_time, ingredients) VALUES (%s, %s, %s)",
            (name, time, ingredients)
        )
    
    conn.commit()
    conn.close()
```

**Use Cases:**
- Moving data between different database systems
- Importing data from Excel, CSV, JSON files
- Data cleansing and transformation pipelines
- Database backups and synchronization

---

**4. Automation and Scheduled Tasks**

```python
# Daily automated script to clean up old data
import mysql.connector
from datetime import datetime, timedelta

def cleanup_old_recipes():
    """Delete recipes older than 1 year that haven't been viewed."""
    conn = mysql.connector.connect(host='localhost', user='cf-python', passwd='password')
    cursor = conn.cursor()
    cursor.execute("USE task_database")
    
    one_year_ago = datetime.now() - timedelta(days=365)
    
    cursor.execute("""
        DELETE FROM Recipes 
        WHERE created_date < %s AND last_viewed IS NULL
    """, (one_year_ago,))
    
    deleted_count = cursor.rowcount
    conn.commit()
    conn.close()
    
    print(f"Cleaned up {deleted_count} old recipes")

# Run this script daily using cron job or Task Scheduler
```

**Use Cases:**
- Scheduled data cleanup
- Automated report generation
- Data synchronization between systems
- Backup automation

---

**5. Command-Line Tools and Scripts**

```python
# Our Exercise 1.6 recipe management system
# User interacts via terminal to manage recipes in database

def create_recipe(conn, cursor):
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time: "))
    # ... insert into database
```

**Use Cases:**
- Database administration tools
- Bulk data operations
- System utilities
- Internal company tools

---

**6. Machine Learning and AI Applications**

```python
# Training a recipe recommendation system
import mysql.connector
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Fetch training data from database
conn = mysql.connector.connect(host='localhost', user='cf-python', passwd='password')
cursor = conn.cursor()
cursor.execute("SELECT ingredients, difficulty, user_rating FROM Recipes")
data = cursor.fetchall()

# Train ML model
# ... machine learning code ...

# Store predictions back to database
cursor.execute("UPDATE Recipes SET predicted_popularity = %s WHERE id = %s", 
               (prediction, recipe_id))
conn.commit()
```

**Use Cases:**
- Recommendation engines
- Predictive analytics
- Natural language processing with stored text data
- Image recognition with database metadata

---

#### **Limitations of Python Database Interaction**

While Python is versatile, it has limitations when interacting with databases:

---

**1. Performance Limitations**

**Problem: Slower than Native Database Operations**

```python
# ❌ SLOW: Fetching data to Python for processing
cursor.execute("SELECT * FROM Recipes")
recipes = cursor.fetchall()

# Processing 1 million recipes in Python
total_time = 0
for recipe in recipes:  # Very slow for large datasets!
    total_time += recipe[3]

average_time = total_time / len(recipes)

# ✓ FAST: Let database do the work
cursor.execute("SELECT AVG(cooking_time) FROM Recipes")
average_time = cursor.fetchone()[0]  # Much faster!
```

**Why:** 
- Network latency transferring data from database to Python
- Python loops are slower than SQL's optimized engine
- Memory constraints loading large datasets

**Solution:** Use SQL aggregation functions (SUM, AVG, COUNT, MAX, MIN) instead of Python loops

---

**2. Connection Overhead**

**Problem: Opening/Closing Connections is Expensive**

```python
# ❌ INEFFICIENT: Opening connection for each operation
for i in range(1000):
    conn = mysql.connector.connect(host='localhost', user='cf-python', passwd='password')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Recipes ...")
    conn.commit()
    conn.close()  # Opening/closing 1000 times!

# ✓ EFFICIENT: Reuse connection
conn = mysql.connector.connect(host='localhost', user='cf-python', passwd='password')
cursor = conn.cursor()
for i in range(1000):
    cursor.execute("INSERT INTO Recipes ...")
conn.commit()  # Commit once at the end
conn.close()  # Close once at the end
```

**Why:** Each connection requires authentication, handshake, resource allocation

**Solution:** Use connection pooling or keep connections open

---

**3. SQL Injection Vulnerabilities**

**Problem: User Input Can Compromise Database**

```python
# ❌ DANGEROUS: SQL Injection vulnerability
search_term = input("Enter ingredient: ")
query = f"SELECT * FROM Recipes WHERE ingredients LIKE '%{search_term}%'"
cursor.execute(query)

# Malicious input: "; DROP TABLE Recipes; --"
# Resulting query: SELECT * FROM Recipes WHERE ingredients LIKE '%'; DROP TABLE Recipes; --%'
# YOUR ENTIRE TABLE GETS DELETED!

# ✓ SAFE: Use parameterized queries
search_term = input("Enter ingredient: ")
cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", (f"%{search_term}%",))
# MySQL connector automatically escapes the input
```

**Why:** String concatenation doesn't sanitize user input

**Solution:** Always use parameterized queries with placeholders (%s)

---

**4. Limited Transaction Control**

**Problem: Python Can't Match Database's ACID Guarantees**

```python
# Python code is not atomic by default
try:
    cursor.execute("INSERT INTO Recipes ...")
    # If error occurs here, first insert is already committed!
    cursor.execute("INSERT INTO Ingredients ...")
    conn.commit()
except:
    # Can't rollback if we've already committed!
    pass

# ✓ Better: Use transactions properly
try:
    cursor.execute("INSERT INTO Recipes ...")
    cursor.execute("INSERT INTO Ingredients ...")
    conn.commit()  # Both succeed or both fail
except:
    conn.rollback()  # Undo both operations
```

**Why:** Python code execution is not inherently transactional

**Solution:** Explicit transaction management with commit()/rollback()

---

**5. Type Conversion Issues**

**Problem: Mismatch Between Python and SQL Types**

```python
# Python datetime vs MySQL DATETIME
from datetime import datetime

# Python uses datetime objects
python_time = datetime.now()

# MySQL expects string format
cursor.execute("INSERT INTO Recipes (created_at) VALUES (%s)", (python_time,))
# mysql-connector handles conversion, but other libraries might not

# List to comma-separated string (our Exercise limitation!)
ingredients = ['Milk', 'Sugar', 'Chocolate']
# MySQL doesn't support array types well
ingredients_str = ', '.join(ingredients)  # Must convert manually
cursor.execute("INSERT INTO Recipes (ingredients) VALUES (%s)", (ingredients_str,))

# Later: Convert back to list
cursor.execute("SELECT ingredients FROM Recipes WHERE id = 1")
result = cursor.fetchone()[0]  # Returns string: 'Milk, Sugar, Chocolate'
ingredients_list = result.split(', ')  # Manual conversion back to list
```

**Why:** Python and SQL have different type systems

**Solution:** Manual conversion or use ORM (Object-Relational Mapper)

---

**6. Lack of Schema Management**

**Problem: Python Can't Enforce Database Schema**

```python
# Python doesn't know about database schema
cursor.execute("INSERT INTO Recipes (name, cooking_time) VALUES (%s, %s)",
               ("Tea", "five"))  # Oops! "five" is string, should be integer

# Error only discovered at runtime!
# Database rejects it, but Python didn't catch it beforehand
```

**Why:** Python is dynamically typed, doesn't validate against schema

**Solution:** Use ORM frameworks (SQLAlchemy, Django ORM) or manual validation

---

**7. Concurrency Challenges**

**Problem: Multiple Python Processes Can Conflict**

```python
# Process 1
cursor.execute("SELECT quantity FROM Stock WHERE id = 1")
quantity = cursor.fetchone()[0]  # quantity = 10
# ... some processing time ...
cursor.execute("UPDATE Stock SET quantity = %s WHERE id = 1", (quantity - 1,))

# Process 2 (running simultaneously)
cursor.execute("SELECT quantity FROM Stock WHERE id = 1")
quantity = cursor.fetchone()[0]  # quantity = 10 (same value!)
cursor.execute("UPDATE Stock SET quantity = %s WHERE id = 1", (quantity - 1,))

# Result: Both set quantity to 9, but should be 8!
# Lost update problem!
```

**Why:** No automatic locking in Python code

**Solution:** Use database transactions with proper isolation levels or row locking

---

**8. Resource Management**

**Problem: Memory Constraints with Large Datasets**

```python
# ❌ MEMORY ISSUE: Loading 1 million recipes into Python
cursor.execute("SELECT * FROM Recipes")
all_recipes = cursor.fetchall()  # Loads everything into RAM!
# Can crash if dataset is too large

# ✓ BETTER: Use pagination or streaming
cursor.execute("SELECT * FROM Recipes LIMIT 1000 OFFSET 0")
batch = cursor.fetchall()  # Process in batches

# Or use server-side cursors
cursor = conn.cursor(buffered=False)  # Fetches on demand
```

**Why:** Python loads all results into memory by default

**Solution:** Pagination, streaming, or server-side cursors

---

**Summary: When to Use Python vs. Pure SQL**

| Task | Best Tool | Reason |
|------|-----------|---------|
| Complex calculations | SQL | Database optimized for math |
| Data aggregation (SUM, AVG, COUNT) | SQL | Much faster than Python loops |
| String manipulation | Python | More flexible string methods |
| API integration | Python | Rich library ecosystem |
| External file processing | Python | Better file handling |
| Complex joins and queries | SQL | Optimized query engine |
| Machine learning | Python | ML libraries not in SQL |
| Web application backend | Python + SQL | Python handles logic, SQL handles data |

**Best Practice:** Let the database do what it's good at (storing, indexing, querying), and use Python for what it's good at (logic, integration, user interaction).

---

## Key Concepts Learned

### 1. Database Fundamentals

**RDBMS (Relational Database Management System):**
- Stores data in tables (relations)
- Tables have rows (records) and columns (fields)
- Relationships between tables using keys
- ACID properties: Atomicity, Consistency, Isolation, Durability

**MySQL Server:**
- Open-source RDBMS
- Client-server architecture
- Uses SQL (Structured Query Language)
- Supports multiple users and databases

---

### 2. SQL (Structured Query Language)

**Data Definition Language (DDL):**
```sql
-- Create database
CREATE DATABASE IF NOT EXISTS task_database;

-- Use database
USE task_database;

-- Create table
CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
);

-- Modify table
ALTER TABLE Recipes ADD COLUMN created_date DATE;
ALTER TABLE Recipes RENAME COLUMN name TO recipe_name;
ALTER TABLE Recipes DROP COLUMN created_date;

-- Delete table
DROP TABLE IF EXISTS Recipes;
```

**Data Manipulation Language (DML):**
```sql
-- Insert data
INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) 
VALUES ('Tea', 'Tea Leaves, Sugar, Water', 5, 'Easy');

-- Read/Query data
SELECT * FROM Recipes;
SELECT name, cooking_time FROM Recipes WHERE difficulty = 'Easy';
SELECT * FROM Recipes WHERE ingredients LIKE '%Sugar%';

-- Update data
UPDATE Recipes SET cooking_time = 7 WHERE id = 1;
UPDATE Recipes SET difficulty = 'Medium' WHERE cooking_time >= 10;

-- Delete data
DELETE FROM Recipes WHERE id = 5;
DELETE FROM Recipes WHERE difficulty = 'Hard';
```

---

### 3. Python-MySQL Integration

**Connection Management:**
```python
import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password',
    database='task_database'
)

# Create cursor
cursor = conn.cursor()

# Execute queries
cursor.execute("SELECT * FROM Recipes")

# Commit changes
conn.commit()

# Close connection
cursor.close()
conn.close()
```

**Parameterized Queries (Prevent SQL Injection):**
```python
# ✓ SAFE: Using placeholders
name = input("Enter recipe name: ")
cursor.execute("SELECT * FROM Recipes WHERE name = %s", (name,))

# ❌ UNSAFE: String concatenation
name = input("Enter recipe name: ")
cursor.execute(f"SELECT * FROM Recipes WHERE name = '{name}'")  # Vulnerable!
```

---

### 4. CRUD Operations

**Create:**
```python
def create_recipe(conn, cursor):
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time: "))
    ingredients = []
    
    num_ingredients = int(input("How many ingredients? "))
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)
    
    ingredients_str = ", ".join(ingredients)
    difficulty = calculate_difficulty(cooking_time, ingredients)
    
    sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (name, ingredients_str, cooking_time, difficulty)
    cursor.execute(sql, val)
    conn.commit()
```

**Read:**
```python
def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    
    all_ingredients = []
    for row in results:
        ingredients_list = row[0].split(', ')
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    # Display and search
    search_ingredient = input("Enter ingredient to search: ")
    cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", 
                   (f"%{search_ingredient}%",))
    results = cursor.fetchall()
    
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Difficulty: {row[4]}")
```

**Update:**
```python
def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    recipes = cursor.fetchall()
    
    for recipe in recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")
    
    recipe_id = int(input("Enter recipe ID to update: "))
    column = input("Update (name/cooking_time/ingredients): ")
    new_value = input("Enter new value: ")
    
    if column == "cooking_time":
        # Recalculate difficulty
        cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        ingredients_str = cursor.fetchone()[0]
        ingredients = ingredients_str.split(', ')
        new_difficulty = calculate_difficulty(int(new_value), ingredients)
        
        cursor.execute("UPDATE Recipes SET cooking_time = %s, difficulty = %s WHERE id = %s",
                      (new_value, new_difficulty, recipe_id))
    else:
        cursor.execute(f"UPDATE Recipes SET {column} = %s WHERE id = %s",
                      (new_value, recipe_id))
    
    conn.commit()
```

**Delete:**
```python
def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    recipes = cursor.fetchall()
    
    for recipe in recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")
    
    recipe_id = int(input("Enter recipe ID to delete: "))
    
    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
    conn.commit()
    print("Recipe deleted successfully!")
```

---

### 5. Data Type Conversions

**Python List ↔ SQL String:**
```python
# List to comma-separated string (for storage)
ingredients = ['Milk', 'Sugar', 'Chocolate']
ingredients_str = ", ".join(ingredients)
# Result: "Milk, Sugar, Chocolate"

cursor.execute("INSERT INTO Recipes (ingredients) VALUES (%s)", (ingredients_str,))

# Comma-separated string to list (for processing)
cursor.execute("SELECT ingredients FROM Recipes WHERE id = 1")
result = cursor.fetchone()[0]
# Result: "Milk, Sugar, Chocolate"

ingredients_list = [ing.strip() for ing in result.split(',')]
# Result: ['Milk', 'Sugar', 'Chocolate']
```

---

### 6. SQL Wildcard Searching

**LIKE Operator with Wildcards:**
```sql
-- % represents zero or more characters
SELECT * FROM Recipes WHERE ingredients LIKE '%Sugar%';
-- Finds: "Tea Leaves, Sugar, Water", "Milk, Sugar", "Sugar, Eggs, Flour"

-- _ represents exactly one character
SELECT * FROM Recipes WHERE name LIKE 'T__';
-- Finds: "Tea", "Tic" (3 characters starting with T)

-- Combining wildcards
SELECT * FROM Recipes WHERE ingredients LIKE '%Sugar%' OR ingredients LIKE '%Honey%';
-- Finds recipes with Sugar OR Honey
```

**Python Implementation:**
```python
search_ingredient = input("Enter ingredient: ")
search_pattern = f"%{search_ingredient}%"
cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", (search_pattern,))
results = cursor.fetchall()
```

---

## Code Examples from Exercise

### Complete Recipe Management System Structure

```python
import mysql.connector

# Database Connection
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)
cursor = conn.cursor()

# Create database and table
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")
cursor.execute("""CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)""")

# Helper function: Calculate difficulty
def calculate_difficulty(cooking_time, ingredients):
    num_ingredients = len(ingredients)
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"

# Main menu loop
def main_menu(conn, cursor):
    while True:
        print("\n1. Create Recipe")
        print("2. Search Recipe")
        print("3. Update Recipe")
        print("4. Delete Recipe")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            conn.commit()
            conn.close()
            break

# Run application
main_menu(conn, cursor)
```

---

## Challenges and Solutions

### Challenge 1: MySQL Installation and Configuration

**Problem:** Setting up MySQL server, creating users, granting privileges.

**Solution:**
```sql
-- In MySQL Command Line Client
CREATE USER 'cf-python'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'cf-python'@'localhost';
FLUSH PRIVILEGES;
```

---

### Challenge 2: SQL Injection Prevention

**Problem:** User input can compromise database security.

**Solution:** Always use parameterized queries:
```python
# ❌ Vulnerable
query = f"SELECT * FROM Recipes WHERE name = '{user_input}'"

# ✓ Safe
query = "SELECT * FROM Recipes WHERE name = %s"
cursor.execute(query, (user_input,))
```

---

### Challenge 3: Storing Lists in MySQL

**Problem:** MySQL doesn't fully support array/list types.

**Solution:** Convert lists to comma-separated strings:
```python
# Storing
ingredients = ['Milk', 'Sugar', 'Chocolate']
ingredients_str = ", ".join(ingredients)

# Retrieving
ingredients_list = [ing.strip() for ing in ingredients_str.split(',')]
```

---

### Challenge 4: Transaction Management

**Problem:** Ensuring data consistency across multiple operations.

**Solution:**
```python
try:
    cursor.execute("INSERT INTO Recipes ...")
    cursor.execute("INSERT INTO Ingredients ...")
    conn.commit()  # Both succeed or both fail
except Exception as e:
    conn.rollback()  # Undo all changes
    print(f"Error: {e}")
```

---

### Challenge 5: Connection Resource Management

**Problem:** Forgetting to close connections can exhaust server resources.

**Solution:**
```python
# Using try-finally
try:
    conn = mysql.connector.connect(...)
    cursor = conn.cursor()
    # ... operations ...
finally:
    cursor.close()
    conn.close()

# Or using context managers (advanced)
with mysql.connector.connect(...) as conn:
    with conn.cursor() as cursor:
        # ... operations ...
    # Automatically closed
```

---

## Skills Developed

1. **Database Design**: Creating normalized table structures with appropriate data types
2. **SQL Proficiency**: Writing CREATE, INSERT, SELECT, UPDATE, DELETE statements
3. **Python-Database Integration**: Using mysql-connector-python library
4. **Data Validation**: Ensuring data integrity before insertion
5. **User Input Handling**: Collecting and validating user input safely
6. **Error Handling**: Managing database exceptions gracefully
7. **Transaction Management**: Using commit() and rollback() appropriately
8. **Security Awareness**: Preventing SQL injection attacks
9. **Data Transformation**: Converting between Python and SQL data types
10. **Application Architecture**: Organizing code with functions for each operation

---

## Real-World Applications

**This exercise prepared me for:**
- Building web applications with database backends (Flask, Django)
- Creating REST APIs that interact with databases
- Data analysis and reporting systems
- E-commerce platforms (products, orders, customers)
- Content management systems
- User authentication and authorization systems
- Inventory management applications
- Social media and blogging platforms

---

## Conclusion

Exercise 1.6 was a crucial step in my development journey, introducing me to the world of databases and SQL. Moving from file-based storage (Exercise 1.4) to database-driven applications represents a major leap in capability and professionalism.

**Key Takeaways:**
- Databases provide structured, efficient, and secure data storage
- SQL is a powerful language for data manipulation
- Python and databases work seamlessly together
- Proper connection management and security are critical
- CRUD operations form the foundation of most applications

**Personal Growth:**
- From storing data in files to managing it in a professional database
- From linear file searches to optimized SQL queries
- From manual data validation to database constraints
- From single-user files to multi-user database systems

This knowledge is foundational for web development with Django, where databases are central to every application. Understanding how Python interacts with databases at this low level will make working with Django's ORM (Object-Relational Mapper) much easier.

---

**Date Completed:** October 19, 2025  
**Status:** ✅ All tasks completed successfully  
**Next Steps:** Exercise 1.7 - Continue building on database and OOP concepts

---

**Total Hours Invested:** ~6 hours  
**Lines of Code Written:** ~350 lines  
**Recipes Created:** 4  
**SQL Queries Written:** ~25  
**Confidence Level:** 🌟🌟🌟🌟🌟
