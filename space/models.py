from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    user = models.ForeignKey(User, related_name="space_lists", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
    period = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.title
