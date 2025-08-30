from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('singup/', views.singUp, name='singup'),
    path('login/', views.UserLogin, name='login'),
    path('user-dashboard/', views.user_dashboard, name='user-dashboard')
]
