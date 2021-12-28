from django.db import models

# Local Models
from users.models import UserProfile

class TasksOfUser(models.Model):
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                 null=False, blank=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    file = models.FileField(blank=True)

    def __str__(self):
        return self.name