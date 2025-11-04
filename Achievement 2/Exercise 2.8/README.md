# Exercise 2.8 - Data Analysis and Visualization in Django

## Overview
This exercise focuses on implementing data analysis and visualization features in a Django web application. The Recipe App now includes advanced search capabilities, data filtering, and interactive charts to visualize recipe data.

## Project Information
- **Developer:** Sourav Das
- **Course:** Python for Web Developers
- **Achievement:** 2
- **Exercise:** 2.8
- **Submission Date:** November 4, 2025

## Live Application
🌐 **Heroku Deployment:** https://recipe-app-cf-sourav-d5b3ff514bd4.herokuapp.com/

## Exercise Objectives

### Learning Outcomes
By completing this exercise, I have learned to:
1. ✅ Implement data analysis using pandas DataFrame
2. ✅ Create data visualizations with matplotlib (bar, pie, line charts)
3. ✅ Build search and filter functionality in Django
4. ✅ Encode images as base64 for HTML embedding
5. ✅ Display data in multiple formats (table and charts)
6. ✅ Deploy Django applications to Heroku with PostgreSQL
7. ✅ Handle static and media files in production

### Technical Skills Developed
- **Data Analysis:** pandas DataFrames, data manipulation, filtering
- **Visualization:** matplotlib chart generation, image encoding
- **Django:** Class-based views, QuerySets, template rendering
- **Deployment:** Heroku, PostgreSQL, environment variables
- **Testing:** Django test framework, 85% code coverage

## Features Implemented

### 1. Advanced Search Functionality
- Search recipes by name (partial match, case-insensitive)
- Filter recipes by ingredient
- Filter recipes by difficulty level (Easy, Medium, Intermediate, Hard)
- Results display in paginated table format

### 2. Data Visualization
Three chart types available:
- **Bar Chart:** Cooking time comparison across recipes
- **Pie Chart:** Recipe distribution by difficulty level
- **Line Chart:** Cooking time trends

### 3. User Authentication
- User registration (signup)
- User login/logout
- Protected views (login required for recipes)
- Superuser accounts for admin access

### 4. Recipe Management
- View all recipes with pagination
- View individual recipe details
- Add new recipes (authenticated users)
- Calculate difficulty automatically
- Display ingredients as formatted list

### 5. Admin Panel
- Custom Django admin interface
- Modern styling (red gradient theme)
- Recipe management with search and filters
- User management

## Technical Implementation

### Data Analysis Workflow
1. User submits search form with criteria
2. Django QuerySet filters recipes from database
3. Filtered results converted to pandas DataFrame
4. DataFrame used to generate matplotlib chart
5. Chart saved to BytesIO buffer
6. Image encoded as base64 string
7. Chart embedded in HTML template

### Technologies Used
- **Backend:** Django 5.2.7, Python 3.14.0
- **Data Analysis:** pandas 2.2.3, matplotlib 3.9.3
- **Database:** SQLite (development), PostgreSQL (production)
- **Deployment:** Heroku, gunicorn, whitenoise
- **Frontend:** HTML5, CSS3, Bootstrap styling
- **Image Processing:** Pillow 11.0.0

## Project Structure
```
Exercise-2.8/
├── README.md                 # This file
├── TESTING_REPORT.md         # Comprehensive test coverage report
├── learning-journal.md       # Weekly learning reflections
├── learning-journey.md       # Overall learning journey
└── screenshots/              # Application screenshots
    ├── 1-homepage.png
    ├── 2-recipes-list.png
    ├── 3-search-results-chart.png
    ├── 4-recipe-detail.png
    ├── 5-add-recipe.png
    ├── 6-admin-panel.png
    ├── 7-about-page.png
    └── 8-test-report.png
```


## Testing Results

### Test Summary
- **Total Tests:** 39
- **Pass Rate:** 100% ✅
- **Code Coverage:** 85%
- **Execution Time:** ~28 seconds

### Test Categories
1. Model Tests (8 tests) - Recipe model functionality
2. View Tests (15 tests) - List, detail, search views
3. Form Tests (8 tests) - Search form validation
4. Search Tests (8 tests) - Filter and pagination

See `TESTING_REPORT.md` for detailed coverage analysis.

## Deployment Information

### Heroku Configuration
- **App Name:** recipe-app-cf-sourav
- **Region:** US
- **Stack:** Heroku-24
- **Database:** PostgreSQL (postgresql-perpendicular-54168)
- **Buildpack:** Python

