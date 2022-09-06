from django.contrib import admin

from core.models import livro, user, categoria, autor, editora

admin.site.register(livro)
admin.site.register(user)
admin.site.register(categoria)
admin.site.register(autor)
admin.site.register(editora)
