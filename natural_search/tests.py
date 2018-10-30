import unittest
# from django.test import TestCase


# Create your tests here.
class TestProponent(unittest.TestCase):

    def test_for_gitlabci_build(self):
        a = 1
        b = 1

        self.assertEqual(a, b)
    