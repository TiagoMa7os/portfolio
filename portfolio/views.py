from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Projeto
from .form import ProjetoForm


def is_gestor(user):
    return user.is_authenticated and user.groups.filter(name="gestor-portfolio").exists()


class GestorRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = "login"

    def test_func(self):
        return is_gestor(self.request.user)


class ProjetoListView(ListView):
    model = Projeto
    template_name = "portfolio/projeto_list.html"
    context_object_name = "projetos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_gestor"] = is_gestor(self.request.user)
        return context


class ProjetoCreateView(GestorRequiredMixin, CreateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = "portfolio/form.html"
    success_url = reverse_lazy("projeto_list")


class ProjetoUpdateView(GestorRequiredMixin, UpdateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = "portfolio/form.html"
    success_url = reverse_lazy("projeto_list")


class ProjetoDeleteView(GestorRequiredMixin, DeleteView):
    model = Projeto
    template_name = "portfolio/confirm_delete.html"
    success_url = reverse_lazy("projeto_list")

class SobreView(TemplateView):
    template_name = "portfolio/sobre.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["making_of_texto"] = """


Este projeto consistiu na criação de uma aplicação web em Django para gestão de projetos do meu portfólio.

## Desafio

O principal desafio foi organizar a aplicação de forma clara, usando a arquitetura MVT do Django.

## O que foi feito

* Criação dos modelos no ficheiro `models.py`
* Criação das views para listar, criar, editar e apagar projetos
* Criação dos templates HTML
* Aplicação de CSS para melhorar o aspeto visual
* Ligação ao GitHub para controlo de versões

## Dificuldades

* Compreender melhor as relações entre modelos
* Criar corretamente as URLs
* Resolver erros nas views e nos templates

## Correções

As correções foram feitas passo a passo, testando a aplicação no browser e analisando as mensagens de erro do Django.

## Justificação

Estas alterações permitiram tornar a aplicação mais organizada, funcional e fácil de manter.
"""

        return context

class HomeView(TemplateView):
    template_name = "portfolio/home.html"