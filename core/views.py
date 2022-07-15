from genericpath import exists
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, View

from .models import Anel
from carrinho.models import Carrinho , CarrinhoAneis

# Class based View
class IndexView(TemplateView):
    template_name: str = 'index.html'
    return_url = None


    def get(self, request):
        IndexView.return_url = request.GET.get('return_url')

        context = {
        'aneis': Anel.objects.all()
        }

        if request.session.has_key('carrinho'):
            print(request.session['carrinho'])
            return render(request, "index.html", context)
        else:
            request.session['carrinho'] = {}
            print(request.session['carrinho'])
            print('não')
            return render(request, "index.html", context)



class AneisDetailView(DetailView):
    template_name: str = 'aneis.html'

    queryset = Anel.objects.all()

    def get_object(self):
        obj = super().get_object()
        return obj



    def post(self, request, *args, **kwargs):
        postData = request.POST
        c_carrinho =  Carrinho.objects.get(id=5)
        c_carrinho_id = c_carrinho.id
        anel = Anel.objects.get(id=(postData.get('anel_id')))
        anel_id = anel.nome
        anel_preco = Anel.real_br_money(anel.preco)
        anel_imagem = anel.imagem
        quantidade = postData.get('quantidade')
        carrinho = request.session['carrinho']
        print(f'carrinho{carrinho}')
        loop = True
        n = 1
        pk = str(n)

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

        
        

        # carrinho_anel.register()
        print(request)
        return redirect('/')

        
""" carrinho_anel = CarrinhoAneis(carrinho_id=carrinho_id,
                            anel_id=anel_id,
                            quantidade=quantidade)"""




#  carrinho_anel = CarrinhoAneis(5, carrinho.id, anel.id, quantidade=3)