from django.contrib import admin
from .models import *


@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla", "semestres", "creditos")
    search_fields = ("nome",)


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano", "semestre", "ects")
    search_fields = ("nome",)
    list_filter = ("ano", "semestre")


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data", "unidade_curricular")
    search_fields = ("titulo",)
    list_filter = ("data",)
    filter_horizontal = ("tecnologias", "competencias", "tags")


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "interesse")
    search_fields = ("nome",)


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nivel")
    search_fields = ("nome",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "entidade", "data_inicio")
    search_fields = ("nome",)


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ano", "interesse")
    search_fields = ("titulo",)


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data")
    search_fields = ("titulo",) 