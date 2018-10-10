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
            PRONAC = projetos['PRONAC']
            ano_projeto = projetos['ano_projeto'] 	
            nome = projetos['nome']
            cgccpf = projetos['cgccpf']
            proponente = projetos['proponente']
            segmento = projetos['segmento']
            area = projetos['area']
            UF  = projetos['UF']
            municipio = projetos['municipio']
            data_inicio = projetos['data_inicio']
            data_termino = projetos['data_termino']
            mecanismo = projetos['mecanismo']
            enquadramento = projetos['enquadramento']
            valor_projeto = projetos['valor_projeto']
            valor_captado = projetos['valor_captado']
            valor_proposta = projetos['valor_proposta']
            valor_solicitado = projetos['valor_solicitado']
            valor_aprovado = projetos['valor_aprovado']
            _links = projetos['_links']
           

            #quarta camada: Links
            fornecedores = _links['fornecedores']
            _self = _links['self']
            incentivadores = _links['incentivadores']
            _proponente = _links['proponente']
   
search_projects()
