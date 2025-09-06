from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    notes_title = models.CharField(max_length=255, null=True)
    notes_text = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f"{self.notes_title}"
    
    
class UserInfos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    user_imge = models.ImageField(null=True)
    user_email = models.EmailField(null=True)
    shared_notes = models.ForeignKey(Notes, on_delete=models.CASCADE, null=True)
    