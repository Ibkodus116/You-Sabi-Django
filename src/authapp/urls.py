from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_auth ,name='login'),
    path('logout', views.logout_auth ,name='logout'),
    path('signup', views.signup_auth ,name='signup'),
]