from django.db.models import Sum
from django.views.generic import TemplateView, DetailView

from src.accounts.models import User


class HomeView(TemplateView):
    template_name = 'website/home.html'

