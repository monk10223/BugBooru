from django.urls import path

from comments.views import CommentEditView, CommentDeleteView, RecentCommentsView

urlpatterns = [
    path('recent/', RecentCommentsView.as_view(), name='comment-list'),
    path('<int:pk>/edit/', CommentEditView.as_view(), name='comment-edit'),
    path('<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]