# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from snippets.models import Snippet


# Register your models here.
@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    pass
