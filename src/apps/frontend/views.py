from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomepageView (TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context["matheuszin"] = "god"
        return context

