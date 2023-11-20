from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),

    path('register', views.register, name='register'),
    path('login', views.userLogin, name='login'),

    path('dashboard', views.dashboard, name='dashboard'),

    path('create', views.create_employee, name='create'),
    path('update/<int:pk>', views.update_employee, name='update'),
    path('employee/<int:pk>', views.view_employee, name='employee'),
     path('delete/<int:pk>', views.delete_employee, name='delete'),


    path('logout', views.userLogout, name='logout'),
]
