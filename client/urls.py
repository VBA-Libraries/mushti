from django.urls import path
from .views import CreateClientView,ClientListView,ClientUpdateView

urlpatterns=[
    path('add/', CreateClientView.as_view(), name='add_client'),
    path('list/', ClientListView.as_view(), name='list_client'),
    path('update/<pk>', ClientUpdateView.as_view(), name='update_client')
    
    ]
