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
| 22/11/2018         |           0.5               | Mudanças e adições de novas histórias de usuário | [Shermam Tácia da Costa Lima](https://github.com/tacia68) |
| 24/11/2018         |           1.0               | Adições de novas histórias de usuário | [Shermam Tácia da Costa Lima](https://github.com/tacia68) |


## 1. Processamento de Dados da API Salic

### 1.1 Criar estrutura do banco de dados

|**história de usuário** | **descrição** |
|:---:|:---:|
| US02 | Eu, como desenvolvedor, desejo criar uma tabela de projetos no banco de dados da aplicação. |
| US03 | Eu, como desenvolvedor, desejo criar uma tabela de propostas no banco de dados da aplicação. |

### 1.2 Consumir dados da API Salic

| **história de usuário** | **descrição** |
|:---:|:---:|
| US06| Eu, como desenvolvedor, desejo consumir dados de projetos da API Salic. |
| US07| Eu, como desenvolvedor, desejo consumir dados de propostas da API Salic. |
| US08| Eu, como desenvolvedor, desejo consumir dados de proponentes da API Salic. |
| US21| Eu, como desenvolvedor, desejo verificar se houveram mudanças nos dados da API Salic e atualizá-las, caso existam, na aplicação Natural Search. |

### 1.3 Realizar o processamento dos dados

| **história de usuário** | **descrição** |
|:---:|:---:|
| US09 | Eu, como desenvolvedor, desejo remover informações desnecessárias de projetos que serão utilizadas. |
| US10 | Eu, como desenvolvedor, desejo remover informações desnecessárias de projetos que serão utilizadas. |

### 1.4 Disponibilizar os dados Processados

| **história de usuário** | **descrição** |
|:---:|:---:|
| US12 | Eu, como desenvolvedor, desejo converter os dados processados de projetos para o formato JSON e salvar em um arquivo. |
| US13 | Eu, como desenvolvedor, desejo criar uma API para disponibilizar as informações obtidas em formato JSON |
| US19 | Eu, como desenvolvedor, desejo testar toda a aplicação de processamento de dados da Salic API |
| US20 | Eu, como desenvolvedor, desejo documentar a API criada para fornecer detalhes das informações disponibilizadas de projetos e proponentes. |


## 2. Visualização em Grafos

### 2.1 Popular banco de dados

| **história de usuário** | **descrição** |
|:---:|:---:|
| US14| Eu, como desenvolvedor, desejo popular a tabela de projetos do banco de dados com os dados consumidos da API Salic. |
| US15| Eu, como desenvolvedor, desejo popular a tabela de proponentes do banco de dados com os dados consumidos da API Salic. |
| US16| Eu, como desenvolvedor, desejo conectar os projetos com os respectivos proponentes no banco de dados. |
| US17| Eu, como desenvolvedor, desejo popular o banco de dados do serviço de processamento de dados da Salic API com os dados de projetos e proponentes. |

### 2.2 Visualizar os dados

| **história de usuário** | **descrição** |
|:---:|:---:|
| US01 | Eu, como usuário, desejo realizar uma pesquisa com qualquer palavra, frase, ou número que interessar. |
| US04 | Eu, como desenvolvedor, desejo criar uma tela inicial para visualizar informações gerais sobre o produto. |
| US11 | Eu, como desenvolvedor, desejo criar a tela de resultados da pesquisa. |
| US05 | Eu, como desenvolvedor, desejo criar a tela de visualização dos resultados da pesquisa por meio de grafo. |
| US18 | Eu, como desenvolvedor, desejo testar toda a aplicação de visualização de grafos |



## Histórias Técnicas de Usuário

| **história de usuário** | **descrição** |
|:---:|:---:|
| TS01 | Eu, como desenvolvedor, desejo modificar o banco de dados no ambiente de desenvolvimento de Postgre para neo4j. |
| TS02,| Eu, como desenvolvedor, desejo consumir os dados de projetos e propostas utilizando o Node.js. |
| TS03 | Eu, como desenvolvedor, desejo realizar pesquisas no banco de dados utilizando o Node.js. |
| TS04 | Eu, como desenvolvedor, desejo otimizar a tela de visualização dos resultados da pesquisa por meio de grafos. |
| TS05 | Eu, como desenvolvedor, desejo realizar o deploy da aplicação para disponibilizar todos os incrementos realizados até o momento e automatizar o processo. |
| TS06 | Eu, como desenvolvedor, desejo realizar todos os testes da aplicação para visualização e processamento de dados. |
| TS07 | Eu, como desenvolvedor, desejo aprimorar o método de pesquisa para que possa se adequar a pesquisa de projetos. |
| TS08 | Eu, como desenvolvedor, desejo obter os dados de projetos e proponentes e gerar um arquivo Json que apresente-os no formato para o D3.js |
| TS09 | Eu, como desenvolvedor, desejo realizar a integração dos serviços de processamento de dados e visualização em grafos. |
| TS10 | Eu, como desenvolvedor, desejo aprimorar o estilo da tela inicial e tela de pesquisa. |
| TS11 | Eu, como desenvolvedor, desejo realizar a conversão dos dados do proponente e os respectivos projetos selecionados para o formato de json suportado pelo D3.js. |