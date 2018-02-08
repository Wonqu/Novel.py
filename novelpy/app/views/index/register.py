from django.shortcuts import render
from django.http import HttpResponseRedirect
from novelpy.app.views.index.forms.register import UserCreateForm as RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from novelpy.app.text import messages as msg
from novelpy.app.views.app import dashboard
from django.urls import reverse


def view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, msg.message_register_success)
                return HttpResponseRedirect(reverse(dashboard, kwargs={'username': user.username}))
            return HttpResponseRedirect('/app/')
    else:
        form = RegisterForm()
    return render(request, "userform.html", {'form': form})
