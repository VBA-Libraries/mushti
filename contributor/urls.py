from django.urls import path
from django.urls import URLPattern
from .views import CreateContributorView,ContributorListView,ContributorUpdateView

urlpatterns= [
    path('add/', CreateContributorView.as_view(), name ='add_contributor'),
    path('list/', ContributorListView.as_view(), name ='list_contributor'),
    path('update/', ContributorUpdateView.as_view(), name ='update_contributor')

]