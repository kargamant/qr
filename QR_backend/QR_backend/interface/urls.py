from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('register/', views.register, name='register'),
    path('login/', views.User_login, name='login')
]