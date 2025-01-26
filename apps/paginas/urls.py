from django.urls import path
from .views import IndexView, ProdutosView, CategoriasView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  
    path('produtos', ProdutosView.as_view(), name='list_produtos'),  
    path('categoria', CategoriasView.as_view(), name='list_categorias'),  
]