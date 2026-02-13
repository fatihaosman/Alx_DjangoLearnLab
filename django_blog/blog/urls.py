from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, profile_view


from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    # add_comment,
    CommentUpdateView,
    CommentDeleteView,
    CommentCreateView,
    
)

# urlpatterns = [
#     path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('register/', register_view, name='register'),
#     path('profile/', profile_view, name='profile'),
    
    
#     path('posts/', PostListView.as_view(), name='post-list'),
#     path('posts/new/', PostCreateView.as_view(), name='post-create'),
#     path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
#     path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
#     path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
# ]


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),

    # Blog CRUD URLs (ALX-compatible)
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    
   # Comment URLs (IMPORTANT FOR ALX)
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

]

