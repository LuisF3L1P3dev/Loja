from django.views.generic import TemplateView, ListView, CreateView
from .models import Produto, Categoria, Fornecedor
from .forms import CadastroFornecedoresForms
from django.urls import reverse_lazy

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

class FornecedorView(ListView):
    model = Fornecedor
    template_name = 'paginas/list_fornecedores.html'
    context_object_name = 'fornecedores'

class FornecedorCreateView(CreateView):
    template_name = "paginas/form_cadastro_Fornecedor.html"
    model = Fornecedor
    form_class = CadastroFornecedoresForms
    success_url = reverse_lazy('list_fornecedores')
    
