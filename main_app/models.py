from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=300)
    desc = models.TextField(max_length=300)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_success_url(self):
        return reverse('/', kwargs={'Comment.id': self.id})

