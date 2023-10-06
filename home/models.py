from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    place = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/', default=None)
    time = models.TimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.title
    

class Donation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.amount}'
