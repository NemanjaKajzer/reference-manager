
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

from .forms import CreateUserForm

BIB_FILE = '../references.bib'

@permission_classes((AllowAny,))
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    



class ReferenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows references to be viewed or edited.
    """
    queryset = Reference.objects.all().order_by('-id')
    # serializer_class = ReferenceSerializer



def registerPage(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('upload')
    else:
        if (request.method == 'POST'):
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

    context = {'form' :form}
    return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('upload')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('upload')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')



@login_required(login_url='login')
def upload(request):
    context = {}
    pp = pprint.PrettyPrinter(indent=4)   
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        pp.pprint(uploaded_file.name)
        pp.pprint(uploaded_file.size)
        bibfile = metamodel_for_language('bibtex').model_from_file('C:\\Users\\Korisnik\\Desktop\\Diplomski\\sladic.bib')
        # bibfile = metamodel_for_language('bibtex').model_from_file(uploaded_file.file..getvalue())

        pp.pprint(uploaded_file.name)
        for e in bibfile.entries:
             if e.__class__.__name__ == 'BibRefEntry':
                
                author_field = get_field(e, 'author')
                journal_field = get_field(e, 'journal')
                localfile_field = get_field(e, 'localfile')
                pages_field = get_field(e, 'pages')
                publisher_field = get_field(e, 'publisher')
                title_field = get_field(e, 'title')
                doi_field = get_field(e, 'doi')
                volume_field = get_field(e, 'volume')
                year_field = get_field(e, 'year')
                rank_field = get_field(e, 'rank')
                project_field = get_field(e, 'project')
                pages_field = get_field(e, 'pages')

                booktitle_field = get_field(e, 'booktitle')
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

                #techreport
                address_field = get_field(e, 'address')
                institution_field = get_field(e, 'institution')

                try:
                    author_value = author_field.value
                except:
                    author_value = ""
                try:    
                    journal_value = journal_field.value
                except:
                    journal_value = ""
                try:
                    localfile_value = localfile_field.value
                except:
                    localfile_value = ""
                try:
                    pages_value = pages_field.value
                except:
                    pages_value = ""
                try:
                    publisher_value = publisher_field.value
                except:
                    publisher_value = ""
                try:
                    title_value = title_field.value
                except:
                    title_value = ""
                try:
                    doi_value = doi_field.value
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
                    rank_value = rank_field.value
                except:
                    rank_value = ""
                try:
                    project_value = project_field.value
                except:
                    project_value = ""
                try:
                    pages_value = pages_field.value
                except:
                    pages_value = ""

                try:
                    booktitle_value = booktitle_field.value
                except:
                    booktitle_value = ""
                try:
                    editor_value = editor_field.value
                except:
                    editor_value = ""
                try:
                    isbn_value = isbn_field.value
                except:
                    isbn_value = ""
                try:
                    month_value = month_field.value
                except:
                    month_value = ""
                try:
                    issn_value = issn_field.value
                except:
                    issn_value = ""
                try:
                    keywords_value = keywords_field.value
                except:
                    keywords_value = ""
                try:
                    url_value = url_field.value
                except:
                    url_value = ""
                try:
                    location_value = location_field.value
                except:
                    location_value = ""
                try:
                    number_value = number_field.value
                except:
                    number_value = 0
                try:
                    eprint_value = eprint_field.value
                except:
                    eprint_value = ""
                try:
                    file_value = file_field.value
                except:
                    file_value = ""
                try:
                    comment_value = comment_field.value
                except:
                    comment_value = ""
                try:
                    note_value = note_field.value
                except:
                    note_value = ""
                try:
                    owner_value = owner_field.value
                except:
                    owner_value = ""
                try:
                    series_value = series_field.value
                except:
                    series_value = ""
                try:
                    eid_value = eid_field.value
                except:
                    eid_value = ""
                try:
                    address_value = address_field.value
                except:
                    address_value = ""
                try:
                    institution_value = institution_field.value
                except:
                    institution_value = ""
                
                #list of authors
                authors = get_authors(author_field)

                pp.pprint(authors)
                pp.pprint(author_value)
                
                pp.pprint("                   ")



    return render(request, 'upload.html')    

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

def get_authors(f):
    astr = f.value
    if 'and ' in astr:
        astr = astr.split('and ')
    if ',' in astr:
        astr = astr.split(',')
    return astr


def to_key(k):
    nonkeychars = re.compile('[^a-zA-Z0-9]')
    k = unidecode.unidecode(k.strip().lower())
    k = nonkeychars.sub('', k)
    return k