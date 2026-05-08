from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Artigo
from .forms import ArtigoForm, ComentarioForm


def is_autor(user):
    return user.is_authenticated and user.groups.filter(name="autores").exists()


def artigo_list(request):
    artigos = Artigo.objects.all().order_by("-data_criacao")
    return render(request, "artigos/artigo_list.html", {
        "artigos": artigos,
        "is_autor": is_autor(request.user),
    })


def artigo_detail(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    form = ComentarioForm()

    if request.method == "POST" and request.user.is_authenticated:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
            return redirect("artigo_detail", pk=artigo.pk)

    return render(request, "artigos/artigo_detail.html", {
        "artigo": artigo,
        "form": form,
        "is_autor": is_autor(request.user),
    })


@login_required(login_url="login")
def artigo_create(request):
    if not is_autor(request.user):
        return redirect("artigo_list")

    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect("artigo_list")
    else:
        form = ArtigoForm()

    return render(request, "artigos/artigo_form.html", {"form": form})


@login_required(login_url="login")
def artigo_update(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    if not is_autor(request.user) or artigo.autor != request.user:
        return redirect("artigo_list")

    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect("artigo_detail", pk=artigo.pk)
    else:
        form = ArtigoForm(instance=artigo)

    return render(request, "artigos/artigo_form.html", {"form": form})


def artigo_like(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    if request.user.is_authenticated:
        if request.user in artigo.likes.all():
            artigo.likes.remove(request.user)
        else:
            artigo.likes.add(request.user)

    return redirect("artigo_detail", pk=artigo.pk)