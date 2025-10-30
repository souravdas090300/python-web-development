# learning-journey.md

# Exercise 2.7 Learning Journey

## Before
I had a protected Recipes list and detail pages from previous work. This exercise extended the app with interactive search and lightweight analytics using pandas and matplotlib.

## During
- I planned the search UX first: one page (/recipes/) with a clean form, and three chart types.
- I implemented the form and handled POST safely with CSRF protection.
- I filtered via QuerySet, converted results into a DataFrame, and added computed fields (difficulty, ingredients_count).
- I generated charts via matplotlib and embedded them as base64 images.
- I leaned on tests to validate both the search and chart paths.

## Obstacles and breakthroughs
- 405 on POST with ListView: Implemented post() and reused get() logic to keep everything centralized.
- Chart rendering polish: Switched to AGG backend, cleared state between renders, and used tight_layout() to avoid label clipping.
- Keeping routes consistent: Verified that the app uses /login, /logout, /recipes, and /recipes/<id>/—no /accounts/ or /recipes/search.

## What I’m proud of
- A clear end-to-end pipeline: form → QuerySet → DataFrame → table + chart
- Comprehensive automated tests (including charts) that kept refactoring safe
- A user flow that stays compact and predictable

## If I had more time
- Linkify names directly in the DataFrame output for clickable results inside the search table
- Add more analytics (e.g., pivots, top-N charts) and an export button
- Add time-based data and trend charts if/when timestamps are added to Recipe

## Execution flow I’ll demonstrate (screenshots/screencast)
- Home (/) → Login (/login/) → Recipes (/recipes/) → Enter search → Submit → See table + chart → Click name → Detail (/recipes/:id/) → Logout (/logout/)
- I’ll capture screenshots at each step and include them in “Exercise 2.7/screenshots” or record a short “user-journey.mp4”.

## Confidence snapshot
- QuerySet filtering and evaluation: high
- DataFrame transformations and plotting: high
- Django view/form testing: high
