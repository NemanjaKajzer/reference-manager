from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class Editor(models.Model):
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length=40, default='')

class Team(models.Model):
    name = models.CharField(unique=True, max_length=50, default='')
    user = models.ManyToManyField(User)

class Project(models.Model):
    team = models.ManyToManyField(Team)
    code = models.CharField(unique=True, max_length=40)

class Rank(models.Model):
    code = models.CharField(unique=True, max_length=40)

class Reference(models.Model):
    uploadedBy = models.ManyToManyField(User, related_name='user_id', related_query_name='user_id')
    editor = models.CharField(unique=True, max_length=300, default='')
    book_title = models.CharField(max_length=80, default='title')
    publisher = models.CharField(max_length=40, default='publisher')
    month = models.CharField(max_length=12, default='month')
    journal = models.CharField(max_length=40, default='journal')
    year = models.IntegerField(default=2020)
    volume = models.IntegerField(default=1)
    isbn = models.CharField(unique=True, max_length=40, default='isbn')

