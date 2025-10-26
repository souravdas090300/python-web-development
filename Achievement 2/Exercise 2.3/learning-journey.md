# Learning Journey: Django Recipe App - Exercise 2.3# Learning Journey: Django Recipe App



## What This Exercise Taught MeThis exercise helped me understand:



### Database Design Philosophy- How to design a relational database schema for a real-world application

- **Simplicity over complexity:** Started with normalized multi-table design (Recipe, Ingredient, Category), but learned that storing ingredients as CSV is sufficient for this scope- Why a single-app design can be simpler to maintain for small scopes

- **Computed vs. stored data:** Difficulty doesn't need to be in the database—calculating it on-the-fly keeps the data clean and single-source-of-truth- How to resolve migration and model errors (reverse accessor clashes, default values)

- **When to normalize:** Understand the trade-offs between normalization (more tables, complex queries) and denormalization (simpler queries, easier maintenance for small datasets)- The importance of organizing code and removing unused files for maintainability

- How to use Django admin for data entry and management

### Django Model Best Practices- Writing and running tests for computed model methods and edge cases

- **Single responsibility:** One app (recipes) handles all recipe-related functionality

- **Helper methods:** `ingredients_list()` and `difficulty()` make the model more usable without polluting the database## Environments Learned (2025-10-26)

- **CharField vs TextField:** Use CharField for short, indexed fields (name); TextField for long or multi-line content (ingredients, description)- Maintained two separate settings files: `settings_local.py` and `settings_prod.py`

- **blank=True:** Allows optional fields like description without requiring database-level NULL- Used `DJANGO_SETTINGS_MODULE` to switch environments

- Ran production-ready servers:

### Migrations & Schema Changes	- ASGI: `uvicorn recipestore.asgi:application`

- **Iterative development:** Changed from TextField → M2M → back to TextField during development	- WSGI: `waitress-serve recipestore.wsgi:application`

- **Migration dependencies:** Learned how to resolve migration conflicts when restructuring apps

- **Default values:** When adding non-nullable fields to existing tables, Django requires a default or one-time value## Mentor Requirements I Implemented

- **Testing after migrations:** Always run tests after schema changes to catch breakages early- Single `recipes` app with a simple `Recipe` model

- `ingredients` stored as a comma-separated string; `difficulty()` computed

### Environment Management- Added at least five recipes via admin and prepared required screenshots

- **Settings separation:** `settings_local.py` (DEBUG=True) vs `settings_prod.py` (DEBUG=False, security headers)

- **Virtual environments per purpose:** a2-e23-local for dev, a2-e23-prod for production testingI gained confidence in:

- **DJANGO_SETTINGS_MODULE:** Environment variable to switch configurations without code changes- Using Django’s app structure for modular development

- **Server options:** ASGI (Uvicorn for async) vs WSGI (Waitress for sync); both suitable for Django- Debugging and iterating on model definitions

- Managing migrations and database changes

### Django Admin Power- Documenting my work for future reference

- **ModelAdmin customization:** Added `difficulty_display()` to show computed values in list view
- **list_display, search_fields, list_filter:** Make admin more usable for data entry and review
- **Admin as a tool:** Not just for CRUD—can display computed properties and validate data entry

### Testing Strategy
- **Test-Driven Development (TDD):** Wrote 10 tests covering model logic, views, and admin
- **Edge cases matter:** Empty ingredients, whitespace handling, all difficulty levels
- **Separation of concerns:** Model tests in tests.py for clean organization
- **Regression prevention:** Tests caught issues when switching between M2M and CSV approaches

### Production Readiness
- **Security settings:** SECURE_SSL_REDIRECT, SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE for HTTPS
- **Environment-driven config:** Use os.environ.get() for secrets and host configuration
- **Static file handling:** STATIC_ROOT for production (collectstatic), MEDIA_ROOT for uploads
- **Server choice:** Uvicorn for modern async workloads, Waitress for traditional sync apps

## Skills I Gained Confidence In

### Technical Skills
✅ Designing simple, maintainable database schemas  
✅ Writing Django models with computed properties  
✅ Customizing Django admin for better UX  
✅ Managing multiple environments (local/prod) with separate settings  
✅ Running production-ready servers (Uvicorn ASGI, Waitress WSGI)  
✅ Writing comprehensive test suites (model + view + admin)  
✅ Debugging migration errors and resolving dependencies  
✅ Using environment variables for configuration  

### Soft Skills
✅ Following mentor feedback and iterating on design  
✅ Documenting decisions and trade-offs (README, journals)  
✅ Breaking down complex problems into simple steps  
✅ Knowing when to simplify vs. when to optimize  

## Key Takeaways

