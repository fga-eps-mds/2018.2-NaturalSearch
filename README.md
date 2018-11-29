---
layout: default
---

# Passo a Passo instalação NaturalSearch 

NaturalSearch é um sistema que reúne dados a respeito de propostas de projetos e proponentes culturais a serem incentivados pelo Ministério da Cultura [MINC](http://www.cultura.gov.br/) por meio da [lei Rouanet](http://rouanet.cultura.gov.br/o-que-e/). Nele é possivel realizar uma pesquisa sobre as informações dos projetos e proponentes e visualizar o resultado em forma de grafo e suas conexões.  Você pode encontrar mais sobre o NaturalSearch em [https://fga-eps-mds.github.io/2018.2-NaturalSearch/](https://fga-eps-mds.github.io/2018.2-NaturalSearch/).


- Package version: 1.0.0
- Host: *http://68.183.107.229:3000* or *0.0.0.0:3000*

## Requerimentos.

Docker, docker-compose.

## Instalação e Uso


### 2018.2- Natural Search
Repositório oficial do projeto Natural Search da Universidade de Brasília. Link para repositório oficial https://github.com/fga-eps-mds/2018.2-NaturalSearch.

### Como contribuir

1. Crie um fork ou clone o repositório.

```sh
git clone https://github.com/NaturalSearch/NaturalSearch_visualization.git
```

2. Caso queira alterar algo crie uma branch seguindo a política de branchs deste projeto. 

3. Dentro da pasta NaturalSearch_visualization/NaturalSearch onde contém o Dockerfile execute o comando use (sudo se necessário):
```sh
$ docker-compose run app bash
```
4. Dentro do container execute para a instalação de todos os módulos necessários:

```sh
root@cf461053cf90:/code# npm install
```
5. Abra outra instância do terminal fora do container e execute:

```sh
$ docker-compose up
```
6. O servidor local deverá estar funcionando e você poderá acessar o Neo4j na porta:
```
0.0.0.0:7474

```
7. O username, o password e o link default de acesso ao banco estão dentro da NaturalSearch em arquivos .txt. Com elas você terá acesso ao Banco local.

![Natural_neo4j](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/Natural_neo4j.png)

[ver imagem em tamanho original](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/Natural_neo4j.png)

8. Para acessar a página, com o servidor local rodando vá até:  **0.0.0.0:3000**

![Natural_index](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/Natural_index.png)

[ver imagem em tamanho original](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/Natural_index.png)


9. Visualizar os resultados de uma pesquisa 0.0.0.0:3000/result

![Natural_result](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/Natural_result.png)

[ver imagem em tamanho original](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/Natural_result.png)

10. Para visualizar o grafo gerado com as informações de todos os projetos ligados a algum proponente clique no ícone da lupa. 

![Natural_graph](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/Natural_graph.png)

[ver imagem em tamanho original](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/Natural_graph.png)


## Autorizações

Todos os endpoints não requerem autorização para consulta entretanto para adicionar, deletar ou modificar dados é necessário o login como administrador.

## Documentação

Toda documentação e toda informação do projeto se encontram em: https://fga-eps-mds.github.io/2018.2-NaturalSearch/

## Autores

equipe.naturalsearch@gmail.com





