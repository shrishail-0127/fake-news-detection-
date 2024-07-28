from django.contrib import admin
from django.urls import path
from fake_news_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('predict/', views.predict, name='predict'),
]
