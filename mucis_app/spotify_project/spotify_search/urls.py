from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('callback/', views.callback, name='callback'),
]