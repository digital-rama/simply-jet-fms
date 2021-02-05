from file.models import UploadGroup, UploadedFile
from django.contrib import admin

# Register your models here.

admin.site.register(UploadedFile)
admin.site.register(UploadGroup)
