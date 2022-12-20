from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

class Reservation(models.Model):
    NAME = models.CharField(max_length=50)
    BIRTH = models.CharField(max_length=10)
    HOSPITAL = models.CharField(max_length=50)
    VACCINE = models.CharField(max_length=50)
    DATE = models.CharField(default='YYYY-MM-DD', max_length=10)
    HOUR = models.CharField(max_length=50)
    
    def __str__(self):
        return self.subject