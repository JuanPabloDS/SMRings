from django.urls import path

from .views import IndexView, AneisDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('services', IndexView.as_view(), name='index#aneis'),
    path('aneis/<int:pk>', AneisDetailView.as_view(), name='aneis'),

]