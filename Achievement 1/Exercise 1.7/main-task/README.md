# Exercise 1.7: Object Relational Mapping with SQLAlchemy

## Overview
This exercise demonstrates the use of **SQLAlchemy ORM** (Object Relational Mapping) to build a Recipe Management Application. Instead of writing raw SQL queries, we use Python objects to interact with the MySQL database.

## What is ORM?
**ORM (Object Relational Mapping)** is a technique that allows developers to:
- Work with database tables as Python classes
- Manipulate database rows as Python objects
- Perform database operations using Python methods instead of SQL queries

## Technology Stack
- **Python 3.14**
- **SQLAlchemy 2.0.44** - ORM framework
- **PyMySQL 1.1.2** - MySQL connector for SQLAlchemy
- **MySQL 9.x** - Database server
- **Cryptography** - Required for MySQL authentication

## Database Schema

### Table: `final_recipes`
| Column        | Type         | Constraints               |
|---------------|--------------|---------------------------|
| id            | INT          | PRIMARY KEY, AUTO_INCREMENT |
| name          | VARCHAR(50)  | Recipe name               |
| ingredients   | VARCHAR(255) | Comma-separated ingredients |
| cooking_time  | INT          | Time in minutes           |
| difficulty    | VARCHAR(20)  | Easy/Medium/Intermediate/Hard |

## Application Features

### 1. Create a New Recipe
- Collects recipe name (max 50 characters)
- Validates cooking time (must be positive integer)
- Accepts ingredients one by one
- Automatically calculates difficulty based on:
  - Cooking time < 10 min + < 4 ingredients = **Easy**
  - Cooking time < 10 min + ≥ 4 ingredients = **Medium**
  - Cooking time ≥ 10 min + < 4 ingredients = **Intermediate**
  - Cooking time ≥ 10 min + ≥ 4 ingredients = **Hard**

### 2. View All Recipes
- Displays all recipes in a formatted view
- Shows ID, name, ingredients, cooking time, and difficulty

### 3. Search by Ingredient
- Extracts all unique ingredients from existing recipes
- Allows user to select ingredient(s) by number
- Uses SQL `LIKE` operator with wildcards for flexible searching
- Displays all matching recipes

### 4. Edit a Recipe
- Lists all available recipes with IDs
- Allows editing of:
  - Recipe name
  - Cooking time (recalculates difficulty)
  - Ingredients (recalculates difficulty)
- Validates all inputs

### 5. Delete a Recipe
- Lists all recipes with IDs
- Requires confirmation before deletion
- Safely removes recipe from database

### 6. Exit
- Closes database session properly
- Terminates application gracefully

## Key ORM Concepts Demonstrated

### 1. Model Definition
```python
class Recipe(Base):
    __tablename__ = "final_recipes"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    # ... other columns
```

### 2. CRUD Operations

**Create:**
```python
recipe = Recipe(name="Tea", cooking_time=5, ingredients="...")
session.add(recipe)
session.commit()
```

**Read:**
```python
# Get all
recipes = session.query(Recipe).all()

# Get one by ID
recipe = session.query(Recipe).get(1)

# Filter
recipes = session.query(Recipe).filter(Recipe.name == 'Tea').one()
```

**Update:**
```python
recipe.name = "New Name"
session.commit()
```

**Delete:**
```python
session.delete(recipe)
session.commit()
```

### 3. Advanced Queries

**Search with LIKE:**
```python
session.query(Recipe).filter(Recipe.ingredients.like('%Sugar%')).all()
```

**Multiple conditions:**
```python
session.query(Recipe).filter(
    Recipe.ingredients.like('%Milk%'),
    Recipe.ingredients.like('%Sugar%')
).all()
```

**Unpacking conditions:**
```python
conditions = [Recipe.ingredients.like('%Milk%'), ...]
session.query(Recipe).filter(*conditions).all()
```

## Setup Instructions

### 1. Install Required Packages
```bash
pip install sqlalchemy
pip install pymysql
pip install cryptography
```

### 2. Configure Database Connection
Update the connection string in `recipe_app.py`:
```python
engine = create_engine("mysql+pymysql://username:password@localhost/task_database")
```

### 3. Run the Application
```bash
python recipe_app.py
```

## Error Handling
The application includes comprehensive error handling for:
- Invalid menu choices
- Empty or oversized inputs
- Non-numeric inputs where numbers are expected
- Non-existent recipe IDs
- Database connection issues

## Input Validation
- Recipe names: max 50 characters, non-empty
- Cooking time: positive integers only
- Ingredients: max 255 characters total, at least one ingredient required
- Menu choices: must match available options

## Differences from Exercise 1.6

| Feature | Exercise 1.6 (MySQL Connector) | Exercise 1.7 (SQLAlchemy ORM) |
|---------|--------------------------------|-------------------------------|
| Database Connection | `mysql.connector.connect()` | `create_engine()` + `sessionmaker()` |
| Query Execution | `cursor.execute("SQL")` | `session.query(Model)` |
| Data Representation | Tuples from cursor | Python objects |
| Table Creation | Manual SQL CREATE TABLE | `Base.metadata.create_all()` |
| Insert Data | SQL INSERT with placeholders | `session.add(object)` |
| Update Data | SQL UPDATE statement | Modify object attributes |
| Delete Data | SQL DELETE statement | `session.delete(object)` |
| Search | SQL SELECT with WHERE | `.filter()` method |
| Code Style | Procedural with SQL | Object-Oriented |

## Advantages of Using ORM
1. ✅ **Pythonic Code**: Work with objects instead of SQL strings
2. ✅ **Type Safety**: Model definitions catch errors early
3. ✅ **Reduced SQL Injection Risk**: Parameterized queries by default
4. ✅ **Database Agnostic**: Easy to switch databases (MySQL → PostgreSQL)
5. ✅ **Maintainability**: Changes to schema reflected in Python code
6. ✅ **Relationships**: Easy handling of foreign keys and joins

## Files in This Exercise

```
Exercise 1.7/
├── main-task/
│   ├── recipe_app.py          # Main application file
│   ├── README.md              # This file
│   └── screenshots/           # Screenshots of testing
├── 1.7-Practice Task 1/
│   └── screenshots/           # Adding entries with ORM
├── 1.7-Practice Task 2/
│   └── screenshots/           # Search with filter()
└── 1.7-Practice Task 3/
    └── screenshots/           # Update entries
```

## Testing Checklist
- ✅ Create multiple recipes with varying complexities
- ✅ View all recipes
- ✅ Search by different ingredients
- ✅ Edit recipe names
- ✅ Edit cooking times (verify difficulty recalculation)
- ✅ Edit ingredients (verify difficulty recalculation)
- ✅ Delete recipes with confirmation
- ✅ Test invalid inputs (letters for numbers, oversized text, etc.)
- ✅ Test with empty database
- ✅ Test menu navigation

## Learning Outcomes
By completing this exercise, you will:
1. Understand how ORMs work
2. Use SQLAlchemy to define models and tables
3. Perform CRUD operations using Python objects
4. Write complex queries using ORM methods
5. Build a complete database application with proper error handling
6. Compare SQL-based vs ORM-based approaches

## Author
Created for CareerFoundry Python Web Development Course - Achievement 1, Exercise 1.7

## Next Steps
- Exercise 1.8: Advanced ORM concepts (relationships, joins)
- Exercise 2.1: Django framework introduction
