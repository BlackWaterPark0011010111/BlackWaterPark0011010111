from django.urls import path, include
from .views import (
    HomePageview,
    UserListView,
    UserDetailView,
    PostListView,
    PostDetailView,
    UserPostView,
    RegisterUserView,
    PostCreateView,
    UpdateUserView,DeleteUserView,
    UpdatePostView,
    DeletePostView
)

urlpatterns = [
    path("", HomePageview.as_view(), name="home"),
    path("users/", UserListView.as_view(), name="users-list"),
    path("users/<str:username>/", UserDetailView.as_view(), name="user-detail"),
    path("posts/", PostListView.as_view(), name="posts-list"),
    path("posts/<int:post_id>/", PostDetailView.as_view(), name="post-detail"),
    path("users/<str:username>/posts/", UserPostView.as_view(), name="user-posts"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("users/<str:username>/posts/create/", PostCreateView.as_view(), name="create-post"),
    path('users/<str:username>/update/',UpdateUserView.as_view(),name='update-user'),
    path('users/<str:username>/delete/',DeleteUserView.as_view(),name='delete-user'),
    path('users/<str:username>/posts/<int:post_id>/update/',UpdatePostView.as_view(),name='update-post'),
    path('users/<str:username>/posts/<int:post_id>/delete/',DeletePostView.as_view(),name='delete-post'),
]
# path('url/',views,name_for_html_h)
