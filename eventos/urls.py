from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_eventos, name='ver_eventos'),  # Rota principal de /eventos/
  # Rota completa /eventos/url_para_eventos/
]
