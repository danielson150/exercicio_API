from django.urls import path, include
from .views import *

urlpatterns = [
    path('', RootApi.as_view(), name='api-root'),
    path('api-authentication/', include('rest_framework.urls')),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('profile-posts/', ProfilePostList.as_view(), name='profile-post-list'),
    path('profile-posts/<int:pk>/', ProfilePostDetail.as_view(), name='profile-post-detail'),
    path('posts-comments/', PostCommentList.as_view(), name='post-comment-list'),
    path('posts-comments/<int:pk>/', PostCommentDetail.as_view(), name='post-comment-detail'),
    path('posts/<int:pk>/comments/', CommentList.as_view(), name='comment-list'),
    path('posts/<int:pk>/comments/<int:comment_pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('profile-posts-comments/', ProfilePostsComments.as_view(), name='profile-posts-comments'),
   
]