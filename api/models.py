from django.db import models

# Create your models here.
class Task(models.Model):
    desc=models.TextField()
    status=models.BooleanField(default=False)

