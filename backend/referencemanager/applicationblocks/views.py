from rest_framework import viewsets
from referencemanager.applicationblocks.serializers import UserSerializer, ReferenceSerializer
from .models import Reference

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect

from textx import metamodel_for_language
from txbibtex import bibfile_str

import unidecode
import re
import pprint

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import Team, Rank, Reference, Project
from .forms import CreateUserForm
from .filters import TeamFilter, ProjectFilter, ReferenceByProjectFilter, ReferenceByRankFilter, ReferenceByTeamFilter, \
    ReferenceByUserFilter, ReferenceFilter, RankFilter
from temp import tempfile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
import time
from .decorators import *


# region Deletion
@login_required(login_url='login')
@is_admin
def deleteRank(request, pk):
    rank = Rank.objects.get(id=pk)
    rank.delete()

    return redirect('/refmng/ranks/')

@login_required(login_url='login')
@belongs_to_user
def deleteTeam(request, pk):
    team = Team.objects.get(id=pk)
    team.delete()

    return redirect('/refmng/teams/')

@login_required(login_url='login')
@belongs_to_user
def deleteReference(request, pk):
    reference = Reference.objects.get(id=pk)
    reference.delete()

    return redirect('/refmng/references/')

@login_required(login_url='login')
@belongs_to_user
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()

    return redirect('/refmng/projects/')


# endregion Deletion

# region Creation and preview pages

@login_required(login_url='login')
def teamCreationPage(request):
    teams = Team.objects.all()
    users = User.objects.all()

    teamFilter = TeamFilter(request.GET, queryset=teams)
    teams = teamFilter.qs

    pp = pprint.PrettyPrinter(indent=4)
    if (request.method == "POST"):
        if request.POST.get("Create"):
            teamName = request.POST.get("teamName")
            team = Team.objects.create(name=teamName)
            for user in users:
                if request.POST.get("c" + str(user.id)) == "clicked":
                    team.user.add(user)

    users = users.order_by('last_name')
    return render(request, 'teams.html', {"users": users, "teams": teams, "teamFilter": teamFilter})


@login_required(login_url='login')
def projectCreationPage(request):
    projects = Project.objects.all()
    teams = Team.objects.all()

    projectFilter = ProjectFilter(request.GET, queryset=projects)
    projects = projectFilter.qs

    pp = pprint.PrettyPrinter(indent=4)
    if (request.method == "POST"):
        if request.POST.get("Create"):
            projectCode = request.POST.get("projectCode")
            projectTitle = request.POST.get("projectTitle")
            project = Project.objects.create(code=projectCode, title=projectTitle)
            for team in teams:
                if request.POST.get("c" + str(team.id)) == "clicked":
                    project.team.add(team)

    return render(request, 'projects.html', {"projects": projects, "teams": teams, "projectFilter": projectFilter})


@login_required(login_url='login')
def rankCreationPage(request):
    ranks = Rank.objects.all()
    rankFilter = RankFilter(request.GET, queryset=ranks)
    ranks = rankFilter.qs
    pp = pprint.PrettyPrinter(indent=4)
    if (request.method == "POST"):
        if request.POST.get("Create"):
            rankCode = request.POST.get("rankCode")
            Rank.objects.create(code=rankCode)

    return render(request, 'ranks.html', {"ranks": ranks, "rankFilter": rankFilter})


# endregion Creation and preview pages

# region Profile pages

@login_required(login_url='login')
def referenceProfilePage(request, pk):
    reference = Reference.objects.get(id=pk)

    return render(request, 'referenceProfile.html', {"reference": reference})


@login_required(login_url='login')
def teamProfilePage(request, pk):
    team = Team.objects.get(id=pk)
    users = team.user.all()

    references = Reference.objects.filter(team=team).all()

    reference_count = len(references)

    referenceFilter = ReferenceByTeamFilter(request.GET, queryset=references)
    references = referenceFilter.qs

    return render(request, 'teamProfile.html',
                  {"users": users, "team": team, "references": references, "reference_count": reference_count,
                   "referenceFilter": referenceFilter})


@login_required(login_url='login')
def rankProfilePage(request, pk):
    rank = Rank.objects.get(id=pk)

    references = Reference.objects.filter(rank=rank).all()

    reference_count = len(references)

    referenceFilter = ReferenceByRankFilter(request.GET, queryset=references)
    references = referenceFilter.qs

    return render(request, 'rankProfile.html',
                  {"rank": rank, "references": references, "reference_count": reference_count,
                   "referenceFilter": referenceFilter})


