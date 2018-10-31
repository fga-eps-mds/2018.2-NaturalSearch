import unittest
from django.test import TestCase, RequestFactory
from natural_search import views

# Create your tests here.
class TestProponent(TestCase):
    def setUp(self):

        self.proponent_current_link = "http://api.salic.cultura.gov.br/v1/proponentes/?limit=100&offset=44200&format=json&"
        self.proponent_current_link_wrong = "http://api.salic.cultura.gov.br/v1/wrongurl"
        self.projects_current_link ="http://api.salic.cultura.gov.br/v1/projetos/?limit=100&offset=92400&format=json&"
        self.projects_current_link_wrong ="http://api.salic.cultura.gov.br/v1/wrongurl"

    def test_search_proponents_wrong_link(self):

        with self.assertRaises(Exception):
            search_proponents(self.proponent_current_link_wrong)

    def test_search_projects_wrong_link(self):

        with self.assertRaises(Exception):
            search_projects(self.projects_current_link_wrong)
