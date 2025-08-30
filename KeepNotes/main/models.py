from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    notes_title = models.CharField(max_length=255, null=True)
    notes_text = models.CharField(max_length=255, null=True)
    