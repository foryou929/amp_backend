from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    GENDER_CHOICES = [
        (0, "Undefined"),
        (1, "Male"),
        (2, "Female"),
        (3, "Other"),
    ]

    OCCUPATION_CHOICES = [
        (0, "Undefined"),
        (1, "Student"),
        (2, "Professional"),
        (3, "Unemployed"),
        (4, "Other"),
    ]

    TRANSPORTATION_CHOICES = [
        (0, "Undefined"),
        (1, "Car"),
        (2, "Bicycle"),
        (3, "Public transportation"),
        (4, "Walking"),
        (5, "Other"),
    ]

    RESIDENCE_CHOICES = [
        (0, "Undefined"),
        (1, "House"),
        (2, "Apartment"),
        (3, "Condo"),
        (4, "Other"),
    ]

    TYPE_CHOICES = [
        (0, "Undefined"),
        (1, "Type A"),
        (2, "Type B"),
        (3, "Type C"),
        (4, "Other"),
    ]

    username = models.CharField(max_length=100, default="")
    birthday = models.DateTimeField()
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=0)
    gendor = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=0)
    occupation = models.PositiveSmallIntegerField(choices=OCCUPATION_CHOICES, default=0)
    primary_transportation = models.PositiveSmallIntegerField(
        choices=TRANSPORTATION_CHOICES, default=0
    )
    residence_type = models.PositiveSmallIntegerField(
        choices=RESIDENCE_CHOICES, default=0
    )
    self_introduction = models.TextField(default="")
    activity_scope = models.CharField(max_length=100, default="")
    area = models.PositiveIntegerField(default=0)
    available_space = models.PositiveIntegerField(default=0)
    follower_count = models.PositiveIntegerField(default=0)
    usage_frequency = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
