# -*- coding: utf-8 -*-
from django.shortcuts import render
from natural_search.models import ProjetoList, Proposition, Proponent
from natural_search.serializers import ProjetoListSerializer, PropositionSerializer, ProponentSerializer
import requests,json   
from rest_framework import viewsets

proponent_current_link = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=100&offset=44000&format=json&"
projects_current_link = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&offset=91900&format=json&"

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

def search_projects(projects_current_link):
    #para testar só as duas ultimas paginas descomente:
    #projects_current_link = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&offset=91700&format=json&"
    
    

    projects_list = []

    while True:
        
        url = projects_current_link
        response = requests.get(url)
        data = json.loads(response.text)

        #primeira camada: dicionário
        total = data['total'] 
        count = data['count'] #já é um int
        links = data['_links'] #é um dicionário
        embedded = data['_embedded']

        #segunda camada: links
        #self_link = links['self']
        #first_link = links['first']
        #last_link = links['last']

        print(projects_current_link)

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
        
        with open('projects.json', 'w') as project_file:
            json.dump(projects_json, project_file, ensure_ascii=False)
        
        #print(projects_json)


def get_projects_labels(embedded, count):

    projects = []
    project = {}

    for numero_projeto in range(0,count):
            #segunda camada: embedded
            #projetos = embedded['projetos'][numero_projeto]['projetos']
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

search_projects(projects_current_link)

# ViewSets define the view behavior.
class ProjetoListViewSet(viewsets.ModelViewSet):
    queryset = ProjetoList.objects.all()
    serializer_class = ProjetoListSerializer

# ViewSets define the view behavior.
class PropositionViewSet(viewsets.ModelViewSet):
    queryset = Proposition.objects.all()
    serializer_class = PropositionSerializer

# ViewSets define the view behavior.
class ProponentViewSet(viewsets.ModelViewSet):
    queryset = Proponent.objects.all()
    serializer_class = ProponentSerializer