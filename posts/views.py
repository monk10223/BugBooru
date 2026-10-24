from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from comments.forms import CommentForm
from posts.models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'post'
    ordering = '-created_at'

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_names = self.request.GET.getlist('tag')
        if tag_names:
            queryset = queryset.filter(tags__name__in=tag_names).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_tags'] = self.request.GET.getlist('tag')
        return context


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'posts/post-details.html'
    context_object_name = 'post'
    form = CommentForm

    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.get_object()
        comment.save()
        return super().form_valid(form)

#TODO create views for creating, editing, deleting posts