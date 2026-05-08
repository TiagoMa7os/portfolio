from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from .forms import RegistoForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("projeto_list")

    erro = None
    mensagem = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        if email:
            try:
                user = User.objects.get(email=email)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)

                link = settings.SITE_URL + reverse(
                    "magic_login_confirm",
                    kwargs={"uidb64": uid, "token": token}
                )

                send_mail(
                    "Link mágico de autenticação",
                    f"Clica neste link para entrar na aplicação:\n\n{link}",
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

                mensagem = "Foi enviado um link mágico para o teu email."
            except User.DoesNotExist:
                erro = "Não existe nenhum utilizador com esse email."

        else:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("projeto_list")
            else:
                erro = "Username ou password inválidos."

    return render(request, "accounts/login.html", {
        "erro": erro,
        "mensagem": mensagem,
    })


def magic_login_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        login(request, user)
        return redirect("projeto_list")

    return redirect("login")


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("login")


def registo_view(request):
    if request.user.is_authenticated:
        return redirect("projeto_list")

    if request.method == "POST":
        form = RegistoForm(request.POST)

        if form.is_valid():
            user = form.save()

            grupo, created = Group.objects.get_or_create(name="autores")
            user.groups.add(grupo)

            login(request, user)
            return redirect("projeto_list")
    else:
        form = RegistoForm()

    return render(request, "accounts/registo.html", {"form": form})