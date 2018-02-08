from novelpy.app.views.app.input_base import view_input_base
from novelpy.app.models import Note
from novelpy.app.views.app.forms import NoteCreateForm


def view(request, username, codename):
    return view_input_base(request=request, username=username, codename=codename, model=Note,
                           modelform=NoteCreateForm, existing_id=None)


def view_existing(request, username, codename, existing_id):
    return view_input_base(request=request, username=username, codename=codename, model=Note,
                           modelform=NoteCreateForm, existing_id=existing_id)
