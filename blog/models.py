from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self) -> str:
        return f"{self.title} by {self.author.username}"