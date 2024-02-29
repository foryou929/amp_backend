from django.contrib.auth.models import AbstractUser
from django.db import models


class List(AbstractUser):
    birthday = models.CharField(max_length=10, default="0000-0-0")
    type = models.IntegerField(default=0)
    gendor = models.IntegerField(default=0)
    occupation = models.IntegerField(default=0)
    primary_transportation = models.IntegerField(default=0)
    residence_type = models.IntegerField(default=0)
    self_introduction = models.TextField(default="")
    activity_scope = models.CharField(max_length=100, default="")
    area = models.PositiveIntegerField(default=0)
    available_space = models.PositiveIntegerField(default=0)
    follower_count = models.PositiveIntegerField(default=0)
    usage_frequency = models.PositiveIntegerField(default=0)
    main_service = models.TextField(default="")
    main_pr_target = models.TextField(default="")
    main_message = models.TextField(default="")
    website_url = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
