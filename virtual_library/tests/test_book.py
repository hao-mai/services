from django.urls import reverse
from rest_framework import status
# from rest_framework.test import APITestCase
from django.test import TestCase

from virtual_library.models import Book
from virtual_library.factories import BookFactory


class BookTests(TestCase):
    def setUp(self):
        pass

    def test_get_all_books(self):
        pass

    def test_get_book(self):
        pass

    def test_delete_book(self):
        pass
