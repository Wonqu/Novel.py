from django.shortcuts import render
from django.http import HttpResponseRedirect
from novelpy.app.models import User
from novelpy.app.views.util import projects


def view(request, username):
    if request.user.is_authenticated:
        u = User.objects.get(username=username)
        data = {}
        data = projects(data, u.id)
        data['username'] = username
        return render(request, 'dashboard.html', data)
    else:
        return HttpResponseRedirect('/app/')
