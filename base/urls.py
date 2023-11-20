from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),

    path('register', views.register, name='register'),
    path('login', views.userLogin, name='login'),

    path('dashboard', views.dashboard, name='dashboard'),

    path('create', views.create_employee, name='create'),


    path('logout', views.userLogout, name='logout'),
]
