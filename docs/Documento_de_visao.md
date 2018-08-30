---
layout: default
---

# Documento de Visão

## Histórico de Revisão

|           Data          |         Versão         |       Descrição   |         Autores   |
|:----------------------:|:------------------------:|:---------------------:|:--------------:|
| 28/08/2018         |           0.1                | Abertura de documento |  Mikhaelle Bueno, Marcos Vinícius Rodrigues, Fabiana Luiza V.P.Ribas, Michel Camargo |
|28/08/2018 | 0.2      | Itens atualizados 1.1, 1.2, 1.3, 1.4, 1.5, 2.1, 2.2, 2.3|Mikhaelle Bueno, Marcos Vinícius Rodrigues, Fabiana Luiza V.P.Ribas |
| 29/08/2018         |           0.3                | Itens atualizados 3.1, 3.2, 3.4.2, 3.4.3, 3.7|  Gustavo Duarte Moreira |
| 29/08/2018         |           0.4               | Itens atualizados 3.4.1, 3.5, 4.1, 4.2, 4.3|  Mikhaelle Bueno, Fabiana Luiza V.P.Ribas |
| 30/08/2018         |           0.5               | Itens atualizados 3.6|  Michel Camargo |
| 30/08/2018         |           0.6               | Itens atualizados 5.1|  Adrielly Rodrigues|


## 1:Introdução
-------------------

