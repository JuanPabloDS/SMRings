from django.urls import path

from .views import index, aneis

urlpatterns = [
    path('', index, name='index'),
    path('services', index, name='index#aneis'),
    path('aneis/<int:pk>', aneis, name='aneis'),

]