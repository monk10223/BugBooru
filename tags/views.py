from django.db.models import Count
from django.views.generic import ListView

from tags.models import Tag


# Create your views here.
class MostUsedTagsView(ListView):
    model = Tag
    template_name = 'tags/most-used-tags.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return (
            Tag.objects
            .annotate(post_count=Count('post'))
            .order_by('-post_count')[:30]
        )