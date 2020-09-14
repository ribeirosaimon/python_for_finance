from django.urls import path
from .views import CarteiraView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', CarteiraView.as_view(), name='home'),
]
