from django.urls import path


from main_user.views import *

urlpatterns = [
    path('login/',UserLoginView.as_view(),name='login_view'),
    path('signup/',UserCreateView.as_view(),name='signup_view' )
]