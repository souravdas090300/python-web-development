from django.db import models
from recipes.models import Recipe


class Ingredient(models.Model):
	name = models.CharField(max_length=100)
	quantity = models.FloatField()
	unit = models.CharField(max_length=20)
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredient_items', related_query_name='ingredient')

	def __str__(self) -> str:
		return f"{self.quantity} {self.unit} of {self.name}"
