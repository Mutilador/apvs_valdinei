from django.shortcuts import render
from django.utils import timezone
from .forms import ClienteForm
from django.http import HttpResponseRedirect

# Create your views here.
def cadastro_cliente(request):

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/register-car/')
    else:
        form = ClienteForm()

    return render(request, 'cliente/cadastro_cliente.html', {'form': form})


def register_car(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/register-car/')
    else:
        form = ClienteForm()

    return render(request, 'cliente/index2.html', {'form': form})