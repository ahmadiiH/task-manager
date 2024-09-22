from django.db import models
from django .contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    title= models.CharField(max_length=50)
    description= models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(default=timezone.now)
