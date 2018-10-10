import requests, json
    
def search_projects():
    #para testar só as duas ultimas paginas descomente:
    #actualLink = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&offset=91700&format=json&"
    
    actualLink = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&format=json&"

    while True:
        
        url = actualLink
        response = requests.get(url)
        data = json.loads(response.text)

        #primeira camada: dicionário
        total = data['total'] #já é um int
        count = data['count'] #já é um int
        links = data['_links'] #é um dicionário
        embedded = data['_embedded'] #é um dicionário

        #segunda camada: links
        self_link = links['self']
        first_link = links['first']
        last_link = links['last']

        print(actualLink)

        getProposalPag(embedded,count)
        
        if 'next' in links:
            actualLink = links['next']
        else:
            break

def getProposalPag(embedded,count):
    for numero_projeto in range(0,count):
            #segunda camada: embedded
            projetos = embedded['projetos'][numero_projeto]#[nummero_projeto] é um vetor q contem outro dicionário
            
            #terceira camada: projetos
            etapa = projetos['etapa']
            providencia = projetos['nome']
            area = projetos['area']
            enquadramento = projetos['enquadramento']
            objetivos = projetos['objetivos']
            ficha_tecnica = projetos['ficha_tecnica']
            situacao = projetos['situacao']
            outras_fontes = projetos['outras_fontes']
            acessibilidade = projetos['acessibilidade']  
            sinopse = projetos['sinopse']
            nome = projetos['nome']
            cgccpf = projetos['cgccpf']
            mecanismo = projetos['mecanismo']
            segmento = projetos['segmento']
            PRONAC = projetos['PRONAC']
            estrategia_execucao = projetos['estrategia_execucao']
            valor_aprovado = projetos['valor_aprovado']
            justificativa = projetos['justificativa']
            resumo = projetos['resumo']
            valor_solicitado = projetos['valor_solicitado']
            especificacao_tecnica = projetos['especificacao_tecnica']
            municipio = projetos['municipio']
            data_termino = projetos['data_termino']
            UF = projetos['UF']
            impacto_ambiental = projetos['impacto_ambiental']
            democratizacao = projetos['democratizacao']
            valor_projeto = projetos['valor_projeto']
            proponente = projetos['proponente']
            ano_projeto = projetos['ano_projeto']
            data_inicio = projetos['data_inicio']
            valor_captado = projetos['valor_captado']
            valor_proposta = projetos['valor_proposta']
            _links = projetos['_links']

            #quarta camada: Links
            fornecedores = _links['fornecedores']
            _self = _links['self']
            incentivadores = _links['incentivadores']
            _proponente = _links['proponente']
   
search_projects()