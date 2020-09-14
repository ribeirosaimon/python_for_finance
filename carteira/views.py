from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Carteira
import requests
from django.views.generic import TemplateView

class GetDroplets(TemplateView):
    template_name = 'droplets.html'
    def get_context_data(self, *args, **kwargs):
        pass


class CarteiraView(ListView):
    model = Carteira
    template_name = 'home.html'
