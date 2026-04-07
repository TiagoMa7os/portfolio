import json
from portfolio.models import TFC, Tecnologia

with open("portfolio/data/tfcs_2025.json", encoding="utf-8") as f:
    dados = json.load(f)

for item in dados:
    tfc, created = TFC.objects.get_or_create(
        titulo=item["titulo"],
        defaults={
            "autores": item["autores"],
            "orientador": item["orientador"],
            "parceria": item["parceria"],
            "licenciatura": item["licenciatura"],
            "ano": int(item["ano"]),
            "email": item["email"],
            "sumario": item["sumario"],
            "pdf": item["pdf"],
            "imagem": item["imagem"],
            "palavras_chave": item["palavras_chave"],
            "areas": item["areas"],
            "tecnologias_usadas": item["tecnologias_usadas"],
            "rating": item["rating"],
        }
    )

    if created:
        print(f"O TFC '{tfc.titulo}' foi criado!")
    else:
        print(f"O TFC '{tfc.titulo}' já foi criado!")