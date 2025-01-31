from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(3, 'o campode ter no minimo 3 caracteres')])
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.TextField(blank=True, null=True, default=None)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE, related_name='produtos', default=None, null=True)
    
    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    produtos = models.ManyToManyField(Produto, related_name='categorias')

    def __str__(self):
        return self.nome
    
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)


    def __str__(self):
        return self.nome
    

