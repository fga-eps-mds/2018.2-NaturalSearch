from django.shortcuts import render
import requests,json 
    
def search_projects():
    #para testar só as duas ultimas paginas descomente:
    #projects_current_link = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&offset=91700&format=json&"
    
    projects_current_link = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&format=json&"

    projects_list = []

    while True:
        
        url = projects_current_link
        response = requests.get(url)
        data = json.loads(response.text)

        #primeira camada: dicionário
        total = data['total'] 
        count = data['count']
        links = data['_links'] 
        embedded = data['_embedded'] 

        #segunda camada: links
        self_link = links['self']
        first_link = links['first']
        last_link = links['last']

        #print(projects_current_link)

        projects = get_projects_labels(embedded,count)

        for project in projects:
            projects_list.append(project)
        
        if 'next' in links:
            projects_current_link = links['next']
        else:
            break
        
        projects_json = {
            'projects': projects_list
        }
        
        with open('projects.json' 'w') as project_file:
            json.dump(projects_json, project_file, ensure_ascii=False)


def get_projects_labels(embedded,count):
    projects = []
    project = {}

    for numero_projeto in range(0,count):
            #segunda camada: embedded
            projetos = embedded['projetos'][numero_projeto]['projetos']
            PRONAC = embedded['projetos'][numero_projeto]['PRONAC']
            ano_projeto = embedded['projetos'][numero_projeto]['ano_projeto'] 	
            nome = embedded['projetos'][numero_projeto]['nome']
            cgccpf = embedded['projetos'][numero_projeto]['cgccpf']
            proponente = embedded['projetos'][numero_projeto]['proponente']
            segmento = embedded['projetos'][numero_projeto]['segmento']
            area = embedded['projetos'][numero_projeto]['area']
            UF  = embedded['projetos'][numero_projeto]['UF']
            municipio = embedded['projetos'][numero_projeto]['municipio']
            data_inicio = embedded['projetos'][numero_projeto]['data_inicio']
            data_termino = embedded['projetos'][numero_projeto]['data_termino']
            mecanismo = embedded['projetos'][numero_projeto]['mecanismo']
            enquadramento = embedded['projetos'][numero_projeto]['enquadramento']
            valor_projeto = embedded['projetos'][numero_projeto]['valor_projeto']
            valor_captado = embedded['projetos'][numero_projeto]['valor_captado']
            valor_proposta = embedded['projetos'][numero_projeto]['valor_proposta']
            valor_solicitado = embedded['projetos'][numero_projeto]['valor_solicitado']
            valor_aprovado = embedded['projetos'][numero_projeto]['valor_aprovado']
            _links = embedded['projetos'][numero_projeto]['_links']
           
            project = {
                'projetos': numero_projeto, 
                'PRONAC': PRONAC,
                'ano_projeto': ano_projeto,
                'nome': nome,
                'cgccpf' : cgccpf,
                'proponente' : proponente,
                'segmento' : segmento,
                'area' : area,
                'UF'  : UF,
                'municipio' : municipio,
                'data_inicio' : data_inicio,
                'data_termino' : data_termino,
                'mecanismo' : mecanismo,
                'enquadramento' : enquadramento,
                'valor_projeto' : valor_projeto,
                'valor_captado' : valor_captado,
                'valor_proposta' : valor_proposta,
                'valor_solicitado' : valor_solicitado,
                'valor_aprovado' : valor_aprovado
            }

            #quarta camada: Links
            fornecedores = _links['fornecedores']
            _self = _links['self']
            incentivadores = _links['incentivadores']
            _proponente = _links['proponente']
   
            projects.append(project)

            project = {}

    return projects

search_projects()
