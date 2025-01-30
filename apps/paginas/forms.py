from django import forms
from .models import Fornecedor, Produto, Categoria
class CadastroFornecedoresForms(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'
        
class CadastroProdutosForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        
class CadastroCategoriaForms(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'