import unittest
from django.test import TestCase
from natural_search import views

# Create your tests here.
""" class TestProponent(unittest.TestCase):
    
    def test_get_proponents_labels(self):
        #last_proponent_json_link = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=1&offset=44171&format=json&"
        json = {'proponentes': 
                [{'nome': 'Aguinaldo Silva Filho', 
                  'cgccpf': '***855788**', 
                  '_links': 
                    {'self': 'http://api.salic.cultura.gov.br/v1/proponentes/217713ede204e05fe552821b4f7898419a0da9c47f4662d568bd15', 
                    'projetos': 'http://api.salic.cultura.gov.br/v1/projetos/?proponente_id=217713ede204e05fe552821b4f7898419a0da9c47f4662d568bd15'}, 
                  'tipo_pessoa': 'fisica', 
                  'responsavel': 'Aguinaldo Silva Filho', 
                  'UF': 'SP', 
                  'total_captado': 299190.0, 
                  'municipio': 'São Paulo'}]}
        result = views.save_projects_data(json, 1)
        proponent = [{'nome': 'Aguinaldo Silva Filho', 
                      'responsavel': 'Aguinaldo Silva Filho', 
                      'tipo_pessoa': 'fisica', 
                      'UF': 'SP', 
                      'municipio': 'São Paulo', 
                      'total_captado': 299190.0, 
                      'proponente_id': '217713ede204e05fe552821b4f7898419a0da9c47f4662d568bd15'
                      }]

        self.assertEqual(result, proponent) """