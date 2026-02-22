from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView

# Create DRF router
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# Combine router URLs with additional views
urlpatterns = [
    path('', include(router.urls)),         # Register the posts and comments routes
    path('feed/', FeedView.as_view(), name='user-feed'),  # Feed endpoint
]


# GET     /api/posts/
# POST    /api/posts/
# GET     /api/posts/{id}/
# PUT     /api/posts/{id}/
# DELETE  /api/posts/{id}/