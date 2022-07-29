from django.urls import path
from .views import CreateClientView

urlpatterns=[path('add/', CreateClientView.as_view(), name='add_client')]