### 1. Start Simple, Iterate as Needed
- CSV storage for ingredients works perfectly for this use case
- Don't over-engineer early—add complexity only when requirements demand it
- Premature optimization (like normalizing ingredients into a separate table) adds maintenance burden without clear benefit at this scale

### 2. Computed Properties Are Powerful
- `difficulty()` is always accurate because it's calculated from current data
- No risk of stale data (if we stored difficulty, it could become inconsistent with cooking_time or ingredients)
- Easier to change logic (just update the method, not migrate data)

### 3. Environment Separation Prevents Mistakes
- Debug mode in production = security risk
- Separate settings files make it explicit which config is active
- Virtual environments per config reduce dependency conflicts

### 4. Tests Are Documentation
- 10 tests explain how the app should behave
- Future changes can be validated by running the test suite
- Tests caught regressions when switching from M2M to CSV

### 5. Admin Is a Product
- Customizing admin improves developer/stakeholder experience
- `difficulty_display()` makes the admin list view immediately useful
- Good admin UX speeds up data entry and review

## Challenges Overcome

### Challenge 1: Migration Conflicts
- **Problem:** Switching from M2M Ingredient back to TextField caused migration dependency errors
- **Solution:** Created a new migration to remove M2M field, delete Ingredient model, and add TextField with a default value
- **Lesson:** Understand Django's migration graph; sometimes a clean migration is better than trying to fix a broken one

### Challenge 2: manage.py Settings Error
- **Problem:** manage.py defaulted to non-existent `recipe_project.settings`
- **Solution:** Updated manage.py to default to `recipe_project.settings_local`
- **Lesson:** Always configure default settings module when using split settings files

### Challenge 3: Test Failures After Model Changes
- **Problem:** Tests assumed M2M Ingredient objects but model used CSV strings
- **Solution:** Rewrote tests to use CSV strings; fixed indentation errors
- **Lesson:** Tests must reflect the actual model implementation; update tests when refactoring

### Challenge 4: Understanding Production Server Options
- **Problem:** Didn't know difference between ASGI (Uvicorn) and WSGI (Waitress)
- **Solution:** Researched both; installed and tested each; documented usage
- **Lesson:** ASGI supports async views (future-proof), WSGI is battle-tested and simpler for sync apps

## What I Would Do Differently Next Time

1. **Plan settings split from the start:** Would create settings_local.py and settings_prod.py in initial project setup, not retrofit later
2. **Write tests first:** TDD would have caught model changes earlier and guided design decisions
3. **Document as I go:** Would update README and journals after each major step, not at the end
4. **Use fixtures for test data:** Would create JSON fixtures for common test recipes instead of creating them in setUp()
5. **Add management commands:** Would create a `seed_recipes` management command to quickly populate DB with sample data

## How This Applies to Real-World Development

### In a Startup/Small Team
- Start with simple CSV storage; normalize later only if search/filtering becomes a bottleneck
- Single-app monoliths are easier to understand and maintain than microservices at small scale
- Admin customization saves hours of building custom CRUD interfaces

### In Enterprise/Large Team
- Environment separation (local/staging/prod) is critical for safe deployments
- Comprehensive tests enable confident refactoring and prevent regressions
- Production servers (Uvicorn/Waitress) must be configured correctly for scale and security

### For My Career
- Understanding Django's full stack (models, admin, views, templates, settings, migrations, testing, deployment) makes me a versatile backend developer
- Being able to explain trade-offs (CSV vs. normalized tables) shows architectural thinking
- Documented learning journey demonstrates growth mindset and self-reflection

## Next Steps in My Learning

1. **Enhance this project:** Add user authentication, allow users to create their own recipes, add recipe ratings
2. **Learn Django REST Framework:** Build an API for the Recipe model
3. **Add frontend:** Use React or Vue.js to consume the API
4. **Deploy to cloud:** Use Railway, Heroku, or AWS to deploy the production config
5. **Add full-text search:** Implement PostgreSQL full-text search for ingredients
6. **Performance optimization:** Add database indexes, caching (Redis), and query optimization

## Reflection

This exercise was a turning point in understanding **pragmatic software development**. The mentor's feedback to simplify the design taught me that:

- **Elegance is simplicity, not complexity**
- **Good code solves the problem at hand, not hypothetical future problems**
- **Tests and documentation are as important as the code itself**

I'm proud of the final implementation: a single-app Recipe model with CSV ingredients, computed difficulty, full test coverage, and production-ready configuration. It's simple, maintainable, and solves the requirements without over-engineering.

Most importantly, I learned to **listen to feedback, iterate quickly, and document the journey**—skills that will serve me throughout my career.
