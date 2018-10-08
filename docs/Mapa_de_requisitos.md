---
layout: default
---

# Mapa de Requisitos

## Histórico de Revisão

|           Data          |         Versão         |       Descrição   |         Autores   |
|:----------------------:|:------------------------:|:---------------------:|:--------------:|
| 09/09/2018         |           0.1                | Versão inicial do Mapa de Requisitos | [Filipe Coelho Hilário Barcelos](https://github.com/FilipeKN4), [Igor Araújo de Sousa](https://github.com/zero101010) |
| 23/09/2018 | 0.2 | Mundança de épico e adição de features | [Filipe Coelho Hilário Barcelos](https://github.com/FilipeKN4) |
| 08/10/2018 | 0.3 | Mundança de escopo do projeto | [Filipe Coelho Hilário Barcelos](https://github.com/FilipeKN4) |

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
| **nossa solução** | consome dados referentes a projetos disponíveis no Salic(Sistema de Apoio às Leis de Incentivo à Cultura) e realiza o processamento dos dados visando retirar os dados não selecionados e adequar a um banco de dados orientado à grafos. |

| | |
|:--:|:--:|
| **critérios de sucesso** | Consumir os dados da API Salic, realizar o processamento dos dados e disponibilizá-los com os devidos relacionamentos. |
| **no escopo** | Consumo de dados da API salic, processamento removendo dados inutilizados e evidenciando os relacionamentos entre eles, além da disponibilização dos dados processados. |
| **fora do escopo** | - |

#### Features

* Criar estrutura do banco de dados
* Consumir dados da API Salic
* Realizar o processamento dos dados
* Disponibilizar os dados processados

### Visualização em Grafos

| | |
|:--:|:--:|
| **Para** | cidadãos, incentivadores e fornecedores  |
| **que** | desejam visualizar de forma mais clara informações disponíveis no Salic |
| **o** | Natural Search |
| **é uma** | aplicação Web |
| **que** | possibilita a visualização de projetos |
| **diferente** | - |
| **nossa solução** | disponibiliza os resultados de pesquisa e proporciona a visualização de forma individual e mais detalhada de modo que se torna possível visualizar as informações mais relevantes do projeto de forma mais limpa e intuitiva. |

| | |
|:--:|:--:|
| **critérios de sucesso** |  realizar pesquisa e disponibilizar os resultados em forma de grafos evidenciando os relacionamentos entre os dados |
| **no escopo** | Tela para pesquisa, Tela para exibição de resultados e telas para visualização das informações relacionadas por meio de grafos |
| **fora do escopo** | - |

#### Features

* Popular banco de dados
* Realizar pesquisa
* Visualizar os dados relacionados
