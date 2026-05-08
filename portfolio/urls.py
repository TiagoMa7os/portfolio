from django.urls import path
from .views import (
    ProjetoListView,
    ProjetoCreateView,
    ProjetoUpdateView,
    ProjetoDeleteView,
    SobreView,
)

urlpatterns = [
    path("projetos/", ProjetoListView.as_view(), name="projeto_list"),
    path("projetos/criar/", ProjetoCreateView.as_view(), name="projeto_create"),
    path("projetos/<int:pk>/editar/", ProjetoUpdateView.as_view(), name="projeto_update"),
    path("projetos/<int:pk>/apagar/", ProjetoDeleteView.as_view(), name="projeto_delete"),
    path("sobre/", SobreView.as_view(), name="sobre"),
]