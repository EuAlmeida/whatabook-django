from django.contrib import admin

from core.models import editora


class editoraAdmin(admin.ModelAdmin):
    list_display = ("nome_editora", "desc_editora", "email_editora")
    search_fields = ("nome_editora",)

admin.site.register(editora, editoraAdmin)