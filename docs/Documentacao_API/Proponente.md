---
layout: default
---


# Proponente

## Propriedades
|Nome| Tipo | Descrição | Notas
------------ | ------------- | ------------- | -------------
**nome** | **str** |  | Nome do proponente (valor exato ou parcial)
**responsavel** | **str** |  | 
**tipo_pessoa** | **str** |  | Tipo de pessoa  
**uf** | **str** |  | Estado 
**municipio** | **str** |  | Cidade 
**total_captado** | **float** |  | |

Esse método recebe os atributos da classe proponente presentes na api Salic em formato JSON e insere no DB do DjangoRest:

```python

def get_proponents_labels(embedded, count):
# This function receives the json and inserts proponent data into DB
        for proponent_number in range(0, count):
                # Second layer: embedded
                # proponents.append(embedded['proponentes'][proponent_number])
                nome = embedded['proponentes'][proponent_number]['nome']
                responsavel = embedded['proponentes'][proponent_number]['responsavel']
                tipo_pessoa = embedded['proponentes'][proponent_number]['tipo_pessoa']
                UF = embedded['proponentes'][proponent_number]['UF']
                municipio = embedded['proponentes'][proponent_number]['municipio']
                total_captado = embedded['proponentes'][proponent_number]['total_captado']

                # Para adicionar os proponentes no banco descomentar as prox duas linhas
                # PS: nao rodar migrate/makemigrations com as prox duas linhas comentadas

                proponent_instance = Proponent.objects.create(nome = nome, responsavel = responsavel, tipo_pessoa = tipo_pessoa, UF=UF, municipio= municipio, total_captado=total_captado )
                proponent_instance.save()
```

![proponente_API](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/proponente_API.png)

[ver imagem em tamanho original](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/proponente_API.png)