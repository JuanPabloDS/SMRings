from genericpath import exists
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, View, ListView
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q

from .models import Anel
from carrinho.models import Carrinho , CarrinhoAneis


# Class based View
class IndexView(TemplateView):
    template_name: str = 'index.html'
    return_url = None

    def get_queryset(self):
        query = self.request.GET.get("search")
        object_list = Anel.objects.filter(
            Q(nome__icontain=query)
        )
        return object_list

    def get(self, request):
        IndexView.return_url = request.GET.get('return_url')

        # Redirect para o carrinho
        request.session['redirect'] = 'index'
        request.session['index'] = 'service'

        if self.request.GET.get("search"):
            query = self.request.GET.get("search")
            values = Anel.objects.filter(
                Q(nome__icontains=query)
            )
        else:
            print('foi')
            values = Anel.objects.all()

        if self.request.GET.get("page"):
            pass
        else:
            pass
#-----------------------------------------------------------#
        # Paginação

        
        paginator = Paginator(values, 5) # Mostra 6 contatos por página

        # Make sure page request is an int. If not, deliver first page.
        # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        # Se o page request (9999) está fora da lista, mostre a última página.
        try:
            aneis = paginator.page(page)
        except (EmptyPage, InvalidPage):
            aneis = paginator.page(paginator.num_pages)

# ----------------------------------------------------------#



        context = {
            'aneis': aneis,
        }

        if request.session.has_key('carrinho'):
            print(request.session['carrinho'])
            return render(request, "index.html", context)
        else:
            request.session['carrinho'] = {}
            print(request.session['carrinho'])
            print('não')
            return render(request, "index.html", context)

    def listing(request):

        return render('index.html',)

class SearchResultsView(ListView):
    
    template_name = "index.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Anel.objects.filter(
            Q(nome__icontain=query)
        )
        return object_list




class AneisDetailView(DetailView):
    template_name: str = 'aneis.html'

    queryset = Anel.objects.all()

    """def get_object(self):

        # Redirect para o carrinho
        # request.session['redirect'] = 'aneis'

        obj = super().get_object()
        return obj"""
    
    def get(self, request, pk):

        # Redirect para o carrinho
        request.session['redirect'] = f'../aneis/{pk}'

        anel = Anel.objects.get(id=pk)


        context = {
            'anel' : anel
            }
        return render(request, 'aneis.html', context)



    def post(self, request, *args, **kwargs):
        postData = request.POST

        if postData.get('excluir'):
            id_ex = postData.get('excluir')
            inter = int(id_ex)
            print(inter)
            carrinho_new =  request.session['carrinho'].pop(f'{id_ex}')
            print(id_ex)
            print(f'sss: {carrinho_new}')
            request.session['carrinho'] = carrinho_new
        else:
            print('Funciona')
            c_carrinho =  Carrinho.objects.get(id=5)
            c_carrinho_id = c_carrinho.id
            anel = Anel.objects.get(id=(postData.get('anel_id')))
            anel_id = anel.nome
            anel_preco = Anel.real_br_money(anel.preco)
            anel_imagem = anel.imagem
            quantidade = postData.get('quantidade')
            carrinho = request.session['carrinho']
            loop = True
            n = 1
            pk = str(n)
            total = 0

            while loop == True:
                if Anel.get_key(pk, carrinho):
                    n += 1
                    pk = str(n)
                    print(f'pk: {pk}')
                else:
                    loop = False
                    novo_carrinho = {pk: [c_carrinho_id, anel_id, quantidade, anel_preco, str(anel_imagem) ]}
                    carrinho.update(novo_carrinho)
                    request.session['carrinho'] = carrinho
                    print(request.session['carrinho'])


            for preco in request.session['carrinho'].values():
                anel_total = preco[3]
                quantidade_tl = int(preco[2])
                totais = Anel.dolar_money(anel_total) * quantidade_tl
                total = total + totais
                total_conv = Anel.real_br_money(total)
                request.session['total'] = total_conv
                print(request.session['total'])

        


        return redirect('/')

        
""" carrinho_anel = CarrinhoAneis(carrinho_id=carrinho_id,
                            anel_id=anel_id,
                            quantidade=quantidade)"""




#  carrinho_anel = CarrinhoAneis(5, carrinho.id, anel.id, quantidade=3)