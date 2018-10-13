# -*- coding: utf-8 -*-
from django.shortcuts import render
import requests,json   

proponent_current_link = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=100&offset=44000&format=json&"

def home(request):
    return render(request,'natural_search/home.html')

def get_proponents_json(proponent_current_link):
    #para testar só as duas ultimas paginas descomente:
    #actualLink = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=100&offset=44000&format=json&"

    proponents_list = []
    
    while True:
        url = proponent_current_link
        response = requests.get(url)
        data = json.loads(response.text)

        #primeira camada: dicionário
        count = data['count'] #já é um int
        links = data['_links'] #é um dicionário
        embedded = data['_embedded'] #é um dicionário
        #print(proponent_current_link)


        proponents = get_proponents_labels(embedded, count)
        for proponent in proponents:
                proponents_list.append(proponent)

        #print(proponents_list)       

        if 'next' in links:
            proponent_current_link = links['next']
        else:
            break
        
    proponents_json = {
        'proponentes': proponents_list
    }

    with open('proponentes.json', 'w') as proponents_file:
        json.dump(proponents_json, proponents_file, ensure_ascii=False)

    #print(proponents_json)


def get_proponents_labels(embedded, count):
        proponents = []
        proponent = {}
        for proponent_number in range(0, count):

                #proponents.append(embedded['proponentes'][proponent_number])
                
                nome = embedded['proponentes'][proponent_number]['nome']
                responsavel = embedded['proponentes'][proponent_number]['responsavel']
                tipo_pessoa = embedded['proponentes'][proponent_number]['tipo_pessoa']
                UF = embedded['proponentes'][proponent_number]['UF']
                municipio = embedded['proponentes'][proponent_number]['municipio']
                total_captado = embedded['proponentes'][proponent_number]['total_captado']
                proponent_id_aux = embedded['proponentes'][proponent_number]['_links']['projetos'].split('=')
                proponent_id = proponent_id_aux[1]

                proponent = {
                        'nome': nome,
                        'responsavel': responsavel,
                        'tipo_pessoa': tipo_pessoa,
                        'UF': UF,
                        'municipio': municipio,
                        'total_captado': total_captado,
                        'proponente_id': proponent_id
                }
                '''
                proponent.append(embedded['proponentes'][proponent_number]['nome'])
                proponent.append(embedded['proponentes'][proponent_number]['responsavel'])
                proponent.append(embedded['proponentes'][proponent_number]['tipo_pessoa'])
                proponent.append(embedded['proponentes'][proponent_number]['UF'])
                proponent.append(embedded['proponentes'][proponent_number]['municipio'])
                proponent.append(embedded['proponentes'][proponent_number]['total_captado'])
                proponent.append(proponent_id)
                '''
                proponents.append(proponent)

                proponent = {}
        
        return proponents

get_proponents_json(proponent_current_link)

