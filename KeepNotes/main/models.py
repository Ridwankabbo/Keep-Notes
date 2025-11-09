from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    notes_title = models.CharField(max_length=255, null=True)
    notes_text = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="notes_images", null=True, blank=True)
    
    def __str__(self):
        return f"{self.notes_title}"
    
    
class UserInfos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    user_imge = models.ImageField(null=True)
    user_email = models.EmailField(null=True)
    shared_notes = models.ForeignKey(Notes, on_delete=models.CASCADE, null=True)
    
    
class SharedNotes(models.Model):
    class Permission_type(models.TextChoices):
        READ = 'RD', 'Readable'
        WRITE = 'WR', 'Writable'
    
    class status_type(models.TextChoices):
        ACTIVE = 'AC', 'Active'
        DISABLE = 'DS', 'Disable'
    share_from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='form_me')
    share_to_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='to_me')
    notes = models.ForeignKey(Notes, on_delete=models.CASCADE, null=True )
    permission_type = models.CharField(max_length=2, choices=Permission_type.choices)
    status = models.CharField(max_length=2, choices=status_type.choices, default=status_type.ACTIVE)
    date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.share_from_user} to {self.share_to_user} at {self.date}. Permission type: {self.permission_type}"
    