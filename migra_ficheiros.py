import os
from django.core.files import File
from portfolio.models import Docente, Tecnologia, Projeto, Formacao, MakingOf

def migrar_ficheiro(obj, campo_nome):

    campo = getattr(obj, campo_nome)

    if campo and campo.name:

        local_path = os.path.join("media", campo.name)

        if os.path.exists(local_path):

            with open(local_path, "rb") as f:

                campo.save(
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )

            print(f"Migrado: {obj} -> {campo_nome}")

        else:
            print(f"Não encontrado: {obj} -> {local_path}")

for obj in Docente.objects.all():
    migrar_ficheiro(obj, "imagem")

for obj in Tecnologia.objects.all():
    migrar_ficheiro(obj, "logo")

for obj in Projeto.objects.all():
    migrar_ficheiro(obj, "imagem")

for obj in Formacao.objects.all():
    migrar_ficheiro(obj, "imagem")

for obj in MakingOf.objects.all():
    migrar_ficheiro(obj, "foto")