from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Projeto
from django.template import loader
from django.http import Http404
from django.shortcuts import render, redirect
from datetime import datetime
from dateutil.parser import parse




def index(request):
    return render(request, "projetos/index.html")


def projetos(request):
    lista_projetos = Projeto.objects.order_by("data_projeto")
    context = {"lista_projetos": lista_projetos }
    return render(request, "projetos/projetos.html", context)


def detalhe(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    return render(request, "projetos/detalhe.html", {"projeto": projeto})

def novo(request):
    return render(request, "projetos/novo.html")


def edit(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    return render(request, "projetos/edit.html", {"projeto": projeto})


def projeto_update(request, id):
    projeto = Projeto.objects.get(pk=id)
    if request.method == 'POST':

        print(request.POST.get('nome_projeto'))
        print(request.POST.get('descricao_projeto'))
        print(request.POST.get('data_projeto'))
        print(request.POST.get('foto_projeto'))

        try:
            projeto.nome_projeto = request.POST.get('nome_projeto')
            projeto.descricao_projeto = request.POST.get('descricao_projeto')
            projeto.foto_projeto = request.POST.get('foto_projeto')
            projeto.data_projeto = request.POST.get('data_projeto')
            try:
                projeto.data_projeto = parse(projeto.data_projeto).date()
            except ValueError:
                return render(request, 'item_form.html', {'error': 'Invalid date format. Please use a recognizable date format.'})
        except ValueError:
            print("Falhas ao salvar")
    return render(request, "projetos/detalhe.html", {"projeto": projeto})
    
def adicionar(request):
    if request.method == 'POST':

       #try:
        nome = request.POST.get('nome_projeto')
        descricao = request.POST.get('descricao_projeto')
        foto = request.POST.get('foto_projeto')
        data = request.POST.get('data_projeto')
        projeto = Projeto(nome_projeto=nome, descricao_projeto=descricao, data_projeto=data, foto_projeto=foto)
        projeto.save()
        print(projeto.id)
        return redirect(f'{projeto.id}/', {"projeto": projeto})  
        
    

def deletar(request, id):
    if request.method == 'POST':
        projeto = get_object_or_404(Projeto, pk=id)
        projeto.delete()
        return redirect('/projetos/projetos')


    # try:
    #     projeto = Projeto.objects.get(pk=id)
    # except Projeto.DoesNotExist:
    #     raise Http404("Projeto não existe")
    
    # template = loader.get_template("projetos/detalhe.html")
    # context = {"projeto": projeto}
    # return HttpResponse(template.render(context, request))




