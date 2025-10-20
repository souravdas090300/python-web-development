from django.db import models


class Recipe(models.Model):
	DIFFICULTY_CHOICES = [
		('easy', 'Easy'),
		('medium', 'Medium'),
		('hard', 'Hard'),
	]

	name = models.CharField(max_length=120)
	cooking_time = models.PositiveIntegerField(help_text='in minutes')
	ingredients = models.TextField()
	description = models.TextField()
	difficulty_level = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
	category = models.ForeignKey('recipe_categories.Category', on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self) -> str:
		return self.name
