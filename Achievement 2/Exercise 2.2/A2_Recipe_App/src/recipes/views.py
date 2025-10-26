from django.shortcuts import render


def home(request):
	"""Simple welcome page for the Recipe App."""
	return render(request, 'recipes/recipes_home.html')
