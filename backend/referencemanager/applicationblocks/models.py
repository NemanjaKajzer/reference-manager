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
        return '{} - {}'.format(self.code, self.title)


class Rank(models.Model):
    code = models.CharField(unique=True, max_length=90)

    def __str__(self):
        return '{}'.format(self.code)


class Reference(models.Model):
    authors = models.ManyToManyField(User, related_name='user_id', related_query_name='user_id')
    team = models.ForeignKey(Team, null=True, related_name='team_id', related_query_name='team_id',
                             on_delete=models.SET_NULL, default=None)
    project = models.ForeignKey(Project, null=True, related_name='project_id', related_query_name='project_id',
                                on_delete=models.SET_NULL, default=None)
    rank = models.ForeignKey(Rank, null=True, related_name='rank_id', related_query_name='rank_id',
                             on_delete=models.SET_NULL, default=None)
    editor = models.ManyToManyField(User, related_name='editor_id', related_query_name='editor_id', default=None)
    book_title = models.CharField(max_length=180, default='title')
    publisher = models.CharField(max_length=190, default='publisher')
    month = models.CharField(max_length=12, default='month')
    journal = models.CharField(max_length=190, default='journal')
    year = models.IntegerField(default=2020)
    volume = models.CharField(max_length=20, default='volume')
    isbn = models.CharField(max_length=90, default='isbn')
    issn = models.CharField(max_length=90, default='issn')
    doi = models.CharField(max_length=90, default='doi')

    local_file = models.CharField(max_length=290, default='local_file')
    file = models.CharField(max_length=290, default='file')
    url = models.CharField(max_length=290, default='url')
    pages = models.CharField(max_length=90, default='pages')
    keywords = models.CharField(max_length=390, default='keywords')
    location = models.CharField(max_length=160, default='location')
    number = models.IntegerField(default=1)
    eprint = models.CharField(max_length=90, default='eprint')

    comment = models.CharField(max_length=90, default='comment')
    note = models.CharField(max_length=390, default='note')
    owner = models.CharField(max_length=90, default='owner')
    series = models.CharField(max_length=360, default='series')
    eid = models.CharField(max_length=90, default='eid')
    address = models.CharField(max_length=180, default='address')
    institution = models.CharField(max_length=200, default='institution')

    def __str__(self):
        return '{}'.format(self.book_title)
