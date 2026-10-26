from typing import Any

from django.urls import reverse
from django.views.generic import UpdateView, DeleteView, ListView

from comments.forms import CommentEditForm
from comments.models import Comment


# Create your views here.
class CommentEditView(UpdateView):
    model = Comment
    template_name = 'comments/comments-edit.html'
    form_class = CommentEditForm

    def get_success_url(self):
        return reverse('post-details', kwargs={'pk': self.object.post_id})


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/comments-delete.html'
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse('post-details', kwargs={'pk': self.object.post_id})


class RecentCommentsView(ListView):
    model = Comment
    template_name = 'comments/comments-recent.html'
    context_object_name = 'comments'
    ordering = '-created_at'
    paginate_by = 20

    def get_queryset(self):
        return super().get_queryset().select_related('post')