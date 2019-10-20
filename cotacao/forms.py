from django import forms
from .models import HospedeModels, CotaçõesHospedeModels, CriançasDadoModels

class HospedeForms(forms.ModelForm):
    class Meta:
        model = HospedeModels
        fields = '__all__'

class CotaçãoForms(forms.ModelForm):
    class Meta:
        model = CotaçõesHospedeModels
        fields = '__all__'
