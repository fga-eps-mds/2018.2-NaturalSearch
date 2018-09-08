---
layout: default
---

# Contribuindo com o NaturalSearch

Antes de decidir se deseja de fato contribuir conosco leia o [README](https://github.com/fga-eps-mds/2018.2-NaturalSearch/blob/gh-pages/README.md) do projeto e conheça melhor como funciona o nosso projeto, bem como o código de conduta da equipe.

# Como contribuir?

## Reportar Bugs

Caso deseje reportar um _bug_ no projeto, então:

* Crie uma [_issue_](https://github.com/fga-eps-mds/2018.2-NaturalSearch/issues/new) e marque-a com a label **bug** para que possamos ver e resolver o problema o mais rápido possível.

* Caso exista uma _issue_ para o problema, então, é possível adicionar um comentário sobre o problema se achar necessário.

## Adicionar/Modificar funcionalidades

Se o objetivo é adicionar e/ou modificar uma funcionalidade já existente, então:

* Verifique se existe uma _issue_ com a mesma modificação ou adição que você pretende realizar.

* Se não existir, crie uma nova [_issue_](https://github.com/fga-eps-mds/2018.2-NaturalSearch/issues/new) com um título significativo, adicione uma descrição e, no mínimo, uma label.

* Submeta as mudanças através de um _pull request_ e aguarde pela aprovação da equipe.

## Política de _commits_

É recomendado que todo contribuinte do projeto siga as orientações a seguir para realizar _commits_ de forma padronizada:

* _Commits_ exclusivamente em **inglês**.

* Mensagens curtas e significativas sobre o conteúdo do _commit_.

* Apenas _commits_ que adicionem incrementos significativos, ou seja, nada de _commits_ apenas mudando nomes de variáveis, por exemplo.

* Se estiver trabalhando em conjunto especifique os participantes no _commit_.

Exemplo:

    Adds project license (Descrição de uma atividade)

    Adds project code of conduct file

    Co-authored-by: FilipeKN4 <filipekn4@gmail.com> (Assinatura do(s)participante(s))

## Política de _branches_

Visando padronizar a criação de _branchs_ e facilitar a identificação do objetivo de criação de cada uma delas a equipe adota uma política de _branches_ que deve ser seguida completamente para qualquer um que visa contribuir com este projeto. A política segue o fluxo de trabalho da ferramenta [_git flow_](https://github.com/nvie/gitflow), sendo assim, recomenda-se fortemente a instalação e utilização dela. Os tipos de branch são utilizados são:

* **master** - é a _branch_ principal do repositório e realiza o papel de ambiente de produção. Nela só é aceito código devidamente testado e validado, de modo que todas as inserções nela feitas serão as _releases_ do projeto.

* **development** - é a _branch_ que concentrará todas as novas funcionalidades do projeto, onde realizará o papel de concentrar o trabalho do ambiente de desenvolvimento, correção de bugs e finalização de testes.   

* **feature/** - tipo de _branch_ utlizada para o desenvolvimento de uma nova _feature_ do projeto, de modo que o nome do deve ser "US - " e o número da história de usuário que essa _feature_ representa. Ex: "feature/ US - 01"

* **bugfix/** - _branch_ utilizada para corrigir _bugs_ de baixa ou média urgências e não estão presentes na **master**. O nome deve ser a descrição do _bug_. Ex: "bugfix/ descricao"

* **hotfix/** - _branch_ utilizada para corrigir _bugs_ de alta urgências que foram passados para a **master**. O nome deve ser a descrição do _bug_. Ex: "hotfix/ descricao"

* **release/** - _branch_ utilizada para a homologação do sistema e correções finais, caso sejam necessárias. O nome deve ser o  número da versão da nova _release_. Ex: "release/ v1.0"

### Usando o _git flow_

Para seguir o fluxo do _git flow_ no projeto da melhor forma abra o terminal do Linux e configure-o da seguinte forma. 

1 - Clone o repositório para sua máquina com o comando:

    git clone https://github.com/fga-eps-mds/2018.2-NaturalSearch.git

2 - Vá até a pasta do projeto e utilize:

    git flow init

Responda as perguntas exatamente da seguinte forma:

    Which branch should be used for bringing forth production releases?
        - development
        - gh-pages
        - master
    Branch name for production releases: [master]         

    Which branch should be used for integration of the "next release"?
        - development
        - gh-pages
    Branch name for "next release" development: [] development         

    How to name your supporting branch prefixes?
    Feature branches? [feature/] 
    Bugfix branches? [bugfix/] 
    Release branches? [release/] 
    Hotfix branches? [hotfix/] 
    Support branches? [support/] 
    Version tag prefix? [] v

Para a pergunta "Hooks and filters directory?" apenas pressine ENTER.

Agora que o _git flow_ foi configurado na sua máquina basta utilizá-lo. 

## Política de Issues

Para facilitar a comunicação e padronização de atividades da equipe por meio de [_issues_]() a equipe do Natural Search optou pela criação de uma política de _issues_ que deve ser seguida sem excessões por todos os membros e possíveis contribuintes com o produto. A seguir os padrões de _issues_ utilizados:

* Iniciadas sempre com verbo no infinitivo. Exemplo: 

    - "Elaborar Documento de Visão."

* Breve descrição que explica sobre o que se trata a _issue_ adicionada. Exemplo:

    - "Esta _issue_ refere-se a criação do Documento de Visão do Natural Search por parte dos membros da disciplina MDS."

Para issues referentes a histórias de usuário e histórias técnicas devem ser considerados, também, os padrões a seguir:

**User Story**: tipo de _issue_ utilizada para a marcação de histórias de usuário. O padrão deve ser:

- US01 - "descrição da issue"

**Tecnical Story**: tipo de _issue_ utilizada para marcação de histórias técnicas. O padrão deve ser:

- TS23 - "descrição da issue"

