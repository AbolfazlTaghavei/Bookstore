from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # blank is form side arqument and permmision to blank input
    # but null is bd side arqument and permmision to None cell of db
    age = models.PositiveIntegerField(blank=True, null=True)
  