from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book


class BookAPITests(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Sapiens:A brief history of humankind",
            author="Yuval Noah Harari",
            isbn="9780132350884",
            pages=480,
            published_date="2011-08-01",
        )
        self.list_url = reverse("book-list")

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        payload = {
            "title": "Odyssey",
            "author": "Homer",
            "isbn": "9780135957059",
            "pages": 352,
            "published_date": "2026-07-17",
        }
        response = self.client.post(self.list_url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Sapiens:A brief history of humankind")

    def test_update_book(self):
        url = reverse("book-detail", args=[self.book.id])
        response = self.client.patch(url, {"pages": 500})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.pages, 500)

    def test_delete_book(self):
        url = reverse("book-detail", args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_create_book_missing_field_fails(self):
        response = self.client.post(self.list_url, {"title": "No Author"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
