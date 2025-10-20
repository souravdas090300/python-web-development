from django.test import TestCase
from .models import Recipe


class RecipeModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Recipe.objects.create(
			name="Masala Omelette",
			ingredients="eggs, onion, chili, salt, oil",
			cooking_time=10,
			description="Quick breakfast",
			difficulty_level='easy'
		)

	def test_name_label(self):
		recipe = Recipe.objects.get(id=1)
		field_label = recipe._meta.get_field('name').verbose_name
		self.assertEqual(field_label, 'name')

	def test_name_max_length(self):
		recipe = Recipe.objects.get(id=1)
		max_length = recipe._meta.get_field('name').max_length
		self.assertEqual(max_length, 120)

	def test_str_returns_name(self):
		recipe = Recipe.objects.get(id=1)
		self.assertEqual(str(recipe), 'Masala Omelette')
