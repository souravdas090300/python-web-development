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
│   └── screenshot/
│       ├── 1.6 p1 step1 creating database and table.png
│       ├── 1.6 p1 step2 insert database.png
│       └── 1.6 p1 step3 showing all entries.png
│
├── main-task/
│   ├── recipe_mysql.py            # Complete recipe management system
│   ├── TASK_README.md             # Task-specific documentation
│   └── screenshots/               # Task execution screenshots
│       ├── 1.6 m step1 connecting mysql.png
│       ├── 1.6 m step2 created sushi recipe.png
│       ├── 1.6 m step3 created tea recipe.png
│       ├── 1.6 m step4 created pancakes recipe.png
│       ├── 1.6 m step5 created smoothie recipe.png
│       ├── 1.6 m step6 search milk.png
│       ├── 1.6 m step7 search fish.png
│       ├── 1.6 m step8 updated tea recipe.png
│       ├── 1.6 m step9 change smoothie name.png
│       ├── 1.6 m step10 change pancake ingredients.png
│       ├── 1.6 m step11 deleted Berry smoothie.png
│       └── 1.6 m step12 exit the menu.png
│
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

---

## 🚀 Main Features

### 1. **Create Recipe**
- Collects recipe name, cooking time, and ingredients from user
- Automatically calculates difficulty based on cooking time and ingredient count
- Converts ingredient list to comma-separated string for MySQL storage
- Inserts new recipe into database

### 2. **Search Recipe by Ingredient**
- Displays all unique ingredients from all recipes
- Allows user to select ingredient to search for
- Uses SQL `LIKE` operator with wildcards for flexible searching
- Displays all recipes containing the selected ingredient

### 3. **Update Recipe**
- Lists all recipes with their IDs
- Allows user to update: name, cooking_time, or ingredients
- Automatically recalculates difficulty when time or ingredients change
- Commits changes to database

### 4. **Delete Recipe**
- Displays all recipes with IDs
- Confirms deletion before executing
- Removes recipe from database permanently

### 5. **Exit Program**
- Commits all pending changes
- Safely closes database connection
- Clean program termination

---

## 💻 How to Run

### Prerequisites

1. **MySQL Server** installed and running
2. **Python 3.x** installed
3. **mysql-connector-python** package installed
4. **MySQL user** configured:
   - Username: `cf-python`
   - Password: `password`
   - Privileges: ALL on all databases

### Running the Application

```bash
# Navigate to main-task directory
cd "c:\Users\dasau\python-web-development\Exercise 1.6\main-task"

# Activate virtual environment (optional)
..\..\Exercise 1.4\cf-python-base\Scripts\Activate.ps1

# Run the script
python recipe_mysql.py
```

---

## 📸 Deliverables

### Practice Task 1:
✅ Screenshots of creating database, inserting data, displaying entries

### Main Task:
✅ Complete `recipe_mysql.py` script (384 lines)  
✅ 12 screenshots documenting all operations:
- Database connection
- 4 recipes created (Sushi, Tea, Pancakes, Smoothie)
- 2 searches performed (Milk, Fish)
- 3 updates performed (Tea time, Smoothie name, Pancake ingredients)
- 1 deletion (Berry Smoothie)
- Clean exit

✅ Learning journal with 3 reflection questions  
✅ Learning journey with personal growth documentation  
✅ README documentation

---

## 📚 Key Concepts Mastered

### Database Fundamentals
- RDBMS architecture and client-server model
- Database creation and management
- Table design with appropriate data types
- Primary keys and auto-increment

### SQL Proficiency
```sql
-- Database Management
CREATE DATABASE IF NOT EXISTS task_database;
USE task_database;

-- Table Operations
CREATE TABLE IF NOT EXISTS Recipes (...);
ALTER TABLE Recipes MODIFY COLUMN ...;

-- CRUD Operations
INSERT INTO Recipes (...) VALUES (...);
SELECT * FROM Recipes WHERE ingredients LIKE '%Sugar%';
UPDATE Recipes SET cooking_time = %s WHERE id = %s;
DELETE FROM Recipes WHERE id = %s;
```

### Python-MySQL Integration
- Connection management with mysql-connector-python
- Cursor objects for query execution
- Parameterized queries for SQL injection prevention
- Transaction management (commit/rollback)
- Result fetching (fetchone, fetchall)
- Proper resource cleanup

### Security Best Practices
- SQL injection prevention using parameterized queries
- Input validation and error handling
- Safe user confirmation for destructive operations

