# Recipe Application - Exercise 2.6: User Authentication

A Django-based web application for managing and sharing recipes with secure user authentication and authorization features.

## Exercise 2.6 Overview

This exercise implements comprehensive user authentication and authorization, protecting sensitive recipe data and providing personalized user experiences.

## New Features in Exercise 2.6

### 🔐 Authentication System
- **User Login**: Secure authentication form with credential validation
- **User Logout**: Clean logout process with success confirmation page
- **Session Management**: Django's built-in session handling for authenticated users
- **Password Protection**: All recipe views require authentication

### 🛡️ Protected Views
- **Recipe List View**: Login required to view all recipes
- **Recipe Detail View**: Login required to view recipe details
- **Automatic Redirect**: Unauthenticated users redirected to login page

### 🎨 User Interface Enhancements
- **Login Page**: Clean, styled authentication form at `/login/`
- **Logout Success Page**: Beautiful success page with animations and navigation options
- **Navigation Links**: Login/Logout buttons on all relevant pages
- **Admin Panel Link**: Quick access to Django admin from homepage

## Technologies Used

- **Python 3.14.0**: Core programming language
- **Django 5.2.7**: Web framework with built-in authentication
- **Pillow 12.0.0**: Image processing library
- **SQLite3**: Database management
- **HTML5 & CSS3**: Frontend with responsive design
- **Django Authentication System**: Built-in user authentication

## Project Structure
├── recipe_project/
│ ├── recipe_project/ # Main project directory
│ │ ├── settings.py # Production settings
│ │ ├── settings_local.py # Development settings
│ │ ├── urls.py # Main URL configuration
│ │ ├── views.py # Login/Logout views ⭐ NEW
│ │ └── wsgi.py
│ ├── recipe/ # Recipe application
│ │ ├── models.py # Recipe model
│ │ ├── views.py # Home, list, detail views (protected) ⭐ UPDATED
│ │ ├── urls.py # App-level URLs
│ │ ├── admin.py # Custom admin configuration ⭐ UPDATED
│ │ ├── templates/recipe/
│ │ │ ├── recipes_home.html # Welcome page with login link
│ │ │ ├── recipes_list.html # Protected recipe list ⭐ UPDATED
│ │ │ └── recipe_detail.html # Protected recipe detail ⭐ UPDATED
│ │ └── tests/ # Test suite (all passing)
│ ├── templates/ # Project-level templates ⭐ NEW
│ │ ├── auth/
│ │ │ ├── login.html # Login form ⭐ NEW
│ │ │ └── success.html # Logout success page ⭐ NEW
│ │ ├── admin/
│ │ │ └── base_site.html # Custom admin with home button ⭐ NEW
│ │ ├── static/ # Static files
│ │ │ └── recipe/images/
│ │ │ └── welcome-page.jpeg
│ │ └── media/ # User-uploaded files
│ │ └── recipes/
│ ├── db.sqlite3
│ └── manage.py
└── README.md


## Installation & Setup

### Prerequisites
- Python 3.14.0 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/souravdas090300/recipe-app.git
   cd recipe-app/recipe_project
   
   2. Create and activate virtual enviroment
   # Windows
python -m venv web-dev
web-dev\Scripts\activate

# macOS/Linux
python3 -m venv web-dev
source web-dev/bin/activate

3. Install dependencies:
pip install django pillow

4. Apply database migration:
py manage.py migrate

5. Create superuser (for admin access):
python manage.py createsuperuser
Enter username, email, and password when prompted.

6. Run development server:
python manage.py runserver

7. Access the application:

Homepage: http://127.0.0.1:8000/
Login Page: http://127.0.0.1:8000/login/
Admin Panel: http://127.0.0.1:8000/admin/
Recipe List: http://127.0.0.1:8000/recipes/ (requires login)
Authentication Features
Login System
URL: /login/

Features:

Django's AuthenticationForm for secure credential validation
CSRF protection for form security
Error messages for invalid credentials
Automatic redirect to recipe list after successful login
Clean, responsive design

Login View Implementation:

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipe:recipes-list')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

    Logout System
URL: /logout/

Features:

Instant logout using Django's logout() function
Beautiful success page with:
Animated checkmark icon
Gradient background
Feature list
"Log Back In" and "Go to Homepage" buttons
Responsive design

Logout View Implementation:
def logout_view(request):
    logout(request)
    return render(request, 'auth/success.html')

Protected Views
Both recipe views are protected using LoginRequiredMixin:
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe/recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe/recipe_detail.html'

Behavior:

