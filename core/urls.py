from django.urls import path

from .views import IndexView, AneisDetailView # LoginView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('aneis/<int:pk>', AneisDetailView.as_view(), name='aneis'),

]