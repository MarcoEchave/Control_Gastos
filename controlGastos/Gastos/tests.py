from django.test import TestCase
from .models import Banco
from django.urls.base import reverse

class TestBanco(TestCase):
    def setUp(self):
        self.valid_data = {
            'banco':'Bbva'
        }
        self.bad_data ={
            'banco':4592
        }
        Banco.objects.create(banco='Bbva')

    def test_create_banco_valid(self):
        response =self.client.get(reverse('getBanco'))
        self.assertEqual(response.status_code,302)

