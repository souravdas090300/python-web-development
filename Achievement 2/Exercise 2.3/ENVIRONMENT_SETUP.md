# Exercise 2.3 - Environment Setup Guide

## Two Separate Settings Files

Per mentor instructions, this project uses **two separate settings files** (no shared base):

### 1. Local Environment (`settings_local.py`)
Complete standalone settings file for development.

**Activate:**
```powershell
.\a2-e23-local\Scripts\Activate.ps1
```

**Run server:**
```powershell
cd src
python manage.py runserver --settings=recipestore.settings_local
```

**Features:**
- DEBUG = True
- SQLite database
- No ALLOWED_HOSTS restriction
- Full debug context processors

---

### 2. Production Environment (`settings_prod.py`)
Complete standalone settings file for production deployment.

**Activate:**
```powershell
.\a2-e23-prod\Scripts\Activate.ps1
```

**Run server:**
```powershell
cd src
python manage.py runserver --settings=recipestore.settings_prod
```

**Features:**
- DEBUG = False
- ALLOWED_HOSTS configured
- Security headers enabled
- STATIC_ROOT and MEDIA_ROOT configured
- Ready for deployment

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

# 3. Run development server with local settings
python manage.py runserver --settings=recipestore.settings_local

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

# Note: You may need to run collectstatic for static files:
# python manage.py collectstatic --settings=recipestore.settings_prod
```

---

## Running Tests
```powershell
# With local environment active
cd src
python manage.py test --settings=recipestore.settings_local

# Take screenshot and save as: screenshots/Test-Report.jpg
```

---

## Running Migrations

### For Local Environment:
```powershell
cd src
python manage.py makemigrations --settings=recipestore.settings_local
python manage.py migrate --settings=recipestore.settings_local
```

### For Production Environment:
```powershell
cd src
python manage.py makemigrations --settings=recipestore.settings_prod
python manage.py migrate --settings=recipestore.settings_prod
```

---

## Creating Superuser

### For Local:
```powershell
cd src
python manage.py createsuperuser --settings=recipestore.settings_local
```

### For Production:
```powershell
cd src
python manage.py createsuperuser --settings=recipestore.settings_prod
```

---

## Dependencies
Both environments have Django 5.2.7 installed. See `requirements.txt` for full list.

---

## Important Notes

### Settings Files
- **settings_local.py** - Complete standalone settings for local development (DEBUG=True)
- **settings_prod.py** - Complete standalone settings for production (DEBUG=False)
- **settings_base.py.backup** - Old base settings file (kept as backup, not used)
- Always specify `--settings=recipestore.settings_local` or `--settings=recipestore.settings_prod` with manage.py commands

### Virtual Environments
- Virtual environments are NOT tracked in git (in .gitignore)
- `a2-e23-local` uses settings_local.py
- `a2-e23-prod` uses settings_prod.py
- Both have Django 5.2.7 installed

### Best Practices
- Use `settings_local.py` for all development work
- Use `settings_prod.py` when testing production configuration
- Always activate the appropriate environment before running commands
- Specify settings file explicitly in all manage.py commands
