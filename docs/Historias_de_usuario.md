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
| 08/10/2018         |           0.4                | Mudanças e adições de novas histórias de usuário | [Filipe Coelho Hilário Barcelos](https://github.com/FilipeKN4) |
| 31/10/2018         |           0.5                | Mudanças e adições de novas histórias de usuário | [Filipe Coelho Hilário Barcelos](https://github.com/FilipeKN4) |

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
| consumir dados de proponentes  | Eu, como desenvolvedor, desejo consumir dados de proponentes da API Salic. |

### 1.3 Realizar o processamento dos dados

| **história de usuário** | **descrição** |
|:---:|:---:|
| remover informações desnecessárias de projetos | Eu, como desenvolvedor, desejo remover informações desnecessárias de projetos que serão utilizadas. |
| remover informações desnecessárias de proponentes | Eu, como desenvolvedor, desejo remover informações desnecessárias de projetos que serão utilizadas. |

### 1.4 Disponibilizar os dados Processados

| **história de usuário** | **descrição** |
|:---:|:---:|
| converter os dados de projetos para o formato JSON | Eu, como desenvolvedor, desejo converter os dados processados de projetos para o formato JSON e salvar em um arquivo. |
| converter os dados de proponentes para o formato JSON | Eu, como desenvolvedor, desejo converter os dados processados de proponentes para o formato JSON e salvar em um arquivo. |
| criar API para fornecer o JSON | Eu, como desenvolvedor, desejo criar uma API para disponibilizar as informações obtidas em formato JSON. |
| documentar API | Eu, como desenvolvedor, desejo documentar a API criada para fornecer detalhes das informações disponibilizadas de projetos e proponentes. |

## 2. Visualização em Grafos

### 2.1 Popular banco de dados

| **história de usuário** | **descrição** |
|:---:|:---:|
| popular com projetos | Eu, como desenvolvedor, desejo popular a tabela de projetos do banco de dados com os dados consumidos da API Salic. |
| popular com proponentes | Eu, como desenvolvedor, desejo popular a tabela de proponentes do banco de dados com os dados consumidos da API Salic. |
| popular com projetos e proponentes| Eu, como desenvolvedor, desejo popular o banco de dados do serviço de processamento de dados da Salic API com os dados de projetos e proponentes. |
| conectar projetos e proponentes | Eu, como desenvolvedor, desejo conectar os projetos com os respectivos proponentes no banco de dados. |

### 2.2 Visualizar os dados

| **história de usuário** | **descrição** |
|:---:|:---:|
| realizar pesquisa | Eu, como usuário, desejo realizar uma pesquisa com qualquer palavra, frase, ou número que interessar. |
| criar tela inicial | Eu, como desenvolvedor, desejo criar uma tela inicial para visualizar informações gerais sobre o produto. |
| criar tela de resultados | Eu, como desenvolvedor, desejo criar a tela de resultados da pesquisa. |
| criar tela de visualização | Eu, como desenvolvedor, desejo criar a tela de visualização dos resultados da pesquisa por meio de grafos. |


## Histórias Técnicas de Usuário

| **história de usuário** | **descrição** |
|:---:|:---:|
| modificar banco de dados | Eu, como desenvolvedor, desejo modificar o banco de dados no ambiente de desenvolvimento de Postgre para neo4j. |
| consumir dados da API Salic com Node.js | Eu, como desenvolvedor, desejo consumir os dados de projetos e propostas utilizando o Node.js. |
| realizar pesquisa utilizando o Node.js| Eu, como desenvolvedor, desejo realizar pesquisas no banco de dados utilizando o Node.js. |
| otimizar tela de visualização | Eu, como desenvolvedor, desejo otimizar a tela de visualização dos resultados da pesquisa por meio de grafos. |
| testar o serviço de visualização | Eu, como desenvolvedor, desejo testar toda a aplicação de visualização de grafos. |
| testar o serviço de processamento de dados | Eu, como desenvolvedor, desejo testar toda a aplicação de processamento de dados da Salic API. |
| realizar o deploy da aplicação | Eu, como desenvolvedor, desejo realizar o deploy da aplicação para disponibilizar todos os incrementos realizados até o momento e automatizar o processo. |
| realizar todos os testes da aplicação | Eu, como desenvolvedor, desejo realizar todos os testes da aplicação para visualização e processamento de dados. |
| aprimorar a pesquisa da aplicação | Eu, como desenvolvedor, desejo aprimorar o método de pesquisa para que possa se adequar a pesquisa de projetos. |
| adaptar visualização em grafo para projetos | Eu, como desenvolvedor, desejo obter os dados de projetos e proponentes e gerar um arquivo Json que apresente-os no formato para o D3.js. |