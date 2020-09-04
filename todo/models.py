from django.db import models

# Create your models here.
# task,title,isCompeleted

class Todo(models.Model):
    task        = models.CharField(max_length=200)
    title       = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default=False)