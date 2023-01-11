from django.shortcuts import render, redirect, get_object_or_404
from .models import Contatos
from .forms import FormContatos
from django.contrib import messages


def home(request):
    contatos = Contatos.objects.all()
    context = {'contatos':contatos}
    return render(request, 'app/home.html', context)


def adicionar_contato(request):
    if request.method == 'POST':
        form = FormContatos(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato adicionado com sucesso.')
            return redirect('home')
        else:
            print(form.errors)
            messages.success(request, 'Erro ao adicionar contato.')
    else:
        form = FormContatos()

    operacao = 'Adicionar'
    context = {'form':form, 'operacao':operacao}
    return render(request, 'app/form_contato.html', context)

def editar_contato(request, pk=None):    
    contato = get_object_or_404(Contatos, pk=pk)
    if request.method == 'POST':
        form = FormContatos(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato atualizado com sucesso.')
            return redirect('home')
        else:
            print(form.errors)
            messages.success(request, 'Erro ao atualizar contato.')
    else:
        form = FormContatos(instance=contato)

    operacao = 'Editar'
    context = {'form':form, 'operacao':operacao, 'contato':contato}
    return render(request, 'app/form_contato.html', context)


def excluir_contato(request, pk=None):
    contato = get_object_or_404(Contatos, pk=pk)
    contato.delete()
    messages.success(request, 'Contato excluído com sucesso')
    return redirect('home')

