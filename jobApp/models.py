from django.db import models

# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=40)
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    def __str__(self):
        return self.nickname

class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    def __str__(self):
        return self.title

