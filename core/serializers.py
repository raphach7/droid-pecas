from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import Endereco, Anunciante, Contato, Demanda


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = ["rua", "numero", "complemento", "bairro", "cep", "estado", "cidade"]
        
class AnuncianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anunciante
        fields = "__all__"
        
class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ["ddd", "celular"]
        
class DemandaSerializer(serializers.ModelSerializer):
    endereco_entrega = EnderecoSerializer()
    contato = ContatoSerializer()
    anunciante = serializers.CharField()

    class Meta:
        model = Demanda
        fields = "__all__"
