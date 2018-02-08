from django import forms
from novelpy.app.models import Note


class NoteCreateForm(forms.Form):
    name = forms.CharField(label='Title', max_length=200, widget=forms.TextInput(
        attrs={'size': 80, 'class': 'form-control text-field'}))
    description = forms.CharField(label='Note', widget=forms.Textarea(
        attrs={'cols': 150, 'rows': 35, 'class': 'form-control text-field'}))
    project = forms.IntegerField(label='Project ID', widget=forms.HiddenInput())

    class Meta:
        model = Note
        fields = ("name", "project")
