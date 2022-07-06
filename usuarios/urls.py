from django.urls import URLPattern, path
from django.contrib.auth import views as auth_views # para autenticação e logout

urlpatterns = [
    # path('', view, name=""),
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/form.html'
    ), name='login')
]