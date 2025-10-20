from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
	list_display = ("name", "cooking_time", "difficulty_level", "category")
	search_fields = ("name", "ingredients")
	list_filter = ("difficulty_level", "category")