Unauthenticated users attempting to access protected views are automatically redirected to /login/
After successful login, users are redirected to the recipes list
Session maintained across page navigation
URL Structure
URL	            View	            Access      	Description
/	            home	            Public	        Welcome page with login button
/login/	        login_view	        Public	        Authentication form
/logout/	    logout_view	        Public	        Logout and success page
/recipes/	    RecipeListView	    Protected	    List of all recipes
/recipes/<pk>/	RecipeDetailView	Protected	    Individual recipe details
/admin/	        Django Admin	    Admin only	    Admin panel with custom homepage button

Settings Configuration
Authentication Settings (settings_local.py)
# Authentication
LOGIN_URL = '/login/'

# Templates - includes project-level templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Project-level templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

Static and Media files
# Static files (project-level)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'templates' / 'static']

# Media files (user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'templates' / 'media'

Database
The application uses SQLite3 with the following data:

5 Sample Recipes: Tea, Omelette, Pasta, Chicken Curry, Cake
User Model: Django's built-in User model
Recipe Model: Custom model with authentication relationship
Recipe Model Fields
name: Recipe name
cooking_time: Time in minutes
ingredients: Comma-separated ingredients
description: Optional recipe description
category: Meal category (breakfast, lunch, dinner, dessert, snack)
pic: Recipe image (ImageField)
user: Foreign key to User model (recipe author) ⭐ Authentication Link

Testing
Run All Tests:
py manage.py test

Current Status: ✅ All 20 tests passing

Test Coverage
Authentication-Aware Tests:

Model tests: Recipe creation, methods, difficulty calculation
View tests: Home page, protected list/detail views with login
URL tests: Routing and reverse lookups
Admin tests: Custom configuration
Example Test with Authentication:

def test_recipes_list_view(self):
    # Log in before accessing protected view
    self.client.login(username='testuser', password='password123')
    response = self.client.get(reverse('recipe:recipes-list'))
    self.assertEqual(response.status_code, 200)

User Journey
Typical User Flow
Landing on Homepage

User visits http://127.0.0.1:8000/
Sees welcome page with hero image
Clicks "Log In" button
Authentication

Redirected to /login/
Enters username and password
Submits form
Access Protected Content

Successfully authenticated
Redirected to /recipes/ (recipe list)
Can view all recipes with images
Can click any recipe to see details
Viewing Recipe Details

Clicks on recipe name or image
Redirected to /recipes/<id>/
Sees full recipe information with difficulty
Logging Out

Clicks "Logout" button (on list or detail page)
Redirected to /logout/
Sees success page with options
Can log back in or return to homepage
Security Features
CSRF Protection: All forms include {% csrf_token %}
Password Hashing: Django uses PBKDF2 algorithm
Session Security: Secure session management

URL Protection: Unauthorized access redirects to login
Input Validation: Form validation prevents injection attacks
Admin Panel Customization

Custom Admin Features
# Custom admin site headers
admin.site.site_header = "Recipe App Administration"
admin.site.site_title = "Recipe App Admin"
admin.site.index_title = "Welcome to Recipe App Admin Panel"

Admin Panel Features:

🏠 "Go to Homepage" button in top-right corner
Custom branding (Recipe App Administration)
Recipe management with list filters
Search functionality for recipes
Difficulty display in admin changelist
Future Enhancements
Planned Features
 User registration (signup) page
 Password reset functionality
 User profiles with custom avatars
 Email verification for new users
 Social authentication (Google, Facebook)
 Two-factor authentication (2FA)
 Remember me functionality
 User-specific recipe collections
 Recipe sharing with permissions
 Activity logs and user analytics
Security Enhancements
 Rate limiting for login attempts
 CAPTCHA for login form
 Email notifications for suspicious activity
 Password strength requirements
 Session timeout configuration

 Contributing
This is a learning project for CareerFoundry's Python Web Development course. Feedback and suggestions are welcome!

License
This project is created for educational purposes as part of CareerFoundry's Python Web Development course.

Author
Sourav Das

GitHub: @souravdas090300
Repository: recipe-app
Acknowledgments
CareerFoundry mentors and tutors
Django documentation and community
Python community
Exercise 2.6 guidance and requirements
Version History
v2.6 (October 2025) - User Authentication & Authorization

Added login/logout functionality
Protected recipe views with LoginRequiredMixin
Created custom admin panel with homepage button

Enhanced welcome page with clearer hero image
All 20 tests passing
v2.5 (October 2025) - Django Models & Views

Recipe model with category field
List and detail views
Comprehensive welcome page
Static and media file configuration
