# Learning Journal: Django Recipe App Exercise

## Step 1: Database Blueprint
- Identified main entities: Recipe, Ingredient, Category
- Designed relationships: Recipe has many Ingredients, Recipe belongs to one Category
- Outlined schema for each model

## Step 2: App Creation
- Created three Django apps: recipes, recipe_categories, recipe_ingredients
- Updated `INSTALLED_APPS` in settings

## Step 3: Model Implementation
- Defined Recipe model with fields: name, cooking_time, ingredients, description, difficulty_level, category (FK)
- Defined Category model with name field
- Defined Ingredient model with name, quantity, unit, recipe (FK)

## Step 4: Admin Registration
- Registered Recipe, Category, and Ingredient models in their respective admin.py files

## Step 5: Migrations
- Ran `makemigrations` and `migrate` to create database tables

## Step 6: Testing
- Wrote and ran tests for Recipe model fields and constraints

## Step 7: Admin Data Entry
- Created superuser
- Added sample categories, recipes, and ingredients via Django admin

## Notes
- Resolved model and migration errors (reverse accessor, default values)
- Removed unused app folders for clarity
