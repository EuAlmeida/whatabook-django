from django.contrib import admin

from core.models import categoria

class categoriaAdmin(admin.ModelAdmin):
    list_display = ("nome_categoria", "desc_categoria")

admin.site.register(categoria, categoriaAdmin)
