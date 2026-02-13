# admin.py
from django.contrib import admin
from .models import Murojaat

@admin.register(Murojaat)
class MurojaatAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "created_at")
    search_fields = ("firstname", "lastname", "email")
    list_filter = ("created_at",)
