from django import forms


class CategoriaForm(forms.Form):
    nome = forms.CharField(label="Nome do Formulário", max_length=100)
