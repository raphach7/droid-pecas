from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Anunciante, Demanda
from rest_framework.test import APIClient



# Create your tests here.
class FluxoPrincipalTestes(TestCase):
  def setup(self):
    #criar usuario anunciante
    usuario_anunciante = User.objects.create(username="bob")
    usuario_anunciante.set_password("naotemsenha123")
    usuario_anunciante.save()
    Anunciante.objects.create(usuario = usuario_anunciante)
    

  """
  Teste CRUD e manipulacao de demanda
  """
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
    
    cliente = APIClient()
    cliente.credentials(HTTP_AUTHORIZATION="Token " + str(usuario.auth_token))
    
    """
    Criar demanda
    """
    url = "/demandas/"
    request = cliente.post(url, format="json", data=data)
    self.assertEqual(request.status_code, 201)
    
    """
    Listar demandas
    """
    url = "/demandas/"
    request = cliente.get(url)
    self.assertEqual(request.status_code, 200)
    
    """
    Finalizar demanda
    """
    url = "/demandas/1/finalizar/"
    request = cliente.get(url)
    self.assertEqual(request.status_code, 200)
    
    demanda = Demanda.objects.get(id=1)
    self.assertEqual(demanda.status_finalizacao, True)
    
    """
    Editar demanda
    """
    data = {"descricao": "roda",
           "endereco_entrega": {
               "rua": "Avenida Castro Alves",
               "numero": "77",
               "complemento": "Casa",
               "bairro": "Centro",
               "cep": "46765-000",
               "estado": "BA",
               "cidade": "Piatã"},
           "contato": {
               "ddd": "77",
               "celular": "98104-2000"}
           }
    url = "/demandas/1/"
    request = cliente.put(url, format="json", data=data)
    self.assertEqual(request.status_code, 200)
    
    """
    Deletar demanda
    """
    url = "/demandas/1/"
    request = cliente.delete(url)
    self.assertEqual(request.status_code, 200)
    
    
  