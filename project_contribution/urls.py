from .views import *
from django.urls import path




urlpatterns = [
    path('add/', project_contribution_create_view, name="contribution_create_view" )
]