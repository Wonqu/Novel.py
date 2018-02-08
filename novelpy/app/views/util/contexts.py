from novelpy.app.models import User, Project, Note
from django.db.models import Q


def basic(user_id):
    context = dict()
    context['username'] = User.objects.get(id=user_id).username
    context['projects'] = Project.objects.filter(owner_id=user_id)
    return context


def projects(context, user_id):
    """
    Add Projects that meet parameter criteria to the context.
    :param context: Template context (dictionary)
    :param user_id: ID of Projects owner
    :return: new_context with added Projects info from requesting user
    """
    data = Project.objects.filter(owner_id=user_id)
    new_context = context.copy()
    new_context['projects'] = data
    return new_context


def notes(context, project_id, name):
    """
    Add Notes that meet parameter criteria to the context.
    :param context: Template context (dictionary)
    :param project_id: ID of queried novelpy
    :param name: Name of notes to be queried.
    :return:
    """
    query = Q(project_id__exact=project_id)
    if name:
        query &= Q(name__contains=name)
    data = Note.objects.filter(query)
    new_context = context.copy()
    new_context['notes'] = data
    return new_context
