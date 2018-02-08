from django.shortcuts import render
from django.http import HttpResponseRedirect
from novelpy.app.models import Project, User
from novelpy.app.views.util import projects, notes
from django.http import JsonResponse


def view(request, username, codename):
    if request.user.is_authenticated:
        data = all_notes(username, codename)
        r = render(request, 'projectboard.html', data)
        return r
    else:
        return HttpResponseRedirect('/app/')


def all_notes(username, codename):
    u = User.objects.get(username=username)
    p = Project.objects.get(owner=u.id, codename=codename)
    data = {}
    data = projects(data, u.id)
    data = notes(data, p.id, name=None)
    data['username'] = username
    data['codename'] = codename
    data['project'] = p
    return data


def notes_json(request, username, codename):
    if request.user.is_authenticated:
        data = all_notes(username, codename)
        return JsonResponse({'notes': list(data['notes'].values('id', 'name', 'description', 'project'))})
    else:
        return JsonResponse({'please': 'log in'})
