from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20)
    descricao = models.TextField()
    semestres = models.PositiveIntegerField()
    creditos = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20)
    ano = models.PositiveIntegerField()
    semestre = models.PositiveIntegerField()
    ects = models.PositiveIntegerField()
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    docente = models.CharField(max_length=150, blank=True)
    link_docente = models.URLField(blank=True)

    licenciatura = models.ForeignKey(
        Licenciatura,
        on_delete=models.CASCADE,
        related_name='unidades_curriculares'
    )

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, blank=True)
    descricao = models.TextField(blank=True)
    logo = models.ImageField(upload_to='tecnologias/')
    link_oficial = models.URLField()
    interesse = models.PositiveIntegerField(help_text='Escala de 1 a 5')

    def __str__(self):
        return self.nome


class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    data = models.DateField()
    github_url = models.URLField()
    video_demo_url = models.URLField(blank=True)

    unidade_curricular = models.ForeignKey(
        UnidadeCurricular,
        on_delete=models.CASCADE,
        related_name='projetos'
    )
    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name='projetos',
        blank=True
    )
    competencias = models.ManyToManyField(
        Competencia,
        related_name='projetos',
        blank=True
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='projetos',
        blank=True
    )

    def __str__(self):
        return self.titulo


class TFC(models.Model):
    titulo = models.CharField(max_length=250)
    autores = models.CharField(max_length=250)
    orientador = models.CharField(max_length=250)
    parceria = models.CharField(max_length=250, blank=True)
    licenciatura = models.CharField(max_length=250)
    ano = models.PositiveIntegerField()
    email = models.EmailField(blank=True)
    sumario = models.TextField()
    pdf = models.URLField(blank=True)
    imagem = models.URLField(blank=True)
    palavras_chave = models.TextField(blank=True)
    areas = models.TextField(blank=True)
    tecnologias_usadas = models.TextField(blank=True)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo        

class Formacao(models.Model):
    nome = models.CharField(max_length=100)
    entidade = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='formacoes/', blank=True, null=True)

    competencias = models.ManyToManyField(
        Competencia,
        related_name='formacoes',
        blank=True
    )

    def __str__(self):
        return self.nome

class MakingOf(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    foto = models.ImageField(upload_to='making_of/')
    ferramentas_ia = models.TextField(blank=True)
    descricao = models.TextField()
    erros = models.TextField(blank=True)
    correcao = models.TextField(blank=True)
    justificacao = models.TextField(blank=True)

    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='makingofs'
    )

    def __str__(self):
        return self.titulo