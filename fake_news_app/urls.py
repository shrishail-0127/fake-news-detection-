from django.urls import path
from . import views

# app_name = 'fake_news_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/',views.user_register, name='register'),
    path('predict/', views.predict, name='predict'),
]
