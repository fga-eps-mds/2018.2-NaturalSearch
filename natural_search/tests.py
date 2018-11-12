import unittest, json
from django.test import TestCase, RequestFactory
from natural_search import views

# Create your tests here.
class TestHomepage(TestCase):
    def test_home(self):
        resp = views.home('natural_search/home.html')

        self.assertEqual(resp.status_code, 200)


class TestProponent(TestCase):
#classe de testes para proponentes
    def setUp(self):
    #Define dados de proponentes para testar a API

        #links da api para proponentes
        self.proponent_current_link = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=100&offset=44200&format=json&"
        self.proponent_current_link_wrong = "http://api.salic.cultura.gov.br/v1/wrongurl"

    #testa search_proponents com um link da API errado
    def test_search_proponents_wrong_link(self):
        print(self.proponent_current_link_wrong)
        with self.assertRaises(Exception):
            views.search_proponents(self.proponent_current_link_wrong)

    #testa search_proponents com um link da API válido
    def test_search_proponents_link(self):
        print(self.proponent_current_link)
        self.assertIsNone(views.search_proponents(self.proponent_current_link))

class TestProject(TestCase):
#classe de teste de projetos
    def setUp(self):
        #Define dados de projetos para testar a API

        #links da API para teste de projetos
        self.projects_current_link ="http://api.salic.cultura.gov.br/v1/projetos/?limit=100&offset=92400&format=json&"
        self.projects_current_link_wrong ="http://api.salic.cultura.gov.br/v1/wrongurl"

    #testa search_projects com um link da api errado
    def test_search_projects_wrong_link(self):
        print(self.projects_current_link_wrong)
        with self.assertRaises(Exception):
            views.search_projects(self.projects_current_link_wrong)

    #testa search_projects com um link da api válido
    def test_search_projects_link(self):
        print(self.projects_current_link)
        self.assertIsNone(views.search_projects(self.projects_current_link))