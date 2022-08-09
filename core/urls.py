from django.urls import path

from .views import IndexView, AneisDetailView, ErroView, ErroCadastroView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('aneis/<int:pk>', AneisDetailView.as_view(), name='aneis'),
    path('erro', ErroView.as_view(), name='erro'),
    path('erro-cadastro/', ErroCadastroView.as_view(), name='erro no cadastro'),

]