---

## 🎓 Skills Developed

1. **Database Design**: Creating normalized schemas with appropriate constraints
2. **SQL Proficiency**: Writing complex queries with wildcards and conditions
3. **Python Integration**: Using mysql-connector-python effectively
4. **CRUD Operations**: Implementing all four database operations
5. **Error Handling**: Managing database exceptions gracefully
6. **Security**: Preventing SQL injection attacks
7. **Data Transformation**: Converting between Python and SQL data types
8. **User Experience**: Building intuitive menu-driven applications
9. **Transaction Management**: Using commit/rollback appropriately
10. **Code Organization**: Structuring modular, maintainable code

---

## 🎯 Completion Checklist

### Part 1: Database Setup
- ✅ MySQL server installed and running
- ✅ User 'cf-python' created with proper privileges
- ✅ Database `task_database` created
- ✅ Table `Recipes` created with correct schema

### Part 2: Main Menu Implementation
- ✅ Menu loop with 5 options
- ✅ Exit option commits and closes connection

### Part 3: Create Recipe Function
- ✅ Collects user input (name, time, ingredients)
- ✅ Calculates difficulty automatically
- ✅ Converts list to comma-separated string
- ✅ Inserts into database with parameterized query

### Part 4: Search Recipe Function
- ✅ Fetches all ingredients from database
- ✅ Builds unique ingredients list (no duplicates)
- ✅ Uses LIKE operator with % wildcards
- ✅ Displays all matching recipes

### Part 5: Update Recipe Function
- ✅ Displays all recipes with IDs
- ✅ Allows selection of column to update
- ✅ Recalculates difficulty when needed
- ✅ Commits changes to database

### Part 6: Delete Recipe Function
- ✅ Displays all recipes for selection
- ✅ Confirms deletion with user
- ✅ Executes DELETE query
- ✅ Commits changes

### Part 7: Testing & Documentation
- ✅ Created 4 recipes (Sushi, Tea, Pancakes, Smoothie)
- ✅ Searched by 2 ingredients (Milk, Fish)
- ✅ Updated 3 recipes (Tea, Smoothie, Pancakes)
- ✅ Deleted 1 recipe (Berry Smoothie)
- ✅ Exited program cleanly
- ✅ 12+ screenshots captured
- ✅ Learning journal completed
- ✅ Learning journey documented
- ✅ README files created

---

## 🔮 Real-World Applications

This exercise prepared me for:

- **Web Development**: Backend systems with Django/Flask
- **E-commerce Platforms**: Product catalogs, inventory management
- **Content Management Systems**: Blogs, articles, media libraries
- **User Management Systems**: Authentication, profiles, permissions
- **Data Analytics**: Collection and reporting systems
- **RESTful APIs**: Database-backed web services

---

## 📖 Documentation Files

- **`learning_journal.md`**: Technical documentation with 3 reflection questions covering database fundamentals, primary/foreign keys, and Python-database interaction limitations
- **`learning_journey.md`**: Personal journey from MySQL installation through complete application development
- **`main-task/TASK_README.md`**: Task-specific implementation details and code examples

---

## 🐛 Troubleshooting

**Connection Issues:**
```python
# Ensure MySQL server is running
# Check username and password
# Verify privileges granted
```

**Module Not Found:**
```bash
pip install mysql-connector-python
```

**Database Not Found:**
```python
# Script automatically creates database
# Ensure user has CREATE privilege
```

---

## 🏆 Achievement Summary

- **Database Tables Created:** 1 (Recipes)
- **SQL Queries Written:** 25+
- **Recipes Managed:** 4 created, 3 updated, 1 deleted
- **Lines of Code:** 384
- **Screenshots Captured:** 15+
- **Time Invested:** ~6 hours
- **Confidence Level:** ⭐⭐⭐⭐⭐

---

## 👨‍💻 Author

**Sourav Das**  
Python for Web Developers Course  
October 2025

---

## 📝 Notes

This exercise represents a crucial transition from file-based storage to professional database-driven applications. The skills learned here—SQL queries, database connections, CRUD operations, and transaction management—form the foundation for modern web development and will be extensively used with Django's ORM in future exercises.

**Key Achievement:** Successfully built a complete, secure database-driven command-line application demonstrating proficiency in both Python and SQL.

---

**Exercise Status:** ✅ **COMPLETED**  
**Date Completed:** October 19, 2025  
**Ready for Submission:** ✅ YES
