from django.db import models

# Create your models here.
from django.db import models
from section.models import List as Section


class List(models.Model):
    section = models.OneToOneField(Section, on_delete=models.CASCADE, related_name="section_payment")
    point = models.IntegerField()
    is_paid = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
