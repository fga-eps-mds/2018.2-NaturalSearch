---
layout: default
---

# Histórias de Usuário

## Histórico de Revisão

|           Data          |         Versão         |       Descrição   |         Autores   |
|:----------------------:|:------------------------:|:---------------------:|:--------------:|
| 09/09/2018         |           0.1                | Versão inicial das Histórias de Usuário | [Filipe Coelho Hilário Barcelos](https://github.com/FilipeKN4), [Igor Araújo de Sousa](https://github.com/zero101010) |
| 23/09/2018         |           0.2                | Adição de novas histórias de usuário e histórias técnicas | [Filipe Coelho Hilário Barcelos](https://github.com/FilipeKN4) |
| 03/10/2018         |           0.3                | Adição de novas histórias para a feature de disponibilizar dados processados | [Filipe Coelho Hilário Barcelos](https://github.com/FilipeKN4) |


## 1. Processamento de Dados da API Salic

### 1.1 Criar estrutura do banco de dados

|**história de usuário** | **descrição** |
|:---:|:---:|
| criar projeto | Eu, como desenvolvedor, desejo criar uma tabela de projetos no banco de dados da aplicação. |
| criar proposta | Eu, como desenvolvedor, desejo criar uma tabela de propostas no banco de dados da aplicação. |

### 1.2 Consumir dados da API Salic

| **história de usuário** | **descrição** |
|:---:|:---:|
| consumir dados de projetos | Eu, como desenvolvedor, desejo consumir dados de projetos da API Salic. |
| consumir dados de propostas  | Eu, como desenvolvedor, desejo consumir dados de propostas da API Salic. |

### 1.3 Realizar o processamento dos dados

| **história de usuário** | **descrição** |
|:---:|:---:|
| definir categorias dos dados | Eu, como desenvolvedor, desejo definir as categorias dos dados de projetos e propostas de acordo com o resumo. |
| classificar os dados | Eu, como desenvolvedor, desejo classificar os dados de projetos e propostas nas categorias encontradas. |
| relacionar os dados | Eu como desenvolvedor, desejo relacionar os dados de projetos e propostas de acordo com as categorias em que foram classificados. |

### 1.4 Disponibilizar os dados Processados

| **história de usuário** | **descrição** |
|:---:|:---:|
| converter os dados para o formato JSON | Eu, como desenvolvedor, desejo converter os dados processados para o formato JSON. |
| criar API para fornecer o JSON | Eu, como desenvolvedor, desejo criar uma API para fornecer os dados processados em formato JSON. |

## 2. Visualização em Grafos

### 2.1 Popular banco de dados

| **história de usuário** | **descrição** |
|:---:|:---:|
| popular com projetos | Eu, como desenvolvedor, desejo popular a tabela de projetos do banco de dados com os dados consumidos da API Salic. |
| popular com propostas | Eu, como desenvolvedor, desejo popular a tabela de propostas do banco de dados com os dados consumidos da API Salic. |

### 2.2 Realizar pesquisa inteligente

| **história de usuário** | **descrição** |
|:---:|:---:|
| realizar pesquisa | Eu, como usuário, desejo realizar uma pesquisa com qualquer palavra, frase, ou número que interessar. |
| pesquisar projetos | Eu, como usuário, desejo receber como resultados da pesquisa apenas projetos. |
| pesquisar propostas | Eu, como usuário, desejo receber como resultados da pesquisa apenas propostas. |
| filtrar pesquisa | Eu, como desenvolvedor, desejo filtrar os resultados da pesquisa e fornecer apenas respostas relevantes ao que foi submetido pelo usuário. |

### 2.3 Visualizar os dados relacionados

| **história de usuário** | **descrição** |
|:---:|:---:|
| criar tela inicial | Eu, como desenvolvedor, desejo criar uma tela inicial para visualizar informações gerais sobre o produto. |
| criar tela de visualização | Eu, como desenvolvedor, desejo criar a tela de visualização dos resultados da pesquisa por meio de grafos. |

## Histórias Técnicas de Usuário

| **história de usuário** | **descrição** |
|:---:|:---:|
| modificar banco de dados | Eu, como desenvolvedor, desejo modificar o banco de dados no ambiente de desenvolvimento de Postgre para neo4j. |
| consumir dados da API Salic com Node.js | Eu, como desenvolvedor, desejo consumir os dados de projetos e propostas utilizando o Node.js. |
| realizar pesquisa utilizando o Node.js| Eu, como desenvolvedor, desejo realizar pesquisas no banco de dados utilizando o Node.js. |