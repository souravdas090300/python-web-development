# Exercise 2.3 - Django Models and Admin

## Overview
This exercise implements a simple Recipe model in Django with Django admin integration, following mentor recommendations for a clean, single-app architecture.

## Project Structure
```
Exercise 2.3/
├── src/
│   ├── recipes/           # Single app for all recipe functionality
│   │   ├── models.py      # Recipe model (simple design)
│   │   ├── admin.py       # Admin configuration
│   │   └── tests.py       # Test cases
│   ├── recipestore/       # Project settings
│   │   ├── settings.py    # Base settings
│   │   ├── settings_local.py   # Local development settings
│   │   └── settings_prod.py    # Production settings
│   └── manage.py
├── a2-e23-local/          # Local virtual environment
├── a2-e23-prod/           # Production virtual environment
├── requirements.txt       # Python dependencies
├── screenshots/           # Required screenshots
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

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Run Development Server
```powershell
# Activate local environment
.\a2-e23-local\Scripts\Activate.ps1

cd src
python manage.py runserver
```

Access admin at: http://127.0.0.1:8000/admin/

### Run Tests
```powershell
cd src
python manage.py test
```

## Mentor Revisions Implemented

✅ **Simplified to single app:** Removed `recipe_categories` and `recipe_ingredients` apps, consolidated everything into `recipes` app

✅ **Simple model design:** Recipe model uses comma-separated string for ingredients instead of complex relationships

✅ **Computed difficulty:** Difficulty is calculated on-the-fly, not stored in database

✅ **Two environments:** Created separate local and production virtual environments with appropriate settings

✅ **Schema diagram:** Prepared instructions for creating UML diagram using online tools

✅ **Test naming:** Test screenshot should be named `Test-Report.jpg`

✅ **Five recipes:** Admin configured to add and display recipes

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
