import json
from portfolio.models import TFC, Tecnologia

with open("portfolio/data/tfcs_2025.json", encoding="utf-8") as f:
    dados = json.load(f)

for item in dados:
    tfc = TFC.objects.create(
        titulo = item["titulo"],
        autores = item["autores"],
        orientadores = item["orientadores"],
        resumo = item["resumo"],
        licenciatura = item["licenciatura"],
        email = item["email"],
        rating = item["rating"],
        pdf = item["pdf"],
        imagem = item["imagem"],
    )

for tech_nome in item["tecnologias"]:
    tech, _ = Tecnologia.objects.get_or_create(nome = tech_nome)
    tfc.tecnologias.add(tech)

print(f"O TFC '{tfc.titulo}' foi criado!")