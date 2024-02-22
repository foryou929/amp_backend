from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    user = models.ForeignKey(User, related_name="project_lists", on_delete=models.CASCADE)
    area = models.IntegerField(default=0)
    content_size = models.CharField(max_length=255)
    description = models.TextField()
    name = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    project_period = models.IntegerField(default=0)
    recruitment_content = models.IntegerField(default=0)
    recruitment_number = models.IntegerField(default=0)
    recruitment_period = models.IntegerField(default=0)
    space_type = models.IntegerField(default=0)
    year_designation = models.IntegerField(default=0)

    PROGRESS_CHOICES = [
        (0, "Undefined"),
        (1, "提案"),
        (2, "選定"),
        (3, "承諾"),
        (4, "仮払い"),
        (5, "広告物発送"),
        (6, "広告物受け取り"),
        (7, "開始報告"),
        (8, "経過報告"),
        (9, "終了報告"),
        (10, "支払い"),
        (11, "レビュー"),
    ]

    progress = models.PositiveSmallIntegerField(choices=PROGRESS_CHOICES, default=1)

    def __str__(self):
        return self.name
