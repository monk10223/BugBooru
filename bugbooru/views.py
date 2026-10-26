from django.shortcuts import redirect
from django.views.generic import TemplateView

from posts.forms import SearchForm


def homepage_redirect(request):
    return redirect('home')


class HomepageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context