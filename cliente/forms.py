#from django.forms import ModelForm
from .models import Cliente

#class ClienteForm(ModelForm):

#    class Meta:
#        model = Cliente
#        fields = ('nome','email','cidade','bairro','telefone')

from django import forms
import urllib.request,json


class ClienteForm(forms.Form):
    nome = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Nome','class':'mdl-textfield__input'}),max_length=200,required=True)
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'E-mail','class':'mdl-textfield__input'}),required=True)
    cidade = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Cidade','class':'mdl-textfield__input'}),max_length=100,required=True)
    bairro = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Bairro','class':'mdl-textfield__input'}),max_length=100,required=True)
    telefone = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Telefone','class':'mdl-textfield__input'}),max_length=10,required=True)


class FipeDetailsForm(forms.Form):
    user = forms.ModelChoiceField(queryset=Cliente.objects.all(),widget=forms.HiddenInput())
    marca = forms.ChoiceField(label='',required=True, widget=forms.Select(attrs={'id':'marcas-dropdown','class':'mdl-textfield__input'}))
    modelo = forms.ChoiceField(label='',required=True, widget=forms.Select(attrs={'id':'modelos-dropdown','class':'mdl-textfield__input'}))
    ano = forms.ChoiceField(label="",required=True, widget=forms.Select(attrs={'id':'anos-dropdown','class':'mdl-textfield__input'}))
    valor = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Valor do veiculo R$','id':'valor-fipe','class':'mdl-textfield__input'}),disabled=True)

