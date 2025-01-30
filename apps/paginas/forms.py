from django import forms
from .models import Fornecedor

class CadastroFornecedoresForms(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'
        
