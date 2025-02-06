from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView, CreateView
from .models import Produto, Categoria, Fornecedor
from .forms import CadastroFornecedoresForms, CadastroProdutosForms, CadastroCategoriaForms
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = 'paginas/index.html'
    
class ProdutosView(ListView):
    model = Produto
    template_name = 'paginas/list_produtos.html'
    context_object_name = 'produtos'
    paginate_by = 5

    def get_queryset(self):
        queryset = Produto.objects.all()
        query = self.request.GET.get('produto')

        if query:
            queryset = queryset.filter(nome__icontains=query)
        return queryset
    
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
    
class ProdutoCreateView(CreateView):
    template_name = "paginas/form_create_produto.html"
    model = Produto
    form_class = CadastroProdutosForms
    success_url = reverse_lazy('list_produtos')
    
class CategoriaCreateView(CreateView):
    template_name = "paginas/form_create_categoria.html"
    model = Categoria
    form_class = CadastroCategoriaForms
    success_url = reverse_lazy('list_categorias')