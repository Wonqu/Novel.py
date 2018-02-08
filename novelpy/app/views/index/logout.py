from django.http import HttpResponseRedirect
from django.contrib.auth import logout


def view(request):
    logout(request=request)
    return HttpResponseRedirect(redirect_to='/app/')