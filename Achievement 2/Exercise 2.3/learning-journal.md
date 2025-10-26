# Learning Journal: Django Recipe App Exercise 2.3

Date: October 26, 2025

## Initial Approach vs. Mentor-Revised Approach

### Original Design (Multi-App)
- Three apps: recipes, recipe_categories, recipe_ingredients
- Complex relationships: ForeignKeys and separate Ingredient/Category models
- Difficulty stored as a database field

### Revised Design (Mentor Recommendation)
- **Single app:** recipes only
- **Simple ingredients:** stored as comma-separated string in TextField
- **Computed difficulty:** calculated on-the-fly from cooking_time and ingredient count
- **Rationale:** Simpler to maintain, fewer tables, aligns with project scope

## Step 1: Database Blueprint
- Drew schema for Recipe table with fields: name, cooking_time, ingredients (CSV), description
- Identified difficulty as a computed property (not stored)
- Planned to use dbdiagram.io for final UML diagram screenshot

## Step 2: App Creation (Simplified per Mentor)
- Created single `recipes` app
- Removed previous recipe_categories and recipe_ingredients apps
- Updated `INSTALLED_APPS` in settings to include only `recipes`

## Step 3: Model Implementation
**Recipe Model:**
- `name`: CharField(max_length=120)
- `cooking_time`: PositiveIntegerField (in minutes)
- `ingredients`: TextField (stores CSV like "salt, water, sugar")
- `description`: TextField(blank=True)

**Helper Methods:**
- `ingredients_list()`: Splits CSV into list of strings, strips whitespace
- `difficulty()`: Returns "Easy", "Medium", "Intermediate", or "Hard" based on:
  - Easy: time < 10 and ingredients < 4
  - Medium: time < 10 and ingredients ≥ 4
  - Intermediate: time ≥ 10 and ingredients < 4
  - Hard: time ≥ 10 and ingredients ≥ 4

## Step 4: Admin Configuration
- Registered `Recipe` model in admin
- Created `RecipeAdmin` class with:
  - `difficulty_display()` method to show computed difficulty in list
  - `list_display = ("name", "cooking_time", "difficulty_display")`
  - `search_fields = ("name", "ingredients")`
  - `list_filter = ("cooking_time",)`

## Step 5: Migrations
- Fixed manage.py to default to `settings_local` (was pointing to non-existent settings.py)
- Ran `makemigrations` to create initial Recipe table
- Resolved migration issues when switching from M2M back to TextField (provided default value)
- Applied migrations successfully with `migrate --settings=recipestore.settings_local`

## Step 6: Testing (14 Tests Total)
**Model Tests (recipes/tests.py - 10 tests):**
- Recipe creation and field validation
- `ingredients_list()` parsing from CSV
- Difficulty calculations for all four levels
- Empty ingredients handling
- Whitespace normalization in CSV parsing
- `__str__` method and max_length validation

**View/Admin Tests (recipes/tests_views.py - 4 tests):**
- Home view returns 200 and uses correct template
- Admin requires login (redirects to /admin/login/)
- Admin changelist displays "Difficulty" column and computed values

All tests passing ✅

## Step 7: Virtual Environments
- Created `a2-e23-local` for local development
- Created `a2-e23-prod` for production testing
- Installed Django 5.2.7, Uvicorn (ASGI), and Waitress (WSGI) in both

## Step 8: Settings Split
- `settings_local.py`: DEBUG=True, local dev config
- `settings_prod.py`: DEBUG=False, environment-driven secrets, security headers
- Updated `asgi.py` and `wsgi.py` to default to settings_local
- Verified both configs pass Django system checks

## Step 9: Production Server Setup
- Configured ASGI entrypoint for Uvicorn
- Configured WSGI entrypoint for Waitress
- Documented how to switch environments via DJANGO_SETTINGS_MODULE

## Step 10: Admin Data Entry
- Created superuser with username/password
- Added 5 sample recipes via admin interface
- Verified difficulty column displays correctly in changelist

## Step 11: Documentation & Screenshots
- Updated README.md with mentor revisions and run instructions
- Prepared screenshot checklist:
  - `recipe-app-schema.jpg`: UML diagram of Recipe model
  - Admin screenshot: list with 5+ recipes and Difficulty column
  - `Test-Report.jpg`: test suite results (14 tests OK)

## Key Challenges & Solutions

**Challenge 1:** Migration errors when model changed from M2M to TextField
- **Solution:** Provided default value during migration; created new migration to replace M2M with TextField

**Challenge 2:** manage.py looking for non-existent settings.py
- **Solution:** Updated manage.py to default to `recipe_project.settings_local`

**Challenge 3:** Tests failing after M2M → CSV switch
- **Solution:** Rewrote all tests to use CSV strings instead of Ingredient objects; fixed indentation errors

**Challenge 4:** Understanding when to use production vs. local settings
- **Solution:** Set DJANGO_SETTINGS_MODULE environment variable before running production servers

## Lessons Learned
- Start simple: CSV storage is sufficient for many use cases; normalize only when needed
- Computed properties reduce DB complexity and keep data consistent
- Environment-specific settings enable safe testing of production config
- Always specify --settings flag when using split settings files
- Test-driven development catches regressions early (14 tests validated model changes)

## Next Steps for Submission
1. ✅ Code complete and tested
2. 📸 Create UML diagram and export as recipe-app-schema.jpg
3. 📸 Capture admin screenshot showing 5+ recipes with Difficulty
4. 📸 Run tests and save screenshot as Test-Report.jpg
5. 📤 Submit to mentor for review
