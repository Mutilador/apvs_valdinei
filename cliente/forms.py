from .models import Cliente, FipeDetail
from django import forms

CARRO_RESERVA = (
    ('7','7 dias R$ 10,00'),
    ('10', '14 dias R$ 20,00')
)

REBOQUE_DISTANCIA = (
    ('300','300Km R$ 22,22'),
    ('500','500Km R$ 32,03')
)

class ClienteForm(forms.Form):
    nome = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Nome','class':'mdl-textfield__input'}),max_length=200,required=True)
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'E-mail','class':'mdl-textfield__input'}),required=True)
    cidade = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Cidade','class':'mdl-textfield__input'}),max_length=100,required=True)
    bairro = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Bairro','class':'mdl-textfield__input'}),max_length=100,required=True)
    telefone = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Telefone','class':'mdl-textfield__input'}),max_length=10,required=True)


class FipeDetailsForm(forms.Form):
    user = forms.ModelChoiceField(queryset=Cliente.objects.all(),widget=forms.HiddenInput())
    marca = forms.CharField(label='',required=True, widget=forms.Select(attrs={'id':'marcas-dropdown','class':'mdl-textfield__input'}))
    modelo = forms.CharField(label='',required=True, widget=forms.Select(attrs={'id':'modelos-dropdown','class':'mdl-textfield__input'}))
    ano = forms.CharField(label="",required=True, widget=forms.Select(attrs={'id':'anos-dropdown','class':'mdl-textfield__input'}))
    valor = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Valor do veiculo R$','id':'valor-fipe','class':'mdl-textfield__input'}),max_length=20)
    dd_date = forms.DateTimeField(widget=forms.HiddenInput(),required=False)

class SeguroDetailForm(forms.Form):
    fipe_detail = forms.ModelChoiceField(queryset=FipeDetail.objects.all(),widget=forms.HiddenInput())
    choice_dano = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id':'dano-teceiros','class':'mdl-checkbox__input'}),required=False)
    choice_reboque_distancia = forms.CharField(widget=forms.RadioSelect(choices=REBOQUE_DISTANCIA,attrs={'class':'mdl-radio__button'}), max_length=3)
    choice_reembolso = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id':'reembolso','class':'mdl-checkbox__input'}),required=False)
    choice_reserva = forms.CharField(widget=forms.RadioSelect(choices=CARRO_RESERVA,attrs={'class':'mdl-radio__button'}), max_length=3)

