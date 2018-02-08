from django.shortcuts import render
from django.http import HttpResponseRedirect
from novelpy.app.views.index.forms.login import LoginForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages
from novelpy.app.text import messages as msg
from django.urls import reverse
from novelpy.app.views.app import dashboard


def view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                django_login(request, user)
                messages.add_message(request, messages.SUCCESS, msg.message_login_success)
                return HttpResponseRedirect(reverse(dashboard, kwargs={'username': user.username}))
            else:
                messages.add_message(request, messages.ERROR, msg.message_login_error)
                return render(request, "userform.html", {'form': form})
        form = LoginForm()
    return render(request, "userform.html", {'form': form})
