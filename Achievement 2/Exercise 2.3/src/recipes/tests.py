from django.test import TestCase
from .models import Recipe


class RecipeModelTest(TestCase):
    """Test cases for the simplified Recipe model."""

    def setUp(self):
        """Create test recipe instances."""
        Recipe.objects.create(
            name="Easy Salad",
            cooking_time=5,
            ingredients="lettuce, tomato, cucumber",
            description="A simple fresh salad"
        )
        Recipe.objects.create(
            name="Complex Pasta",
            cooking_time=25,
            ingredients="pasta, tomato sauce, garlic, basil, olive oil, parmesan",
            description="A hearty pasta dish"
        )

    def test_recipe_creation(self):
        """Test that recipes are created correctly."""
        salad = Recipe.objects.get(name="Easy Salad")
        pasta = Recipe.objects.get(name="Complex Pasta")
        
        self.assertEqual(salad.cooking_time, 5)
        self.assertEqual(pasta.cooking_time, 25)

    def test_ingredients_list_method(self):
        """Test ingredients_list() returns correct list."""
        salad = Recipe.objects.get(name="Easy Salad")
        ingredients = salad.ingredients_list()
        
        self.assertEqual(len(ingredients), 3)
        self.assertIn("lettuce", ingredients)
        self.assertIn("tomato", ingredients)
        self.assertIn("cucumber", ingredients)

    def test_difficulty_easy(self):
        """Test difficulty calculation for Easy recipe."""
        salad = Recipe.objects.get(name="Easy Salad")
        # cooking_time=5 (<10) and 3 ingredients (<4) = Easy
        self.assertEqual(salad.difficulty(), "Easy")

    def test_difficulty_hard(self):
        """Test difficulty calculation for Hard recipe."""
        pasta = Recipe.objects.get(name="Complex Pasta")
        # cooking_time=25 (>=10) and 6 ingredients (>=4) = Hard
        self.assertEqual(pasta.difficulty(), "Hard")

    def test_difficulty_medium(self):
        """Test difficulty calculation for Medium recipe."""
        smoothie = Recipe.objects.create(
            name="Fruit Smoothie",
            cooking_time=5,
            ingredients="banana, strawberry, blueberry, yogurt, honey",
            description="A refreshing smoothie"
        )
        # cooking_time=5 (<10) and 5 ingredients (>=4) = Medium
        self.assertEqual(smoothie.difficulty(), "Medium")

    def test_difficulty_intermediate(self):
        """Test difficulty calculation for Intermediate recipe."""
        soup = Recipe.objects.create(
            name="Simple Soup",
            cooking_time=15,
            ingredients="broth, salt, pepper",
            description="A basic soup"
        )
        # cooking_time=15 (>=10) and 3 ingredients (<4) = Intermediate
        self.assertEqual(soup.difficulty(), "Intermediate")

    def test_str_method(self):
        """Test __str__ method returns recipe name."""
        salad = Recipe.objects.get(name="Easy Salad")
        self.assertEqual(str(salad), "Easy Salad")

    def test_name_max_length(self):
        """Test name field max length is 120."""
        recipe = Recipe.objects.get(name="Easy Salad")
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 120)

    def test_ingredients_list_empty(self):
        """Test ingredients_list() with empty ingredients."""
        empty_recipe = Recipe.objects.create(
            name="Empty Recipe",
            cooking_time=10,
            ingredients="",
            description="No ingredients"
        )
        self.assertEqual(empty_recipe.ingredients_list(), [])

    def test_ingredients_list_whitespace_handling(self):
        """Test ingredients_list() handles extra whitespace correctly."""
        recipe = Recipe.objects.create(
            name="Whitespace Test",
            cooking_time=10,
            ingredients="  salt  ,  pepper  ,  garlic  ",
            description="Testing whitespace"
        )
        ingredients = recipe.ingredients_list()
        self.assertEqual(ingredients, ["salt", "pepper", "garlic"])

