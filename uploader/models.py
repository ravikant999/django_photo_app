from django.db import models
from django.contrib.auth.models import User

class Upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    text = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:20]}"

class Like(models.Model):
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('upload', 'user')  # prevents duplicate likes by same user

    def __str__(self):
        return f"{self.user.username} liked {self.upload.id}"

class Comment(models.Model):
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.upload.id}: {self.text[:20]}"
