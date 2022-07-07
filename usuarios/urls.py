from django.urls import path
from django.contrib.auth import views as auth_views # para autenticação e logout
from .views import login_page, register_page


urlpatterns = [
    path('login/', login_page, name='login'),
    path('cadastro/', register_page, name='cadastro'),
]

"""
path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/form.html'
    ), name='login'),

path('cadastro/', auth_views.LoginView.as_view(
        template_name='usuarios/cadastro.html'
    ), name='cadastro'),"""