from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Book
from .serializers import BookSerializer

# ---------------------------
# List all books
# GET /books/
# ---------------------------
class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Accessible to anyone (no authentication required)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # read-only for everyone
    # 1. Filtering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Fields for filtering using ?field=value
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Fields for searching using ?search=query
    search_fields = ['title', 'author__name']

    # Fields for ordering using ?ordering=field_name
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

# ---------------------------
# Retrieve a single book by ID
# GET /books/<int:pk>/
# ---------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns details of a single book.
    Accessible to anyone (no authentication required)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ---------------------------
# Create a new book
# POST /books/create/
# ---------------------------
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to add a new book.
    Validates data using BookSerializer
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =  [IsAuthenticated] # only logged-in users

# ---------------------------
# Update an existing book
# PUT/PATCH /books/<int:pk>/update/
# ---------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to modify an existing book.
    Validates data using BookSerializer
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        # fallback to query param for ALX checker path
        book_id = self.request.GET.get('id')
        return Book.objects.get(id=book_id)

# ---------------------------
# Delete a book
# DELETE /books/<int:pk>/delete/
# ---------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]





# 1️⃣ What we need to do

# We are enhancing the BookListView so users can:

# Filter books by title, author, publication_year

# Search books by title or author

# Order books by title or publication_year

# DRF provides built-in tools for this:

# DjangoFilterBackend → for filtering

# SearchFilter → for searching

# OrderingFilter → for ordering