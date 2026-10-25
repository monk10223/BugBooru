from django.urls import reverse
from django.views.generic import UpdateView, DeleteView

from comments.forms import CommentEditForm
from comments.models import Comment


# Create your views here.
class CommentEditView(UpdateView):
    model = Comment
    template_name = 'comments/comments-edit.html'
    form_class = CommentEditForm

    def get_success_url(self):
        return reverse('posts:details', kwargs={'pk': self.object.pk})


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/comments-delete.html'
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse('posts:details', kwargs={'pk': self.object.pk})