### Environment Variables
```
DJANGO_SECRET_KEY=<secret>
DJANGO_ALLOWED_HOSTS=*
DJANGO_CSRF_TRUSTED_ORIGINS=https://recipe-app-cf-sourav-d5b3ff514bd4.herokuapp.com
DJANGO_SECURE_SSL_REDIRECT=true
DJANGO_SESSION_COOKIE_SECURE=true
DJANGO_CSRF_COOKIE_SECURE=true
```

### Deployment Process
1. Create Heroku app and PostgreSQL database
2. Configure environment variables
3. Set up Procfile for gunicorn
4. Deploy via git push to Heroku
5. Run database migrations
6. Create superuser accounts
7. Load sample recipe data

## User Accounts

### For Mentor Access
- **Username:** mentorCF
- **Password:** Ment0r@CareerF0undry
- **Role:** Superuser (full admin access)

### Developer Account
- **Username:** souravdas090300
- **Password:** [Set via Heroku CLI]
- **Role:** Superuser

## Sample Data
The application includes 15 sample recipes across different categories:
- Breakfast: Classic Pancakes, Veggie Omelette
- Lunch: Grilled Chicken Salad, Caesar Salad
- Dinner: Spaghetti Carbonara, Grilled Salmon
- Dessert: Chocolate Cake, Tiramisu
- Snack: Guacamole, Hummus

## Challenges and Solutions

### Challenge 1: Image Storage on Heroku
**Problem:** Heroku's ephemeral filesystem doesn't persist uploaded images
**Solution:** Modified model to allow null images, templates handle missing images gracefully
**Future Enhancement:** Implement AWS S3 or Cloudinary for permanent storage

### Challenge 2: CSRF Verification Failed
**Problem:** 403 errors on form submissions in production
**Solution:** Added CSRF_TRUSTED_ORIGINS environment variable with Heroku domain

### Challenge 3: Chart Generation in Production
**Problem:** Matplotlib requires specific backend for server-side rendering
**Solution:** Used 'AGG' backend (Anti-Grain Geometry) for non-interactive plotting

### Challenge 4: Static Files on Heroku
**Problem:** Static files not serving correctly in production
**Solution:** Configured whitenoise for static file serving without separate server

## Key Learnings

### Data Analysis with Django
- Converting QuerySets to pandas DataFrames for analysis
- Using DataFrame methods for aggregation and filtering
- Generating charts from DataFrame data

### Image Encoding
- Saving matplotlib figures to BytesIO buffer
- Base64 encoding for HTML image embedding
- Memory management (closing buffers after use)

### Production Deployment
- Difference between development and production settings
- Environment variable configuration
- Database migration management on Heroku
- SSL and security settings

### Django Best Practices
- Class-based views for reusable code
- LoginRequiredMixin for protecting views
- Form validation and error handling
- Template inheritance and context processors

## Future Enhancements

### Planned Features
1. **Cloud Image Storage:** AWS S3 integration for recipe images
2. **User Profiles:** Custom user profiles with favorite recipes
3. **Recipe Ratings:** User ratings and reviews
4. **Advanced Filtering:** Multi-criteria filtering (category + difficulty)
5. **Recipe Export:** PDF generation for recipe cards
6. **Social Sharing:** Share recipes on social media
7. **Nutrition Info:** Calculate calories and nutritional values

### Code Improvements
1. Add caching for frequently accessed recipes
2. Implement full-text search with PostgreSQL
3. Add API endpoints for mobile app integration
4. Improve chart interactivity with JavaScript libraries
5. Add more test coverage for edge cases

## Resources and References

### Documentation
- Django Documentation: https://docs.djangoproject.com/
- pandas Documentation: https://pandas.pydata.org/docs/
- matplotlib Documentation: https://matplotlib.org/stable/
- Heroku Django Guide: https://devcenter.heroku.com/articles/django-app-configuration

### Libraries Used
- Django 5.2.7
- pandas 2.2.3
- matplotlib 3.9.3
- Pillow 11.0.0
- gunicorn 23.0.0
- psycopg2-binary 2.9.10
- whitenoise 6.8.2
- coverage 7.11.0

## Acknowledgments
- **CareerFoundry:** Course materials and guidance
- **Mentor:** Code review and technical support
- **Django Community:** Excellent documentation and resources

## License
This project is created for educational purposes as part of the CareerFoundry Full-Stack Web Development course.

---

**Last Updated:** November 4, 2025  
**Version:** 1.0  
**Status:** Complete and Deployed ✅
