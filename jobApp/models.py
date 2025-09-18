from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
