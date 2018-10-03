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
| 30/08/2018         |           0.6               | Itens atualizados 5.1, 6.1, 6.2, 6.3, 6.4, 7|  Adrielly Rodrigues|
| 30/08/2018         |           0.7             | Adisão do sumário e Linkamento dos tópicos  |  Adrielly Rodrigues|
| 30/08/2018         |           0.8             | Itens atualizados 3.6  |  Michel Camargo |
| 30/08/2018         |           0.9             | Itens atualizados 8, 9.1, 9.2  |  Mikhaelle Bueno |
| 04/09/2018         |           1.0             | Itens atualizados 1.1, 1.2, 1.5, 2.1, 4.1  |  Mikhaelle Bueno |
| 04/09/2018         |           1.1             | Revisão do documento  |  Gustavo Duarte Moreira |

# Sumário
1. [Introdução](#1)
  * 1.1 [Propósito](#1.1)
  * 1.2 [Escopo](#1.2)
  * 1.3 [Definições, acrônimos e abreviações](#1.3)
  * 1.4 [Referências](#1.4)
  * 1.5 [Visão Geral](#1.5)
2. [Posicionamento](#2)
  * 2.1 [Oportunidade de Negócio](#2.1)
  * 2.2 [Descrição do Problema](#2.2)
  * 2.3 [Instrução de Posição do Produto](#2.3)
3. [Descrição da Parte Interessada e do Usuário](#3)
  * 3.1 [Resumo da Parte Interessada](#3.1)
  * 3.2 [Resumo do Usuário](#3.2)
  * 3.3 [Ambiente do Usuário](#3.3)
  * 3.4 [Perfis das Partes Interessadas](#3.4)
    * 3.4.1 [Usuário do Serviço](#3.4.1)
    * 3.4.2 [Equipe de Desenvolvimento](#3.4.2)
    * 3.4.3 [Equipe de Gestão de Projetos](#3.4.3)
  * 3.5 [Perfis dos Usuários](#3.5)
  * 3.6 [Principais Necessidades da Parte Interessada ou do Usuário](#3.6)
  * 3.7 [Alternativas e Concorrência](#3.7)
4. [Visão Geral do Produto](#4)
  * 4.1 [Perspectiva do produto](#4.1)
  * 4.2 [Resumo das Capacidades](#4.2)
  * 4.3 [Licenciamento e Instalação](#4.3)
5. [Recursos do Produto](#5)
  * 5.1 [Facilidade na Obtenção das Informações Reunidas](#5.1)
6. [Restrições](#6)
  * 6.1 [Restrições de Design](#6.1)
  * 6.2 [Restrições de Escopo](#6.2)
  * 6.3 [Restrições de Uso](#6.3)
  * 6.4 [Restrições de Implementação](#6.4)
7. [Faixas de Qualidade](#7)
8. [Precedência e Prioridade](#8)
9. [Outros Requisitos do Produto](#9)
  * 9.1 [Requisitos do Sistema](#9.1)
  * 9.2 [Requisitos de Desempenho](#9.2)

## <a name="1"></a> 1:Introdução
-------------------

### <a name="1.1"></a> 1.1 Propósito
O **NaturalSearch** é uma ferramenta para navegação e pesquisa que, por meio dos projetos culturais registrados no site [**VerSalic**](http://versalic.cultura.gov.br/#/home) e utilizando linguagem natural(LN), visa encontar documentos correlacionados. Quando uma pesquisa é realizada o resultado dos projetos e propostas similares serão retornando em forma de grafos.

### <a name="1.2"></a> 1.2 Escopo
Na essência, todos os sites de busca e pesquisa funcionam da mesma forma: montam um banco de dados com diversos textos com milhões de linhas e mostram os resultados/textos que têm a ver com a palavra/dados que você digitou na tela de procura. A diferença está nos detalhes.
Por exemplo: que página deve aparecer primeiro? Se você digitar algo como “São Paulo”, o site de buscas não sabe se você está atrás de informações sobre a maior cidade brasileira ou sobre o santo. Mas ele tem que dar um jeito de “saber o que você está pensando”.
Cada site usa fórmulas específicas para ordenar os resultados de uma pesquisa. O jeito mais comum,é colocar no topo da lista as páginas que contém mais palavras igual a palavra pesquisada.
Entretanto com o **NaturalSearch**, que é o projeto a ser desenvolvido, haverá um sistema de visualização de conteúdos similares. Os dados serão consultados na base do ___Sistema de Apoio às Leis de Incentivo à Cultura___ – [SALIC](http://www.cultura.gov.br/documents/10883/1339972/Apresenta%C3%A7%C3%A3o+SalicNet.pdf/2f7b8065-eca4-41d6-860e-425d111e2ee7), por meio de sua API, para que eles sejam tratados com LN e passados para o banco de dados da aplicação. Os dados disponibilizados pela API são atualizados e retornados, através de grafos, tornando a pesquisa mais interessante e eficiente. O grafo irá permitir uma visualização mais intuitiva das correlações entre os dados.

### <a name="1.3"></a> 1.3 Definições, acrônimos e abreviações

|           Abreviação        |           Definição           |
|:---------------------------:|:-----------------------------:|
|  LN    |     Linguagem Natural     |
|  SALIC    |   Sistema de Apoio às Leis de Incentivo à Cultura    |
|  MDS   |   Métodos de Desenvolvimento de Software |
|  EPS   | Engenharia de Produto de Software |

### <a name="1.4"></a> 1.4 Referências

- [Versalic](http://versalic.cultura.gov.br/#/home)
- [IBM Knowledge Center](https://hangouts.google.com/_/elUi/chat-redirect?dest=https%3A%2F%2Fwww.ibm.com%2Fsupport%2Fknowledgecenter%2Fpt-br%2FSSWMEQ_4.0.6%2Fcom.ibm.rational.rrm.help.doc%2Ftopics%2Fr_vision_doc.html)
- [MIT License org.](https://hangouts.google.com/_/elUi/chat-redirect?dest=https%3A%2F%2Fmit-license.org%2F)

### <a name="1.5"></a> 1.5 Visão Geral

Neste documento estão descritas as funções, os objetivos do projeto, perfis de usuário, equipe do projeto e características técnicas da aplicação.
Está organizado em: posicionamento, descrição da parte interessada e do usuário, visão geral e recursos do produto, restrições, faixas de qualidade, procedência e prioridade, requisitos e documentação do produto e apêndice.

## <a name="2"></a> 2: Posicionamento
--------------

### <a name="2.1"></a> 2.1 Oportunidade de Negócios
O **NaturalSearch** facilitará a pesquisa de projetos e propostas da Lei Rouanet entregando uma visualização de forma mais clara dos projetos que se assemelham, proporcionando uma melhor experiência na navegação da plataforma por dispor as informações mais relevantes de forma inteligente.
Atualmente sites como o *spotify* e o *netflix* utilizam do recurso de sugestões inteligentes ao usuário, mas não há registro de aplicações que funcionem para diversas APIs em sites de busca.

### <a name="2.2"></a> 2.2 Instrução do Problema

|||  
|----------|----------|          
|**Problema** |As pesquisas por palavra chave se tornam limitadas e frequentemente ineficientes. |
|**Funçoes Afetadas** | A entrega de um resultado de pesquisa não esperado e irrelevante.     |
|**Efeito** | O usuário encontra dificuldade em visualizar as informações relevantes. |
|**Solução** |Utilizar os princípios da LN para filtrar de maneira mais eficiente os dados e oferecer ao usuário uma visualização mais intuitiva dos resultados  mais relevantes e correlacionados. |


### <a name="2.3"></a> 2.3 Instrução de Posição do Produto

|||  
|----------|----------|          
|**Público Alvo** |Usuários do site de busca. |
|**Carências** | Resultados relevantes.    |
|**Solução** | **NaturalSearch**. |
|**Descrição da Solução** |Através dos princípios da LN e de grafos a aplicação será capaz de entregar um resultado de busca mais eficiente e intuitivo. Possibilitando interação de forma fácil. |
|**Diferenciais** | Metodos de buscas mais inteligentes utilizando LN e retorno de resultados correlacionados em forma de grafo. |
   

## <a name="3"></a> 3: Descrição da Parte Interessada e do Usuário
---------------

### <a name="3.1"></a> 3.1 Resumo da Parte Interessada

| Nome  | Descrição |Responsabilidade|
| ------ | ------------- | ------------ |
| Equipe  |      Composta por graduandos em Engenharia de Software 2°2018 pela Universidade de Brasília, no Campus Gama, discentes das disciplinas de Métodos de Desenvolvimento de Software e Engenharia de Produto de Software.           | Desenvolver e gerir o software. |
| Clientes  |        Interessados em realizar pesquisas de maneira mais eficientes de projetos culturais que recebem incentivos fiscais do Minstério da Cultura, por meio de visualização em grafos.       |              |

### <a name="3.2"></a> 3.2 Resumo do Usuário

| Nome  | Descrição | Parte interessada |
| ------ | ------------- | ------------ |
| Cidadão  | Pessoa interessada em visualizar informações de forma intuitiva e simples por meio de grafos              | Usuário             |

### <a name="3.3"></a> 3.3 Ambiente do Usuário

O acesso aos serviços da aplicação poderá ser feito por navegadores de internet, como o Mozilla Firefox, Google Chrome, Apple Safari.

### <a name="3.4"></a> 3.4 Perfis das Partes Interessadas

#### <a name="3.4.1"></a> 3.4.1 Usuário do Serviço

|||  
|----------|----------|          
|**Representantes** | Jornalistas, Produtores culturais e Público da [Lei Rouanet](http://rouanet.cultura.gov.br/). |
|**Descrição** | Cidadão que deseja pesquisar sobre os projetos e suas informações.  |
|**Tipo** | Usuário informal. |
|**Responsabilidades** |Utilizar a aplicação e obter dados. Disponibilizados em forma de grafos. |
|**Critérios de Sucesso** |Quando o usuário achar informações relevantes a sua pesquisa. |
|**Envolvimento** | Baixo - O usuário não está envolvido diretamente na execução do projeto. |
|**Comentários ou Problemas**|A aplicação depende de divulgação. Os usuários não serão atendidos se não houver divulgação da plataforma.|

#### <a name="3.4.2"></a> 3.4.2 Equipe de Desenvolvimento

|||  
|----------|----------|          
|**Representantes** | [Adrielly Rodrigues de Jesus](https://github.com/drykette), [Fabiana Luiza V. P. Ribas](https://github.com/FabianaRibas), [Gustavo Duarte Moreira](https://github.com/gustavoduartemoreira), [Marcos Vinícius Rodrigues da Conceição](https://github.com/marcos-mv), [Michel Martins de Camargo](https://github.com/micheldcamargo), [Mikhaelle de Carvalho Bueno](https://github.com/Mikhaelle);|
|**Descrição** | Desenvolvedores|
|**Tipo** | Grupo de Estudadntes da Faculdade do Gama (FGA), matriculados na disciplina de MDS.|
|**Responsabilidades** | Elaborar documentação base sobre o contexto do projeto.Desenvolver o projeto.  |
|**Critérios de Sucesso** | Aplicar metodologias ágeis ao longo do processo e obter um produto que satisfaça a necessidade do cliente.|
|**Envolvimento** | Alto |
|**Comentários ou Problemas**| ---    |             

#### <a name="3.4.3"></a> 3.4.3 Equipe de Gestão de Projetos

|||  
|----------|----------|        
|**Representantes** | [Filipe Coelho Hilário Barcelos](https://github.com/FilipeKN4), [Igor Araújo de Sousa](https://github.com/zero101010), [Shermam Tácia da Costa Lima](https://github.com/tacia68); |
|**Descrição** | Gerentes de Projeto|
|**Tipo** | Grupo de Estudadntes da Faculdade do Gama (FGA), matriculados na disciplina EPS |
|**Responsabilidades** | Gerenciar, supervisionar e manter a equipe de desenvolvimento a fim de que as metodologias ágeis sejam aplicadas e o produto seja entregue ao cliente no final.|
|**Critérios de Sucesso** | Aplicar metodologias ágeis ao longo do processo e obter um produto que satisfaça a necessidade do cliente.|
|**Envolvimento** | Alto                 ||||
| ------------- | ------------- |

### <a name="3.5"></a> 3.5 Perfis dos Usuários

|||
| ------------- | ------------- |
| **Representantes** |      Usuário           |
| **Descrição**   |      Cidadão que deseja alguma informação sobre os projetos da Lei Rouanet        |
| **Tipo**  |      Usuário informal        |
|**Responsabilidade** |         Utilizar a aplicação e obter dados da Lei Rouanet         |
|**Critério de sucesso**|     Quando o usuário achar informações relevantes a sua pesquisa     |
|**Envolvimento**|        Baixo - O usuário não está envolvido diretamente na execução do projeto      |
|**Comentários ou Problemas**|       A aplicação depende de divulgação. Os usuários não serão atendidos se não houver divulgação da plataforma           |

### <a name="3.6"></a> 3.6 Principais Necessidades da Parte Interessada ou do Usuário

|           Necessidade     |        Prioridade        |       Interesse     |         Solução Atual     |      Solução Proposta     |
|:----------------------:|:------------------------:|:---------------------:|:--------------:|:---------------:|
| Realizar busca inteligente com resultados relevantes | Alta | Facilitar a busca de dados mais relevantes | Mecanismos de busca tradicional que buscam tags ou palavras-chave específicas | Utilizar os princípios da LN para realizar pesquisas relevantes |
| Exibir resultados de pesquisa por relevância de forma intuitiva através de grafos | Alta | Facilitar a vizualização dos dados | Exibição dos resultados de forma linear | Através de grafos relacionar os resultados de forma a evidenciar os mais relevantes para a pesquisa |
| Exibir nos resultados de pesquisa resultados semelhantes ao tema pesquisado | Alta | Linkar resultados da pesquisa de acordo com o tema pesquisado exibindo resultados correlatos | Resultados de pesquisa somente sobreo que foi pesquisado | Sistema de pesquisa resultados baseado em conteúdo |

### <a name="3.7"></a> 3.7 Alternativas e Concorrência

Não foram encontradas aplicações que realizem pesquisas por meio de LN e mostrem resultados por meio de grafos.

## <a name="4"></a> 4: Visão Geral do Produto
-------------

### <a name="4.1"></a> 4.1 Perspectiva do produto
O sistema **NaturalSearch** tem a finalidade de retornar os resultados mais relevantes, com resultados que se assemelham, a pesquisa feita pelo usuário sobre projetos da [Lei Rouanet](http://rouanet.cultura.gov.br). Para o cumprimento do propósito do sistema, ele deverá acessar os dados da API do site [Versalic](http://versalic.cultura.gov.br/#/home) obtendo os dados que contém informações como, tipo, valor solicitado, valor aprovado, municípo, ano, situação do projeto, além dos detalhes das etapas, objetivos, sinopse, entre outras informações sobre o projeto, que possibilitará o processamento de LN e retornar recomendações, em forma de grafo, que se assemelham ao que foi pesquisado.

### <a name="4.2"></a> 4.2 Resumo das Capacidades

| Benefício para o cliente  | Recursos de Suporte |
|:------:|:-------------:|
| Rápido retorno do resultado de busca  |    Pesquisa no banco de dados do **NaturalSearch**   |
| Satisfação com o resultado de busca obtido  |  Grafos  |              


### <a name="4.3"></a> 4.3 Licenciamento e Instalação
A distribuição do software esta submetida a licença do [MIT](https://mit-license.org). A licença é aberta quanto a visualização, permissão para modificação e utilização do software.

## <a name="5"></a> 5: Recursos do produto
-------------

### <a name="5.1"></a> 5.1 Facilidade na Obtenção das Informações Reunidas

O **NaturalSearch** deve consultar os dados apresentados na API do SALIC, passando para o próprio banco de dados orientado a grafos para então ser mostrado, de forma que os usuários possam efetuar suas pesquisas com rapidez e eficácia através da aplicação. Sendo, ainda, de fácil acesso e uso para todos os tipos de usuário.  



## <a name="6"></a> 6: Restrições
-------------

### <a name="6.1"></a> 6.1 Restrições de Design
O sistema deve ter uma interface de fácil uso, que seja intuitiva de forma a não necessitar de conhecimento prévio para uso.
### <a name="6.2"></a> 6.2 Restrições de Escopo  
O projeto faz parte de uma disciplina com vida útil de 4 meses do curso de Engenharia de Software da Universidade de Brasília, sendo assim a implementação dos principais requisitos tem um tempo limitado para serem realizados.

### <a name="6.3"></a> 6.3 Restrições de Uso
Para a utilização do **NaturalSearch** o usuário deve estar em conexão com a internet, para que o sistema tenha acesso aos dados do banco necessários para a conclusão da pesquisa. Caso o usuário não tenha esse pré-requisito o sistema não será capaz de concluir a consulta.

### <a name="6.4"></a> 6.4 Restrições de Implementação
O sistema será desenvolvido utilizando a linguagem Python, HTML, CSS, JavaScript, BootStrap.  


## <a name="7"></a> 7: Faixas de Qualidade
-------------

A aplicação será via web, para maior eficiência, devido a maior parte dos usuários terem mais acessibilidade a um browser(ex: Google Chrome, Mozilla Firefox, Safari, etc.) do que um aparelho mobile. Contudo, o NaturalSearch também deve se adequar às telas de smartphones e tablets, para que não haja transtornos ao ser utilizado.

## <a name="8"></a> 8: Precedência e Prioridade
-------------
A principal prioridade é utilizar a LN aplicada aos dados da API do [Versalic](http://versalic.cultura.gov.br/#/home) para construir o banco de dados do NaturalSearch o que permitirá um retorno do resultado de pesquisa rápido e na mesma prioridade há o retorno do resultado de pesquisa no site em forma de grafos que além de utilizar as palavras chaves também retornara projeto semelhantes aos pesquisados, em segundo plano fica o design do site que deverá ser bastante intuitivo.

## <a name="9"></a> 9: Outros Requisitos do Produto
--------------

## <a name="9.1"></a> 9.1 Requisitos do Sistema
O usuário deverá ter acesso a internet para acessar a página web do **NaturalSearch**

## <a name="9.2"></a> 9.2 Requisitos de Desempenho
O sistema será acessível a grande parte dos aparelhos que tem os requisitos do sistema e suprirá grande parte da necessidade de tráfego do site. Como o projeto contará com uma base de dados própria, o desempenho do aparelho não influênciará no retorno de resultados, mas poderá influenciar na visualização dos resultados em forma de grafos.
