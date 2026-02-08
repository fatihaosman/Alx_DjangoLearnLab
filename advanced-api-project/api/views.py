from rest_framework import generics, permissions
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
    permission_classes = [permissions.AllowAny]  # read-only for everyone

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
    permission_classes = [permissions.AllowAny]

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
    permission_classes = [permissions.IsAuthenticated]  # only logged-in users

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
    permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [permissions.IsAuthenticated]
