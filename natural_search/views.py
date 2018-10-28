# -*- coding: utf-8 -*-
from django.shortcuts import render
from natural_search.models import Project, Proponent
from natural_search.serializers import ProjectSerializer, ProponentSerializer
import requests,json   
from rest_framework import viewsets

proponent_current_link = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=100&offset=44000&format=json&"
projects_current_link = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&offset=91900&format=json&"

Proponent.objects.all().delete()
Project.objects.all().delete()

def home(request):
    return render(request,'natural_search/home.html')

def get_proponents(proponent_current_link):

    while True:

        url = proponent_current_link
        response = requests.get(url)
        data = json.loads(response.text)

        #primeira camada: dicionário
        count = data['count'] #já é um int
        links = data['_links'] #é um dicionário
        embedded = data['_embedded'] #é um dicionário
        print(proponent_current_link)

        save_proponents_data(embedded, count)

        if 'next' in links:
            proponent_current_link = links['next']
        else:
            break

def save_proponents_data(embedded, count):

    for proponent_number in range(0, count):

            # proponents.append(embedded['proponentes'][proponent_number])
            
            nome = embedded['proponentes'][proponent_number]['nome']
            responsavel = embedded['proponentes'][proponent_number]['responsavel']
            tipo_pessoa = embedded['proponentes'][proponent_number]['tipo_pessoa']
            UF = embedded['proponentes'][proponent_number]['UF']
            municipio = embedded['proponentes'][proponent_number]['municipio']
            total_captado = embedded['proponentes'][proponent_number]['total_captado']

            #PS: nao rodar migrate/makemigrations com as prox duas linhas descomentadas
            proponent_instance = Proponent.objects.create(nome = nome, responsavel = responsavel, tipo_pessoa = tipo_pessoa, UF=UF, municipio= municipio, total_captado=total_captado )
            proponent_instance.save()

def get_projects(projects_current_link):

    while True:
        
        url = projects_current_link
        response = requests.get(url)
        data = json.loads(response.text)

        #primeira camada: dicionário
        total = data['total'] 
        count = data['count'] #já é um int
        links = data['_links'] #é um dicionário
        embedded = data['_embedded']

        print(projects_current_link)

        save_projects_data(embedded,count)

        if 'next' in links:
            projects_current_link = links['next']
        else:
            break


def save_projects_data(embedded, count):

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
           
            #PS: nao rodar migrate/makemigrations com as prox duas linhas descomentadas
            project_instance = Project.objects.create(PRONAC=PRONAC, ano_projeto=ano_projeto, nome=nome, cgccpf=cgccpf, proponente=proponente, segmento=segmento, area=area, UF=UF, municipio=municipio, data_inicio= data_inicio, data_termino=data_termino, mecanismo=mecanismo, enquadramento=enquadramento, valor_projeto=valor_projeto, valor_captado=valor_captado, valor_proposta = valor_proposta, valor_solicitado=valor_solicitado, valor_aprovado=valor_aprovado)
            project_instance.save()

get_proponents(proponent_current_link)
get_projects(projects_current_link)

# ViewSets define the view behavior.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# ViewSets define the view behavior.
class ProponentViewSet(viewsets.ModelViewSet):
    queryset = Proponent.objects.all()
    serializer_class = ProponentSerializer