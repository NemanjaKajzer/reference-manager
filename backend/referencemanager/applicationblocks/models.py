from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=40)

class Reference(models.Model):
    title = models.CharField(max_length=32)
    someNumber = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    coauthors = models.ManyToManyField(Author, related_name='coauthor_id', related_query_name='coauthor_id')



