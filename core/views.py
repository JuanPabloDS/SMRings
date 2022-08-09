from genericpath import exists
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, View, ListView
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q
from django.contrib import messages
from numpy import empty

from .models import Anel, Tamanho
from carrinho.models import Carrinho , CarrinhoAneis


# Class based View
class IndexView(TemplateView):
    template_name: str = 'index.html'
    return_url = None
    

    def get(self, request):
        IndexView.return_url = request.GET.get('return_url')
        mensagem = ''

        # Redirect para o carrinho
        request.session['redirect'] = 'index'

        #------------------------#
        # Exibir mensagem de anel enviado ao carrinho

        if request.session.has_key('mensagem_carrinho_salvo'):
            
            messages.success(request, 'Enviado com sucesso para o carrinho!' )
            request.session.pop('mensagem_carrinho_salvo')

        elif request.session.has_key('logado'):
            
            nome = request.session['logado']
            messages.success(request, f'Bem vindo {nome}!' )
            request.session.pop('logado')

            
            

        #------------------------#
        

        if self.request.GET.get("search"):
            search = self.request.GET.get("search")
            request.session['mensagem'] = f'Resultado para pesquisa: {search.title()}'
            query = self.request.GET.get("search")
            values = Anel.objects.filter(
                Q(nome__icontains=query)
            )
            mensagem = request.session['mensagem']

            if len(values) == 0:
                request.session['mensagem'] = [mensagem, 'vazio']
            else:
                request.session['mensagem'] = [mensagem, '']
        else:
            print('foi')
            values = Anel.objects.all()

        print(f'Pega -> {mensagem}')

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
        empty = []

        context = {
            'aneis': aneis,
            'mensagem': mensagem,
            'empty': empty,
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
            tamanho = postData.get('tamanho')
            print(f'----> {tamanho}')
            carrinho = request.session['carrinho']
            loop = True
            n = 1
            pk = str(n)
            total = 0

            #------------------------------------------#
            """Verifica se o Tamanho e quantidade possuem valores validos"""

            try:
                teste_quantidade = int(quantidade)
                teste_tamanho = int(tamanho)
                print('----- -----')
                print(teste_quantidade)
                listar = [num for num in anel.tamanho.all()]
                lista2 = ([str(num) for num in listar])

                for num in lista2:
                    
                    if teste_tamanho == int(num):
                        erro = False

                if erro == True or teste_quantidade > 50:
                    return redirect('erro')

            except:
                return redirect('erro')




            #-------------------------------------------#


            while loop == True:
                if Anel.get_key(pk, carrinho):
                    n += 1
                    pk = str(n)
                    print(f'pk: {pk}')
                else:
                    loop = False
                    novo_carrinho = {pk: [c_carrinho_id, anel_id, quantidade, anel_preco, str(anel_imagem), tamanho ]}
                    carrinho.update(novo_carrinho)
                    request.session['carrinho'] = carrinho
                    print(request.session['carrinho'])

                    #-----------------------------#
                    # Exindo mensagem de anel salvo no carrinho

                    request.session['mensagem_carrinho_salvo'] = 'Anel adicionado ao carrinho'

                    #------------------------------#



            for preco in request.session['carrinho'].values():
                anel_total = preco[3]
                quantidade_tl = int(preco[2])
                totais = Anel.dolar_money(anel_total) * quantidade_tl
                total = total + totais
                total_conv = Anel.real_br_money(total)
                request.session['total'] = total_conv
                print(request.session['total'])

        


        return redirect('/')

    
class ErroView(TemplateView):
    template_name: str = 'erro.html'
    return_url = None


class ErroCadastroView(TemplateView):
    template_name: str = 'erro-cadastro.html'
    return_url = None

