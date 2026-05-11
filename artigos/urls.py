from django.urls import path
from . import views

urlpatterns = [
    path("artigos/", views.artigo_list, name="artigo_list"),
    path("artigos/criar/", views.artigo_create, name="artigo_create"),
    path("artigos/<int:pk>/", views.artigo_detail, name="artigo_detail"),
    path("artigos/<int:pk>/editar/", views.artigo_update, name="artigo_update"),
    path("artigos/<int:pk>/like/", views.artigo_like, name="artigo_like"),
    path("<int:pk>/delete/", views.artigo_delete, name="artigo_delete"),
]