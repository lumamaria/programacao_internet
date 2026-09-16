from django.shortcuts import render

from . import models


# Create your views here.
def projetoList(request):
  projetos = models.Projeto.objects.all()
  return render(request, 'projeto/lista.html', {
    'projetos': projetos
  })

def projetoDetail(request, projeto_id):
  projeto = models.Projeto.objects.get(id=projeto_id)
  return render(request, 'projeto/detalhe.html', {
    'projeto': projeto
  })