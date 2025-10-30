# Exercise 2.4: Django Views and Templates

## Overview
Created a custom welcome page for the Recipe App using Django views and templates. This exercise focused on understanding and implementing the View and Template components of Django's MVT (Model-View-Template) architecture.

## What Was Implemented

### 1. View Created
- **File**: `recipe_project/recipe/views.py`
- **Function**: `home(request)` - Function-Based View that renders the welcome page
- **Purpose**: Handles HTTP request and returns rendered HTML template

```python
def home(request):
    """Home view for the recipe app."""
    return render(request, 'recipe/recipes_home.html')