from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


def get_name(self):
    return self.first_name + ' ' + self.last_name


User.add_to_class("__str__", get_name)


class Editor(models.Model):
    first_name = models.CharField(max_length=90, default='')
    last_name = models.CharField(max_length=90, default='')


class Team(models.Model):
    name = models.CharField(unique=True, max_length=50, default='')
    user = models.ManyToManyField(User)

    def __str__(self):
        return '{}'.format(self.name)


class Project(models.Model):
    team = models.ManyToManyField(Team)
    code = models.CharField(unique=True, max_length=90)
    title = models.CharField(max_length=50, default='')

    def __str__(self):
        title_to_show = ''
        if len(self.title) > 12:
            title_to_show = self.title[0:11]
            return '{} - {}...'.format(self.code, title_to_show)
        return '{} - {}'.format(self.code, self.title)

class Rank(models.Model):
    code = models.CharField(unique=True, max_length=90)

    def __str__(self):
        return '{}'.format(self.code)

class ReferenceAttribute(models.Model):
    name = models.CharField(max_length=200, default='key')
    value = models.CharField(max_length=800, default='value')

class Reference(models.Model):
    title = models.CharField(max_length=180, default='title')
    author = models.ManyToManyField(User, related_name='user_id', related_query_name='user_id')
    team = models.ForeignKey(Team, null=True, related_name='team_id', related_query_name='team_id',
                             on_delete=models.SET_NULL, default=None)
    project = models.ForeignKey(Project, null=True, related_name='project_id', related_query_name='project_id',
                                on_delete=models.SET_NULL, default=None)
    rank = models.ForeignKey(Rank, null=True, related_name='rank_id', related_query_name='rank_id',
                             on_delete=models.SET_NULL, default=None)
    year = models.IntegerField(default=2020)
    isbn = models.CharField(max_length=90, default='isbn')
    issn = models.CharField(max_length=90, default='issn')
    doi = models.CharField(max_length=90, default='doi')
    editor = models.ManyToManyField(User, related_name='editor_id', related_query_name='editor_id', default=None)
    key = models.CharField(max_length=20, default='key')
    type = models.CharField(max_length=30, default='type')
    attributes = models.ManyToManyField(ReferenceAttribute, related_name='editor_id', related_query_name='editor_id', default=None)

    def __str__(self):
        return '{}'.format(self.title)




