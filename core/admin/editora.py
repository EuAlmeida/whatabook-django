from django.contrib import admin

from core.models import editora


class editoraAdmin(admin.ModelAdmin):
    list_display = ("nome_editora", "desc_editora", "email_editora")

admin.site.register(editora, editoraAdmin)