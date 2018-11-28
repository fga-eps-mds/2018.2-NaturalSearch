---
layout: default
---

# Projeto

## Propriedades
|Nome | Tipo |..... | Descrição
------------ | ------------- | ------------- | -------------
**pronac** | **str** |  | Número do PRONAC
**ano_projeto** | **str** |  | Ano em que o projeto foi apresentado em dois dígitos. Formato AA
**nome** | **str** |  | Nome do projeto (valor exato ou parcial)
**cgccpf** | **str** |  | Cgc/Cpf do proponente
**proponente** | **str** |  | Nome do proponente do projeto (valor exato ou parcial)
**segmento** | **str** |  | Código do Segmento do projeto 
**area** | **str** |  | Código da Área do projeto 
**uf** | **str** |  | Estado de origem no formato EE 
**municipio** | **str** |  | Cidade 
**data_inicio** | **date** |  | Data de início no formato aaaa-mm-dd 
**data_termino** | **date** |  | Data de finalização no formato aaaa-mm-dd 
**mecanismo** | **str** |  |  
**enquadramento** | **str** |  |  
**valor_projeto** | **float** |  |  
**valor_captado** | **float** |  |  
**valor_proposta** | **float** |  |  
**valor_solicitado** | **float** |  |  
**valor_aprovado** | **float** |  |  |


Esse método recebe os atributos da classe projeto presentes na api Salic em formato JSON e insere no DB do DjangoRest:

```python

def get_projects_labels(embedded, count):
# This function receives the json and inserts projects data into DB
    for numero_projeto in range(0,count):
            # Second layer: embedded
            # projetos = embedded['projetos'][numero_projeto]['projetos']
            PRONAC = embedded['projetos'][numero_projeto]['PRONAC']
            ano_projeto = embedded['projetos'][numero_projeto]['ano_projeto']
            nome = embedded['projetos'][numero_projeto]['nome']
            cgccpf = embedded['projetos'][numero_projeto]['cgccpf']
            proponente = embedded['projetos'][numero_projeto]['proponente']
            segmento = embedded['projetos'][numero_projeto]['segmento']
            area = embedded['projetos'][numero_projeto]['area']
            UF = embedded['projetos'][numero_projeto]['UF']
            municipio = embedded['projetos'][numero_projeto]['municipio']
            data_inicio = embedded['projetos'][numero_projeto]['data_inicio']
            data_termino = embedded['projetos'][numero_projeto]['data_termino']
            mecanismo = embedded['projetos'][numero_projeto]['mecanismo']
            enquadramento = embedded['projetos'][numero_projeto]['enquadramento']
            valor_projeto = embedded['projetos'][numero_projeto]['valor_projeto']
            valor_captado = embedded['projetos'][numero_projeto]['valor_captado']
            valor_proposta = embedded['projetos'][numero_projeto]['valor_proposta']
            valor_solicitado = embedded['projetos'][numero_projeto]['valor_solicitado']
            valor_aprovado = embedded['projetos'][numero_projeto]['valor_aprovado']
            _links = embedded['projetos'][numero_projeto]['_links']

            # Para adicionar os projetos no banco descomentar as prox duas linhas
            # PS: nao rodar migrate/makemigrations com as prox duas linhas descomentadas

            project_instance = Project.objects.create(PRONAC=PRONAC, ano_projeto=ano_projeto, nome=nome, cgccpf=cgccpf, proponente=proponente, segmento=segmento, area=area, UF=UF, municipio=municipio, data_inicio= data_inicio, data_termino=data_termino, mecanismo=mecanismo, enquadramento=enquadramento, valor_projeto=valor_projeto, valor_captado=valor_captado, valor_proposta = valor_proposta, valor_solicitado=valor_solicitado, valor_aprovado=valor_aprovado)
            project_instance.save()
```
![projeto_API](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/projeto_API.png)

[ver imagem em tamanho original](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/projeto_API.png)
