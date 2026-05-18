from django.urls import path
from .views import (
    landing,
    ProjetoListView, ProjetoCreateView, ProjetoUpdateView,
    ProjetoDeleteView, ProjetoDetailView,
    SobreView,
    TecnologiaListView, TecnologiaCreateView, TecnologiaUpdateView, TecnologiaDeleteView,
    CompetenciaListView, CompetenciaCreateView, CompetenciaUpdateView, CompetenciaDeleteView,
    FormacaoListView, FormacaoCreateView, FormacaoUpdateView, FormacaoDeleteView,
    MakingOfListView, MakingOfCreateView, MakingOfUpdateView, MakingOfDeleteView,
)

urlpatterns = [
    path("", landing, name="landing"),

    # Projetos
    path("projetos/", ProjetoListView.as_view(), name="projeto_list"),
    path("projetos/criar/", ProjetoCreateView.as_view(), name="projeto_create"),
    path("projetos/<int:pk>/editar/", ProjetoUpdateView.as_view(), name="projeto_update"),
    path("projetos/<int:pk>/apagar/", ProjetoDeleteView.as_view(), name="projeto_delete"),
    path("projeto/<int:pk>/", ProjetoDetailView.as_view(), name="projeto_detail"),

    # Sobre
    path("sobre/", SobreView.as_view(), name="sobre"),

    # Tecnologias
    path("tecnologias/", TecnologiaListView.as_view(), name="tecnologia_list"),
    path("tecnologias/criar/", TecnologiaCreateView.as_view(), name="tecnologia_create"),
    path("tecnologias/<int:pk>/editar/", TecnologiaUpdateView.as_view(), name="tecnologia_update"),
    path("tecnologias/<int:pk>/apagar/", TecnologiaDeleteView.as_view(), name="tecnologia_delete"),

    # Competências
    path("competencias/", CompetenciaListView.as_view(), name="competencia_list"),
    path("competencias/criar/", CompetenciaCreateView.as_view(), name="competencia_create"),
    path("competencias/<int:pk>/editar/", CompetenciaUpdateView.as_view(), name="competencia_update"),
    path("competencias/<int:pk>/apagar/", CompetenciaDeleteView.as_view(), name="competencia_delete"),

    # Formações
    path("formacoes/", FormacaoListView.as_view(), name="formacao_list"),
    path("formacoes/criar/", FormacaoCreateView.as_view(), name="formacao_create"),
    path("formacoes/<int:pk>/editar/", FormacaoUpdateView.as_view(), name="formacao_update"),
    path("formacoes/<int:pk>/apagar/", FormacaoDeleteView.as_view(), name="formacao_delete"),

    # Making Of
    path("makingof/", MakingOfListView.as_view(), name="makingof_list"),
    path("makingof/criar/", MakingOfCreateView.as_view(), name="makingof_create"),
    path("makingof/<int:pk>/editar/", MakingOfUpdateView.as_view(), name="makingof_update"),
    path("makingof/<int:pk>/apagar/", MakingOfDeleteView.as_view(), name="makingof_delete"),
]