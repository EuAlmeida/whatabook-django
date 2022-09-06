from django.contrib import admin

from core.models import livro, user, categoria, autor

admin.site.register(livro)
admin.site.register(user)
admin.site.register(categoria)
admin.site.register(autor)