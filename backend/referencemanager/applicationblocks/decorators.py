from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('references')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def belongs_to_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        pk = kwargs['pk']
        path = request.path_info

        if 'reference' in path:
            reference = Reference.objects.get(pk=pk)
            if reference is not None:
                if request.user in reference.author.all() or checkIfUserIsAdmin(request.user) is True:
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('forbidden')
            else:
                return redirect('forbidden')
        elif 'project' in path:
            project = Project.objects.get(pk=pk)
            if project is not None:
                for team in project.team.all() or checkIfUserIsAdmin(request.user) is True:
                    if request.user in team.user.all():
                        return view_func(request, *args, **kwargs)
                    else:
                        return redirect('forbidden')
            else:
                return redirect('forbidden')
        elif 'team' in path:
            team = Team.objects.get(pk=pk)
            if team is not None:
                if request.user in team.user.all() or checkIfUserIsAdmin(request.user) is True:
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('forbidden')
            else:
                return redirect('forbidden')
    return wrapper_func

def is_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if checkIfUserIsAdmin(request.user) is True:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('forbidden')
    return  wrapper_func

#region Helper Methods
def checkIfUserIsAdmin(user):
    group = None

    if user.groups.exists():
        group = user.groups.all()[0].name

    if group == 'admin':
        return True

    return False
#endregion Helper Methods