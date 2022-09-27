from django.contrib import admin

from core.models import autor


class autorAdmin(admin.ModelAdmin):
    list_display = ("nome_autor", "autor_nasc", "autor_falecimento")

admin.site.register(autor, autorAdmin)