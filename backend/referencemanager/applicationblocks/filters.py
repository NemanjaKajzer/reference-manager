import django_filters
from django_filters import NumberFilter
from django_filters import CharFilter
from django_filters import ModelChoiceFilter
from django import forms
from .models import *

class TeamFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Name: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    user = ModelChoiceFilter(field_name='user', queryset=User.objects.all(), label='User: ', widget=forms.Select(attrs={'class': 'filter-field'}))
    class Meta:
        model = Team
        fields = ''

class RankFilter(django_filters.FilterSet):
    code = CharFilter(field_name='code', lookup_expr='icontains', label='Code: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    class Meta:
        model = Rank
        fields = ''

class UserFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains', label='First Name: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains', label='Username: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    username = CharFilter(field_name='username', lookup_expr='icontains', label='Username: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    email = CharFilter(field_name='email', lookup_expr='icontains', label='E-mail: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    class Meta:
        model = User
        fields = ''

class ProjectFilter(django_filters.FilterSet):
    code = CharFilter(field_name='code', lookup_expr='icontains', label='Code: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    team = ModelChoiceFilter(field_name='team', queryset=Team.objects.all(), label='Team: ', widget=forms.Select(attrs={'class': 'filter-field'}))

    class Meta:
        model = Project
        fields = ''

class ReferenceFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    isbn = CharFilter(field_name='isbn', lookup_expr='icontains', label='ISBN: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    issn = CharFilter(field_name='issn', lookup_expr='icontains', label='ISSN: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    doi = CharFilter(field_name='doi', lookup_expr='icontains', label='DOI: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    rank = ModelChoiceFilter(field_name='rank', queryset=Rank.objects.all(), label='Rank: ', widget=forms.Select(attrs={'class': 'filter-field'}))
    author = ModelChoiceFilter(field_name='author', queryset=User.objects.all(), label='User: ', widget=forms.Select(attrs={'class': 'filter-field'}))
    team = ModelChoiceFilter(field_name='team', queryset=Team.objects.all(), label='Team: ', widget=forms.Select(attrs={'class': 'filter-field'}))
    project = ModelChoiceFilter(field_name='project', queryset=Project.objects.all(), label='Project: ', widget=forms.Select(attrs={'class': 'filter-field'}))
    startYear = NumberFilter(field_name='year', lookup_expr='gte', widget=forms.NumberInput(attrs={'class': 'filter-field'}))
    endYear = NumberFilter(field_name='year', lookup_expr='lte', widget=forms.NumberInput(attrs={'class': 'filter-field'}))

    class Meta:
        model = Reference
        fields = ''

class ReferenceByUserFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    project = ModelChoiceFilter(field_name='project', queryset=Project.objects.all(), label='Project: ', widget=forms.Select(attrs={'class': 'filter-field'}))
    startYear = NumberFilter(field_name='year', lookup_expr='gte', widget=forms.NumberInput(attrs={'class': 'filter-field'}))
    endYear = NumberFilter(field_name='year', lookup_expr='lte', widget=forms.NumberInput(attrs={'class': 'filter-field'}))

    class Meta:
        model = Reference
        fields = ''

class ReferenceByTeamFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    project = ModelChoiceFilter(field_name='project', queryset=Project.objects.all(), label='Project: ', widget=forms.Select(attrs={'class': 'filter-field'}))
    startYear = NumberFilter(field_name='year', lookup_expr='gte', label='From year: ', widget=forms.NumberInput(attrs={'class': 'filter-field'}))
    endYear = NumberFilter(field_name='year', lookup_expr='lte', label='To year: ', widget=forms.NumberInput(attrs={'class': 'filter-field'}))
    class Meta:
        model = Reference
        fields = ''

class ReferenceByProjectFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    user = ModelChoiceFilter(field_name='author', queryset=User.objects.all(), label='User: ', widget=forms.Select(attrs={'class': 'filter-field'}))
    startYear = NumberFilter(field_name='year', lookup_expr='gte', label='From year: ', widget=forms.NumberInput(attrs={'class': 'filter-field'}))
    endYear = NumberFilter(field_name='year', lookup_expr='lte', label='To year: ', widget=forms.NumberInput(attrs={'class': 'filter-field'}))
    class Meta:
        model = Reference
        fields = ''

class ReferenceByRankFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title: ', widget=forms.TextInput(attrs={'class': 'filter-field'}))
    project = ModelChoiceFilter(field_name='project', queryset=Project.objects.all(), label='Project: ', widget=forms.Select(attrs={'class': 'filter-field'}))
    user = ModelChoiceFilter(field_name='author', queryset=User.objects.all(), label='User: ', widget=forms.Select(attrs={'class': 'filter-field'}))
    team = ModelChoiceFilter(field_name='team', queryset=Team.objects.all(), label='Team: ', widget=forms.Select(attrs={'class': 'filter-field'}))
    startYear = NumberFilter(field_name='year', lookup_expr='gte', label='From year: ', widget=forms.NumberInput(attrs={'class': 'filter-field'}))
    endYear = NumberFilter(field_name='year', lookup_expr='lte', label='To year: ', widget=forms.NumberInput(attrs={'class': 'filter-field'}))
    class Meta:
        model = Reference
        fields = ''
