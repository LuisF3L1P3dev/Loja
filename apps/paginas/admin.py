from django.contrib import admin

# Register your models here.
from .models import Produto, Categoria, Fornecedor

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'preco', 'quantidade', 'data_criacao']
    search_fields = ['codigo', 'nome']
    list_filter = ['data_criacao']
  
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
admin.site.register(Fornecedor)