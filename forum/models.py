from django.db import models
import datetime 
from django.utils import timezone

# Create your models here.
class Pergunta(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    detalhe = models.TextField(null=False)
    tentativa = models.TextField()
    data_criacao = models.DateTimeField("criado em")
    usuario = models.CharField(max_length=200, null=False, default="anonimo")

    def __str__(self):
        return "[" + str(self.id) + "]" + self.titulo
    def foi_publicada_recentemente(self):
        return self.data_criacao >= timezone.now() - datetime.timedelta(days=1)
    def strings_detalhada(self):
        return "id: " +str(self.id) + "; titulo : " +self.titulo + "; detalhe: " +self.detalhe + "; tentativa: " + self.tentativa
    
class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.TextField(null=False)
    votos = models.IntegerField(null=False)
    data_criacao = models.DateTimeField("criado em")
    usuario = models.CharField(max_length=200, null=False, default="anonimo")

    def __str__(self):
        return "[" + str(self.id) + "]" + self.texto
    def foi_publicada_recentemente(self):
        return self.data_criacao >= timezone.now() - datetime.timedelta(days=1)