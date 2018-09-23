---
layout: default
---

# Mapa de Requisitos

## Histórico de Revisão

|           Data          |         Versão         |       Descrição   |         Autores   |
|:----------------------:|:------------------------:|:---------------------:|:--------------:|
| 09/09/2018         |           0.1                | Versão inicial do Mapa de Requisitos | [Filipe Coelho Hilário Barcelos](https://github.com/FilipeKN4), [Igor Araújo de Sousa](https://github.com/zero101010) |
| 23/09/2018 | 0.2 | Mundança de épico e adição de features | [Filipe Coelho Hilário Barcelos](https://github.com/FilipeKN4) |

## Épicos

### Processamento de Dados da API Salic

| | |
|:--:|:--:|
| **Para** | Cidadãos, incentivadores e fornecedores  |
| **que** | desejam visualizar de forma mais clara informações disponíveis no Salic |
| **o** | Natural Search |
| **é uma** | aplicação Web |
| **que** | possibilita o consumo de dados da API Salic |
| **diferente** | - |
| **nossa solução** | consome dados referentes a projetos e propostas disponíveis no Salic(Sistema de Apoio às Leis de Incentivo à Cultura) e realiza o processamento visando demonstrar os relacionamentos entre eles.|

| | |
|:--:|:--:|
| **critérios de sucesso** | Consumir os dados da API Salic, realizar o processamento dos dados e disponibilizá-los com os devidos relacionamentos. |
| **no escopo** | Consumo de dados da API salic, processamento construindo os relacionamentos entre eles e a disponibilização dos dados processados. |
| **fora do escopo** | - |

#### Features

* [Criar estrutura do banco de dados]()
* [Consumir dados da API Salic]()
* [Realizar o processamento dos dados]()
* [Disponibilizar os dados processados]()

### Visualização em Grafos

| | |
|:--:|:--:|
| **Para** | cidadãos, incentivadores e fornecedores  |
| **que** | desejam visualizar de forma mais clara informações disponíveis no Salic |
| **o** | Natural Search |
| **é uma** | aplicação Web |
| **que** | possibilita a visualização de projetos e propostas |
| **diferente** | - |
| **nossa solução** | disponibiliza os resultados de pesquisa mais relevantes evidenciando as relações entre eles por meio de uma visualização em grafos |

| | |
|:--:|:--:|
| **critérios de sucesso** |  realizar pesquisa e disponibilizar os resultados em forma de grafos evidenciando os relacionamentos entre os dados |
| **no escopo** | Tela para pesquisa e Tela para exibição de resultados |
| **fora do escopo** | - |

#### Features

* [Popular banco de dados]()
* [Realizar pesquisa inteligente]()
* [Visualizar os dados relacionados]()
