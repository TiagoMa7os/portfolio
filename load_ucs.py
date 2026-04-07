import requests
from portfolio.models import Licenciatura, UnidadeCurricular

school_year = "202526"
course_code = 12  # LIG
headers = {"content-type": "application/json"}

# Buscar detalhes do curso
response = requests.post(
    "https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail",
    json={
        "language": "PT",
        "courseCode": course_code,
        "schoolYear": school_year,
    },
    headers=headers,
    timeout=30,
)

response.raise_for_status()
dados_curso = response.json()

licenciatura, created = Licenciatura.objects.update_or_create(
    sigla="LIG",
    defaults={
        "nome": dados_curso.get("name", "Licenciatura em Informática de Gestão"),
        "descricao": (
            dados_curso.get("presentation")
            or dados_curso.get("description")
            or ""
        ),
        "semestres": 6,
        "creditos": 180,
    },
)

if created:
    print(f"Licenciatura '{licenciatura.nome}' criada com sucesso.")
else:
    print(f"Licenciatura '{licenciatura.nome}' atualizada com sucesso.")

# Buscar detalhes de cada UC e guardar
for uc in dados_curso.get("courseFlatPlan", []):
    codigo_uc = uc.get("curricularIUnitReadableCode")
    if not codigo_uc:
        continue

    response_uc = requests.post(
        "https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails",
        json={
            "language": "PT",
            "curricularIUnitReadableCode": codigo_uc,
        },
        headers=headers,
        timeout=30,
    )

    response_uc.raise_for_status()
    dados_uc = response_uc.json()

    nome_uc = (
        dados_uc.get("name")
        or uc.get("curricularUnitName")
        or codigo_uc
    )

    ano_uc = uc.get("curricularYear") or 1
    semestre_uc = uc.get("semester") or ""

    ects_val = uc.get("ects", 0)
    try:
        ects_uc = int(float(ects_val))
    except (TypeError, ValueError):
        ects_uc = 0

    descricao_uc = (
        dados_uc.get("syllabus")
        or dados_uc.get("objectives")
        or dados_uc.get("program")
        or dados_uc.get("description")
        or ""
    )

    uc_obj, created = UnidadeCurricular.objects.update_or_create(
        sigla=codigo_uc,
        licenciatura=licenciatura,
        defaults={
            "nome": nome_uc[:100],
            "ano": ano_uc,
            "semestre": semestre_uc,
            "ects": ects_uc,
            "descricao": descricao_uc,
            "docente": "",
            "link_docente": "",
            "imagem": None,
        },
    )

    if created:
        print(f"UC '{uc_obj.nome}' criada.")
    else:
        print(f"UC '{uc_obj.nome}' atualizada.")