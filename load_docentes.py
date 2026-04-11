import re
import requests
from bs4 import BeautifulSoup
from portfolio.models import Docente

URL = "https://informatica.ulusofona.pt/departamento/docentes/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

lista_docentes_atual = {
    "pedro alves": "pedro hugo de queiros alves",
    "bruno cipriano": "bruno miguel pereira cipriano",
    "bruno saraiva": "bruno david ferreira saraiva",
    "daniel silveira": "daniel tomas de maia mozart silveira",
    "daniel fernandes": "daniel filipe sobral fernandes",
    "iolanda velho": "iolanda raquel fernandes velho",
    "jose cascais bras": "jose manuel catarino barreiros cascais bras",
    "lucio studer": "lucio miguel studer ferreira",
    "pedro serra": "pedro arroz correia bonifacio serra",
    "pedro perdigao": "pedro de almeida perdigao",
    "rui santos": "rui filipe guimaraes dos santos",
    "rui ribeiro": "rui pedro nobre ribeiro",
    "sofia naique": "sofia marta lima naique",
    "fernando angelino": "fernando jose de aires angelino",
    "luis gomes": "luis alexandre ferreira de oliveira gomes",
}

def normalizar(texto):
    texto = texto.lower().strip()
    mapa = str.maketrans(
        "áàãâäéèêëíìîïóòõôöúùûüç",
        "aaaaaeeeeiiiiooooouuuuc"
    )
    texto = texto.translate(mapa)
    texto = re.sub(r"\s+", " ", texto)
    return texto

def encontrar_docente_existente(nome_site):
    nome_site_norm = normalizar(nome_site)

    for docente in Docente.objects.all():
        nome_bd_norm = normalizar(docente.nome)

        if nome_bd_norm == nome_site_norm:
            return docente

        if nome_bd_norm in lista_docentes_atual and lista_docentes_atual[nome_bd_norm] == nome_site_norm:
            return docente

    return None

def carregar_docentes():
    response = requests.get(URL, headers=HEADERS, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    tabela = soup.find("table")
    if not tabela:
        print("Tabela de docentes não encontrada.")
        return

    linhas = tabela.find_all("tr")
    vistos = set()

    for linha in linhas:
        colunas = linha.find_all("td")

        if len(colunas) < 3:
            continue

        primeira_coluna = colunas[0]
        link = primeira_coluna.find("a")

        if link:
            nome = link.get_text(strip=True)
            href = link.get("href", "").strip()
            if href.startswith("//"):
                href = "https:" + href
            elif href.startswith("/"):
                href = "https://informatica.ulusofona.pt" + href
        else:
            nome = primeira_coluna.get_text(strip=True)
            href = ""

        if not nome:
            continue

        nome_norm = normalizar(nome)
        if nome_norm in vistos:
            continue
        vistos.add(nome_norm)

        docente = encontrar_docente_existente(nome)

        if docente is None:
            docente = Docente.objects.create(
                nome=nome,
                link_pagina=href
            )
            print(f"Docente criado: {nome}")
        else:
            alterado = False

            if docente.nome != nome:
                docente.nome = nome
                alterado = True

            if href and docente.link_pagina != href:
                docente.link_pagina = href
                alterado = True

            if alterado:
                docente.save()
                print(f"Docente atualizado: {docente.nome}")
            else:
                print(f"Docente sem alterações: {docente.nome}")

    print("Carregamento de docentes concluído.")