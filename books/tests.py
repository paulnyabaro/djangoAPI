from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = 'A good title'
            subtitle = 'An excellent subtitle'
            author = 'Tom Christie'
            isbn = '1234567890123'
        )
    
    

