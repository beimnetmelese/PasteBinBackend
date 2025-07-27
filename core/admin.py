from django.contrib import admin
from .models import Snippet
# Register your models here.
@admin.register(Snippet)
class UserAdmin(admin.ModelAdmin):
    list_display = ('content_encrypted', 'slug')
    search_fields = ('slug', 'language')