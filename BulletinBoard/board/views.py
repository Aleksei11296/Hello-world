from django.shortcuts import render
from django.views.generic import ListView
from .models import Ads

class AdsList(ListView):
    model = Ads
    ordering = 'heading'
    template_name = 'ads.html'
    context_object_name = 'ads'
    paginate_by = 10
# Create your views here.
