from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=40, default='firstname')
    last_name = models.CharField(max_length=40, default='lastname')

class Editor(models.Model):
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length=40, default='')

class Team(models.Model):
    author = models.ManyToManyField(Author)

class Project(models.Model):
    team = models.ManyToManyField(Team)
    code = models.CharField(unique=True, max_length=40)

class Rank(models.Model):
    code = models.CharField(unique=True, max_length=40)

class Reference(models.Model):
    author = models.ManyToManyField(Author, related_name='author_id', related_query_name='author_id')
    editor = models.ManyToManyField(Editor, related_name='editor_id', related_query_name='editor_id')
    book_title = models.CharField(max_length=80, default='title')
    publisher = models.CharField(max_length=40, default='publisher')
    month = models.CharField(max_length=12, default='month')
    journal = models.CharField(max_length=40, default='journal')
    year = models.IntegerField(default=2020)
    volume = models.IntegerField(default=1)
    isbn = models.CharField(unique=True, max_length=40, default='isbn')