### 1.1 Propósito
O **NaturalSearch** é uma ferramenta para navegação e pesquisa que, através dos projetos culturais registrados no site [**VerSalic**](http://versalic.cultura.gov.br/#/home) e utilizando linguagem natural, visa encontar documentos correlacionados, tornando o resultado mais amplo, em forma de grafos, quando uma pesquisa for realizada pelo usuário.

### 1.2 Escopo
Na essência, todos os sites de busca e pesquisa funcionam da mesma forma: montam um banco de dados com diversos textos com milhões de linhas e mostram os resultados/textos que têm a ver com a palavra/dados que você digitou na tela de procura. A diferença está nos detalhes.
Por exemplo: que página deve aparecer primeiro? Se você digitar algo como “São Paulo”, o site de buscas não sabe se você está atrás de informações sobre a maior cidade brasileira ou sobre o santo. Mas ele tem que dar um jeito de “saber o que você está pensando”.
Cada site usa fórmulas específicas para ordenar os resultados de uma pesquisa. O jeito mais comum,é colocar no topo da lista as páginas que contém mais palavras igual a palavra pesquisada.
Entretanto com o NaturalSearch, que é o projeto a ser desenvolvido,os dados apresentados são consultados em tempo real na base do ___Sistema de Apoio às Leis de Incentivo à Cultura___ – [SALIC](http://www.cultura.gov.br/documents/10883/1339972/Apresenta%C3%A7%C3%A3o+SalicNet.pdf/2f7b8065-eca4-41d6-860e-425d111e2ee7), através de sua API. Os dados disponibilizados pela API são atualizados e disponibilizados, através de grafos, tornando a pesquisa mais interessante e eficiente.

### 1.3 Definições, acrônimos e abreviações

|           Abreviação        |           Definição           |
|:---------------------------:|:-----------------------------:|
|         LN                    |              Linguagem Natural                 |

### 1.4 Referências

[Versalic](http://versalic.cultura.gov.br/#/home)
[IBM Knowledge Center](https://hangouts.google.com/_/elUi/chat-redirect?dest=https%3A%2F%2Fwww.ibm.com%2Fsupport%2Fknowledgecenter%2Fpt-br%2FSSWMEQ_4.0.6%2Fcom.ibm.rational.rrm.help.doc%2Ftopics%2Fr_vision_doc.html)
[MIT License org.](https://hangouts.google.com/_/elUi/chat-redirect?dest=https%3A%2F%2Fmit-license.org%2F)

### 1.5 Visão geral

Este documento está organizado de maneira a se compreender primeiramente as funções e os objetivos do projeto, seguidos pelos perfis de usuário e equipe do projeto. Por fim, são descritas as características técnicas da aplicação. Está organizado em: posicionamento, descrição da parte interessada e do usuário, visão geral e recursos do produto, restrições, faixas de qualidade, procedência e prioridade, requisitos e documentação do produto e apêndice.

## 2:Posicionamento
--------------

### 2.1 Oportunidade de negócios
O NaturalSearch facilitará a procura de assuntos relevantes ao usuário por entregar sugestões inteligentes sobre o assunto pesquisado, proporcionando uma melhor experiência na navegação da plataforma e maior aprendizado.
Atualmente sites como o *spotify* e o *netflix* utilizam do recurso de sugestões inteligentes ao usuário, mas não há registro de aplicações que funcionem para diversas APIs em sites de busca.

### 2.2 Instrução do Problema

- Problema: As pesquisas por palavra chave se tornam limitadas e frequentemente ineficientes
- Funçoes Afetadas: A entrega de um resultado de pesquisa não esperado e irrelevante     
- Efeito: O usuário continua sem a informação correta         
- Solução: Utilizar os princípios da linguagem natural para filtrar de maneira mais eficiente os dados e oferecer ao usuário uma visualização mais intuitiva dos resultados de busca


### 2.3 Instrução de Posição do Produto


- Público Alvo :Usuários do site de busca            
- Carências: Resultados relevantes          
- Solução: NaturalSearch          
- Descrição da Solução: Através dos princípios da LN e grafos a aplicação será capaz de entregar um resultado de busca mais eficiente e intuitivo     
- DIferenciais: Metodos de buscas mais inteligentes utilizando LN    

## 3:Descrição da Parte Interessada e do Usuário
---------------

### 3.1 Resumo da Parte Interessada

| Nome  | Descrição |Responsabilidade|
| ------ | ------------- | ------------ |
| Equipe  |      Composta por graduandos em Engenharia de Software 2°2018 pela Universidade de Brasília, no Campus Gama, discentes das disciplinas de Métodos de Desenvolvimento de Software e Engenharia de Produto de Software.           | Desenvolver e gerir o software. |
| Clientes  |        Interessados em realizar pesquisas de maneira mais eficientes de projetos culturais que recebem incentivos fiscais do Minstério da Cultura, por meio de visualização em grafos.       |              |

### 3.2 Resumo do Usuário

| Nome  | Descrição | Parte interessada |
| ------ | ------------- | ------------ |
| Cidadão  | Pessoa interessada em visualizar informações de forma intuitiva e simples por meio de grafos              | Usuário             |

### 3.3 Ambiente do Usuário

O acesso aos serviços da aplicação poderá ser feito por navegadores de internet, como o Mozilla Firefox, Google Chrome, Apple Safari.

### 3.4 Perfis das Partes Interessadas

#### 3.4.1 Usuário do Serviço

|||  
|----------|----------|          
|**Representantes** | Jornalistas, Produtores culturais e Público da [Lei Rouanet](http://rouanet.cultura.gov.br/). |
|**Descrição** | Cidadão que deseja pesquisar sobre os projetos e suas informações.  |
|**Tipo** | Usuário informal. |
|**Responsabilidades** |Utilizar a aplicação e obter dados. Disponibilizados em forma de grafos. |
|**Critérios de Sucesso** |Quando o usuário achar informações relevantes a sua pesquisa. |
|**Envolvimento** | Baixo - O usuário não está envolvido diretamente na execução do projeto. |
|**Comentários ou Problemas**|A aplicação depende de divulgação. Os usuários não serão atendidos se não houver divulgação da plataforma.|

#### 3.4.2 Equipe de desenvolvimento


|||  
|----------|----------|          
|**Representantes** | [Adrielly Rodrigues de Jesus](https://github.com/drykette), [Fabiana Luiza V. P. Ribas](https://github.com/FabianaRibas), [Gustavo Duarte Moreira](https://github.com/gustavoduartemoreira), [Marcos Vinícius Rodrigues da Conceição](https://github.com/marcos-mv), [Michel Martins de Camargo](https://github.com/micheldcamargo), [Mikhaelle de Carvalho Bueno](https://github.com/Mikhaelle);|
|**Descrição** | Desenvolvedores|
|**Tipo** | Grupo de Estudadntes da Faculdade do Gama (FGA), matriculados na disciplina de Métodos de Desenvolvimento de Software (MDS)|
|**Responsabilidades** | Elaborar documentação base sobre o contexto do projeto.Desenvolver o projeto.  |
|**Critérios de Sucesso** | Aplicar metodologias ágeis ao longo do processo e obter um produto que satisfaça a necessidade do cliente.|
|**Envolvimento** | Alto |
|**Comentários ou Problemas**| ---    |             

#### 3.4.3 Equipe de Gestão de Projetos

|||  
|----------|----------|        
|**Representantes** | [Filipe Coelho Hilário Barcelos](https://github.com/FilipeKN4), [Igor Araújo de Sousa](https://github.com/zero101010), [Lucas Midlhey Cardoso Naves](https://github.com/lucasmidlhey),  [Shermam Tácia da Costa Lima](https://github.com/tacia68); |
|**Descrição** | Gerentes de Projeto|
|**Tipo** | Grupo de Estudadntes da Faculdade do Gama (FGA), matriculados na disciplina de Engenharia de Produto de Software (EPS)|
|**Responsabilidades** | Gerenciar, supervisionar e manter a equipe de desenvolvimento a fim de que as metodologias ágeis sejam aplicadas e o produto seja entregue ao cliente no final.|
|**Critérios de Sucesso** | Aplicar metodologias ágeis ao longo do processo e obter um produto que satisfaça a necessidade do cliente.|
|**Envolvimento** | Alto                 ||||
| ------------- | ------------- |

### 3.5 Perfis dos Usuários

|||
| ------------- | ------------- |
| **Representantes** |      Usuário           |
| **Descrição**   |      Cidadão que deseja alguma informação sobre os projetos da Lei Rouanet        |
| Tipo  |      Usuário informal        |
|**Responsabilidade** |         Utilizar a aplicação e obter dados da Lei Rouanet         |
|**Critério de sucesso**|     Quando o usuário achar informações relevantes a sua pesquisa     |
|**Envolvimento**|        Baixo - O usuário não está envolvido diretamente na execução do projeto      |
|**Comentários ou Problemas**|       A aplicação depende de divulgação. Os usuários não serão atendidos se não houver divulgação da plataforma           |

### 3.6 Principais Necessidades da parte Interessada ou do usuário

|           Necessidade     |        Prioridade        |       Interesse     |         Solução Atual     |      Solução Proposta     |
|:----------------------:|:------------------------:|:---------------------:|:--------------:|:---------------:|
| Realizar busca inteligente com resultados relevantes | Alta | Facilitar a busca de dados mais relevantes | Mecanismos de busca tradicional que buscam tags ou palavras-chave específicas | Utilizar os princípios da LN para realizar pesquisas relevantes |
| Exibir resultados de pesquisa por relevância de forma intuitiva através de grafos | Alta | Facilitar a vizualização dos dados | Exibição dos resultados de forma linear | Através de grafos relacionar os resultados de forma a evidenciar os mais relevantes para a pesquisa |

### 3.7 Alternativas e Concorrência

Não foram encontradas aplicações que realizem pesquisas por meio de LN e mostrem resultados por meio de grafos.

## 4: Visão Geral do Produto
-------------

### 4.1 Resumo das Capacidades
O sistema NaturalSearch tem a finalidade de retornar resultados relevantes e inteligentes a pesquisa feita pelo usuário sobre projetos da [Lei Rouanet](http://rouanet.cultura.gov.br). Para o cumprimento do propósito do sistema, ele deverá acessar os dados da API do site [Versalic](http://versalic.cultura.gov.br/#/home) obtendo os dados que contém informações como, tipo, valor solicitado, valor aprovado, municípo, ano, situação do projeto, além dos detalhes das etapas, objetivos, sinopse, entre outras informações sobre o projeto, que possibilitará o processamento de LN e o retorno da pesquisa em forma de grafos.

### 4.2 Resumo das Capacidades
| Benefício para o cliente  | Recursos de Suporte |
| ------ | ------------- |
| Rápido retorno do resultado de busca  |    Pesquisa no banco de dados do NaturalSearch   |
| Satisfação com o resultado de busca obtido  |  Grafos  |              


### 4.3 Licenciamento e instalação
A distribuição do software esta submetida a licença do [MIT](https://mit-license.org). A licença é aberta quanto a visualização, permissão para modificação e utilização do software.

## 5: Recursos do produto
-------------


### 5.1 Facilidade na Obtenção das Informações Reunidas

O NaturalSearch deve consultar em tempo real os dados apresentados na API do SALIC, de forma que os usuários possam efetuar suas pesquisas com rapidez através da aplicação. Sendo, ainda, de fácil acesso e uso para todos os tipos de usuário.  
