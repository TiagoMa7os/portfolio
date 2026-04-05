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
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='ucs/')
    docente = models.CharField(max_length=150)
    link_docente = models.URLField()

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
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=200)
    ano = models.PositiveIntegerField()
    resumo = models.TextField()
    orientadores = models.CharField(max_length=200)
    interesse = models.PositiveIntegerField(help_text='Escala de 1 a 5')

    def __str__(self):
        return self.titulo        