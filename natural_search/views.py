from django.shortcuts import render
import requests, json

def home(request):
    return render(request,'natural_search/home.html')

def get_proponents_json():
    #para testar só as duas ultimas paginas descomente:
    #actualLink = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&offset=91700&format=json&"
    
    proponent_current_ink = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=100&offset=44000&format=json&"

    while True:
        
        url = proponent_current_ink
        response = requests.get(url)
        data = json.loads(response.text)

        #primeira camada: dicionário
        count = data['count'] #já é um int
        links = data['_links'] #é um dicionário
        embedded = data['_embedded'] #é um dicionário

        print(proponent_current_ink)

        proponents = []
        proponents.append(get_proponents_labels(embedded, count))        

        if 'next' in links:
            proponent_current_ink = links['next']
        else:
            break


def get_proponents_labels(embedded, count):
        proponents = []
        for proponent_number in range(0, count):

                proponents.append(embedded['proponentes'][proponent_number])

                '''
                nome = proponentes['nome']
                cgccpf = proponentes['cgccpf']
                responsavel = proponentes['responsavel']
                tipo_pessoa = proponentes['tipo_pessoa']
                UF = proponentes['UF']
                municipio = proponentes['municipio']
                total_captado = proponentes['total_captado']
                
                _self = _links['self']
                projetos = _links['projetos']
                '''
        
        return proponents

get_proponents_json()

