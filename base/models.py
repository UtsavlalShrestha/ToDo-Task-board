from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES= [
        ('todo', 'ToDo'),
        ('inporgress', 'InProgress'),
        ('completed', 'Completed'),
        ('deleted', 'Deleted'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,)
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title