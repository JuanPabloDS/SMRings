from django.urls import path
from .views import Login, Signup, logout



urlpatterns = [
    path('cadastro/', Signup.as_view(), name='cadastro'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
]
