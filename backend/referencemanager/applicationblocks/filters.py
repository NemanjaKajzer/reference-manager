import django_filters
from django_filters import NumberFilter
from django_filters import CharFilter
from django_filters import ModelChoiceFilter

from .models import *

class TeamFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Name: ')
    user = ModelChoiceFilter(field_name='user', queryset=User.objects.all(), label='User: ')
    class Meta:
        model = Team
        fields = ''

class RankFilter(django_filters.FilterSet):
    code = CharFilter(field_name='code', lookup_expr='icontains', label='Code: ')
    class Meta:
        model = Rank
        fields = ''

class UserFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains', label='First Name: ')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains', label='Username: ')
    username = CharFilter(field_name='username', lookup_expr='icontains', label='Username: ')
    email = CharFilter(field_name='email', lookup_expr='icontains', label='E-mail: ')
    class Meta:
        model = User
        fields = ''

class ProjectFilter(django_filters.FilterSet):
    code = CharFilter(field_name='code', lookup_expr='icontains', label='Code: ')
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title: ')
    team = ModelChoiceFilter(field_name='team', queryset=Team.objects.all(), label='Team: ')

    class Meta:
        model = Project
        fields = ''

class ReferenceFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title: ')
    isbn = CharFilter(field_name='isbn', lookup_expr='icontains', label='ISBN: ')
    issn = CharFilter(field_name='issn', lookup_expr='icontains', label='ISSN: ')
    doi = CharFilter(field_name='doi', lookup_expr='icontains', label='DOI: ')
    rank = ModelChoiceFilter(field_name='rank', queryset=Rank.objects.all(), label='Rank: ')
    author = ModelChoiceFilter(field_name='author', queryset=User.objects.all(), label='User: ')
    team = ModelChoiceFilter(field_name='team', queryset=Team.objects.all(), label='Team: ')
    project = ModelChoiceFilter(field_name='project', queryset=Project.objects.all(), label='Project: ')
    startYear = NumberFilter(field_name='year', lookup_expr='gte')
    endYear = NumberFilter(field_name='year', lookup_expr='lte')

    class Meta:
        model = Reference
        fields = ''

class ReferenceByUserFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    project = ModelChoiceFilter(field_name='project', queryset=Project.objects.all(), label='Project: ')
    startYear = NumberFilter(field_name='year', lookup_expr='gte')
    endYear = NumberFilter(field_name='year', lookup_expr='lte')

    class Meta:
        model = Reference
        fields = ''

class ReferenceByTeamFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title: ')
    project = ModelChoiceFilter(field_name='project', queryset=Project.objects.all(), label='Project: ')
    startYear = NumberFilter(field_name='year', lookup_expr='gte', label='From year: ')
    endYear = NumberFilter(field_name='year', lookup_expr='lte', label='To year: ')
    class Meta:
        model = Reference
        fields = ''

class ReferenceByProjectFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title: ')
    user = ModelChoiceFilter(field_name='user', queryset=User.objects.all(), label='User: ')
    startYear = NumberFilter(field_name='year', lookup_expr='gte', label='From year: ')
    endYear = NumberFilter(field_name='year', lookup_expr='lte', label='To year: ')
    class Meta:
        model = Reference
        fields = ''

class ReferenceByRankFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title: ')
    project = ModelChoiceFilter(field_name='project', queryset=Project.objects.all(), label='Project: ')
    user = ModelChoiceFilter(field_name='user', queryset=User.objects.all(), label='User: ')
    team = ModelChoiceFilter(field_name='team', queryset=Team.objects.all(), label='Team: ')
    startYear = NumberFilter(field_name='year', lookup_expr='gte', label='From year: ')
    endYear = NumberFilter(field_name='year', lookup_expr='lte', label='To year: ')
    class Meta:
        model = Reference
        fields = ''
