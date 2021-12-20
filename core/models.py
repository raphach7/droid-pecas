from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from localflavor.br.models import BRPostalCodeField
from annoying.fields import AutoOneToOneField

ESTADOS = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    )
class Endereco(models.Model):

    cep = BRPostalCodeField()
    rua = models.CharField(max_length=256)
    numero = models.CharField(max_length=10, default="sn")
    bairro = models.CharField(max_length=200)
    estado = models.CharField(choices=ESTADOS, max_length=2)
    cidade = models.CharField(max_length=30)
    complemento = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f'{self.rua}, {self.numero}, {self.complemento}, {self.bairro}, {self.cep}, {self.cidade}, {self.estado}'
class Contato(models.Model):
    ddd = models.CharField(max_length=2)
    celular = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.ddd} {self.celular}'

class Anunciante(models.Model):
    usuario = AutoOneToOneField(User, on_delete=models.CASCADE, related_name="anunciante")
    endereco = models.ManyToManyField(Endereco)
    contato = models.ManyToManyField(Contato)
    
    def __str__(self):
        return self.usuario.username

class Demanda(models.Model):
    descricao = models.TextField()
    endereco_entrega = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    anunciante = models.ForeignKey(Anunciante, on_delete=models.CASCADE)
    status_finalizacao = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-id']
   
    def __str__(self):
        return self.descricao

'''
Cria token para cada usuario criado
'''
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)