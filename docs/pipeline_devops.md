---
layout: default
---

# Pipeline DevOps

|           Data          |         Versão         |       Descrição   |         Autores   |
|:----------------------:|:------------------------:|:---------------------:|:--------------:|
| 02/10/2018       |           0.1                | Versão inicial do Pipeline do Devops |  Igor Araújo de Sousa |

<br>
<br>

Este documento visa definir como será executado a Integração contínua e deploy Contínuo.
Para que o deploy ocorra de forma simples e direta é necessário criar uma conta no GitHub para versionar o código,a partir daí espelhamos a branch do GitHub com o GitLab para que possamos utilizar as ferramentas do GitLab CI/CD.Logo após configurarmos o .gitlab-ci,arquivo de configuração para Integação Contínua,é necessário utilizar o DockerHub para mandar uma imagem do projeto,que é atualizada toda vez que o pipeline atende os requisitos de passar nos testes unitários.Logo após ,o Gitlab CD pega a imagem do projeto que foi gerada no stage anterior do pipeline e envia para uma máquina via ssh, para que se possa utilizar o serviço,também foi necessário  alugar uma máquina na Digital Ocean para hospedar a aplicação.

![Roadmap_ProductOwner](images/Pipeline_devops.png)

[ver imagem em tamanho original](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/Pipeline_devops.png)