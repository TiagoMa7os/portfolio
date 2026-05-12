from django.urls import path
from .views import (
    HomeView,
    ProjetoListView,
    ProjetoCreateView,
    ProjetoUpdateView,
    ProjetoDeleteView,
    ProjetoDetailView,
    SobreView,
    TecnologiaListView,
    CompetenciaListView,
    FormacaoListView,
    MakingOfListView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    path("projetos/", ProjetoListView.as_view(), name="projeto_list"),
    path("projetos/criar/", ProjetoCreateView.as_view(), name="projeto_create"),
    path("projetos/<int:pk>/editar/", ProjetoUpdateView.as_view(), name="projeto_update"),
    path("projetos/<int:pk>/apagar/", ProjetoDeleteView.as_view(), name="projeto_delete"),
    path("projeto/<int:pk>/", ProjetoDetailView.as_view(), name="projeto_detail"), 

    path("sobre/", SobreView.as_view(), name="sobre"),

    path("tecnologias/", TecnologiaListView.as_view(), name="tecnologia_list"),

    path("competencias/", CompetenciaListView.as_view(), name="competencia_list"),
    
    path("formacoes/", FormacaoListView.as_view(), name="formacao_list"),

    path("makingof/", MakingOfListView.as_view(), name="makingof_list"),
]