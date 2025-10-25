from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
	def difficulty_display(self, obj: Recipe) -> str:
		return obj.difficulty()

	difficulty_display.short_description = "Difficulty"

	list_display = ("name", "cooking_time", "difficulty_display")
	search_fields = ("name", "ingredients")
	list_filter = ("cooking_time",)
