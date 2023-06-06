
from django.views.generic import TemplateView, DetailView, ListView
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import Anel
from carrinho.models import Carrinho, CarrinhoAneis
from django.shortcuts import render, redirect


class IndexView(TemplateView):
    """Class based view Index"""

    template_name: str = 'index.html'
    return_url = None
    
    
    def get(self, request):
        """Função get para visualização dos dados enviados pelo backend """

        mensagem = ''
        IndexView.return_url = request.GET.get('return_url')
        request.session['redirect'] = 'index'  # Redirect para o carrinho

        if request.session.has_key('logado'):
            """Se a sessão 'logaado' estiver criada"""

            if request.session.has_key('compra'):
                """Verifica se a session compra foi criada e deleta a session"""
                request.session.pop('compra')
                request.session.pop('logado')

            else:
                """Recebe a session de logado e exibe o nome do cliente pela massage"""
                nome = request.session['logado']
                messages.success(request, f'Bem vindo {nome}!' )
                request.session.pop('logado')  # Apaga a session de logado

        if self.request.GET.get("search"):
            """Recebe os dados da busca que são passados na URL"""

            search = self.request.GET.get("search")  # Armazena os dados em uma variável
            request.session['mensagem'] = f'Resultado para pesquisa: {search.title()}'
            query = self.request.GET.get("search")
            values = Anel.objects.filter(
                Q(nome__icontains=query)
            )

            mensagem = request.session['mensagem']  # Armazena o resultado da pesquisa passado na session

            if len(values) == 0:
                """Faz a verificação se os dados da pesquisa do banco retornaram vazios"""
                request.session['mensagem'] = [mensagem, 'vazio']
                
            else:
                """Cria na session 'mensagem' informações para usar como parametros na exibição"""
                request.session['mensagem'] = [mensagem, '']
        else:
            """Se não houver requisição para search busca todos os aneis cadastrados"""
            request.session['mensagem'] = ''
            values = Anel.objects.all()

        if self.request.GET.get("page"):
            pass
        else:
            pass
        
        # Paginação dos aneis cadastrodos

        paginator = Paginator(values, 6) # Mostra 6 aneis por página

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


        context = {
            'aneis': aneis,
            'mensagem': mensagem,
        }


        if request.session.has_key('carrinho'):
            """Se a session carrinho estiver criada retorna para index"""
            return render(request, "index.html", context)
        else:
            """Se a session carrinho não estiver criada cria a session vazia"""
            request.session['carrinho'] = {}
            return render(request, "index.html", context)


class AneisDetailView(DetailView):
    """Class based view Aneis"""

    template_name: str = 'aneis.html'

    def get(self, request, pk):
        """Função get para visualização dos dados enviados pelo backend"""

        request.session['redirect'] = f'../aneis/{pk}'  # Retorna o redirect para o carrinho

        anel = Anel.objects.get(id=pk)  # pega os dados do anel no banco de dados e armazena na variável
        
        context = {
            'anel' : anel
            }
        return render(request, 'aneis.html', context)


    def post(self, request, *args, **kwargs):
        """Envia os dados do anel para o carrinho via POST"""

        postData = request.POST  # Recebe os dados do POST

        anel = Anel.objects.get(id=(postData.get('anel_id')))  # Armazena os dados do anel na variável
        anel_id = anel.id  # Armazena o ID do anel na váriavel
        anel_nome = anel.nome   # Armazena o nome do anel na váriavel
        anel_preco = Anel.real_br_money(anel.preco)  # Armazena o preço do anel formatado
        anel_imagem = anel.imagem  # Armazena o endereço da imagem
        print(anel_imagem)
        quantidade = postData.get('quantidade')  # Armazena a qauntidade do anel
        tamanho = postData.get('tamanho')  # Armazena o tamanho do anel
        carrinho = request.session['carrinho']  # Armazena os dados da session carrinho
        preco_qtd = int(quantidade) * anel.preco  # multiplica a quantidade pelo preço
        anel_caminho = anel.caminho

        # Verifica se o Tamanho e quantidade possuem valores validos
 
        try:
            test_qtd = int(quantidade)
            test_tam = int(tamanho)
            listar = [num for num in anel.tamanho.all()]
            lista2 = ([str(num) for num in listar])

            for num in lista2:   
                if test_tam == int(num):
                    erro = False
            if erro == True or test_qtd > 50:
                return redirect('erro')
        except:
            return redirect('erro')

        # Verifica se o ID já existe dentro da session carrinho

        loop = True
        n = 1
        pk = str(n)
        total = 0
  
        while loop == True:
            """Faz um loop verificando o ultimo ID dentro do carrinho para criar um novo"""
            if Anel.get_key(pk, carrinho):
                n += 1
                pk = str(n)
            else:
                """Quando o ultimo Id é verificado o loop acaba e é adicionado os dados do novo anel no carrinho"""
                loop = False
                novo_carrinho = {pk: [ anel_nome, quantidade, anel_preco, tamanho, str(anel_imagem),  str(Anel.real_br_money(preco_qtd)), str(anel_id) ]}
                carrinho.update(novo_carrinho)
                request.session['carrinho'] = carrinho
                messages.success(request, 'Anel enviado com sucesso para o carrinho!' )


        for preco in request.session['carrinho'].values():
            """Salva o todal da soma dos aneis em uma session"""
            anel_total = preco[2]
            quantidade_tl = int(preco[1])
            totais = Anel.dolar_money(anel_total) * quantidade_tl
            total = total + totais
            total_conv = Anel.real_br_money(total)
            request.session['total'] = total_conv

        return redirect('/')


