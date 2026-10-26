from django.urls import path

from tags.views import MostUsedTagsView


urlpatterns = [
    path('', MostUsedTagsView.as_view(), name='tag-list'),
]