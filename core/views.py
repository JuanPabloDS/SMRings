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
            request.session['carrinho'] = {2: ['5', 'anel', '156151', '5'], 3: ['5', 'anel', '156151', '5']}
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
        carrinho_id =  Carrinho.objects.get(id=5)        # postData.get('carrinho_id')
        carrinho_id2 = carrinho_id.id
        anel_id = Anel.objects.get(id=(postData.get('anel_id')))
        anel_id2 = anel_id.nome
        quantidade = postData.get('quantidade')
        carrinho = request.session['carrinho']
        print(carrinho)
        loop = True
        n = 1

        while loop == True:
            if Anel.get_key(n, carrinho):
                +n
            else:
                print(f'-->>{carrinho}')
                loop = False
                novo_carrinho = {n: [carrinho_id2, anel_id2, quantidade ]}
                carrinho.update(novo_carrinho)
                print(carrinho)
                request.session['carrinho'] = carrinho
                print(request.session['carrinho'])


        carrinho_anel = CarrinhoAneis(carrinho_id=carrinho_id,
                            anel_id=anel_id,
                            quantidade=quantidade)
        
        print(carrinho_anel.anel_id)

        carrinho_anel.register()
        return redirect('/')




#  carrinho_anel = CarrinhoAneis(5, carrinho.id, anel.id, quantidade=3)