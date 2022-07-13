from urllib import request
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect
from django.contrib import messages  # Importar o messages
from django.views import View

from .models import Clientes

from django.contrib.auth import authenticate




class Login(View):
    return_url = None
  

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        try:
            req = request.session['cliente']
        except:
            req = ''

        if req == '':
            return render(request, 'usuarios/login.html')
        else:
            return redirect('/')


    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cliente = Clientes.get_cliente_by_email(email)
        error_message = None

        if cliente:
            flag = check_password(senha, cliente.senha)
            if flag:
                request.session['cliente'] = cliente.id
                nome_sobrenome = f'{cliente.nome} {cliente.sobrenome}'
                request.session['cliente_nome'] = nome_sobrenome


                print(request.session['cliente'])

                if Login.return_url:
                    print('12')
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    
                    

                    return redirect('/')
            else:
                error_message = 'Invalid 1 !!'
        else:
            error_message = 'Invalid 2 !!'

  
        print(email, senha)
        print(error_message)
        return render(request, 'usuarios/login.html', {'error': error_message})
  
  
def logout(request):
    request.session.clear()
    return redirect('/')


class Signup (View):
    def get(self, request):
        return render(request, 'usuarios/cadastro.html')
  
    def post(self, request):
        postData = request.POST
        nome = postData.get('nome')
        sobrenome = postData.get('sobrenome')
        telefone = postData.get('telefone')
        email = postData.get('email')
        senha = postData.get('senha')
        # validation
        value = {
            'nome': nome,
            'sobrenome': sobrenome,
            'telefone': telefone,
            'email': email
        }
        print(value)
        error_message = None
  
        cliente = Clientes(nome=nome,
                            sobrenome=sobrenome,
                            telefone=telefone,
                            email=email,
                            senha=senha)
        error_message = self.validarCliente(cliente)

        print(error_message)
        print(f'{cliente} asd')
  
        if not error_message:
            print(nome, sobrenome, telefone, email, senha)
            cliente.senha = make_password(cliente.senha)
            cliente.register()
            return redirect('/login/')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'usuarios/cadastro.html', data)
  
    def validarCliente(self, cliente):
        error_message = None
        if (not cliente.nome):
            error_message = "Por favor coloque ser primeiro nome !!"
        elif len(cliente.nome) < 3:
            error_message = 'Nome precisa ter mais do que 3 caracteres'
        elif not cliente.sobrenome:
            error_message = 'Por favor insira seu sobrenome'
        elif len(cliente.sobrenome) < 3:
            error_message = 'Sobrenome precisa ter mais do que 3 caracteres'
        elif not cliente.telefone:
            error_message = 'Insira seu numero'
        elif len(cliente.telefone) < 12:
            error_message = 'Numero precisa ter mais do que 12 caracteres'
        elif len(cliente.senha) < 5:
            error_message = 'Senha dever ter mais do que 5 caracteres'
        elif len(cliente.email) < 5:
            error_message = 'Email deve ter mais do 5 caracteres'
        elif cliente.isExists():
            error_message = 'Endereço de email já existe.'
        # saving
  
        return error_message




































#----------------------------------------------------------------
"""
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
                    "form": form
              }
    print("User logged in")
    #print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password) 
        print(user)
        #print(request.user.is_authenticated)
        if user is not None:
            #print(request.user.is_authenticated)
            login(request, user)
            print("Login válido")
            # Redireciona para uma página de sucesso.
            return redirect("/")
        else:
            #Retorna uma mensagem de erro de 'invalid login'.
            print("Login inválido")
    return render(request, "usuarios/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
                    "form": form
              }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        # messages.success(request, 'Cadastro feito com sucesso!' )
        return redirect("/login/")
    return render(request, "usuarios/cadastro.html", context)

"""