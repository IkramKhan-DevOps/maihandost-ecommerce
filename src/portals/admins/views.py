
from django.contrib.auth.decorators import user_passes_test

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView, ListView, UpdateView,
    TemplateView)

from src.accounts.models import User
from .models import (
    ProjectType
)

""" GENERIC VIEWS CUSTOM > DASHBOARD AND NGO """


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class DashboardView(TemplateView):
    template_name = 'admins/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['total'] = User.objects.all().count()
        context['admins'] = User.objects.filter(is_superuser=True).count()
        context['staff'] = User.objects.filter(is_staff=True).count()
        context['customers'] = User.objects.filter(is_customer=True, is_active=True).count()
        context['in_active'] = User.objects.filter(is_active=False).count()
        return context


""" GENERIC VIEWS CRUD > PROJECT TYPE """


# @method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
# class ProjectTypeListView(ListView):
#     queryset = ProjectType.objects.all()
#
#
# @method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
# class ProjectTypeCreateView(CreateView):
#     model = ProjectType
#     fields = '__all__'
#     success_url = reverse_lazy('admins:projecttype-list')
#
#
# @method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
# class ProjectTypeUpdateView(UpdateView):
#     model = ProjectType
#     fields = '__all__'
#     success_url = reverse_lazy('admins:projecttype-list')

