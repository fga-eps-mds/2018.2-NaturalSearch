from django.shortcuts import render
import requests,json   

def home(request):
    return render(request,'natural_search/home.html')

def get_proponents_json():
    #para testar só as duas ultimas paginas descomente:
    #actualLink = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&offset=91700&format=json&"
    
    proponent_current_ink = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=1&offset=44171&format=json&"

    while True:
        
        url = proponent_current_ink
        response = requests.get(url)
        data = json.loads(response.text)

        #primeira camada: dicionário
        count = data['count'] #já é um int
        links = data['_links'] #é um dicionário
        embedded = data['_embedded'] #é um dicionário

        #print(proponent_current_ink)

        proponents = []
        proponents.append(get_proponents_labels(embedded, count)) 
        print(proponents)       

        if 'next' in links:
            proponent_current_ink = links['next']
        else:
            break


def get_proponents_labels(embedded, count):
        proponents = []
        proponent = []
        for proponent_number in range(0, count):

                #proponents.append(embedded['proponentes'][proponent_number])
                proponent.append(embedded['proponentes'][proponent_number]['nome'])
                proponent.append(embedded['proponentes'][proponent_number]['responsavel'])
                proponent.append(embedded['proponentes'][proponent_number]['tipo_pessoa'])
                proponent.append(embedded['proponentes'][proponent_number]['UF'])
                proponent.append(embedded['proponentes'][proponent_number]['municipio'])
                proponent.append(embedded['proponentes'][proponent_number]['total_captado'])

                proponent_id = embedded['proponentes'][proponent_number]['_links']['projetos'].split('=')
                proponent.append(proponent_id[1])
                proponents.append(proponent)

                proponent = []
        
        return proponents

get_proponents_json()

