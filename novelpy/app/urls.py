from django.conf.urls import url
from novelpy.app.views.index import *
from novelpy.app.views.app import *

urlpatterns = [
    # Main page urls
    url(r'^$', index, name='index')
    #, url(r'^about/$', about, name='about')
    #, url(r'contact/^$', contact, name='contact')
    , url(r'^login/$', login, name='login')
    , url(r'^logout/', logout, name='logout')
    , url(r'^register/$', register, name='register')
    # Application urls
    , url(r'^(?P<username>[\w.@+-]+)/$', dashboard, name='dashboard')
    , url(r'^(?P<username>[\w.@+-]+)/new_project/$', input_project, name='new_project')
    , url(r'^(?P<username>[\w.@+-]+)/(?P<codename>[\w\s.@+-]+)/$', project, name='project')
    , url(r'^(?P<username>[\w.@+-]+)/(?P<codename>[\w\s.@+-]+)/note/$', input_note, name='note')
    , url(r'^(?P<username>[\w.@+-]+)/(?P<codename>[\w\s.@+-]+)/notes/$', notes, name='notes')
    , url(r'^(?P<username>[\w.@+-]+)/(?P<codename>[\w\s.@+-]+)/notes_json/$', notes_json, name='notes_json')
    , url(r'^(?P<username>[\w.@+-]+)/(?P<codename>[\w\s.@+-]+)/note/(?P<existing_id>[\w\s.@+-]+)/$', change_note, name='existing_note')
]
