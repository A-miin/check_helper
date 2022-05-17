from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('diseases',)
    list_display = ['id', 'email', 'firstname', 'lastname', ]
    list_filter = ['is_staff', ]
    search_fields = ['email', 'firstname', 'lastname']
    readonly_fields = ('id',)
    ordering = ('-id',)
    list_display_links = ['email']



admin.site.register(User, UserAdmin)
