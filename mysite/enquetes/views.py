from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bem vindo a aplicação de enquete!!!!. Disciplina de Desenvolvimento Web, 3° semestre, Matrícula 20231014040003 por Débora Samara dos Santos Rodrigues")
