from django.core.management.base import BaseCommand, CommandError
from django.shortcuts import render, HttpResponse, redirect
import requests,json
from natural_search.models import Project, Proponent
from natural_search.serializers import ProjectSerializer, ProponentSerializer

class Command(BaseCommand):
    def handle(self, *args, **options):
        i=0
        j=0
        ## atualizaçãod e projetos
        project_salic_link = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&offset=92800&format=json&"
        url_proj_salic = project_salic_link
        response_proj_salic = requests.get(url_proj_salic)
        data_proj_salic = json.loads(response_proj_salic.text)
        total_proj_salic = data_proj_salic['total'] #já é um int

        project_api_link = "http://68.183.107.229:8000/projeto/"
        url_proj_api = project_api_link
        response_proj_api = requests.get(url_proj_api)
        data_proj_api = json.loads(response_proj_api.text)
        total_proj_api = data_proj_api['count'] #já é um int

        if total_proj_api < total_proj_salic:
            while (i<2):
                url_proj_salic = project_salic_link
                response_proj_salic = requests.get(url_proj_salic)
                data_proj_salic = json.loads(response_proj_salic.text)
                
                count = data_proj_salic['count']  # já é um int
                links = data_proj_salic['_links']  # é um dicionário
                embedded = data_proj_salic['_embedded']

                check_proj_exist(embedded,count)
                project_salic_link = links['next']
                i+=1
        
        ##atualização de proponentes
        proponent_salic_link = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=100&format=json"
        url_prop_salic = proponent_salic_link
        response_prop_salic = requests.get(url_prop_salic)
        data_prop_salic = json.loads(response_prop_salic.text)
        total_prop_salic = data_prop_salic['total'] #é um dicionário
        #print(total_prop_salic)

        proponent_api_link = "http://68.183.107.229:8000/proponente/"
        url_prop_api = proponent_api_link
        response_prop_api = requests.get(url_prop_api)
        data_prop_api = json.loads(response_prop_api.text)
        total_prop_api = data_prop_api['count'] #é um dicionário
        #print(total_prop_api)

        if(total_prop_api < total_prop_salic):
            print("total de proponentes desatualizado")

def check_proj_exist(embedded, count):
    for numero_projeto in range(0,count):
        PRONAC = embedded['projetos'][numero_projeto]['PRONAC']
        PROJECT = Project.objects.filter(PRONAC=PRONAC)
        print(PROJECT)
        if not PROJECT:
            print(False)
        else:
            print(True)