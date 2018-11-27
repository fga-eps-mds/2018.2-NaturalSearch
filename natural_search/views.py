# -*- coding: utf-8 -*-
# DjangoRest imports
from django.db import connection
from django.shortcuts import render, HttpResponse, redirect
import requests,json
from rest_framework import viewsets

# Local DjangoRest imports
from natural_search.models import Project, Proponent
from natural_search.serializers import ProjectSerializer, ProponentSerializer

# Links para coleta de dados de proponentes e projetos da api
# proponent_current_link = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=100&offset=44200&format=json&"
projects_current_link = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&format=json&"
# projects_current_link ="http://api.salic.cultura.gov.br/v1/projetos/?limit=100&offset=92400&format=json&"
proponent_current_link = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=100&format=json"

def home(request):
#Render the homepage
    return redirect('/projeto/')

def search_proponents(proponent_current_link):
    '''Function responsible for iterate with the api, generating the proponent json,
    extracting data from it and calling the function to insert the data into DB.
    '''
    iteration = 0
    while True:
        iteration += 1

        url = proponent_current_link
        response = requests.get(url)
        data = json.loads(response.text)

        #First layer: Dictionary
        count = data['count'] #já é um int
        links = data['_links'] #é um dicionário
        embedded = data['_embedded'] #é um dicionário
        print(proponent_current_link)

        get_proponents_labels(embedded, count)


        if 'next' in links:
            proponent_current_link = links['next']
        else:
            break

def get_proponents_labels(embedded, count):
# This function receives the json and inserts proponent data into DB
        for proponent_number in range(0, count):
                # Second layer: embedded
                # proponents.append(embedded['proponentes'][proponent_number])
                nome = embedded['proponentes'][proponent_number]['nome']
                responsavel = embedded['proponentes'][proponent_number]['responsavel']
                tipo_pessoa = embedded['proponentes'][proponent_number]['tipo_pessoa']
                UF = embedded['proponentes'][proponent_number]['UF']
                municipio = embedded['proponentes'][proponent_number]['municipio']
                total_captado = embedded['proponentes'][proponent_number]['total_captado']

                # Para adicionar os proponentes no banco descomentar as prox duas linhas
                # PS: nao rodar migrate/makemigrations com as prox duas linhas descomentadas

                proponent_instance = Proponent.objects.create(nome = nome, responsavel = responsavel, tipo_pessoa = tipo_pessoa, UF=UF, municipio= municipio, total_captado=total_captado )
                proponent_instance.save()

def search_projects(projects_current_link):
    '''Function responsible for iterate with the api, generating the project json,
    extracting data from it and calling the function to insert the data into DBself.
    '''
    iteration = 0
    while True:
        iteration += 1

        url = projects_current_link
        response = requests.get(url)
        data = json.loads(response.text)

        # First layer: Dictionary
        # total = data['total']
        count = data['count']  # já é um int
        links = data['_links']  # é um dicionário
        embedded = data['_embedded']
        print(projects_current_link)

        get_projects_labels(embedded, count)

        if 'next' in links:
            projects_current_link = links['next']
        else:
            break

def get_projects_labels(embedded, count):
# This function receives the json and inserts projects data into DB
    for numero_projeto in range(0,count):
            # Second layer: embedded
            # projetos = embedded['projetos'][numero_projeto]['projetos']
            PRONAC = embedded['projetos'][numero_projeto]['PRONAC']
            ano_projeto = embedded['projetos'][numero_projeto]['ano_projeto']
            nome = embedded['projetos'][numero_projeto]['nome']
            cgccpf = embedded['projetos'][numero_projeto]['cgccpf']
            proponente = embedded['projetos'][numero_projeto]['proponente']
            segmento = embedded['projetos'][numero_projeto]['segmento']
            area = embedded['projetos'][numero_projeto]['area']
            UF = embedded['projetos'][numero_projeto]['UF']
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

            # Para adicionar os projetos no banco descomentar as prox duas linhas
            # PS: nao rodar migrate/makemigrations com as prox duas linhas descomentadas

            project_instance = Project.objects.create(PRONAC=PRONAC, ano_projeto=ano_projeto, nome=nome, cgccpf=cgccpf, proponente=proponente, segmento=segmento, area=area, UF=UF, municipio=municipio, data_inicio= data_inicio, data_termino=data_termino, mecanismo=mecanismo, enquadramento=enquadramento, valor_projeto=valor_projeto, valor_captado=valor_captado, valor_proposta = valor_proposta, valor_solicitado=valor_solicitado, valor_aprovado=valor_aprovado)
            project_instance.save()

def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()
    
# ViewSets define the view behavior.
class ProjectViewSet(viewsets.ModelViewSet):
    # project_exists = db_table_exists('natural_search_project')
    queryset = Project.objects.all()
    # if project_exists is True:
    #    if not queryset:
    #        search_projects(projects_current_link)
    serializer_class = ProjectSerializer

# ViewSets define the view behavior.
class ProponentViewSet(viewsets.ModelViewSet):
    # proponent_exists = db_table_exists('natural_search_proponent')
    queryset = Proponent.objects.all()
    # if proponent_exists is True:
    #    if not queryset:
    #        search_proponents(proponent_current_link)
    serializer_class = ProponentSerializer
