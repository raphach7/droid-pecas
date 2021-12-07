from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Anunciante
from rest_framework.test import APIClient



# Create your tests here.
class FluxoPrincipalTestes(TestCase):
  def setup(self):
    #criar usuario anunciante
    usuario_anunciante = User.objects.create(username="bob")
    usuario_anunciante.set_password("naotemsenha123")
    usuario_anunciante.save()
    Anunciante.objects.create(usuario = usuario_anunciante)
    

  '''
  Teste da criacao de demanda
  '''
  def test_demanda(self):
    self.setup()
    usuario = User.objects.get(username="bob")  
    data = {"descricao": "roda",
            "endereco_entrega": {
                "rua": "Rua Reginaldo Fernandes Otavio",
                "numero": "126",
                "complemento": "Casa",
                "bairro": "Tangará",
                "cep": "46765-000",
                "estado": "BA",
                "cidade": "Piatã"},
            "contato": {
                "ddd": "77",
                "celular": "98104-2000"}
            }
    
    url = '/demandas/'
    cliente = APIClient()
    cliente.credentials(HTTP_AUTHORIZATION='Token ' + str(usuario.auth_token))
    request = cliente.post(url, format='json', data=data)
    self.assertQuerysetEqual(str(request.status_code), '201')
  
  