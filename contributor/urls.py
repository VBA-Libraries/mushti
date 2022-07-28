from django.urls import path
from django.urls import URLPattern
from .views import CreateContributorView

urlpatterns= [path('add/', CreateContributorView.as_view(), name ='add_contributor')]