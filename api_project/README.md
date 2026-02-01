## 1. Files we created / modified
1. api/serializers.py ✅

Purpose: Convert Book model instances into JSON so the API can return them


# 2. api/views.py ✅

Purpose: Create a view that the API will use to return data.


# 3. api/urls.py ✅ (new file)

Purpose: Map URLs inside the api app to the views.


# What we accomplished in Task 1

Created a serializer (BookSerializer) to convert model instances to JSON.

Created a view (BookList) using Django REST Framework generics.

Mapped the view to a URL inside api/urls.py.

Connected app URLs to the project URL config (api_project/urls.py).

Tested the endpoint — it works at:



 ## 1. What we accomplished in Task 2

Created a ViewSet (BookViewSet)

Extends viewsets.ModelViewSet

Handles all CRUD operations:

GET → list or retrieve

POST → create

PUT / PATCH → update

DELETE → delete

Uses the BookSerializer to convert model instances to JSON.

# Created a Router (DefaultRouter)

Automatically generates URL patterns for the ViewSet

No need to manually write separate paths for list, create, retrieve, update, delete.

# Registered the ViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

This tells DRF:

“For all URLs starting with books_all/, use BookViewSet to handle requests.”


| Method | URL              | Action                |
| ------ | ---------------- | --------------------- |
| GET    | /books_all/      | list all books        |
| GET    | /books_all/<id>/ | retrieve single book  |
| POST   | /books_all/      | create new book       |
| PUT    | /books_all/<id>/ | update book           |
| PATCH  | /books_all/<id>/ | partially update book |
| DELETE | /books_all/<id>/ | delete book           |


# Kept the old ListAPIView (BookList)

Still accessible via /books/

Just to preserve Task 1 functionality

# Connected router URLs to the app URLs
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),   # Task 1 list view
    path('', include(router.urls)),                          # Task 2 CRUD ViewSet
]
path('', include(router.urls)) means:

Include all URLs the router generated at the root of this app (/api/ from project urls.py).



TokenAuthentication → lets users authenticate using a token in the HTTP header.

IsAuthenticated → prevents anonymous users from accessing the API.