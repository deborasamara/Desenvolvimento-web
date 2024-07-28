from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from django.views import generic
from django.urls import reverse
from . models import Pergunta, Alternativa
from django.views import View


# Create your views here.
class IndexView(View):
    template = 'enquetes/index.html'
    def get(self, request, *arg, **kwargs):
        enquetes = Pergunta.objects.order_by('-data_pub')[:10]
        contexto = {'lista_enquetes': enquetes}
        return render(request, self.template, contexto)

class DetalhesView(View):
    template = 'enquetes/detalhes.html'

    def resposta(self, request, pergunta, *error):
        contexto= {'enquete': pergunta, 'error':error}
        return render(request, self.template, contexto)

    def get(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
        return self.resposta(request, pergunta)

    def post(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
        try:
            id_alternativa = request.POST['escolha']
            alt = pergunta.alternativa_set.get(pk=id_alternativa)
        except(KeyError, Alternativa.DoesNotExist):
            error = 'você precisa selecionar uma alternativa'
            return self.resposta(request, pergunta, error)
        else:
            alt.quant_votos +=1
            alt.save()
            return HttpResponseRedirect(reverse(
                'enquetes:resultado', args=(pergunta.id,)
            ))


class ResultadoView(View):
    template = 'enquetes/resultado.html'
    def get(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
        contexto= {'enquete': pergunta}
        return render(request, self.template, contexto)


### Versões
"""
----------------------------
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

---------------------------

(versão que funcionava)

def index(request):
    enquetes = Pergunta.objects.order_by('-data_pub')[:10]
    contexto = {'lista_enquetes': enquetes}
    return render(request, 'enquetes/index.html', contexto)

def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    contexto= {'enquete': pergunta}
    return render(request, 'enquetes/detalhes.html', contexto)

def resultado(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    contexto= {'enquete': pergunta}
    return render(request, 'enquetes/resultado.html', contexto)

+ função votação
-------------------------------
class IndexView(generic.ListView):
    template_name = 'enquetes/index.html'
    def get_queryset(self):
        return Pergunta.objects.order_by('-data_pub')[:10]

class DetalhesView(generic.DetailView):
    model = Pergunta

class ResultadoView(generic.DetailView):
    model = Pergunta
    template_name = 'enquetes/resultado.html'

def votacao(request, pergunta_id):
     pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        id_alternativa = request.POST['escolha']
        alt = pergunta.alternativa_set.get(pk=id_alternativa)
    except(KeyError, Alternativa.DoesNotExist):
        contexto = {
        'enquete': pergunta,
        'error': 'Você precisa selecionar uma alternativa.'
        }
        return render(request, 'enquetes/detalhes.html', contexto)
    else:
        alt.quant_votos +=1
        alt.save()
        return HttpResponseRedirect(reverse(
            'enquetes:resultado', args=(pergunta.id,)
        ))




"""



