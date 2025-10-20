# Django Recipe App

A Django project for managing recipes, ingredients, and categories.

## Features
- Add, edit, and delete recipes
- Assign recipes to categories
- Add multiple ingredients to each recipe
- Admin interface for easy data management

## Setup
1. Create and activate a virtual environment:
   ```powershell
   python -m venv web-dev
   .\web-dev\bin\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install django
   ```
3. Run migrations:
   ```powershell
   py manage.py makemigrations
   py manage.py migrate
   ```
4. Create a superuser:
   ```powershell
   py manage.py createsuperuser
   ```
5. Start the server:
   ```powershell
   py manage.py runserver
   ```
6. Access the admin at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Project Structure
- `recipes/` — Recipe model and admin
- `recipe_categories/` — Category model and admin
- `recipe_ingredients/` — Ingredient model and admin
- `recipestore/` — Django project settings

## Testing
Run all tests:
```powershell
py manage.py test
```

## Screenshots & Submission
- Add screenshots of admin data entry and model tests to your submission folder
- Include this README, learning-journal.md, and learning-journey.md
