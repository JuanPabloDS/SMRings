from django.urls import path

from .views import IndexView, AneisDetailView, FinalizarCompraDetailView, ErroView, ErroCadastroView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('aneis/<int:pk>', AneisDetailView.as_view(), name='aneis'),
    path('finalizar-compra/', FinalizarCompraDetailView.as_view(), name='finalizar-compra'),
    path('erro', ErroView.as_view(), name='erro'),
    path('erro-cadastro/', ErroCadastroView.as_view(), name='erro no cadastro'),

]