@login_required(login_url='login')
def userProfilePage(request, pk):
    pp = pprint.PrettyPrinter(indent=4)
    user = User.objects.get(id=pk)
    allTeams = Team.objects.all()
    teams = []
    references = []
    for team in allTeams:
        if user in team.user.all():
            teams.append(team)

    for reference in Reference.objects.all():
        if user in reference.author.all():
            references.append(reference)

    referenceFilter = ReferenceByTeamFilter(request.GET, queryset=Reference.objects.filter(
        author__username__icontains=user.username))
    references = referenceFilter.qs

    reference_count = len(references)

    return render(request, 'userProfile.html',
                  {"user": user, "teams": teams, "references": references, "reference_count": reference_count,
                   "referenceFilter": referenceFilter})


@login_required(login_url='login')
def projectProfilePage(request, pk):
    project = Project.objects.get(id=pk)
    teams = project.team.all()
    references = []

    referenceFilter = ReferenceByProjectFilter(request.GET, queryset=Reference.objects.filter(project=project))
    references = referenceFilter.qs

    reference_count = len(references)

    authorized = False

    for team in teams:
        if request.user in team.user.all():
            authorized = True
            break

    return render(request, 'projectProfile.html',
                  {"project": project, "teams": teams, "references": references, "reference_count": reference_count,
                   "referenceFilter": referenceFilter, "authorized": authorized})


# endregion Profile pages

