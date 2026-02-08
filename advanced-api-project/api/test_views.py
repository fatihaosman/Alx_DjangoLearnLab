from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITest(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='tester', password='pass1234')

        # Create an author
        self.author = Author.objects.create(name='John Doe')

        # Create a book
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2020,
            author=self.author
        )

    # ---------------------------
    # Test List API
    # ---------------------------
    def test_list_books(self):
        url = '/books/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    # ---------------------------
    # Test Detail API
    # ---------------------------
    def test_get_book_detail(self):
        url = f'/books/{self.book.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    # ---------------------------
    # Test Create API (requires login)
    # ---------------------------
    def test_create_book_authenticated(self):
        self.client.login(username='tester', password='pass1234')
        url = '/books/create/'
        data = {
            'title': 'New Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    # ---------------------------
    # Test Create API unauthenticated
    # ---------------------------
    def test_create_book_unauthenticated(self):
        url = '/books/create/'
        data = {
            'title': 'Hacker Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # permission denied

    # ---------------------------
    # Test Update API
    # ---------------------------
    def test_update_book(self):
        self.client.login(username='tester', password='pass1234')
        url = '/books/update?id=' + str(self.book.id)
        data = {
            'title': 'Updated Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    # ---------------------------
    # Test Delete API
    # ---------------------------
    def test_delete_book(self):
        self.client.login(username='tester', password='pass1234')
        url = '/books/delete?id=' + str(self.book.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
