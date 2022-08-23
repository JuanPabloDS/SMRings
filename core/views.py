from genericpath import exists
from types import NoneType
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, View, ListView
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q
from django.contrib import messages
from numpy import empty
from django.utils import timezone

from .models import Anel
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
            if request.session.has_key('compra'):
                request.session.pop('compra')
                request.session.pop('logado')

            else:
                nome = request.session['logado']
                messages.success(request, f'Bem vindo {nome}!' )
                request.session.pop('logado')


        # Apaga a session de redirect para finalizar a compra
        if request.session.has_key('compra'):
             request.session.pop('compra')
            
            

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
            request.session['mensagem'] = ''
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
            return render(request, "index.html", context)
        else:
            request.session['carrinho'] = {}
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

        
        # Apaga a session de redirect para finalizar a compra
        if request.session.has_key('compra'):
             request.session.pop('compra')

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
            
            anel = Anel.objects.get(id=(postData.get('anel_id')))
            anel_id = anel.id
            anel_nome = anel.nome
            anel_preco = Anel.real_br_money(anel.preco)
            anel_imagem = anel.imagem
            quantidade = postData.get('quantidade')
            tamanho = postData.get('tamanho')
            carrinho = request.session['carrinho']
            preco_qtd = int(quantidade) * anel.preco
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
                    novo_carrinho = {pk: [ anel_nome, quantidade, anel_preco, tamanho, str(anel_imagem),  str(Anel.real_br_money(preco_qtd)), str(anel_id) ]}
                    carrinho.update(novo_carrinho)
                    request.session['carrinho'] = carrinho
                    print(request.session['carrinho'])

                    #-----------------------------#
                    # Exindo mensagem de anel salvo no carrinho

                    request.session['mensagem_carrinho_salvo'] = 'Anel adicionado ao carrinho'

                    #------------------------------#



            for preco in request.session['carrinho'].values():
                print(preco)
                anel_total = preco[2]
                quantidade_tl = int(preco[1])
                totais = Anel.dolar_money(anel_total) * quantidade_tl
                total = total + totais
                total_conv = Anel.real_br_money(total)
                request.session['total'] = total_conv

        


        return redirect('/')


class FinalizarCompraDetailView(TemplateView):
    template_name: str = 'finalizar-compra.html'

    
    
    def get(self, request):

        if request.session.has_key('carrinho'):

            request.session['redirect'] = '/finalizar-compra/'

            if request.session.has_key('cliente') and request.session.has_key('carrinho') != {}:

                if request.session['carrinho'] == {}:

                    return redirect('index')
                else:
                    return render(request, 'finalizar-compra.html')

        
            else:
                request.session['compra'] = True
                messages.success(request, f'Faça o login primeiro para efetuar a compra.' )
                print(request.session['compra'])
                return redirect('../login/') 

        else:
            return redirect('index')
        
        

    def post(self, request,  *args, **kwargs):
        carrinho = request.session['carrinho']

        id_carrinho = Carrinho.objects.all()
        id_filter = id_carrinho.last()

        if id_filter == None:
            new_id_carr = 1
        else:
            new_id_carr = id_filter.id + 1

        
        cliente_id = request.session['cliente']
        


        criar_carrinho = Carrinho(int(new_id_carr), timezone.now(), timezone.now(), int(cliente_id), True)
        criar_carrinho.save()

        # Salvar aneis

        for id_anel, dados in carrinho.items():
            id_aneis = CarrinhoAneis.objects.all()
            
            id_filter_anel = id_aneis.last()

            if id_filter_anel == None:
                new_id_anel = 1
            else:
                new_id_anel = int(id_filter_anel.id) + 1

            adicionar_anel = CarrinhoAneis(int(new_id_anel), int(new_id_carr), int(dados[6]), int(dados[1]), int(dados[3]) )
            adicionar_anel.save()

        print(carrinho)

        request.session['Compra'] = True
        messages.success(request, f'Obrigado pela compra!!!' )
        request.session.pop('carrinho')


        return redirect('/')




    
class ErroView(TemplateView):
    template_name: str = 'erro.html'
    return_url = None


class ErroCadastroView(TemplateView):
    template_name: str = 'erro-cadastro.html'
    return_url = None

