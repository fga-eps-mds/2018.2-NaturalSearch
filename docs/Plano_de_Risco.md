
# Plano de Gerenciamento de Riscos

### Histórico de versão

| Data | 29/08/2018 | Descrição | Autor |
|----------|----------|----------|----------|
| 29/08/18 | 0.1 | Início do Documento | Lucas Midlhey Cardoso Naves |
| 14/09/18 | 0.2 | detalhamento EAR e analise de riscos | Lucas Midlhey Cardoso Naves |
| 21/09/18 | 0.3 | Formatação e Descrição dos riscos | Shermam Tácia da Costa Lima |


### Sumário
1. Introdução
2. Objetivos
3. Indentificação dos riscos
4. Estrutura Analitica dos riscos
5. Analíse de riscos
6. Definição de probabilidade e impactos de riscos
7. Matriz de probabilidade e Impacto
9. Bibliografia

## 1. Introdução	
O Plano de gerenciamento de riscos tem como objetivo perceber e tratar pequenos riscos a fim de que não se tornem grandes riscos que possam preocupar o projeto.
Risco é o efeito (positivo ou negativo) de um evento ou de uma série de eventos que se manifesta em um ou em vários locais. Ele é calculado a partir da probabilidade deste evento se manifestar e do impacto que ele poderia causar. Alguns elementos devem ser identificados para se analisar riscos, incluindo evento, o que pode acontecer, probabilidade, com que frequência ele pode acontecer, impacto, o quão ruim ele pode ser, Mitigação, como pode reduzir estes riscos, contingência, como poderia reduzir este impacto.

## 2. Objetivos

O objetivo desse artefato é documentar os riscos associados ao projeto, bem como as ações a serem tomadas para que os mesmos sejam mitigados ou contornados.

## 3. Identificação dos Riscos

A identificação dos riscos é evento incerto que deve ser gerenciado para que se tenha um controle de todos os incidentes que podem acontecer. Observar os riscos promove um projeto mais seguro, garantindo eficiência do negócio e diminuindo problemas durante o processo.
Como o projeto é dividido em várias áreas, o processo de identificação de erros é contínuo, assim como, será necessário prevê-los antes da etapa de desenvolvimento.
Podemos encarar a identificação de riscos de duas maneiras positivo ou negativo, mas sendo um evento futuro então conseguimos gerenciá-los, diferente de problema que a nossa única forma de sanar é a contingência.

## 4. Estrutura analítica de Riscos

Trata-se de um mapeamento antecipado dos riscos do projeto, tem como objetivo auxiliar a compreensão e apresentação dos riscos de um projeto de forma estruturada, de certa forma é bem similar a uma Est rutura Analítica de Projeto (EAP) estando quanto mais abaixo o nível do risco maior o seu nível de detalhamento.
 

### Técnico
| Tipo | Descrição |
| -----------| -----------|
| Requisitos | Riscos pela falta de mapeamento e elicitamento de requisitos |
| Tecnologias | Riscos gerados pela tecnologia usada |
| Complexidade | Riscos gerados pela falta de evolução de conhecimento |
| Qualidade | Riscos decorrentes pela métrica do produto final |

### Externos

| Tipo | Descrição |
| -----------| -----------|
| Cliente | riscos gerados pelo cliente recorrentes ao projeto |
| Greve na UnB | Risco gerado pela UnB |

### Organizacional

| Tipo | Descrição |
| -----------| -----------|
| Recursos | Riscos gerados pela falta de material humano e material |
| Priorização | Risco gerados pela má escolha de histórias na Sprint |
| Dependências | Riscos que podem afetar a evolução do projeto |

### Gerenciamento do Projeto

| Tipo | Descrição |
| -----------| -----------|
| Estimativa | Risco que pode afetar o tempo de produção do projeto |
| Controle | Risco relacionado ao controle de atividades |
| Planejamento | Risco relacionado ao planejamento de confecção do projeto |
| Comunicação | Risco relacionado às atividades e meio de comunicação |

## 5. Análise de Riscos

Análise de risco contém três pilares conceituais, o futuro, a escolha e a mudança. Desta forma sempre estarão em evidência, o futuro pelo qual o risco poderá afetar o projeto quando não se sai como esperado, a escolha, que método devemos escolher, tamanho de equipe, delegação de afazeres no projeto e qual será a enfase da qualidade do software, a mudança acarreta principalmente quando influencia os requisitos do sistema e tecnologias de desenvolvimento.

## 6. Identificação dos Riscos

| ID | Se | por conta | o impacto será | Categoria EAR |
| --------- |--------- |--------- |--------- |--------- |
| RN01 | Cliente mudar o escopo | de definição da disciplina | replanejamento do projeto | Comunicação |
| RN02 | Um membro desistir da disciplina |	de motivos diversos | enfraquecimento no desempenho da equipe |	Recursos |
| RN03 | Um membro da equipe ficar ausente | de motivos diversos | enfraquecimento temporário no desempenho da equipe |Recursos |
| RN04 | Houver problemas na comunicação da equipe | do número de membros | dificuldade no gerenciamento | comunicação |
| RN05 | atividades não forem concretizadas no prazo | da falta de integração da equipe de desenvolvimento | atraso na baseline do projeto | Estimativas |
| RN06 | houver perdas de equipamentos | diversos motivos | atraso na entrega | Recursos |
| RN07 | não conseguiu desenvolver a arquitetura | falta de conhecimento no projeto | mal desenvolvimento | Tecnologia |
| RN08 | não tiver domínio no código | da falta de empenho | inviabilidade no projeto | Tecnologia |
| RN09 | Baixa produtividade da equipe | da falta de empenho da equipe de desenvolvimento | atraso no cronograma |Tecnologia |
| RN10 | a equipe não se adaptar a tecnologia de comunicação | da dificuldade de utilização | dificuldade no gerenciamento | Comunicação |
| RN11 | Mudar Arquitetura do projeto | de alguma tecnologia nãocompativel | atraso na entrega e ter que adaptar a nova tecnologia | tecnologia|
| RN12 | 

### 8. Definição de Probabilidades e Impactos de Riscos

A tabela abaixo define os intervalos para o peso de cada risco listado.
| Probabilidade | Intervalo | Peso |
| ----- | ----- | ----- |
| Muito baixa | 1% - 20% | 1 |
| Baixa | 21% - 40% | 2 |
| Média | 41% - 60% | 3 |
| Alta | 61% - 80% | 4 |

## Bibliografia
HILLSON, D. The risk breakdown structure (RBS) as an aid to effective risk management. Fifth European Project Management Conference. Cannes. 2002
PRESSMAN, Roger S. – “ Engenharia de Software ” - Makron Books do Brasil Editora Ltda

