from django.shortcuts import render
from django.utils import timezone
from .forms import ClienteForm, FipeDetailsForm, SeguroDetailForm
from .models import Cliente, FipeDetail
from django.http import HttpResponseRedirect

# Create your views here.
def cadastro_cliente(request):

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            newCliente = Cliente()
            newCliente.nome = form.cleaned_data['nome']
            newCliente.email = form.cleaned_data['email']
            newCliente.telefone = form.cleaned_data['telefone']
            newCliente.cidade = form.cleaned_data['cidade']
            newCliente.bairro = form.cleaned_data['bairro']
            newCliente.save()
            form = FipeDetailsForm(initial={'user': newCliente})
            return render(request, 'fipe/veiculo_cadastro.html', {'form': form})
    else:
        form = ClienteForm()

    return render(request, 'cliente/cadastro_cliente.html', {'form': form})


# Create your views here.
def fipe_register(request):
    if request.method == "POST":
        form = FipeDetailsForm(request.POST)
        if form.is_valid():
            newFipe = FipeDetail()
            newFipe.user = form.cleaned_data['user']
            newFipe.marca = form.cleaned_data['marca']
            newFipe.modelo = form.cleaned_data['modelo']
            newFipe.ano = form.cleaned_data['ano']
            newFipe.valor = form.cleaned_data['valor']
            newFipe.dd_date = form.cleaned_data['dd_date']
            newFipe.save()
            return HttpResponseRedirect('/seguro_detail/')
    else:
        form = FipeDetailsForm()

    return render(request, 'fipe/seguro_detail.html', {'form': form})

def seguro_detail(request):
    if request.method == "POST":
        form = SeguroDetailForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/resumo/')
    else:
        form = SeguroDetailForm()
    return render(request, 'fipe/seguro_detail.html', {'form': form})