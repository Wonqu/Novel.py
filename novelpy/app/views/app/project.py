from django.shortcuts import render
from django.http import HttpResponseRedirect
from novelpy.app.models import Project, User
from novelpy.app.views.util import projects, notes, basic


def view(request, username, codename):
    if request.user.is_authenticated:
        u = User.objects.get(username=username)
        p = Project.objects.get(owner=u.id, codename=codename)
        data = basic(u.id)
        data = projects(data, u.id)
        data = notes(data, p.id, name=None)
        data['project'] = p
        return render(request, 'projectboard.html', data)
    else:
        return HttpResponseRedirect('/app/')
