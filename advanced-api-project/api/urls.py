from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # ALX wants these exact strings
    path('books/update', BookUpdateView.as_view(), name='book-update'),
    path('books/delete', BookDeleteView.as_view(), name='book-delete'),
]

  



# 1️⃣ What we “should have done” before
# Custom APIView:

# You write a class like class MyView(APIView)

# You manually define get(), post(), put(), delete() methods

# You manually call serializers, check permissions, handle errors

# ✅ Works, but a lot of repeated code if you have many models or endpoints


# 2️⃣ What we are doing now with Generic Views

# DRF has pre-made views for common tasks: List, Retrieve, Create, Update, Delete

# You just say:

# Which model to use → queryset

# Which serializer → serializer_class

# Who can access → permission_classes

# 💡 DRF handles all the repetitive work automatically:

# Fetching objects

# Serializing them

# Checking permissions

# Returning proper HTTP responses