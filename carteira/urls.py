from django.urls import path
from carteira import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carteira/', views.lista_acao, name='lista_acao'),
    path('vendas/', views.lista_acao_vendas, name='lista_acao_vendas')
]
