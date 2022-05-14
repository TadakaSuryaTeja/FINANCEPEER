from django import forms

from customerapp.models.fileviewer import JSONFile


class JSONUploadForm(forms.ModelForm):
    class Meta:
        model = JSONFile
        fields = ['file']