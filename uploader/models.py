from django.db import models
from django.contrib.auth.models import User

# Create your models here.


'''class Upload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField()

    def __str__(self):
        return self.description[:30]'''

# uploader/models.py
#from django.contrib.auth.models import User
#from django.db import models

class Upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    text = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:20]}'
