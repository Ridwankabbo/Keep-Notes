from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('singup/', views.singUp, name='singup'),
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.UserLogout, name='logout'),
    path('user-dashboard/', views.user_dashboard, name='user-dashboard'),
    path('insertNewNotes/', views.insertNotes, name='insert-new-notes'),
    path('edite-notes/<int:notes_id>/', views.EditeNotes, name='edite-notes'),
    path('delete-notes/<int:note_id>/', views.DeleteNotes, name='delete-note'),
    path('share-notes/<int:note_id>/', views.ShareNote, name='share-note'),
    path('user-profile/', views.user_profile, name='user-profile'),
    path('user-settings/', views.SettingsPage, name='user-settings'),
    path('disable-shared-note/<int:note_id>/', views.disable_shared_note, name='disable-shared-note')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
