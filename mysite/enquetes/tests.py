import datetime
from django.utils import timezone
from django.urls import reverse
from django.test import TestCase
from . models import Pergunta

# Create your tests here.
# Função utilitária para a criação de perguntas no banco de dados
def criar_pergunta(texto, quant_dias):
    """

    Cria uma pergunta no banco com um texto e data

    """
    data = timezone.now() + datetime.timedelta(days = quant_dias)
    return Pergunta.objects.create(texto = texto, data_pub = data)

class IndexViewTest(TestCase):
    def test_sem_pergunta_cadastrada(self):
        """
        É esperado a exibição da mensagem de erro/ Aviso de que não há enquetes cadastradas.
        """
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Nenhuma enquete cadastrada')
        self.assertQuerysetEqual(
            resposta.context('pergunta_list'), []
        )
    def test_com_pergunta_no_futuro(self):
        """
        É esperado a exibição da mensagem de erro/ Aviso de que não há enquetes cadastradas.
        """
        criar_pergunta('Pergunta no futuro', 1)
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Nenhuma enquete cadastrada')
        self.assertQuerysetEqual(
            resposta.context('pergunta_list'), []
        )
    def test_com_pergunta_no_passado(self):
        """
        Que essa pergunta seja listada
        """
        criar_pergunta('pergunta no passado', -1)
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Nenhuma enquete cadastrada')
        self.assertQuerysetEqual(
           ['pergunta_list'], ['<Pergunta: pergunta no passado>']
        )
    def test_com_pergunta_no_passado_e_outra_no_futuro(self):
        """

        """
        criar_pergunta('Pergunta no passado 1', -2)
        criar_pergunta('Pergunta no passado 2', -1)

class PerguntaModelTest(TestCase):
    def test_publicada_recentemente_pergunta_no_futuro(self):
        """
        O método para pergunta no futuro DEVE retornar false

        AJEITAR OS MÉTODOS TODOS !!!!!!!!!!!
        """
        tempo = timezone.now() + datetime.timedelta(seconds=1)
        p1 = Pergunta(data_pub = tempo)
        self.assertIS(p.publicada_recentemente(), False)

    def test_publicada_recentemente_pergunta_no_futuro(self):
        """
        O método para pergunta no passado DEVE retornar false
        """
        tempo = timezone.now() + datetime.timedelta(seconds=1)
        p1 = Pergunta(data_pub = tempo)
        self.assertIS(p.publicada_recentemente(), False)

    def test_publicada_recentemente_pergunta_no_futuro(self):
        """
        O método para pergunta no presente DEVE retornar true
        """
        tempo = timezone.now() + datetime.timedelta(seconds=1)
        p1 = Pergunta(data_pub = tempo)
        self.assertIS(p.publicada_recentemente(), False)






