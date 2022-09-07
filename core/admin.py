from django.contrib import admin

from core.models import livro, resenha, user, categoria, autor, editora, listafav


class livroAdmin(admin.ModelAdmin):
    list_display = ("titulo_livro", "qtd_paginas", "editora_livro")

admin.site.register(livro, livroAdmin)




class userAdmin(admin.ModelAdmin):
    list_display = ("nome_usuario", "email_user", "adm")

admin.site.register(user, userAdmin)




class categoriaAdmin(admin.ModelAdmin):
    list_display = ("nome_categoria", "desc_categoria")

admin.site.register(categoria, categoriaAdmin)



class autorAdmin(admin.ModelAdmin):
    list_display = ("nome_autor", "autor_nasc", "autor_falecimento")

admin.site.register(autor, autorAdmin)

class editoraAdmin(admin.ModelAdmin):
    list_display = ("nome_editora", "desc_editora", "email_editora")

admin.site.register(editora, editoraAdmin)


class listafavAdmin(admin.ModelAdmin):
    list_display = ("titulo_lista", "user_lista", "desc_lista")

admin.site.register(listafav, listafavAdmin)

class resenhaAdmin(admin.ModelAdmin):
    list_display = ("titulo_resenha", "livro_resenha")

admin.site.register(resenha, resenhaAdmin)
