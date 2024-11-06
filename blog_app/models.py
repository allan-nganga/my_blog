from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()    # Links to the User model
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets on creation
    updated_at = models.DateTimeField(auto_now_add=True)  # Automatically updates on modification

    def __str__(self):
        return self.title