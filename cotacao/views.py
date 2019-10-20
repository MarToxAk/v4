from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import HospedeModels, CotaçõesHospedeModels
from .forms import HospedeForms, CotaçãoForms

class HospedeViews(LoginRequiredMixin, CreateView):
    model = HospedeModels
    form_class = HospedeForms
    template_name = 'cotacao/hospede.html'
    success_url = 'index'

class CotaçãoViews(LoginRequiredMixin, CreateView):
    model = CotaçõesHospedeModels
    form_class = CotaçãoForms
    template_name = 'cotacao/cotacao.html'


