from django.contrib import admin
from .models import Notes, UserInfos, SharedNotes 

# Register your models here.
admin.site.register(Notes)
admin.site.register(UserInfos)
admin.site.register(SharedNotes)
