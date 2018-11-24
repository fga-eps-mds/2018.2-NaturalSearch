from django.core.management.base import BaseCommand, CommandError
from django.shortcuts import render, HttpResponse, redirect
import requests,json

class Command(BaseCommand):
    def handle(self, *args, **options):
        ## atualizaçãod e projetos
        project_salic_link = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&format=json&"
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
            print("total de projetos desatualizado")
        
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


        

