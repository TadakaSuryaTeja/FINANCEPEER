from django.contrib import admin

# Register your models here.
from customerapp.models.fileviewer import JSONFile

admin.site.register(JSONFile)
