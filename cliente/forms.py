#from django.forms import ModelForm
#from .models import Cliente

#class ClienteForm(ModelForm):

#    class Meta:
#        model = Cliente
#        fields = ('nome','email','cidade','bairro','telefone')

from django import forms

class ClienteForm(forms.Form):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Nome'}),max_length=200,required=True)
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'E-mail'}),required=True)
    cidade = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Cidade'}),max_length=100,required=True)
    bairro = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Bairro'}),max_length=100,required=True)
    telefone = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Telefone'}),max_length=10,required=True)
