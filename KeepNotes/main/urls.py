from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('singup/', views.singUp, name='singup'),
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.UserLogout, name='logout'),
    path('user-dashboard/', views.user_dashboard, name='user-dashboard'),
    path('insertNewNotes/', views.insertNotes, name='insert-new-notes'),
    path('edite-notes/<int:notes_id>/', views.EditeNotes, name='edite-notes'),
    path('delete-notes/<int:note_id>/', views.DeleteNotes, name='delete-note'),
    path('user-profile/', views.user_profile, name='user-profile')
]
