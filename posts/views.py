from django.db.models import Count
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView, UpdateView, DeleteView

from comments.forms import CommentForm
from posts.forms import SearchForm, PostCreateForm, PostEditForm
from posts.models import Post
from tags.models import Tag


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
    ordering = '-created_at'
    paginate_by = 30

    def get_queryset(self):
        queryset = super().get_queryset()

        form = SearchForm(self.request.GET)
        if form.is_valid():
            for tag in form.get_tags():
                queryset = queryset.filter(tags__name=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar_tags'] = (
            Tag.objects
            .filter(posts__in=self.object_list)
            .annotate(post_count=Count('posts'))
            .order_by('-post_count')[:30]
        )
        return context


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'posts/post-details.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post-details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.order_by('-created_at')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post-create.html'
    form_class = PostCreateForm

    def get_success_url(self):
        return reverse('post-details', kwargs={'pk': self.object.pk})


class PostEditView(UpdateView):
    model = Post
    template_name = 'posts/post-edit.html'
    form_class = PostEditForm

    def get_success_url(self):
        return reverse('post-details', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post-delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = ', '.join(t.name for t in self.object.tags.all())
        return context