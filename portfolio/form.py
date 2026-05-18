from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao, MakingOf


class BaseStyledForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_class = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{existing_class} input".strip()


class ProjetoForm(BaseStyledForm):
    class Meta:
        model = Projeto
        fields = "__all__"
        widgets = {
            "data": forms.DateInput(attrs={"type": "date", "class": "input"}),
        }


class TecnologiaForm(BaseStyledForm):
    class Meta:
        model = Tecnologia
        fields = "__all__"


class CompetenciaForm(BaseStyledForm):
    class Meta:
        model = Competencia
        fields = "__all__"


class FormacaoForm(BaseStyledForm):
    class Meta:
        model = Formacao
        fields = "__all__"
        widgets = {
            "data_inicio": forms.DateInput(attrs={"type": "date", "class": "input"}),
            "data_fim": forms.DateInput(attrs={"type": "date", "class": "input"}),
        }


class MakingOfForm(BaseStyledForm):
    class Meta:
        model = MakingOf
        fields = "__all__"
        widgets = {
            "data": forms.DateInput(attrs={"type": "date", "class": "input"}),
        }