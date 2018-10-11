from django.shortcuts import render
import requests, json

def home(request):
    return render(request,'natural_search/home.html')

def search_proponent():
        #para testar só as duas ultimas paginas descomente:
        #http://api.salic.cultura.gov.br/v1/proponentes/?limit=100&offset=44000&format=json&

    proponentCurrentLink = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=100&offset=44000&format=json&"

    while True:
        url = actualLink
        respose = requests.get(url)
        data = json.load(response.text)

        count = data['count']
        embedded = data['_embedded']
        total = data['total']
        link = data['_links']

        self_link = links['self']
        first_link = links['first']
        last_link = links['last']

        getProponentPag(embedded, count)

        if 'next' in links:
             proponentCurrentLink = links['next']
        else:
            break

def getProponentPag(enbedded,count):
        proponente = []
        for proponentes_id in range(0,count):
                proponente.append(embedded['proponentes'][proponentes_id], proponentes['nome']) 
                print(proponente)

                cgccpf = proponentes['cgccpf']
                responsavel = proponentes['responsavel']
                tipo_pessoa = proponentes['tipo_pessoa']
                UF = proponentes['UF']
                municipio = proponentes['municipio']
                total_captado = proponentes['total_captado']
                
                _self = _links['self']
                projetos = _links['projetos']

search_proponent()

'''
print(nome)
print(cgccpf)
print(responsavel)
print(tipo_pessoa)
print(UF)
print(municipio)
print(total_captado)
search_projects()
'''