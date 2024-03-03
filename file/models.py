from django.db import models
from message.models import List as Message


class List(models.Model):
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="message_files"
    )
