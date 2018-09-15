from django.db import models

# Create your models here.
class Proposition(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    mecanismo = models.CharField(max_length=20)
    data_aceite = models.CharField(max_length=10)
    data_inicio = models.CharField(max_length=10)
    data_termino = models.CharField(max_length=10)
    data_arquivamento = models.CharField(max_length=10)
    acessibilidade = models.TextField()
    objetivos = models.TextField()
    justificativa = models.TextField()
    etapa = models.TextField()
    ficha_tecnica = models.TextField()
    impacto_ambiental = models.TextField()
    especificacao_tecnica = models.TextField()
    estrategia_execucao = models.TextField()
    providencia = models.TextField()
    democratizacao = models.TextField()
    sinopse = models.TextField()
    resumo = models.TextField()

    def insert_proposition():
        return 0
