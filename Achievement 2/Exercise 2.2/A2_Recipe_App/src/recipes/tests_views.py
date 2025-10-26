from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Recipe


class RecipeViewsTests(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'recipes/recipes_home.html')


class AdminTests(TestCase):
    def setUp(self):
        # Create a superuser for admin access
        User = get_user_model()
        self.admin_username = 'admin_test'
        self.admin_password = 'StrongPass123!'
        self.admin = User.objects.create_superuser(
            username=self.admin_username,
            email='admin_test@example.com',
            password=self.admin_password,
        )

        # Create a sample recipe with CSV ingredients
        self.recipe = Recipe.objects.create(
            name='Test Recipe',
            cooking_time=5,
            ingredients='salt, water, sugar',
            description='Test description',
        )

    def test_admin_requires_login(self):
        # Accessing admin without login should redirect to login page
        response = self.client.get('/admin/', follow=False)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/login/', response['Location'])

    def test_admin_recipe_changelist_shows_difficulty(self):
        # Login to admin
        self.client.login(username=self.admin_username, password=self.admin_password)

        # Access Recipe changelist
        response = self.client.get('/admin/recipes/recipe/')
        self.assertEqual(response.status_code, 200)

        # Check that the Difficulty column header and computed value are present
        self.assertContains(response, 'Difficulty')
        self.assertContains(response, self.recipe.difficulty())
