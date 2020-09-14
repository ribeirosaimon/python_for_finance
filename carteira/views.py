from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Carteira
#def home(request):
#    return render(request, 'home.html', {})

class CarteiraView(ListView):
    model = Carteira
    template_name = 'home.html'
