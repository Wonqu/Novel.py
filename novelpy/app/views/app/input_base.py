from django.shortcuts import render
from django.http import HttpResponseRedirect
from novelpy.app.models import Project, User
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib import messages
from novelpy.app.views.util import basic


def view_input_base(request, username, codename, model, modelform, existing_id):
    if request.user.is_authenticated:
        user_id = User.objects.get(username__exact=username).id
        project = Project.objects.get(owner__exact=user_id, codename__exact=codename)
        project_id = project.id
        clean_form = modelform(initial={'project': project_id})
        clean_form.fields['project'].widget.attrs['readonly'] = True
        clean_form.fields['name'].widget.attrs['autofocus'] = True
        data = basic(user_id)
        data['project'] = project
        data['form'] = clean_form
        if request.method == 'POST':
            form = modelform(request.POST)
            if form.is_valid():
                try:
                    name = request.POST.get('name', '')
                    description = request.POST.get('description', '')
                    print(name, description)
                    if existing_id:
                        model.objects.filter(id=existing_id).update(name=name, description=description)
                    else:
                        new_object = model(project=project, name=name, description=description)
                        new_object.save()
                except ObjectDoesNotExist:
                    pass
        else:
            if existing_id:
                try:
                    #eo == existing object
                    eo = model.objects.get(project=project, id=existing_id)
                    existing_data = {
                        'name': eo.name,
                        'project': eo.project.id,
                        'description': eo.description
                    }
                    data['form'] = modelform(existing_data)
                except ObjectDoesNotExist:
                    pass
            else:
                pass
        return render(request, 'inputform.html', data)
    else:
        return HttpResponseRedirect('/app/')
