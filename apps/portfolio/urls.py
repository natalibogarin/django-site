from django.urls import path
from . import views

app_name='apps.portfolio'

urlpatterns = [
    path('projects', views.projects, name='projects'),
]