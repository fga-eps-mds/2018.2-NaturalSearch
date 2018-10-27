from django.db import models

class Project (models.Model):
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
    #situacao = models.CharField(max_length=200)
    mecanismo = models.CharField(max_length=200) 
    enquadramento = models.CharField(max_length=200) 
    valor_projeto = models.DecimalField(max_digits=10, decimal_places=2)
    #outras_fontes = models.DecimalField(max_digits=8, decimal_places=2)
    valor_captado =  models.DecimalField(max_digits=10, decimal_places=2)
    valor_proposta =  models.DecimalField(max_digits=10, decimal_places=2)
    valor_solicitado =  models.DecimalField(max_digits=10, decimal_places=2)
    valor_aprovado = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nome

class Proponent(models.Model):
    nome = models.CharField(max_length=200)
    responsavel = models.CharField(max_length=200)

    fisica = 'fisica'
    juridica = 'juridica'
    default = '--'
    TIPO_PESSOA = (
        (default,'--'),
        (fisica, 'fisica'),
        (juridica, 'juridica'),
    )

    tipo_pessoa = models.CharField(max_length=8, choices=TIPO_PESSOA, default=default)  
    UF = models.CharField(max_length=2) 
    municipio = models.CharField(max_length=200)
    total_captado = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.nome