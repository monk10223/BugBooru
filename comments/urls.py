from django.urls import path

from comments.views import CommentEditView, CommentDeleteView


urlpatterns = [
    path('<int:pk>/edit/', CommentEditView.as_view(), name='comment-edit'),
    path('<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]