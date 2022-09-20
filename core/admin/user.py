from django.contrib import admin

from core.models import user

class userAdmin(admin.ModelAdmin):
    list_display = ("nome_user", "email_user", "tip")

admin.site.register(user, userAdmin)