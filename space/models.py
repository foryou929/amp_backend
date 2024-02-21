from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    points = models.IntegerField()
    type = models.IntegerField()
    period = models.IntegerField()
    area = models.IntegerField()
    status = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
