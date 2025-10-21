# A2_Recipe_App

Django Recipe Application for Achievement 2, Exercise 2.2

## Project Structure

```
A2_Recipe_App/
├── a2-ve-recipeapp/        # Virtual environment (excluded from git)
│   ├── bin/                # Virtual environment executables
│   ├── include/            # Virtual environment headers
│   ├── lib/                # Python packages
│   └── pyvenv.cfg          # Virtual environment config
└── src/                    # Django project (renamed from recipe_project)
    ├── recipe_project/     # Project configuration
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── manage.py           # Django management script
    └── db.sqlite3          # SQLite database
```

## Setup Instructions

### 1. Activate Virtual Environment

```powershell
cd A2_Recipe_App
.\a2-ve-recipeapp\bin\Activate.ps1
```

Your prompt should show: `(a2-ve-recipeapp)`

### 2. Install Dependencies

If starting fresh:
```powershell
pip install django
```

Or from requirements.txt:
```powershell
pip install -r ../requirements.txt
```

### 3. Run Migrations

```powershell
cd src
python manage.py migrate
```

### 4. Create Superuser

```powershell
python manage.py createsuperuser
```

Follow the prompts to create admin credentials.

### 5. Run Development Server

```powershell
python manage.py runserver
```

Access the application at: http://127.0.0.1:8000/
Access admin dashboard at: http://127.0.0.1:8000/admin/

## Notes

- The Django project folder was renamed from `recipe_project` to `src` as per mentor instructions
- Virtual environment `a2-ve-recipeapp` is excluded from version control via `.gitignore`
- Screenshots documenting the setup process are in the `../screenshots/` folder
