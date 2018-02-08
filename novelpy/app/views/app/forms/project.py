from django import forms
from novelpy.app.models import Project


class ProjectCreateForm(forms.Form):
    name = forms.CharField(label='Project name', max_length=200, widget=forms.TextInput(
        attrs={'size': 80, 'class': 'form-control text-field'}))

    class Meta:
        model = Project
        fields = ("name", )
