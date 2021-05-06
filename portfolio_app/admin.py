from django.contrib import admin
from .models import ProjectModel, ContactModel
# Register your models here.
admin.site.register(ProjectModel)
admin.site.register(ContactModel)