from django.core.management.base import BaseCommand, CommandError
from django.shortcuts import render, HttpResponse, redirect
import requests,json

class Command(BaseCommand):
    def handle(self, *args, **options):
        ## atualizaçãod e projetos
        project_salic_link = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&format=json&"
        url_salic = project_salic_link
        response_salic = requests.get(url_salic)
        data_salic = json.loads(response_salic.text)
        total_salic = data_salic['total'] #já é um int

        project_api_link = "http://68.183.107.229:8000/projeto/"
        url_api = project_api_link
        response_api = requests.get(url_api)
        data_api = json.loads(response_api.text)
        total_api = data_api['count'] #já é um int

        if total_api < total_salic:
            print("total de projetos desatualizado")
        
        ##atualização de proponentes
        proponent_current_link = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=100&offset=44200&format=json&"


        

