from django.contrib import admin
from .models import School

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    pass

admin.site.register(School, SchoolAdmin)