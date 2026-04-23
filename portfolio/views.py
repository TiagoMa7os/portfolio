from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Projeto
from .form import ProjetoForm


class ProjetoListView(ListView):
    model = Projeto
    template_name = "portfolio/projeto_list.html"
    context_object_name = "projetos"


class ProjetoCreateView(CreateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = "portfolio/form.html"
    success_url = reverse_lazy("projeto_list")


class ProjetoUpdateView(UpdateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = "portfolio/form.html"
    success_url = reverse_lazy("projeto_list")


class ProjetoDeleteView(DeleteView):
    model = Projeto
    template_name = "portfolio/confirm_delete.html"
    success_url = reverse_lazy("projeto_list")