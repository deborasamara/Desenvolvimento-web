from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from . models import Pergunta

# Create your views here.
def index(request):
    enquetes = Pergunta.objects.order_by('-data_pub')[:10]
    contexto = {'lista_enquetes': enquetes}
    return render(request, 'enquetes/index.html', contexto)

def detalhes(request, pergunta_id):
    try:
        pergunta = Pergunta.objects.get(pk = pergunta_id)
    except Pergunta.DoesNotExist:
        raise Http404('Identificação de enquete inválida!')
    contexto= {'enquete': pergunta}
    return render(request, 'enquetes/detalhes.html', contexto)

def votacao(request, pergunta_id):
    resultado = 'Votação da enquete de número %s'
    return HttpResponse(resultado%pergunta_id)

def resultado(request, pergunta_id):
    resultado = 'Resultado da enquete de número %s'
    return HttpResponse(resultado%pergunta_id)

### Versões
"""
def index(request):
    lista = Pergunta.objects.all()
    template = loader.get_template('enquetes/index.html')
    contexto = {'lista_enquetes':lista}
    return HttpResponse(template.render(contexto, request))

def detalhes(request, pergunta_id):
    resultado = 'Detalhes da enquete de número %s'
    return HttpResponse(resultado%pergunta_id)

def votacao(request, pergunta_id):
    resultado = 'Votação da enquete de número %s'
    return HttpResponse(resultado%pergunta_id)
"""

