
```markdown
# learning-journal.md

# Exercise 2.7 Learning Journal

## Learning goals
- Implement two-way communication with forms and POST handling
- Add search and chart-based data visualization
- Use Django QuerySet API, pandas DataFrames, and matplotlib

## What I built
A single-page search experience on /recipes/:
- Filter by recipe name (partial, case-insensitive) and optional difficulty
- Convert QuerySet to pandas DataFrame for processing
- Render DataFrame as an HTML table (safe)
- Generate matplotlib charts and embed as base64 images

## Design choices and rationale
- Keep search on /recipes/: Fewer routes, clearer UX
- name__icontains: Satisfies wildcard/partial matching and is case-insensitive
- Difficulty filter: Uses model’s computed difficulty(); filtered via id__in after computing
- Charts:
  - Bar: Clear comparison of cooking times
  - Pie: Quick sense of distribution by difficulty
  - Line: Trend-style view for cooking times by name order
- Rendering: DataFrame.to_html for speed-of-implementation plus safe filter; future enhancement could produce linkified table rows

## QuerySet → DataFrame: when and why
- QuerySet strengths:
  - Database-side filtering, joins, pagination, basic aggregates
  - Lazy evaluation, SQL-optimized, leverages indexes
- DataFrame strengths:
  - Vectorized column operations; easy grouping, reshaping, and plotting
  - Natural fit for generating charts and exports
- Practical split:
  - Use QuerySet to minimize rows/columns
  - Use DataFrame for analytics and visualization

## QuerySet evaluation (aligned with Django docs)
Common triggers that evaluate a QuerySet:
- Iteration: for obj in qs
- list(qs), bool(qs), len(qs)
- .exists(), .count(), .aggregate(), .get(), .first(), .last()
- Materialization in pandas: pd.DataFrame(qs.values())

Note: values()/values_list() return (lazy) QuerySets; evaluation occurs upon iteration/materialization.

## Tests and coverage
- Forms
  - Field presence, choices, required flags, and validity
- Views
  - Authentication protection for protected pages
  - Search on name (exact, partial, case-insensitive)
  - Difficulty filtering
  - “Show all” behavior (empty recipe_name)
  - Chart generation for #1/#2/#3
- Result: 39 tests passing

## Challenges and fixes
- 405 Method Not Allowed on POST to ListView
  - Fix: Implement post() and delegate to get() pipeline; read POST in get_context_data
- Chart rendering
  - Use plt.switch_backend('AGG'); call plt.clf(); apply tight_layout() to avoid clipping
- HTML safety
  - Render DataFrame with to_html and display via |safe in the template

## Things to improve next
- Make search results table clickable by injecting links into the DataFrame HTML or generating custom HTML
- Add more filters (e.g., category, cooking_time range)
- Add CSV/Excel export of filtered results
- Create summary dashboards (e.g., average cooking time per category)

## Key takeaways
- Keep server-side filtering in ORM; move computation-heavy analytics to DataFrames
- Tests give confidence when modifying views/POST behavior
- Base64 embedding simplifies chart delivery without touching the filesystem
