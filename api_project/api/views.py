from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

from rest_framework import permissions

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# NEW: Full CRUD ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializerpermission_classes = [permissions.IsAuthenticated]  # only authenticated users