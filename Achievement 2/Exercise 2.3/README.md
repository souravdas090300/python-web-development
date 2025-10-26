# Exercise 2.3 - Django Models and Admin

## Overview
This exercise implements a simple Recipe model in Django with Django admin integration, following mentor recommendations for a clean, single-app architecture with CSV-based ingredients storage.

## Project Structure
```
Exercise 2.3/
├── src/
│   ├── recipes/           # Single app for all recipe functionality
│   │   ├── models.py      # Recipe model (simple CSV design)
│   │   ├── admin.py       # Admin configuration with computed difficulty
│   │   ├── views.py       # Home view
│   │   ├── urls.py        # App URLs
│   │   ├── tests.py       # Model tests (10 tests)
│   │   ├── tests_views.py # View/admin tests (4 tests)
│   │   └── templates/
│   │       └── recipes/
│   │           └── recipes_home.html
│   ├── recipestore/       # Project settings
│   │   ├── settings_local.py   # Local development settings (DEBUG=True)
│   │   └── settings_prod.py    # Production settings (DEBUG=False)
│   └── manage.py          # Defaults to settings_local
├── a2-e23-local/          # Local virtual environment
├── a2-e23-prod/           # Production virtual environment
├── requirements.txt       # Python dependencies
├── screenshots/           # Required screenshots
├── learning-journal.md    # Development journal
├── learning-journey.md    # Learning reflections
└── README.md
```

## Model Design (Simplified per Mentor Recommendation)

### Recipe Model
Single, simple model with computed difficulty:

**Fields:**
- `name` (CharField): Recipe name
- `cooking_time` (PositiveIntegerField): Cooking time in minutes
- `ingredients` (TextField): Comma-separated list (e.g., "salt, water, sugar")
- `description` (TextField): Recipe instructions/description

**Computed Methods:**
- `ingredients_list()`: Returns ingredients as a Python list
- `difficulty()`: Calculates difficulty based on cooking time and ingredient count
  - Easy: cooking_time < 10 and ingredients < 4
  - Medium: cooking_time < 10 and ingredients >= 4
  - Intermediate: cooking_time >= 10 and ingredients < 4
  - Hard: otherwise

## Environments

### Local Environment
- Virtual environment: `a2-e23-local`
- Settings: `settings_local.py`
- DEBUG = True
- SQLite database

### Production Environment
- Virtual environment: `a2-e23-prod`
- Settings: `settings_prod.py`
- DEBUG = False
- ALLOWED_HOSTS configured

See `ENVIRONMENT_SETUP.md` for detailed setup and usage instructions.

#### How to run (production)
- ASGI (Uvicorn):
  ```powershell
  # from Exercise 2.3/src
  $env:DJANGO_SETTINGS_MODULE='recipestore.settings_prod'
  uvicorn recipestore.asgi:application --host 0.0.0.0 --port 8000 --workers 2
  ```
- WSGI (Waitress):
  ```powershell
  # from Exercise 2.3/src
  $env:DJANGO_SETTINGS_MODULE='recipestore.settings_prod'
  waitress-serve --host=0.0.0.0 --port=8000 recipestore.wsgi:application
  ```

## Required Screenshots (Per Mentor Instructions)

1. **recipe-app-schema.jpg** - UML diagram of Recipe model
2. **Test-Report.jpg** - Screenshot of test results
3. **admin-recipes.jpg** - Admin panel with at least 5 recipes

## Setup and Running

### First-Time Setup
```powershell
# Activate local environment
.\a2-e23-local\Scripts\Activate.ps1

# Navigate to src
cd src

# Run migrations with local settings
python manage.py migrate --settings=recipestore.settings_local

# Create superuser
python manage.py createsuperuser --settings=recipestore.settings_local
```

### Run Development Server
```powershell
# Activate local environment
.\a2-e23-local\Scripts\Activate.ps1

cd src
python manage.py runserver --settings=recipestore.settings_local
```

Access admin at: http://127.0.0.1:8000/admin/

### Run Tests
```powershell
cd src
python manage.py test --settings=recipestore.settings_local
```

### Important: Always Specify Settings
Since this project uses separate settings files (no default settings.py), you must always include:
- `--settings=recipestore.settings_local` for local development
- `--settings=recipestore.settings_prod` for production testing

## Mentor Revisions Implemented

✅ **Simplified to single app:** Consolidated to `recipes` app only (no recipe_categories or recipe_ingredients)

✅ **Simple CSV-based model:** Recipe.ingredients stores comma-separated string (e.g., "salt, water, sugar")

✅ **Computed difficulty:** Difficulty is calculated via method, not stored in database
  - Easy: cooking_time < 10 AND ingredients < 4
  - Medium: cooking_time < 10 AND ingredients ≥ 4
  - Intermediate: cooking_time ≥ 10 AND ingredients < 4
  - Hard: otherwise

✅ **Two environments:** Separate settings_local.py (DEBUG=True) and settings_prod.py (DEBUG=False)

✅ **Environment-specific venvs:** a2-e23-local and a2-e23-prod with Django 5.2.7, Uvicorn, Waitress

✅ **Production server options:** ASGI (Uvicorn) or WSGI (Waitress) via DJANGO_SETTINGS_MODULE

✅ **Schema diagram preparation:** Instructions provided for creating UML diagram using dbdiagram.io or draw.io

✅ **Test naming:** Test screenshot should be named `Test-Report.jpg`

✅ **Admin with 5+ recipes:** Admin displays computed difficulty column; tests verify functionality (14 tests passing)

✅ **Welcome page:** Created home view at root URL rendering recipes_home.html

## Technologies Used
- Python 3.14
- Django 5.2.7
- SQLite (development database)

## Next Steps
1. Create UML schema diagram using dbdiagram.io or draw.io
2. Add at least 5 recipes via Django admin
3. Run tests and capture screenshot
4. Ensure all screenshots are properly named
5. Submit for mentor review
