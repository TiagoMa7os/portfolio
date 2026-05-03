from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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