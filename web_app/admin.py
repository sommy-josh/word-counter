from django.contrib import admin

from .models import *

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']
    list_filter = ['name', 'email', 'subject', 'message']
