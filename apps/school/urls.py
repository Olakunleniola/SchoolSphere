from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomepageView, name='home'),
    path('register', views.RegisterView, name='register')
]