class FinalizarCompraDetailView(TemplateView):
    """Class based view Finalizar Compra"""
    template_name: str = 'finalizar-compra.html'

    def get(self, request):
        """Função get para visualização dos dados enviados pelo backend"""

        if request.session.has_key('carrinho'):
            """Verifica se existe session carrinho criada"""

            request.session['redirect'] = '/finalizar-compra/' # Retorna o redirect para o carrinho 

            if request.session.has_key('cliente') and request.session.has_key('carrinho') != {}:
                """Se existir a session cliente e carrinho"""
                if request.session['carrinho'] == {}:
                    """Se o carrinho estiver vazio volta para Index"""
                    return redirect('index')
                else:
                    """Se não entra na página de finalizar compra"""
                    return render(request, 'finalizar-compra.html')

            else:
                """Se não estiver logado como cliente redireciona para a página de login"""
                request.session['compra'] = True
                messages.success(request, f'Faça o login primeiro para efetuar a compra.' )
                return redirect('../login/') 

        else:
            """Redireciona para Index se não existir session carrinho"""
            return redirect('index')
        
        
    def post(self, request,  *args, **kwargs):
        """Finaliza a compra via POST"""
        carrinho = request.session['carrinho']
        id_carrinho = Carrinho.objects.all()  # Pega o ID do carrinho
        id_filter = id_carrinho.last()  # pega o ID do ultimo carrinho cadastrado no banco de dados

        if id_filter == None:
            """Se o carrinho do banco estiver vazio o ID retorna none e um novo ID é criado"""
            new_cart_id = 1
        else:
            """Se já existir adiciona um novo ID"""
            new_cart_id = id_filter.id + 1

        
        cliente_id = request.session['cliente']  # Pega o cliente logado e armazena na váriavel
        criar_carrinho = Carrinho(int(new_cart_id), timezone.now(), timezone.now(), int(cliente_id), True)  # Cria carrinho para salvar no banco
        criar_carrinho.save()  # Salva o carrinho no banco

        # For usado para salvar os aneis dentro do banco
        for id_anel, dados in carrinho.items():
            id_aneis = CarrinhoAneis.objects.all()  # Pega todos os aneis dentro do carrinho no banco de dados
            
            id_filter_anel = id_aneis.last()  # pega o ID do ultimo anel do carrinho cadastrado no banco de dados

            if id_filter_anel == None:
                """Se o anel no carrinho dentro do banco estiver vazio o ID retorna none e um novo ID é criado"""
                new_id_anel = 1
            else:
                """Se já existir adiciona um novo ID"""
                new_id_anel = int(id_filter_anel.id) + 1

            adicionar_anel = CarrinhoAneis(int(new_id_anel), int(new_cart_id), int(dados[6]), int(dados[1]), int(dados[3]) ) # Cria uma lista com dados do anel para salvar no banco
            adicionar_anel.save()  # Salva os dados do anel no banco

        request.session['Compra'] = True  # Session indicando que a compra foi bem sucedida
        messages.success(request, f'Obrigado pela compra!!!' )
        request.session.pop('carrinho')  # Apaga a session do carrinho


        return redirect('/')  # Redireiciona para Index



class ErroView(TemplateView):
    """Class Based View usada para redireicionar a página de erro"""
    template_name: str = 'erro.html'
    return_url = None


class ErroCadastroView(TemplateView):
    """Class Based View usada para redireicionar a página de erro no cadastro dos dados"""
    template_name: str = 'erro-cadastro.html'
    return_url = None

