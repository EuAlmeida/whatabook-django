from django.contrib import admin

from core.models import livro

class livroAdmin(admin.ModelAdmin):
    list_display = ("titulo_livro", "qtd_paginas", "editora_livro")

admin.site.register(livro, livroAdmin)