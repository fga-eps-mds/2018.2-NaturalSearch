---
layout: default
---

# Resuldado da Sprint 7


## Informações Básicas

| Sprint | Início | Término | Duração | Pontuação Total | Pontuação concluída |
|---|---|---|---|---|---|
| 4 | 22/10/2018 | 27/10/2019 | 6 dias | 54 | 25 |

### Presença na Sprint Review e Retroscpective

| Membro | Presença |
|---|---|
|Filipe Coelho Hilário Barcelos| ok |
|Igor Araújo de Sousa | ok |
|Shermam Tácia da Costa Lima | &#x2718; |
|Mikhaelle de Carvalho Bueno | ok |
|Marcos Vinícius Rodrigues da Conceição | ok |
|Fabiana Luiza V. P. Ribas | ok |
|Gustavo Duarte Moreira | ok |
|Michel Martins de Camargo| ok |

### Papéis 

|Papel | Responsável |
|---|---|
| Shermam Lima | Arquiteta |
| Filipe Barcelos e Igor Sousa | Product Owner |
| Marcos Vinícius Rodrigues | Scrum Master |
| Igor Sousa | Devops |
| Mikhaelle Bueno, Marcos Conceição, Fabiana Ribas, Gustavo Moreira, Michel Camargo | Desenvolvedores |

### Sprint Backlog

| Issue | Descrição | Pontos | Status | Motivo |
|---|---|---|---|---|
|[US13](https://github.com/fga-eps-mds/2018.2-NaturalSearch/issues/128)|US13-Eu, como desenvolvedor, desejo criar uma API para disponibilizar as informações obtidas em formato JSON.|20|Concluída|-|
|[US16](https://github.com/fga-eps-mds/2018.2-NaturalSearch/issues/136)|US16-Eu, como desenvolvedor, desejo conectar os projetos com os respectivos proponentes no banco de dados.|13|60%|Problema com o backup de dados do Neo4j dentro do Docker |
|[US17](https://github.com/fga-eps-mds/2018.2-NaturalSearch/issues/137)|Eu, como desenvolvedor, desejo remover informações desnecessárias de proponentes que serão utilizadas.|5|Concluída|-|
|[US18](https://github.com/fga-eps-mds/2018.2-NaturalSearch/issues/138)|US18-Eu, como desenvolvedor, desejo testar toda a aplicação de visualização de grafos.|8|70%|Atraso devido falta de tempo,e conhecimento insuficiente sobre testes|
|[US19](https://github.com/fga-eps-mds/2018.2-NaturalSearch/issues/139)|US19-Eu, como desenvolvedor, desejo testar toda a aplicação de processamento de dados da Salic API.|8|70%|Atraso devido a dependência da conclusão da US13|

## Pareamento 

| Membro  | Membro |
|---|---|
| Shermam Lima | Michel Camargo |
| Fabiana Ribas | Igor Sousa |
| Gustavo Moreira | Mikhaelle Bueno |
| Filipe Barcelos | Marcos Conceição |

## Monitoramento e Controle da Sprint 

| Membros | 22/10 | 23/10 | 24/10 |25/10 | 26/10 | 27/10 |
|---|---|---|---|---|---|---|
|Filipe Coelho Hilário Barcelos| &#10004; | &#10004; | &#10004;| &#x2718; | &#10004; | &#10004; |
|Igor Araújo de Sousa | &#x2718; | &#10004; | &#10004; | &#10004; | &#10004; | &#10004; |
|Shermam Tácia da Costa Lima | &#10004; | &#10004; | &#10004; | &#10004; | &#10004; | &#x2718; |
|Mikhaelle de Carvalho Bueno | &#10004; | &#10004; | &#10004; | &#10004; | &#10004; | &#10004; |
|Marcos Vinícius Rodrigues da Conceição | &#10004; | &#10004; | &#10004; | &#x2718; | &#10004; | &#10004; |
|Fabiana Luiza V. P. Ribas | &#10004; | &#10004; | &#10004; | &#10004; | &#10004; | &#10004; |
|Gustavo Duarte Moreira | &#10004; | &#10004; | &#10004; | &#10004; | &#10004; | &#10004; |
|Michel Martins de Camargo| &#10004; | &#10004; | &#10004;| &#x2718; | &#10004;| &#10004;|

## Retrospectiva da Sprint

### Pontos Positivos

- Maior aprendizado e facilidade para a implementação da história.
- Conclusão da [US13](https://github.com/fga-eps-mds/2018.2-NaturalSearch/issues/128) essencial para a continuidade de outras histórias. 
- Boa comunicação da equipe.
- Facilidade de pareamento.
- Alto indice de presença e participação nas reuniões.

### Pontos Negativos

- Baixo número de conclusões de histórias devido as dependências entre as mesmas;
- Falta de conhecimento em testes;
- Dificuldade técnica com banco de dados;
- Tecnologia com conhecimento disponível escasso; 
- Tempo restante de projeto.

 

### Melhorias 

- Tentar evitar que histórias se acumulem de maneira que comprometam as sprints seguintes.

## Métricas

### Velocity

O velocity desta semana é apresentado a seguir:

<br>

![velocity_Sprint_7](/docs/images/velocity_sprint7.jpg)

[ver imagem em tamanho original](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/velocity_sprint7.jpg)

<br>

### Burndown

O burndown desta semana é apresentado a seguir:

![velocity_Sprint_7](/docs/images/burndown_sprint7.jpg)

[ver imagem em tamanho original](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/images/burndown_sprint7.jpg)

## Análise do Scrum Master

Está semana o grupo se deparou com um problema onde o atraso de uma história da sprint 06, causou um efeito dómino levando ao atraso da conclusão de outras histórias, outro problema foi a dificuldade de realizar um backup dos dados do neo4j dentro do ambiente docker levando a procura de alternativas de servidores online para sanar esse problema e atrasando a entrega dessa história. A equipe conseguiu obter êxito na conclusão da US-13 e adquiriu conhecimento suficiente para a conclusão dos testes na próxima sprint, agora ganhamos mais um respiro para a continuidade saudável das outras histórias. Além do _burndown_, é possível verificar que a produtividade da equipe caiu um pouco devido a esses problemas de modo a obter uma média de 26,5 pontos no gráfico _velocity_, o que é 0,3 pontos a menos do que na Sprint 6.