# region Registration and authentication


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if (request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('references')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


def forbidden(request):
    return render(request, 'forbidden.html')
# endregion Registration and authentication

# region References upload

@login_required(login_url='login')
def referenceCreationPage(request):
    context = {}
    pp = pprint.PrettyPrinter(indent=4)

    references = Reference.objects.all()
    reference_count = len(references)
    referenceFilter = ReferenceFilter(request.GET, queryset=references)
    references = referenceFilter.qs

    successful = 0
    unsuccessful = 0
    success_message = ''
    error_message = ''

    if request.method == 'POST':

        #region Uploaded File Processing
        uploaded_file = request.FILES['document']

        path = default_storage.save('tmp/references.bib', ContentFile(uploaded_file.read()))
        path_to_file = default_storage.open(r'tmp\references.bib').name

        bibfile = metamodel_for_language('bibtex').model_from_file(path_to_file)
        #endregion Uploaded File Processing

        #region Entries Processing
        for e in bibfile.entries:
            if e.__class__.__name__ == 'BibRefEntry':

                #fields = get_fields(e)
                key = e.key
                type = e.type


                # region Field Assigning
                author_field = get_field(e, 'author')
                journal_field = get_field(e, 'journal')
                localfile_field = get_field(e, 'localfile')
                pages_field = get_field(e, 'pages')
                publisher_field = get_field(e, 'publisher')
                title_field = get_field(e, 'title')
                booktitle_field = get_field(e, 'booktitle')
                doi_field = get_field(e, 'doi')
                volume_field = get_field(e, 'volume')
                year_field = get_field(e, 'year')
                rank_field = get_field(e, 'rank')
                project_field = get_field(e, 'project')
                pages_field = get_field(e, 'pages')

                editor_field = get_field(e, 'editor')
                isbn_field = get_field(e, 'isbn')
                month_field = get_field(e, 'month')

                issn_field = get_field(e, 'issn')
                keywords_field = get_field(e, 'keywords')
                url_field = get_field(e, 'url')

                location_field = get_field(e, 'location')
                number_field = get_field(e, 'number')
                eprint_field = get_field(e, 'eprint')

                file_field = get_field(e, 'file')
                comment_field = get_field(e, 'comment')
                note_field = get_field(e, 'note')

                owner_field = get_field(e, 'owner')
                series_field = get_field(e, 'series')
                eid_field = get_field(e, 'eid')

                address_field = get_field(e, 'address')
                institution_field = get_field(e, 'institution')
                # endregion Field Assigning

                # region Value Assigning
                try:
                    author_value = author_field.value.lstrip().rstrip()
                except:
                    author_value = ""
                try:
                    journal_value = journal_field.value.lstrip().rstrip()
                except:
                    journal_value = ""
                try:
                    localfile_value = localfile_field.value.lstrip().rstrip()
                except:
                    localfile_value = ""
                try:
                    pages_value = pages_field.value.lstrip().rstrip()
                except:
                    pages_value = ""
                try:
                    publisher_value = publisher_field.value.lstrip().rstrip()
                except:
                    publisher_value = ""
                try:
                    title_value = title_field.value.lstrip().rstrip()
                except:
                    title_value = ""
                try:
                    doi_value = doi_field.value.lstrip().rstrip()
                except:
                    doi_value = ""
                try:
                    volume_value = volume_field.value
                except:
                    volume_value = 0
                try:
                    year_value = year_field.value
                except:
                    year_value = 0
                try:
                    rank_value = rank_field.value.lstrip().rstrip()
                except:
                    rank_value = ""
                try:
                    project_value = project_field.value.lstrip().rstrip()
                except:
                    project_value = ""
                try:
                    pages_value = pages_field.value.lstrip().rstrip()
                except:
                    pages_value = ""

                try:
                    booktitle_value = booktitle_field.value.lstrip().rstrip()
                except:
                    booktitle_value = ""
                try:
                    editor_value = editor_field.value.lstrip().rstrip()
                except:
                    editor_value = ""
                try:
                    isbn_value = isbn_field.value.lstrip().rstrip()
                except:
                    isbn_value = ""
                try:
                    month_value = month_field.value.lstrip().rstrip()
                except:
                    month_value = ""
                try:
                    issn_value = issn_field.value.lstrip().rstrip()
                except:
                    issn_value = ""
                try:
                    keywords_value = keywords_field.value.lstrip().rstrip()
                except:
                    keywords_value = ""
                try:
                    url_value = url_field.value.lstrip().rstrip()
                except:
                    url_value = ""
                try:
                    location_value = location_field.value.lstrip().rstrip()
                except:
                    location_value = ""
                try:
                    number_value = number_field.value
                except:
                    number_value = 0
                try:
                    eprint_value = eprint_field.value.lstrip().rstrip()
                except:
                    eprint_value = ""
                try:
                    file_value = file_field.value.lstrip().rstrip()
                except:
                    file_value = ""
                try:
                    comment_value = comment_field.value.lstrip().rstrip()
                except:
                    comment_value = ""
                try:
                    note_value = note_field.value.lstrip().rstrip()
                except:
                    note_value = ""
                try:
                    owner_value = owner_field.value.lstrip().rstrip()
                except:
                    owner_value = ""
                try:
                    series_value = series_field.value.lstrip().rstrip()
                except:
                    series_value = ""
                try:
                    eid_value = eid_field.value.lstrip().rstrip()
                except:
                    eid_value = ""
                try:
                    address_value = address_field.value.lstrip().rstrip()
                except:
                    address_value = ""
                try:
                    institution_value = institution_field.value.lstrip().rstrip()
                except:
                    institution_value = ""

                # endregion Value Assigning

                # region Authors Processing
                # gets list of authors (strings)
                authors = get_users(author_field)
                # trims all strings in a list and writes them to a new list (can't change strings)
                resulting_authors = trim_all_strings(authors)
                # finds user objects that have the same combination of first name and last name
                authors_objects = get_user_objects(resulting_authors)
                # endregion Authors Processing

                # region Duplicate Checking
                # if reference entry is a duplicate, then move on to the next entry
                if check_if_duplicate(isbn_value, issn_value, doi_value, authors_objects, title_value) is True:
                    unsuccessful = unsuccessful + 1
                    continue
                # endregion Duplicate Checking

                # region Editors Processing
                # gets list of editors (strings)
                try:
                    editors = get_users(editor_field)
                except:
                    editors = ''

                # trims all strings in a list and writes them to a new list (can't change strings)
                resulting_editors = trim_all_strings(editors)
                # finds user objects that have the same combination of first name and last name
                editors_objects = get_user_objects(resulting_editors)
                # endregion Editors Processing

                # region Rank Processing
                rank = get_rank_object(rank_value)
                # endregion Rank Processing

                # region Team Processing
                team = get_team_object(authors_objects)
                # endregion Team Processing

                # region Project Processing
                project = get_project_object(project_value)
                # endregion Project Processing

                # region Reference Saving
                reference = Reference.objects.create(team=team, project=project, rank=rank, title = title_value, booktitle=booktitle_value,
                                                     publisher=publisher_value, month=month_value, journal=journal_value,
                                                     year=year_value, volume=volume_value,
                                                     isbn=isbn_value, issn=issn_value, doi=doi_value,
                                                     local_file=localfile_value, file=file_value, url=url_value,
                                                     pages=pages_value,
                                                     keywords=keywords_value, location=location_value, number=number_value,
                                                     eprint=eprint_value, comment=comment_value, note=note_value,
                                                     owner=owner_value, series=series_value, eid=eid_value,
                                                     address=address_value, institution=institution_value, key=key, type=type)
                successful = successful + 1
                for author_object in authors_objects:
                    reference.author.add(author_object)

                for editor_object in editors_objects:
                    reference.editor.add(editor_object)
                # endregion Reference Saving

                reference_count = len(Reference.objects.all())


        #endregion Entries Processing

        time.sleep(2)
        path = default_storage.delete(r'tmp\references.bib')

        #region Messages
        if successful > 0:
            if successful == 1:
                success_message = 'Successfully uploaded ' + str(successful) + ' reference.'
            else:
                success_message = 'Successfully uploaded ' + str(successful) + ' references.'
        if unsuccessful > 0:
            if unsuccessful == 1:
                error_message = 'Skipped ' + str(unsuccessful) + ' reference.'
            else:
                error_message = 'Skipped ' + str(unsuccessful) + ' references.'
        #endregion Messages

        return render(request, 'references.html',
                      {"references": references, "referenceFilter": referenceFilter, "reference_count": reference_count,
                       "success_message": success_message, "error_message": error_message})

    reference_count = len(references)
    references = references.order_by('year')
    return render(request, 'references.html',
                  {"references": references, "referenceFilter": referenceFilter, "reference_count": reference_count})



def get_fields(e):
    fields = [f for f in e.fields]
    if fields:
        return fields

# make new list with trimmed names of authors
def trim_all_strings(strings):
    resulting_authors = []
    for author in strings:
        author_without_space = author.lstrip().rstrip()
        resulting_authors.append(author_without_space)

    return resulting_authors


# get list of user objects from names in bib file
def get_user_objects(names):
    authors_objects = []
    for res_author in names:
        for db_author in User.objects.all():
            if res_author.lower() == (db_author.first_name + ' ' + db_author.last_name).lower():
                authors_objects.append(db_author)

    return authors_objects


# get rank object from code in bib file
def get_rank_object(rank_name):
    for db_rank in Rank.objects.all():
        if rank_name.lower() == db_rank.code.lower():
            return db_rank

    return None


# get team object from authors in bib file
def get_team_object(authors_objects):
    for db_team in Team.objects.all():
        if set(authors_objects) == set(db_team.user.all()):
            return db_team
    return None


# get project object from code in bib file
def get_project_object(project_code):
    for db_project in Project.objects.all():
        if project_code == db_project.code:
            return db_project

    return None


def check_if_duplicate(isbn, issn, doi, authors, title):
    # check if reference with the same isbn, issn or doi already exists
    pp = pprint.PrettyPrinter(indent=4)
    for db_reference in Reference.objects.all():
        # pp.pprint(isbn.lower().lstrip().rstrip() + ' ' + db_reference.isbn.lower().lstrip().rstrip())
        # pp.pprint(doi.lower().lstrip().rstrip() + ' ' + db_reference.doi.lower().lstrip().rstrip())
        # pp.pprint(issn.lower().lstrip().rstrip() + ' ' + db_reference.issn.lower().lstrip().rstrip())
        if isbn.lower().lstrip().rstrip() == db_reference.isbn.lower().lstrip().rstrip():
            if (isbn != ''):
                return True
        if issn.lower().lstrip().rstrip() == db_reference.issn.lower().lstrip().rstrip():
            if (issn != ''):
                return True
        if doi.lower().lstrip().rstrip() == db_reference.doi.lower().lstrip().rstrip():
            if (doi != ''):
                return True

        # check if reference with the same authors and title exists
        if list(authors) == list(db_reference.author.all()) and title.lower() == db_reference.title.lower():
            return True

    return False


def get_field(e, name):
    fields = [f for f in e.fields if f.name == name]
    if fields:
        return fields[0]


def get_author(f):
    astr = f.value
    if ' and ' in astr:
        astr = astr.split(' and ')[0]
    if ',' in astr:
        astr = astr.split(',')[0]
        astr = astr.replace(' ', '')
    return to_key(astr.split()[0])


def get_users(f):
    result = []
    astr = f.value
    if 'and ' in astr:
        astr = astr.split('and ')
        result = astr
    else:
        result.append(astr)

    return result


def to_key(k):
    nonkeychars = re.compile('[^a-zA-Z0-9]')
    k = unidecode.unidecode(k.strip().lower())
    k = nonkeychars.sub('', k)
    return k

# endregion References upload
