---
layout: default
---

# Documento de Arquitetura

## Histórico de Revisão

|           Data          |         Versão         |       Descrição   |         Autores   |
|:----------------------:|:------------------------:|:---------------------:|:--------------:|
| 30/08/2018         |           0.1                | Abertura de documento | [Adrielly Rodrigues de Jesus](https://github.com/drykette), [Fabiana Luiza V. P. Ribas](https://github.com/FabianaRibas), [Gustavo Duarte Moreira](https://github.com/gustavoduartemoreira), [Marcos Vinícius Rodrigues da Conceição](https://github.com/marcos-mv), [Michel Martins de Camargo](https://github.com/micheldcamargo), [Mikhaelle de Carvalho Bueno](https://github.com/Mikhaelle); |
| 05/09/2018 | 0.2 | Definição de metas e restrições de arquitetura |[Michel Martins de Camargo](https://github.com/micheldcamargo) |
| 05/09/2018 | 0.3 | Definição dos itens 1.1.3, 1.1.4 / Criação do item 2, Adição de referências  |[Gustavo Duarte Moreira](https://github.com/gustavoduartemoreira)|
| 09/09/2018 | 0.4 | Definição dos itens 2.1, 2.1.1, 2.1.2, 2.1.3 |[Mikhaelle de Carvalho Bueno](https://github.com/Mikhaelle)|
| 11/09/2018 | 0.5 | Criação do item 3, Correção dos links das referências  |[Gustavo Duarte Moreira](https://github.com/gustavoduartemoreira)|
| 11/09/2018 | 0.6 | Atualizando do documento |[Mikhaelle de Carvalho Bueno](https://github.com/Mikhaelle)|

## Sumário

1. [Introdução](#1)      
    * 1.1 [Finalidade](#1.1)
    * 1.2 [Escopo](#1.2)   
    * 1.3 [Definições, acrônimos e abreviações](#1.3)
    * 1.4 [Visão Geral](#1.5)

2. [Representação da Arquitetura](#2)
    * 2.1 [Django](#2.1)
        * 2.1.1 [Model](#2.1.1)
        * 2.1.2 [View](#2.1.2)
        * 2.1.3 [Template](#2.1.3)
    * 2.2 [Salic API](#2.2)
    * 2.3 [TensorFlow](#2.3)
    * 2.4 [Arbor.js](#2.4)
    * 2.5 [Banco de Dados Orientado à Grafos](#2.5)

3. [Metas e Restrições de Arquitetura](#3)        
    * 3.1 [Ambiente e Ferramentas de Desenvolvimento](#3.1)

4. [Visão Geral](#4)    
    * 4.1 [Diagrama de pacotes](#4.1)    
    * 4.2 [Pacotes de Design Significativos do Ponto de Vista da Arquitetura]($4.2)

5. [Arquitetura dos Serviços e visão de Implementação](#5)
    * 5.1 [Visão Geral](#5.1)
    * 5.2 [Micro Serviços e Camadas](#5.2)

6. [Visão de Dados](#6)                  

7. [Referências](#10)




## <a name="1"></a>1. Introdução


### <a name="1.1"></a>1.1 Finalidade

O objetivo deste documento é fornecer uma visão arquitetural do sistema **NaturalSearch** . Ele deve mostrar de forma clara e objetiva as decisões arquiteturais que foram tomadas em relação ao projeto, fornecendo as informações necessárias para desenvolvedores e demais envolvidos em termos de estrutura da aplicação e tecnologias utilizadas.

### <a name="1.2"></a>1.2 Escopo   

Este documento foi construído sobre a visão da arquitetura utilizada na implementação do sistema **NaturalSearch**, de forma a explicitar as decisões estabelecidas.

### <a name="1.3"></a>1.3 Definições, acrônimos e abreviações

* API - Application Programming Interface
* MVT - Model-View-Template
* MVC - Model-View-Controller.
* LN - Linguagem Natural

### <a name="1.4"></a>1.4 Visão Geral

O projeto **NaturalSearch** tem o objetivo de construir uma ferramenta de navegação e pesquisa que, utilizando Linguagem Natural (LN), visa entregar correlações entre resultados de busca através de grafos.

## <a name="2"></a>2. Representação da Arquitetura

Para o projeto será adotada a arquitetura baseada em componentes. Nesta abordagem o foco está na decomposição dos sistemas possibilitando a reusabilidade, substituição, encapsulamento, independência. O *Django Application* é o conceito responsável por dar flexibilidade e grande reaproveitamento de componentes ao **Django**.

### <a name="2.1"></a>2.1. Django
O NaturalSearch será uma aplicação web desenvolvida a partir do framework Django, utilizando linguagem python para o *back-end* e HTML e Javascript para o *front-end*. Um framework já contém um conjunto de componentes que são normalmente utilizados pela maioria dos desenvolvedores o que ajuda a desenvolver um site de forma mais rápida. O padrão arquitetural que é utilizado pelo Django é o MVT(Model, View, Template) que é uma derivação do MVC(Model, View, Controller) e será melhor explicado nos tópicos abaixo.

A arquitetura do Django segue basicamente o fluxograma da imagem abaixo. Quando o usuário faz uma requisição ao servidor web pela URL, ela é passada na urlresolver do Django e quando encontrada é feita a requisição a View. A View se comunica com o Template e a Model, que por sua vez se comunica com o banco de dados, e vice e versa. Depois o resultado dessa interação é retornado ao usuário.
<center>
<img src="https://naditya.azurewebsites.net/wp-content/uploads/2017/03/Django-Template-214x300.png">
</center>


#### <a name="2.1.1"></a>2.1.1. Model
Os modelos(Models) são classes que representam os dados das tabela do banco de dados, sendo cada model uma tabela uníca. Com essa interação o Django dá uma API de acesso ao banco de dados gerada automaticamente, facilitando o desenvolvimento da aplicação.

#### <a name="2.1.2"></a>2.1.2. View
A View é responsável por receber a requisição web e retornar uma resposta web. Ela se comunica com a Model e a Template com lógicas arbritárias necessárias para retornar uma resposta, como por exemplo quando um usuário tenta fazer login, a view pega a requisição, confere com a model se os dados estão certos e pega com o template a forma visual que deve ser retornado caso o acesso de certo ou errado.

#### <a name="2.1.3"></a>2.1.3. Template
A Template é a camada mais externa e visual do software, que faz o retorno visual ao usuário. Ela é composta por HTML, CSS, javascript e etc.

### <a name="2.2"></a>2.2. Salic API

### <a name="2.3"></a>2.3. TensorFlow


### <a name="2.4"></a>2.4. Arbor.js

### <a name="2.6"></a>2.6 Banco de Dados Orientado à Grafos    

## <a name="3"></a>3. Metas e Restrições de Arquitetura       

O projeto **NaturalSearch** possui as seguintes metas:

* Funcionar nos  principais browsers utilizados atualmente: Mozilla Firefox, Google Chrome e Internet Explorer.
* O código deve ser modularizado facilitando a manutenção e com baixo acoplamento.

### <a name="3.1"></a>3.1. Ambiente e Ferramentas de Desenvolvimento

| Requisito | Ferramenta/Solução | Versão | Descrição |
|---|---|---|---|
|Linguagem| Python | 3.6 | Linguagem de programação de alto nível, orientada a objetos, interpretada e imperativa. |
|Framework| Django | 2.0.8 | Framework para desenvolvimento web rápido de alto nível escrito em python, baseado no padrão MTV. |
|Plataforma| Web - Navegadores Google Chrome, Safari e Firefox | -- | -- |
|Virtualização| Docker | 18.03.1-ce | O Docker fornece uma camada adicional de abstração e automação de virtualização de nível de sistema operacional. |
|Virtualização| Docker-compose | 1.22.0 |  Ferramenta para a criação e execução de múltiplos containers de aplicação da Docker. |
|Base de dados| API Salic | -- | API aberta para acesso aos dados do portal SALIC. |

## <a name="4"></a>4. Visão Geral    

### <a name="4.1"></a>4.1. Diagrama de pacotes

### <a name="4.2"></a>4.2. Pacotes de Design Significativos do Ponto de Vista da Arquitetura  

## <a name="5"></a>5. Arquitetura dos Serviços e visão de Implementação

### <a name="5.1"></a>5.1.

### <a name="5."></a>5.2.

## <a name="6"></a>6. Visão de Dados

## <a name="7"></a>10. Referências
ARTEFATO: DOCUMENTO DE ARQUITETURA DE SOFTWARE. FUNPAR. Disponível em: <http://www.funpar.ufpr.br:8080/rup/process/artifact/ar_sadoc.htm>. Acesso em: 04 de Setembro de 2018.

WIKIPEDIA: Engenharia de software baseada em componentes. Disponível em: <https://pt.wikipedia.org/wiki/Engenharia_de_software_baseada_em_componentes>.  Acesso em: 04 de Setembro de 2018.

DJANGO: DOCUMENTAÇÃO DO DJANGO: <https://docs.djangoproject.com/pt-br/2.1/>. Acesso em: 05 de Setembro de 2018.

PADRÕES ARQUITETURAIS MVC X ARQUITETURA DO DJANGO. GITHUB. Disponível em: <https://github.com/fga-gpp-mds/A-Disciplina/wiki/Padr%C3%B5es-Arquiteturais---MVC-X-Arquitetura-do-Django>. Acesso em: 09 de Setembro de 2018.

DJANGO MODELS. Disponível em: <https://django-portuguese.readthedocs.io/en/1.0/topics/db/models.html>. Acesso em: 09 de Setembro de 2018

