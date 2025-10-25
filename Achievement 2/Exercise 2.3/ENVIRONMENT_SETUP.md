# Exercise 2.3 - Environment Setup Guide

## Two Environments Created

Per mentor instructions, this project has **two separate virtual environments**:

### 1. Local Environment (`a2-e23-local`)
For development and testing on your local machine.

**Activate:**
```powershell
.\a2-e23-local\Scripts\Activate.ps1
```

**Run server:**
```powershell
cd src
python manage.py runserver --settings=recipestore.settings_local
```

**Settings:** `recipestore/settings_local.py`
- DEBUG = True
- SQLite database
- No ALLOWED_HOSTS restriction

---

### 2. Production Environment (`a2-e23-prod`)
For deployment simulation (more secure settings).

**Activate:**
```powershell
.\a2-e23-prod\Scripts\Activate.ps1
```

**Run server:**
```powershell
cd src
python manage.py runserver --settings=recipestore.settings_prod
```

**Settings:** `recipestore/settings_prod.py`
- DEBUG = False
- ALLOWED_HOSTS configured
- Production-ready configuration

---

## Quick Start Commands

### Initial Setup (First Time Only)
```powershell
# Navigate to Exercise 2.3
cd "Achievement 2\Exercise 2.3"

# Activate local environment
.\a2-e23-local\Scripts\Activate.ps1

# Navigate to src
cd src

# Run migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### Daily Development Workflow
```powershell
# 1. Activate local environment
.\a2-e23-local\Scripts\Activate.ps1

# 2. Navigate to src
cd src

# 3. Run development server
python manage.py runserver

# 4. Access admin at: http://127.0.0.1:8000/admin/
```

---

## Testing Production Settings
```powershell
# 1. Activate production environment
.\a2-e23-prod\Scripts\Activate.ps1

# 2. Navigate to src
cd src

# 3. Run with production settings
python manage.py runserver --settings=recipestore.settings_prod

# Note: Static files may need collectstatic in real production
```

---

## Running Tests
```powershell
# With local environment active
cd src
python manage.py test

# Take screenshot and save as: screenshots/Test-Report.jpg
```

---

## Dependencies
Both environments have Django 5.2.7 installed. See `requirements.txt` for full list.

---

## Important Notes
- Virtual environments are NOT tracked in git (in .gitignore)
- Use `settings_local.py` for development
- Use `settings_prod.py` for production/deployment
- Always activate the appropriate environment before running commands
