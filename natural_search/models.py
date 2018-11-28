from django.db import models

class Project (models.Model):
    PRONAC = models.CharField(max_length=50) 
    ano_projeto = models.CharField(max_length=4, null=True) 	
    nome = models.CharField(max_length=1000) 
    cgccpf = models.CharField(max_length=14, null=True) 
    proponente = models.CharField(max_length=1000) 
    segmento = models.CharField(max_length=50, null=True) 
    area = models.CharField(max_length=50, null=True) 
    UF = models.CharField(max_length=2, null=True) 
    municipio = models.CharField(max_length=1000, null=True) 
    data_inicio = models.DateField(null=True) 
    data_termino = models.DateField(null=True) 
    #situacao = models.CharField(max_length=200)
    mecanismo = models.CharField(max_length=500, null=True) 
    enquadramento = models.CharField(max_length=1000, null=True) 
    valor_projeto = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    #outras_fontes = models.DecimalField(max_digits=8, decimal_places=2)
    valor_captado =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    valor_proposta =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    valor_solicitado =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    valor_aprovado = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    def __str__(self):
        return self.nome

class Proponent(models.Model):
    nome = models.CharField(max_length=1000)
    responsavel = models.CharField(max_length=1000, null=True)

    fisica = 'fisica'
    juridica = 'juridica'
    default = '--'
    TIPO_PESSOA = (
        (default,'--'),
        (fisica, 'fisica'),
        (juridica, 'juridica'),
    )

    tipo_pessoa = models.CharField(max_length=9, choices=TIPO_PESSOA, default=default, null=True)  
    UF = models.CharField(max_length=2, null=True) 
    municipio = models.CharField(max_length=1000, null=True)
    total_captado = models.DecimalField(max_digits=11, decimal_places=1, null=True)
    
    def __str__(self):
        return self.nome