from django.urls import path
from .views import *


urlpatterns = [
    path('', ProjectListView.as_view(), name="project_list_view"),
    path('<pk>/',ProjectDetailView.as_view(),name = "project_detail_view")

    
]
