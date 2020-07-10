from django.db import models

class Reference(models.Model):
    title = models.CharField(max_length=32)
    someNumber = models.IntegerField()
