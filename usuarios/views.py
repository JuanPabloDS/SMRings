from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Clientes


class Login(View):
    """Class based view usada para login do cliente"""
    return_url = None

    def get(self, request):
        """Função get para visualização dos dados enviados pelo backend """
        
        Login.return_url = request.GET.get('return_url')  # Retorna url
        request.session['redirect'] = 'login'  # Redirect usado no carrinho

        context = {
            'login': 'True',  # Retorna context como verdadeiro
        }

        if request.session.has_key('cliente'):
            """Se o cliente já estiver logado retorna para index"""
            return redirect('/')
        else:
            """Se não estiver logado é enviado para página de login"""
            return render(request, 'login.html', context)
    

    def post(self, request):
        """Faz a verificação dos dados do cliente ao enviar os dados via POST"""
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cliente = Clientes.get_cliente_by_email(email)

        if cliente:
            """Verifica se o email inserido estava no banco de dados de usuarios"""

            flag = check_password(senha, cliente.senha)  # Verifica se a senha inserida é a mesma do cliente

            if flag:
                request.session['cliente'] = cliente.id  # Salva o id do cliente na session
                nome_sobrenome = f'{cliente.nome} {cliente.sobrenome}'  # Variavel contendo nome e sobrenome do usuario
                request.session['cliente_nome'] = nome_sobrenome  # Salvando nome na session

                if Login.return_url:

                    return HttpResponseRedirect(Login.return_url)
                else:
                    if request.session.has_key('compra'):
                        """Se a requisição tiver a session compra ao logar redireiciona para 
                        finalizar compra"""
                        request.session['logado'] = nome_sobrenome
                        return redirect('/finalizar-compra/')
                        
                    else:
                        """Redireiciona para página de login ao logar como cliente"""
                        Login.return_url = None
                        request.session['logado'] = nome_sobrenome

                    return redirect('/')

            else:
                messages.error(request, 'Login ou senha inválido(s)!' )
        else:
            messages.error(request, 'Login ou senha inválido(s)!' )

        return render(request, 'login.html')
  
  
def logout(request):
    """Sair da conta do cliente"""
    request.session.pop('cliente')
    return redirect('/')


class Signup (View):
    """Class Based View usado para cadastro do cliente"""
    
    def get(self, request):
        """Função get para visualização dos dados enviados pelo backend """

        request.session['redirect'] = 'cadastro'  # Redirect usado no carrinho


        context = {
            'sigup': 'True',  # Retorna contex do cadastro True
        }

        if request.session.has_key('cliente'):
            """Se o cliente já estiver logado retorna para index"""
            return redirect('/')
        else:
            """Se não estiver logado é enviado para página de login"""
            return render(request, "cadastro.html", context)
  
    def post(self, request):
        """Faz o cadastro e verificação dos dados do cliente no banco via POST"""
        postData = request.POST  # Recebe os dados do POST
        nome = postData.get('nome')
        sobrenome = postData.get('sobrenome')
        telefone = postData.get('telefone')
        email = postData.get('email')
        senha = postData.get('senha')

        # Criar o cliente
        cliente = Clientes(nome=nome,
                            sobrenome=sobrenome,
                            telefone=telefone,
                            email=email,
                            senha=senha)

        error_message = self.validarCliente(cliente) 

        if not error_message:
            """Se não tiver mensagem de erro"""
            cliente.senha = make_password(cliente.senha)  # Cria a senha para cliente
            cliente.register()  # Registrar o cliente no banco
            messages.success(request, 'Cadastro efetuado com sucesso!! Faça o login aqui.' )
            return redirect('/login/')
        else:
            """Se existir dado invalidos retorna para página de erro"""
            return redirect('/erro-cadastro/')
  
    def validarCliente(self, cliente):
        """Função criada para validação dos dados do cliente"""
        error_message = None

        if (not cliente.nome):
            error_message = 'Insira o nome corretamente'
        elif len(cliente.nome) < 3:
            error_message = 'Nome precisa ter mais do que 3 caracteres'
        elif len(cliente.nome) > 50:
            error_message = 'Nome precisa ter mais do que 3 caracteres'
        elif not cliente.sobrenome:
            error_message = 'Por favor insira seu sobrenome'
        elif len(cliente.sobrenome) < 3:
            error_message = 'Sobrenome precisa ter mais do que 3 caracteres'
        elif len(cliente.sobrenome) > 50:
            error_message = 'Sobrenome precisa ter mais do que 3 caracteres'
        elif not cliente.telefone:
            error_message = 'Insira seu numero'
        elif len(cliente.telefone) < 14:
            error_message = 'Numero precisa ter mais do que 14 caracteres'
        elif len(cliente.telefone) > 15:
            error_message = 'Numero precisa ter mais do que 14 caracteres'
        elif len(cliente.senha) < 5:
            error_message = 'Senha dever ter mais do que 5 caracteres'
        elif len(cliente.senha) > 100:
            error_message = 'Senha dever ter mais do que 5 caracteres'
        elif len(cliente.email) < 5:
            error_message = 'Email deve ter mais do 5 caracteres'
        elif len(cliente.email) > 50:
            error_message = 'Email deve ter mais do 5 caracteres'
        elif cliente.isExists():
            error_message = 'Endereço de email já existe.'

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