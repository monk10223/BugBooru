from django.urls import path

from posts.views import PostListView, PostCreateView, PostDetailView, PostEditView, PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-details'),
    path('<int:pk>/edit/', PostEditView.as_view(), name='post-edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]