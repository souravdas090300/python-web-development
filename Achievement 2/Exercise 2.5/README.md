# Recipe Application

A Django-based web application for managing and sharing recipes. Built as part of Exercise 2.5 of the Python Web Development bootcamp.

## Features

- **Recipe Management**: Create, view, and organize recipes with detailed information
- **User Authentication**: Secure user registration and login system
- **Category System**: Organize recipes by meal type (Breakfast, Lunch, Dinner, Dessert, Snack)
- **Image Upload**: Add photos to recipes for visual appeal
- **Difficulty Calculation**: Automatic difficulty rating based on cooking time and ingredients
- **Comprehensive Navigation**: Professional navigation system with multiple categories
- **Responsive Design**: Mobile-friendly interface that works on all devices
- **Search Functionality**: Search bar for finding recipes (UI implemented)

## Technologies Used

- **Python 3.14.0**: Core programming language
- **Django 5.2.7**: Web framework
- **Pillow 12.0.0**: Image processing library
- **SQLite3**: Database management
- **HTML5 & CSS3**: Frontend markup and styling

## Project Structure
recipe-app/
├── recipe_project/ # Main project directory
│ ├── recipe_project/ # Project settings
│ │ ├── settings.py # Production settings
│ │ ├── settings_local.py # Development settings
│ │ ├── urls.py # Main URL configuration
│ │ └── wsgi.py # WSGI configuration
│ ├── recipe/ # Recipe application
│ │ ├── models.py # Recipe model with category choices
│ │ ├── views.py # Home, list, and detail views
│ │ ├── urls.py # App-level URL patterns
│ │ ├── admin.py # Admin panel configuration
│ │ ├── templates/ # HTML templates
│ │ │ └── recipe/
│ │ │ ├── recipes_home.html # Welcome page
│ │ │ ├── recipes_list.html # Recipe list view
│ │ │ └── recipe_detail.html # Recipe detail view
│ │ └── tests/ # Test suite
│ │ ├── test_models.py
│ │ ├── test_views.py
│ │ └── test_recipe_list_detail.py
│ ├── media/ # User-uploaded images
│ │ └── recipes/ # Recipe photos
│ └── static/ # Static files
│ └── recipe/
│ └── images/ # Static images (Welcome page.jpeg)
└── README.md # This file


## Models

### Recipe Model

The Recipe model includes the following fields:

- `name`: CharField - Recipe name (max 120 characters)
- `cooking_time`: IntegerField - Time in minutes
- `ingredients`: TextField - Comma-separated ingredients list
- `description`: TextField - Recipe description (optional)
- `category`: CharField - Meal category with predefined choices
- `pic`: ImageField - Recipe photo
- `user`: ForeignKey - Recipe author (linked to User model)

**Category Choices:**
- Breakfast
- Lunch
- Dinner
- Dessert
- Snack

**Computed Properties:**
- `difficulty()`: Returns Easy, Medium, Intermediate, or Hard based on cooking time and number of ingredients
- `ingredients_list()`: Parses comma-separated ingredients into a Python list
- `get_absolute_url()`: Returns URL to recipe detail page

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/souravdas090300/recipe-app.git
   cd recipe-app/recipe_project

Create virtual environment:
python -m venv web-dev
web-dev\Scripts\activate  # Windows

Install dependencies:
pip install django pillow

Apply migrations:
python manage.py migrate

Create superuser:
python manage.py createsuperuser

Run development server:
python manage.py runserver

Access the application:

Homepage: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/
Recipe List: http://127.0.0.1:8000/recipes/
Database
The application currently contains 5 sample recipes with the following data:

Tea - Easy difficulty, 5 minutes, Breakfast
Coffee - Medium difficulty, 10 minutes, Breakfast
Omelette - Easy difficulty, 10 minutes, Breakfast
Pasta - Medium difficulty, 15 minutes, Lunch
Salad - Easy difficulty, 5 minutes, Lunch

Testing
Run the comprehensive test suite:

Test Coverage:
python manage.py test

Model tests: Field validation, methods, relationships
View tests: Homepage, list view, detail view
URL tests: Routing and reverse lookups
Current Status: All 23 tests passing ✅

Static & Media Files

Static Files Configuration
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

Development Settings

During development, media files are served via:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Key Features Implementation
1. Welcome Page
Full-screen hero image with overlay gradient
Comprehensive navigation with 7 dropdown menus (75+ items)
Statistics section showing app metrics
Category grid with hover effects
Professional footer with 8 columns of links
2. Recipe List View
Table display of all recipes
Clickable recipe names and images
Shows recipe name and cooking time
3. Recipe Detail View
Complete recipe information display
Recipe image
Ingredients list
Cooking time

Automatically calculated difficulty
Category information
4. Navigation System
Main Categories:

Dinners (14 subcategories)
Meals (10 subcategories)
Ingredients (8 subcategories)
Occasions (31 subcategories including all major holidays)
Cuisines (7 subcategories)
Features (5 subcategories)
About Us (5 subcategories)
Future Enhancements
 Implement search functionality
 Add recipe rating system
 Enable user comments and reviews
 Create recipe collections/favorites
 Add nutritional information
 Implement recipe sharing on social media
 Add cooking videos
 Create meal planning feature
 Wire up all navigation links
 Add advanced filtering options
Contributing

This is a learning project for the Python Web Development bootcamp. Feedback and suggestions are welcome!

License
This project is created for educational purposes as part of CareerFoundry's Python Web Development course.

Author
Sourav Das

GitHub: @souravdas090300
Acknowledgments
CareerFoundry mentors and tutors
Django documentation
Python community
Exercise 2.5 - Django Recipe App
Python Web Development Bootcamp
October 2025