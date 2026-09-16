from django.contrib import admin

from . import models


# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula')

class PerfilAcademicoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'link_lattes', 'biografia')

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'data_inicio', 'categoria')

admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Aluno, AlunoAdmin)
admin.site.register(models.PerfilAcademico, PerfilAcademicoAdmin)
admin.site.register(models.Projeto, ProjetoAdmin)