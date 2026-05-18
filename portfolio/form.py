from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao, MakingOf


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = "__all__"
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "data_inicio": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "data_fim": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "url": forms.URLInput(attrs={"class": "form-control"}),
            "repositorio": forms.URLInput(attrs={"class": "form-control"}),
            "imagem": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "tecnologias": forms.CheckboxSelectMultiple(),
            "competencias": forms.CheckboxSelectMultiple(),
        }


class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = "__all__"
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "tipo": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "interesse": forms.NumberInput(attrs={"class": "form-control", "min": 1, "max": 5}),
            "link_oficial": forms.URLInput(attrs={"class": "form-control"}),
            "logo": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = "__all__"
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "nivel": forms.NumberInput(attrs={"class": "form-control", "min": 1, "max": 5}),
        }


class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = "__all__"
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "entidade": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "data_inicio": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "data_fim": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "imagem": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "competencias": forms.CheckboxSelectMultiple(),
        }


class MakingOfForm(forms.ModelForm):
    class Meta:
        model = MakingOf
        fields = "__all__"
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "data": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "foto": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }