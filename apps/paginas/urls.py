from django.urls import path
from .views import IndexView, ProdutosView, CategoriasView, FornecedorView, FornecedorCreateView, ProdutoCreateView, CategoriaCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('fornecedor/', FornecedorView.as_view(), name='list_fornecedores'),
    path('produtos/', ProdutosView.as_view(), name='list_produtos'),  
    path('categoria/', CategoriasView.as_view(), name='list_categorias'),

    path('create_fornecedor/', FornecedorCreateView.as_view(), name='create_fornecedor'),  
    path('produtos/create/', ProdutoCreateView.as_view(), name='create_produto'),  
    path('categoria/create/', CategoriaCreateView.as_view(), name='create_categoria'),  
]