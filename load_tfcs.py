import json
from portfolio.models import TFC, Tecnologia, Docente

with open("portfolio/data/tfcs_2025.json", encoding="utf-8") as f:
    dados = json.load(f)

for item in dados:
    tfc, created = TFC.objects.get_or_create(
        titulo=item["titulo"],
        defaults={
            "autores": item["autores"],
            "orientador_texto": item["orientador"],
            "parceria": item["parceria"],
            "licenciatura": item["licenciatura"],
            "ano": int(item["ano"]),
            "email": item["email"],
            "sumario": item["sumario"],
            "pdf": item["pdf"],
            "imagem": item["imagem"],
            "palavras_chave": item["palavras_chave"],
            "areas": item["areas"],
            "rating": item["rating"],
        }
    )

    if not created:
        tfc.autores = item["autores"]
        tfc.orientador_texto = item["orientador"]
        tfc.parceria = item["parceria"]
        tfc.licenciatura = item["licenciatura"]
        tfc.ano = int(item["ano"])
        tfc.email = item["email"]
        tfc.sumario = item["sumario"]
        tfc.pdf = item["pdf"]
        tfc.imagem = item["imagem"]
        tfc.palavras_chave = item["palavras_chave"]
        tfc.areas = item["areas"]
        tfc.rating = item["rating"]
        tfc.save()

    tfc.tecnologias.clear()
    tfc.orientadores.clear()

    tecnologias_str = item.get("tecnologias_usadas", "")
    if tecnologias_str:
        lista_tecnologias = tecnologias_str.split(";")

        for nome_tecnologia in lista_tecnologias:
            nome_tecnologia = nome_tecnologia.strip().rstrip(".")

            if nome_tecnologia:
                tecnologia, _ = Tecnologia.objects.get_or_create(
                    nome=nome_tecnologia,
                    defaults={
                        "tipo": "",
                        "descricao": "",
                        "link_oficial": "",
                        "interesse": 3,
                    }
                )
                tfc.tecnologias.add(tecnologia)

    orientadores_str = item.get("orientador", "")
    if orientadores_str:
        lista_orientadores = orientadores_str.split(",")

        for nome_orientador in lista_orientadores:
            nome_orientador = nome_orientador.strip()

            if nome_orientador:
                docente, _ = Docente.objects.get_or_create(
                    nome=nome_orientador
                )
                tfc.orientadores.add(docente)

    if created:
        print(f"TFC '{tfc.titulo}' criado!")
    else:
        print(f"TFC '{tfc.titulo}' atualizado!")