from django.contrib import admin

from core.models import resenha


class resenhaAdmin(admin.ModelAdmin):
    list_display = ("titulo_resenha", "livro_resenha")
    search_fields = ("titulo_resenha", "nota_resenha")

admin.site.register(resenha, resenhaAdmin)

