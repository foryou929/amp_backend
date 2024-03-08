from django.db import models
from section.models import List
from server.settings import AUTH_USER_MODEL

class List(models.Model):
    section = models.ForeignKey(List, related_name="section_reviews", on_delete=models.CASCADE)
    reviewer = models.ForeignKey(AUTH_USER_MODEL, related_name="user_reviewer", on_delete=models.CASCADE)
    content = models.TextField()
    rank = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name