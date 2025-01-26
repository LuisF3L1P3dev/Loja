from django.views.generic import TemplateView, ListView
from .models import Produto, Categoria, Fornecedor
# Create your views here.
class IndexView(TemplateView):
    template_name = 'paginas/index.html'
    
class ProdutosView(ListView):
    model = Produto
    template_name = 'paginas/list_produtos.html'
    context_object_name = 'produtos'

class CategoriasView(ListView):
    model = Categoria
    template_name = 'paginas/list_categorias.html'
    context_object_name = 'categorias'
