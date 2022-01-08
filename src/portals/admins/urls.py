from django.urls import path, include
from .views import *

app_name = "admins"
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

]
