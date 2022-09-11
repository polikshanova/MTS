from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views
from .views import Installment, installment

urlpatterns = [
    path('register/', register, name='register'),
    path('installment/<int:pk>', installment, name='installment' ),#Installment.as_view(template_name='users/installment.html'), name='installment'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), # TODO добавить перенаправление на главную
    ]