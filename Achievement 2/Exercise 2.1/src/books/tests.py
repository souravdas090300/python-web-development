from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        # Use only the fields that actually exist in your Book model
        Book.objects.create(
            name='Pride and Prejudice', 
            price=23.71,
            genre='classic', 
            book_type='hardcover'
        )

    def test_book_name(self):
        # Get a book object to test
        book = Book.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = book._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        # Get a book object to test
        book = Book.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its max_length
        max_length = book._meta.get_field('name').max_length

        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120)

    def test_genre_choices(self):
        # Get a book object to test
        book = Book.objects.get(id=1)
        
        # Test that the genre is set correctly
        self.assertEqual(book.genre, 'classic')

    def test_book_type_choices(self):
        # Get a book object to test
        book = Book.objects.get(id=1)
        
        # Test that the book type is set correctly
        self.assertEqual(book.book_type, 'hardcover')