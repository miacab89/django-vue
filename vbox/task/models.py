from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=False)
    updated_at = models.DateField(auto_now_add=False)
