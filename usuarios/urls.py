from django.urls import path
from django.contrib.auth import views as auth_views # para autenticação e logout
from .views import Login, Signup



urlpatterns = [
    path('cadastro/', Signup.as_view(), name='cadastro'),
    path('login/', Login.as_view(), name='login'),
    # path('logout', logout, name='logout'),
]





"""
urlpatterns = [
    path('login/', login_page, name='login'),
    path('cadastro/', register_page, name='cadastro'),
]
"""

"""
path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/form.html'
    ), name='login'),

path('cadastro/', auth_views.LoginView.as_view(
        template_name='usuarios/cadastro.html'
    ), name='cadastro'),"""