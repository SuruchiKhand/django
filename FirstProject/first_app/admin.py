from django.contrib import admin
from .models import Students
# Register your models here.
# admin.site.register(Students)

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_number', 'address']