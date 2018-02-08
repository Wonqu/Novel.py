from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from novelpy.app.models import Project, User
from novelpy.app.views.app.forms import ProjectCreateForm
from django.core.exceptions import ObjectDoesNotExist
from novelpy.app.views.util import projects
# from django.contrib import messages
from time import time


def view(request, username):
    if request.user.is_authenticated:
        user = User.objects.get(username__exact=username)
        form = ProjectCreateForm()
        data = {}
        data = projects(data, user.id)
        data['username'] = username
        data['form'] = form
        if request.method == 'GET':
            return render(request, 'inputform.html', data)
        if request.method == 'POST':
            form = ProjectCreateForm(request.POST)
            if form.is_valid():
                try:
                    name = request.POST.get('name', '')
                    codename = str(int(time()))
                    new_object = Project(name=name, owner=user, codename=codename)
                    new_object.save()
                    return HttpResponseRedirect(reverse(viewname='project', kwargs={'username': username,
                                                                                    'codename': codename}))
                except ObjectDoesNotExist:
                    pass
            return HttpResponseRedirect('.')
    else:
        return HttpResponseRedirect('/app/')