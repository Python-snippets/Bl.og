from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
