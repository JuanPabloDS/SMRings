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
            return render(request, "index.html", context)
        else:
            request.session['carrinho'] = {}
            return render(request, "index.html", context)


    
    """def get(self, request, **kwargs):
        IndexView.return_url = request.GET.get('return_url')
        context = super(IndexView, self).get_context_data(**kwargs)
        context['aneis'] = Anel.objects.all()

        if request.session.has_key('carrinho'):
            return render(request, "index.html")
        else:
            request.session['carrinho'] = {}
            return render(request, "index.html")"""


# request.session['carrinho']

class AneisDetailView(DetailView):
    template_name: str = 'aneis.html'

    queryset = Anel.objects.all()

    def get_object(self):
        obj = super().get_object()
        return obj



    def post(self, request, *args, **kwargs):
        postData = request.POST
        carrinho_id =  Carrinho.objects.get(id=5)        # postData.get('carrinho_id')
        anel_id = Anel.objects.get(id=(postData.get('anel_id')))
        quantidade = postData.get('quantidade')

        """carrinho_cheio = ''

        if carrinho_cheio == '':
            request.session['cliente'] = {}
            carrinho = request.session['cliente']
        """
        

        carrinho_anel = CarrinhoAneis(carrinho_id=carrinho_id,
                            anel_id=anel_id,
                            quantidade=quantidade)
        
        print(carrinho_anel.anel_id)

        carrinho_anel.register()
        return redirect('/')




#  carrinho_anel = CarrinhoAneis(5, carrinho.id, anel.id, quantidade=3)