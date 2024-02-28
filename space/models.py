from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="spaces"
    )
    title = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
    period = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
