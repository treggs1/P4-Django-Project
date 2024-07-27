from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'message', 'created_at', 'new_message']
    list_filter = ['new_message']
    search_fields = ['email']
