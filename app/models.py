from django.db import models

class Tweet(models.Model):
    message = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)