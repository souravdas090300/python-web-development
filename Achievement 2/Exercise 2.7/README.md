# README.md

# Exercise 2.7 — Data Analysis and Visualization in Django (Recipe App)

This exercise adds search and data visualization to the Recipe App. Users can search recipes (with partial text match and optional difficulty filter), see results as an HTML table, and view a chart (bar, pie, or line) generated from the results.

## What’s included in Exercise 2.7

- Search form on Recipes page (/recipes/)
  - Recipe name (supports partial/wildcard, case-insensitive)
  - Difficulty filter (All, Easy, Medium, Intermediate, Hard)
  - Chart type (Bar, Pie, Line)
- QuerySet → pandas DataFrame pipeline
  - Filter with Django ORM
  - Convert to DataFrame for processing
  - Compute derived columns (difficulty, ingredients_count)
  - Render table as HTML (safe)
- Charts (matplotlib, embedded as base64 image)
  - Bar: Recipe Name vs Cooking Time (minutes)
  - Pie: Distribution by Difficulty
  - Line: Cooking Time Trend (by Recipe Name)
- UX
  - Results table + chart appear on the protected Recipes page
  - All-Recipes section includes clickable recipe names to detail pages
  - Authentication protection remains in place

## Tech/versions

- Python 3.x
- Django 5.2.x
- pandas 2.3.x
- matplotlib 3.10.x
- SQLite (development)

## URLs

- Home: /
- Login: /login/
- Logout: /logout/
- Recipes (list + search + chart): /recipes/
- Recipe detail: /recipes/<id>/

Note: There is no separate /recipes/search/ page. The search and the chart rendering happen on /recipes/ via POST.

## How it works (data flow)

1) User opens /recipes/ (protected).
2) Fills the search form:
   - Recipe name (optional; partial match via name__icontains)
   - Difficulty (optional)
   - Chart type (required)
3) The view filters a QuerySet using the criteria.
4) The QuerySet is converted to a pandas DataFrame.
5) The DataFrame is enriched:
   - difficulty (computed)
   - ingredients_count
6) The DataFrame is converted to HTML and displayed using the safe filter.
7) A matplotlib chart is generated and embedded as a base64 image below the table.

## Files updated in this exercise

- recipe/forms.py — NEW: RecipeSearchForm (recipe_name, difficulty, chart_type)
- recipe/utils.py — NEW: get_graph (BytesIO + base64) and get_chart (bar/pie/line)
- recipe/views.py — UPDATED: RecipeListView handles POST (search), builds DataFrame and chart
- recipe/templates/recipe/recipes_list.html — UPDATED: search form, results table, chart section
- recipe/tests/
  - test_forms.py — NEW: form tests
  - test_recipes_views.py — UPDATED: search + chart tests added

## Chart mapping (exact)

- Bar chart (#1): X = name, Y = cooking_time (minutes), Title = “Cooking Time by Recipe”
- Pie chart (#2): Slices by difficulty (counts), Title = “Recipe Distribution by Difficulty”
- Line chart (#3): X = name, Y = cooking_time (minutes), Title = “Cooking Time Trend”

## Commands (Windows PowerShell)

From VS Code terminal:

```powershell
cd C:\Users\dasau\recipe-app\recipe_project
& "$Env:USERPROFILE\Envs\web-dev\Scripts\Activate.ps1"
py manage.py runserver

Run test:
cd C:\Users\dasau\recipe-app\recipe_project
& "$Env:USERPROFILE\Envs\web-dev\Scripts\Activate.ps1"
py manage.py test -v 2

Expected tests outcome: 39 tests passing.

Execution flow (Mermaid)
flowchart TD
  A[Home /] -->|Not logged in| B[Login /login/]
  A -->|Already logged in| C[Recipes List /recipes/]
  B -->|Submit valid| C
  C --> D[Enter search criteria on /recipes/]
  D --> E[Submit search (POST)]
  E --> F[Results table + chart on /recipes/]
  F --> G[Click recipe name]
  G --> H[Detail page /recipes/:id]
  H --> I[Logout /logout/]
  I --> J[Success page]

  Screenshots / Screencast (for Task-2.7)
Capture each step with URL:

Home → /
Login → /login/
Recipes (list/search) → /recipes/
After submitting search (POST) → /recipes/ (table + chart visible)
Detail → /recipes/<id>/
Logout → /logout/ (success page)
Save screenshots in Achievement 2/Exercise 2.7/screenshots. Optional: 2–3 minute screencast user-journey.mp4.

Notes
The search results table rendered from DataFrame.to_html isn’t linkified by default. Clickable links are provided in the “All Recipes” section via object.get_absolute_url. You can enhance the DataFrame HTML to include links later if required.
If you see “Couldn’t import Django,” activate the virtual environment before running commands.
