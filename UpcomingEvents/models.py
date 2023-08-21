from django.db import models

# models.py

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    place = models.CharField(max_length=200)

    def __str__(self):
        return self.title
