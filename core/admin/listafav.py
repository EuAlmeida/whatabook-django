from django.contrib import admin

from core.models import listafav


class listafavAdmin(admin.ModelAdmin):
    list_display = ("titulo_lista", "user_lista", "desc_lista")
    search_fields = ("titulo_lista","user_lista")

admin.site.register(listafav, listafavAdmin)