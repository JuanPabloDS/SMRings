from django.urls import path

from .views import index, aneis

urlpatterns = [
    path('', index, name='index'),
    path('aneis.html', aneis, name='aneis')

]