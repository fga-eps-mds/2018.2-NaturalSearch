from django.db import models

class ProjetoList (models.Model):
    PRONAC = models.CharField(max_length=50) 
    ano_projeto = models.CharField(max_length=4) 	
    nome = models.CharField(max_length=200) 
    cgccpf = models.CharField(max_length=14) 
    proponente = models.CharField(max_length=200) 
    segmento = models.CharField(max_length=50) 
    area = models.CharField(max_length=50) 
    UF = models.CharField(max_length=2) 
    municipio = models.CharField(max_length=200) 
    data_inicio = models.DateField() 
    data_termino = models.DateField() 
    situacao = models.CharField(max_length=200)
    mecanismo = models.CharField(max_length=200) 
    enquadramento = models.CharField(max_length=20) 
    valor_projeto = models.CharField(max_length=20) 
    outras_fontes = models.CharField(max_length=20) 
    valor_captado =  models.CharField(max_length=20) 
    valor_proposta =  models.CharField(max_length=20) 
    valor_solicitado =  models.CharField(max_length=20) 
    valor_aprovado = models.CharField(max_length=20) 
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

    def __str__(self):
        return self.nome