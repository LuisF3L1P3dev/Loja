from django import forms
from .models import Fornecedor, Produto, Categoria
from django.core.validators import ValidationError, MinValueValidator
from .validators import validar_preco_positivo, quantidade_estoque_inteiro_positivo,  validar_codigo

class CadastroFornecedoresForms(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'
        
class CadastroProdutosForms(forms.ModelForm):
    preco = forms.DecimalField(validators=[validar_preco_positivo])
    quantidade = forms.IntegerField(validators=[quantidade_estoque_inteiro_positivo])    
    codigo = forms.CharField(validators=[validar_codigo])
    class Meta:
        model = Produto
        fields = '__all__'
        # labels = {
        #     'nome': 'Nome do Produto',
        #     'preco': 'Preço do Produto',
        #     'categoria': 'Categoria do Produto',
        #     'fornecedor': 'Fornecedor do Produto'
        # }
    
    # def clean_preco(self):
    #     preco = self.cleaned_data.get('preco')
    #     if preco <= 0:
    #         raise forms.ValidationError('O preço deve ser maior que zero')
    #     return preco

class CadastroCategoriaForms(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'